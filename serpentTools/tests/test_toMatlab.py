"""
Tests for testing the MATLAB conversion functions
"""

from six import BytesIO, iteritems
from numpy import arange
from numpy.testing import assert_array_equal
from serpentTools.objects import Detector
from serpentTools.tests.utils import MatlabTesterHelper
from serpentTools.data import getFile
from serpentTools.parsers import DepmtxReader


class Det2MatlabHelper(MatlabTesterHelper):
    """Helper class for testing detector to matlab conversion"""

    NBINS = 10
    NCOLS = 12
    # approximate some detector data
    BINS = arange(
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

        from serpentTools.objects.detectors import deconvert, prepToMatlab
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
        for expKey, expValue in iteritems(self.expected):
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


del Det2MatlabHelper, DepmtxMatlabHelper

if __name__ == '__main__':
    from unittest import main
    main()
