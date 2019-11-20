"""
Tests for testing the MATLAB conversion functions
"""

from io import BytesIO

from numpy import arange, ones
from numpy.testing import assert_array_equal
from serpentTools import Detector
from serpentTools.data import getFile, readDataFile
from serpentTools.parsers import DepmtxReader

from tests import MatlabTesterHelper


class Det2MatlabHelper(MatlabTesterHelper):
    """Helper class for testing detector to matlab conversion"""

    NBINS = 10
    NCOLS = 12
    # approximate some detector data
    BINS = ones(
        NCOLS * NBINS, dtype=float).reshape(NBINS, NCOLS)
    # emulate energy grid
    GRID = arange(3 * NBINS).reshape(NBINS, 3)
    GRID_KEY = 'E'

    @classmethod
    def setUpClass(cls):
        cls.detector = Detector('matlabtest')
        cls.detector.bins = cls.BINS
        cls.detector.grids[cls.GRID_KEY] = cls.GRID

    def setUp(self):
        MatlabTesterHelper.setUp(self)

        from serpentTools.detectors import deconvert, prepToMatlab
        # instance methods and/or rename them
        # potential issues sending putting many such functions in this
        # test suite

        self.converterFunc = deconvert if self.CONVERT else prepToMatlab

    def test_det2Matlab(self):
        """Test the conversion to matlab files"""
        from scipy.io import loadmat
        writer = BytesIO()
        self.detector.toMatlab(writer, self.CONVERT, append=False)
        fromMatlab = loadmat(writer)

        binsKey = self.converterFunc(self.detector.name, 'bins')
        self.assertTrue(binsKey in fromMatlab)
        assert_array_equal(fromMatlab[binsKey], self.detector.bins)

        gridKey = self.converterFunc(self.detector.name, self.GRID_KEY)
        self.assertTrue(gridKey in fromMatlab)
        assert_array_equal(fromMatlab[gridKey],
                           self.detector.grids[self.GRID_KEY])


class ConvertedDet2MatlabTester(Det2MatlabHelper):
    """Test the process of writing detector data w/ original names"""

    CONVERT = True


class UnconvertedDet2MatlabTester(Det2MatlabHelper):
    """Test the process of writing detector data w/ custom names"""

    CONVERT = False


class DepmtxMatlabHelper(MatlabTesterHelper):
    """Class for setting up and testing"""

    @classmethod
    def setUpClass(cls):
        cls.depFile = getFile('depmtx_ref.m')

    def setUp(self):
        MatlabTesterHelper.setUp(self)
        self.outFile = BytesIO()
        self.reader = DepmtxReader(self.depFile, self.SPARSE)
        self.reader.read()
        if self.SPARSE:
            self.expected = {'A': self.reader.depmtx.toarray()}
        else:
            self.expected = {'A': self.reader.depmtx}

        n0 = self.reader.n0.reshape(1, self.reader.n0.size)
        n1 = self.reader.n1.reshape(1, self.reader.n1.size)
        zai = self.reader.zai.reshape(1, self.reader.zai.size)

        if self.RECONVERT:
            self.expected['ZAI'] = zai
            self.expected['N0'] = n0
            self.expected['N1'] = n1
        else:
            self.expected['zai'] = zai
            self.expected['n0'] = n0
            self.expected['n1'] = n1

    def test_depmtxToMatlab(self):
        """Verify the depmtx reader can be written to matlab file"""
        from scipy.io import loadmat
        self.reader.toMatlab(self.outFile, self.RECONVERT)
        written = loadmat(self.outFile)
        self.assertEqual(self.reader.deltaT, written['t'])
        for expKey, expValue in self.expected.items():
            self.assertTrue(expKey in written, msg=expKey)
            assert_array_equal(expValue, written[expKey], err_msg=expKey)


class ConvertedDepmtxMatlabTester(DepmtxMatlabHelper):
    RECONVERT = True
    SPARSE = True


class UnconvertedDepmtxMatlabTester(DepmtxMatlabHelper):
    RECONVERT = False
    SPARSE = True


class ConvertedFullDepmtxMatlabTester(DepmtxMatlabHelper):
    RECONVERT = True
    SPARSE = False


class ResultToMatlabHelper(MatlabTesterHelper):
    """Class for testing the result reader matlab export"""

    @classmethod
    def setUpClass(cls):
        cls.reader = readDataFile("pwr_res.m")

    def setUp(self):
        MatlabTesterHelper.setUp(self)
        from scipy.io import loadmat
        self.stream = BytesIO()
        if self.CONVERT:
            from serpentTools.parsers.results import getSerpentCaseName
            self.convertFunc = getSerpentCaseName
        else:
            from serpentTools.parsers.results import getMixedCaseName
            self.convertFunc = getMixedCaseName
        self.reader.toMatlab(self.stream, self.CONVERT, oned='column')
        self.gathered = loadmat(self.stream)

    def checkMaybe1DArrays(self, expValue, loaded, origKey):
        """Check arrays when the gathered value is likely a 2D row vector"""
        if loaded.shape != expValue.shape:
            self.assertEqual(expValue.shape[0], loaded.shape[0],
                             msg=origKey)
            loaded = loaded[:, 0]
        assert_array_equal(expValue, loaded, err_msg=origKey)

    def test_gatheredMetadata(self):
        """Test the writing of metadata to matlab"""
        for origKey, expValue in self.reader.metadata.items():
            expKey = self.convertFunc(origKey)
            self.assertTrue(expKey in self.gathered, msg=origKey)
            actual = self.gathered[expKey]
            if isinstance(expValue, str):
                actValue = actual[0]
                self.assertEqual(expValue, actValue, msg=origKey)
            elif isinstance(expValue, (int, float)):
                # stored as (1, 1) matrix
                actValue = actual.flatten()[0]
                self.assertEqual(expValue, actValue, msg=origKey)
            else:  # try numpy array
                self.checkMaybe1DArrays(expValue, actual, origKey)

    def test_dumpedResdata(self):
        """Test the writing of results data to matlab"""
        for origKey, expValue in self.reader.resdata.items():
            expKey = self.convertFunc(origKey)
            self.assertTrue(expKey in self.gathered, msg=origKey)
            self.checkMaybe1DArrays(expValue, self.gathered[expKey], origKey)

    def test_dumpedUnivData(self):
        """Test the writing of universe data to matlab"""
        univIxKey = self.convertFunc("universes")
        burnIxKey = self.convertFunc("burnStep")
        self.assertTrue(univIxKey in self.gathered)
        self.assertTrue(burnIxKey in self.gathered)
        univOrder = tuple(self.gathered[univIxKey])
        burnOrder = tuple(self.gathered[burnIxKey].flatten())
        for univKey, universe in self.reader.universes.items():
            self.assertTrue(univKey[0] in univOrder,
                            msg="{} // {}".format(univKey, univOrder))
            uIndex = univOrder.index(univKey[0])
            actBurnIx = univKey[2]
            self.assertTrue(actBurnIx in burnOrder,
                            msg="{} // {}".format(univKey, burnOrder))
            burnIndex = burnOrder.index(actBurnIx)
            self.checkUnivContents(universe, uIndex, burnIndex,
                                   universe.infExp, universe.infUnc)
            self.checkUnivContents(universe, uIndex, burnIndex,
                                   universe.b1Exp, universe.b1Unc)
            self.checkUnivContents(universe, uIndex, burnIndex,
                                   universe.gc, universe.gcUnc)

    def checkUnivContents(self, universe, univIndex, burnIndex,
                          expGcD, uncGcD):
        """
        Check the contents of a specific subset of group constant dictionaries
        """
        for origKey, expValue in expGcD.items():
            uncValue = uncGcD[origKey]
            expKey = self.convertFunc(origKey)
            self.assertTrue(expKey in self.gathered, msg=origKey)
            actData = self.gathered[expKey][burnIndex, univIndex, ..., :]
            assert_array_equal(expValue, actData[..., 0], err_msg=origKey)
            assert_array_equal(uncValue, actData[..., 1], err_msg=origKey)


class SerpentCaseResults2MatlabTester(ResultToMatlabHelper):
    CONVERT = True


class MixedCaseResults2MatlabTester(ResultToMatlabHelper):
    CONVERT = False


del Det2MatlabHelper, DepmtxMatlabHelper, ResultToMatlabHelper
