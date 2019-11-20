"""Test the results reader."""
# pylint: disable=line-too-long
from os import remove
from shutil import copy
from unittest import TestCase

from numpy import array
from numpy.testing import assert_array_equal

from serpentTools.settings import rc
from serpentTools.data import getFile, readDataFile
from serpentTools.parsers import ResultsReader
from serpentTools.messages import SerpentToolsException
from serpentTools.utils import RESULTS_PLOT_XLABELS
from tests import (
    plotTest,
    plotAttrTest,
)


GCU_START_STR = "GCU_UNIVERSE_NAME"
NO_BU_GCU_FILE = "./pwr_noGcu_res.m"
ADF_FILE = "./pwr_adf_res.m"
RES_NO_BU = getFile("pwr_noBU_res.m")


def setUpModule():
    """Write the result file with no group constant data."""
    with open(NO_BU_GCU_FILE, 'w') as noGcu, open(RES_NO_BU) as good:
        for line in good:
            if GCU_START_STR in line:
                break
            noGcu.write(line)
    copy(RES_NO_BU, ADF_FILE)
    with open(ADF_FILE, 'a') as stream:
        stream.write("""
% Assembly discontinuity factors (order: W-S-E-N / NW-NE-SE-SW):

DF_SURFACE                (idx, [1:  3])  = 'ADF' ;
DF_SYM                    (idx, 1)        = 1 ;
DF_N_SURF                 (idx, 1)        = 4 ;
DF_N_CORN                 (idx, 1)        = 4 ;
DF_VOLUME                 (idx, 1)        =  4.62250E+02 ;
DF_SURF_AREA              (idx, [1:  4])  = [ 2.15000E+01  2.15000E+01  2.15000E+01  2.15000E+01 ];
DF_MID_AREA               (idx, [1:  4])  = [ 2.15000E+00  2.15000E+00  2.15000E+00  2.15000E+00 ];
DF_CORN_AREA              (idx, [1:  4])  = [ 2.15000E+00  2.15000E+00  2.15000E+00  2.15000E+00 ];
DF_SURF_IN_CURR           (idx, [1:  16]) = [  1.19014E+15 0.00046  1.99543E+14 0.00114  1.19014E+15 0.00046  1.99543E+14 0.00114  1.19014E+15 0.00046  1.99543E+14 0.00114  1.19014E+15 0.00046  1.99543E+14 0.00114 ];
""") # noqa


def tearDownModule():
    """Remove the noGcu file."""
    remove(NO_BU_GCU_FILE)
    remove(ADF_FILE)


class Serp2129Helper(TestCase):
    """Sets the serpentVersion to 2.1.29 for reading"""

    def setUp(self):
        rc['serpentVersion'] = '2.1.29'

    def tearDown(self):
        rc['serpentVersion'] = '2.1.30'


class TestBadFiles(Serp2129Helper):
    """
    Test bad files.

    Tests:
        1. test_noResults: file with no results
        2. test_noUniverses: file with no universes

    Raises SerpentToolsException
    """

    def test_noResults(self):
        """Verify that the reader raises error when no results exist in the file""" # noqa
        badFile = 'bad_results_file.m'
        with open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(str(_line))
        badReader = ResultsReader(badFile)
        with self.assertRaises(SerpentToolsException):
            badReader.read()
        remove(badFile)

    def test_emptyFile_noGcu(self):
        """
        Verify an exception is raised for empty files w/ no gcu data expected.
        """
        badFile = 'bad_results_file.m'
        with open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(str(_line))
        badReader = ResultsReader(badFile)
        with self.assertRaises(SerpentToolsException):
            badReader.read()
        remove(badFile)

    def test_emptyAttributes(self):
        """Verify that the reader raises error when all attributes are empty"""
        testFile = getFile('pwr_emptyAttributes_res.m')
        with self.assertRaises(SerpentToolsException):
            with rc:
                rc['xs.variableExtras'] = ['GC_UNIVERSE_NAME']
                testReader = ResultsReader(testFile)
                testReader.read()


class TestGetUniv(TestCase):
    """
    Test the getUniv method.

    Tests:
        1. test_allVarsNone: burnup, index and timeDays are all set to None
        2. test_nonPostiveIndex: index is zero or negative
        3. test_noUnivState: define ('0',bu,idx,days) a non-existing state
        4. test_validUniv: test that a valid universe state contains
           proper data

    Raises  SerpentToolsException
                    All variables are set to None
            KeyError
                    index is non-positive
                    no universe state exist in the reader
    """
    def setUp(self):
        self.file = getFile('pwr_res.m')
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            self.reader = ResultsReader(self.file)
            self.reader.read()
        self.expectedinfValAbs = array([1.05040E-02, 1.23260E-01])

    def test_allVarsNone(self):
        """Verify that the reader raises error when no time parameters are given""" # noqa
        with self.assertRaises(SerpentToolsException):
            self.reader.getUniv('0', burnup=None, index=None, timeDays=None)

    def test_noUnivState(self):
        """Verify that the reader raises error when the state tuple does not exist""" # noqa
        with self.assertRaises(KeyError):
            self.reader.getUniv('0', burnup=50, index=10, timeDays=5)

    def test_validUniv(self):
        """Verify that getUniv returns the correct universe"""
        xsDict = self.reader.getUniv('0', burnup=0.0, index=0, timeDays=0.0)
        assert_array_equal(xsDict.infExp['infAbs'], self.expectedinfValAbs)


class TesterCommonResultsReader(TestCase):
    """
    Class with common tests for the results reader.

    Expected failures/errors:

        1. test_varsMatchSettings:
                        compares the keys
                        defined by the user to those
                        obtained by the reader
            Raises SerpentToolsException
        2. test_metadata:
                        Check that metadata variables and
                        their values are properly stored
            Raises SerpentToolsException
        3. test_resdata:
                        Check that time-dependent results variables
                        and their values are properly stored
            Raises SerpentToolsException
        4. test_universes:
                        Check that expected states are read
                        i.e., ('univ', bu, buIdx, days)
                        For a single state, check that
                        infExp keys and values are stored.
                        Check that infUnc and metadata are properly stored
            Raises SerpentToolsException
    """

    HAS_UNIV = True
    HAS_BURNUP = True

    def test_varsMatchSettings(self):
        """Verify that the obtained variables match the settings."""
        self.assertSetEqual(self.expVarSettings,
                            self.reader.settings['variables'])

    def test_metadata(self):
        """Verify that user-defined metadata is properly stored."""
        expectedKeys = set(self.expectedMetadata)
        actualKeys = set(self.reader.metadata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        for key, expectedValue in self.expectedMetadata.items():
            if isinstance(expectedValue, str):
                self.assertSetEqual(set(self.reader.metadata[key]),
                                    set(expectedValue))
            else:
                assert_array_equal(self.reader.metadata[key], expectedValue)

    def test_resdata(self):
        """Verify that results data is properly stored."""
        expectedKeys = self.expectedResdata
        actualKeys = set(self.reader.resdata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        assert_array_equal(self.reader.resdata['absKeff'], self.expectedKeff)

    def test_burnup(self):
        """Verify the burnup vector is properly stored."""
        actualBurnDays = self.reader.resdata.get('burnDays', None)
        if actualBurnDays is None:
            if self.HAS_BURNUP:
                raise AttributeError(
                    "{} should have burnup, but does not".format(self))
            raise self.skipTest(
                "{} does not, and should not, have burnup".format(self))
        assert_array_equal(actualBurnDays, self.expectedDays)

    def test_universes(self):
        """Verify that results for all states (univ, bu, buIdx, days) exist.
           Verify that the containers for each state are properly
           created and that the proper information is stored, e.g.
           infExp keys and values"""
        actualStates = set(self.reader.universes.keys())
        if not actualStates:
            if self.HAS_UNIV:
                raise AttributeError(
                    "{} does not have universe data, but should".format(self))
            raise self.skipTest(
                "{} does not, and should not, have universe data".format(self))
        self.assertSetEqual(set(self.expectedStates), actualStates)
        expSt0 = self.expectedStates[0]
        expUniv = self.reader.universes[expSt0]
        self.assertSetEqual(set(expUniv.infExp.keys()), self.expectedInfExp)
        self.assertSetEqual(set(expUniv.gc.keys()), self.expectedUnivgcData)
        assert_array_equal(expUniv.infExp['infFlx'], self.expectedInfVals)
        assert_array_equal(expUniv.infUnc['infFlx'], self.expectedInfUnc)
        assert_array_equal(expUniv.gc['cmmTranspxs'], self.expectedCMM)
        assert_array_equal(expUniv.gcUnc['cmmTranspxs'], self.expectedCMMunc)
        assert_array_equal(expUniv.groups, self.expectedGroups)
        assert_array_equal(expUniv.microGroups, self.expectedMicroGroups)


class TestFilterResults(TesterCommonResultsReader):
    """
    Test the ability to read and filter data.

    Expected outcome:
        1. test_varsMatchSettings:
                        Results read are equal to results set
        2. test_metadata:
                        metadata is filtered
        3. test_resdata:
                        resdata is filtered
        4. test_universes:
                        univ is filtered
    """

    expVarSettings = {
        'VERSION', 'COMPILE_DATE', 'DEBUG', 'TITLE',
        'CONFIDENTIAL_DATA', 'INPUT_FILE_NAME',
        'WORKING_DIRECTORY', 'HOSTNAME', 'CPU_TYPE',
        'CPU_MHZ', 'START_DATE', 'COMPLETE_DATE',
        'GC_UNIVERSE_NAME', 'MICRO_NG', 'MICRO_E', 'MACRO_NG',
        'MACRO_E', 'INF_MICRO_FLX', 'INF_KINF', 'INF_FLX',
        'INF_FISS_FLX', 'TOT', 'CAPT', 'ABS', 'FISS', 'NSF',
        'NUBAR', 'KAPPA', 'INVV', 'TRANSPXS', 'DIFFCOEF',
        'RABSXS', 'REMXS', 'SCATT0', 'SCATT1', 'SCATT2',
        'SCATT3', 'SCATT4', 'SCATT5', 'SCATT6', 'SCATT7',
        'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',
        'CHIT', 'CHIP', 'CHID', 'CMM_TRANSPXS',
        'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y', 'CMM_TRANSPXS_Z',
        'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X', 'CMM_DIFFCOEF_Y',
        'CMM_DIFFCOEF_Z', 'ANA_KEFF', 'IMP_KEFF', 'COL_KEFF',
        'ABS_KEFF', 'ABS_KINF', 'GEOM_ALBEDO',
        'BURN_MATERIALS', 'BURN_MODE', 'BURN_STEP', 'BURNUP',
        'BURN_DAYS', 'COEF_IDX', 'COEF_BRANCH', 'COEF_BU_STEP',
    }

    expectedMetadata = {
        'version': 'Serpent 2.1.29',
        'compileDate': 'Jan  4 2018 17:22:46',
        'debug': 0,
        'title': 'pwr pin',
        'confidentialData': 0,
        'inputFileName': 'pwrPin',
        'workingDirectory': '/home/ajohnson400/research/gpt-dep/testing/depmtx', # noqa
        'hostname': 'ME04L0358GRD04',
        'cpuType': 'Intel(R) Core(TM) i7-6700T CPU @ 2.80GHz',
        'cpuMhz': 194.,
        'startDate': 'Mon Feb 19 15:39:23 2018',
        'completeDate': 'Mon Feb 19 15:39:53 2018',
    }

    expectedResdata = {
        'absKeff', 'absKinf', 'anaKeff', 'burnDays',
        'burnMaterials', 'burnMode', 'burnStep', 'burnup',
        'colKeff', 'geomAlbedo', 'impKeff', 'nubar',
    }

    expectedKeff = array(
        [[9.91938E-01, 0.00145], [1.81729E-01, 0.00240]])
    expectedDays = array([[0.00000E+00], [5.00000E+00]])

    expectedInfExp = {
        'infAbs', 'infCapt', 'infChid', 'infChip', 'infChit',
        'infDiffcoef', 'infFiss', 'infFissFlx', 'infFlx',
        'infInvv', 'infKappa', 'infKinf', 'infMicroFlx',
        'infNsf', 'infNubar', 'infRabsxs', 'infRemxs',
        'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5',
        'infS6', 'infS7', 'infScatt0', 'infScatt1',
        'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5',
        'infScatt6', 'infScatt7', 'infTot', 'infTranspxs',
    }
    expectedUnivgcData = {
        'cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY',
        'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
        'cmmTranspxsY', 'cmmTranspxsZ',
    }
    expectedCMM = array([2.23062E-01, 6.55491E-01])
    expectedCMMunc = array([0.00144, 0.03837])
    expectedMicroGroups = (
        array([1.00000E-11, 5.00000E-09, 1.00000E-08,
               1.50000E-08, 2.00000E-08, 2.50000E-08,
               3.00000E-08, 3.50000E-08, 4.20000E-08,
               5.00000E-08, 5.80000E-08, 6.70000E-08,
               8.00000E-08, 1.00000E-07, 1.40000E-07,
               1.80000E-07, 2.20000E-07, 2.50000E-07,
               2.80000E-07, 3.00000E-07, 3.20000E-07,
               3.50000E-07, 4.00000E-07, 5.00000E-07,
               6.25000E-07, 7.80000E-07, 8.50000E-07,
               9.10000E-07, 9.50000E-07, 9.72000E-07,
               9.96000E-07, 1.02000E-06, 1.04500E-06,
               1.07100E-06, 1.09700E-06, 1.12300E-06,
               1.15000E-06, 1.30000E-06, 1.50000E-06,
               1.85500E-06, 2.10000E-06, 2.60000E-06,
               3.30000E-06, 4.00000E-06, 9.87700E-06,
               1.59680E-05, 2.77000E-05, 4.80520E-05,
               7.55014E-05, 1.48728E-04, 3.67262E-04,
               9.06898E-04, 1.42510E-03, 2.23945E-03,
               3.51910E-03, 5.50000E-03, 9.11800E-03,
               1.50300E-02, 2.47800E-02, 4.08500E-02,
               6.74300E-02, 1.11000E-01, 1.83000E-01,
               3.02500E-01, 5.00000E-01, 8.21000E-01,
               1.35300E+00, 2.23100E+00, 3.67900E+00,
               6.06550E+00, 2.00000E+01]))
    expectedGroups = array(
        [1.00000E+37, 6.25000E-07, 0.00000E+00])
    expectedInfVals = array([2.46724E+18, 2.98999E+17])
    expectedInfUnc = array([0.00115, 0.00311])

    expectedStates = (('0', 0.0, 0, 0.0), ('0', 500, 1, 5.0))

    def setUp(self):
        self.file = getFile('pwr_res.m')
        # universe id, burnup, step, days
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            self.reader = ResultsReader(self.file)
            self.reader.read()


class TestReadAllResults(TesterCommonResultsReader):
    """
    Read the full results file and do NOT filter.

    Note:
        The file was manually filtered to include
        only the variables from 'TestFilterResults' class
        No settings were defined and hence the reader
        should read everything.

    Expected outcome:
        - Same variables and values as in the 'TestFilterResults' class
        1. test_varsMatchSettings:
                        Results read are equal to results set
        2. test_metadata:
                        metadata is not filtered
        3. test_resdata:
                        resdata is not filtered
        4. test_universes:
                        univ is not filtered
    """

    expVarSettings = set()

    expectedMetadata = {
        'version': 'Serpent 2.1.29',
        'compileDate': 'Jan  4 2018 17:22:46',
        'debug': 0,
        'title': 'pwr pin',
        'confidentialData': 0,
        'inputFileName': 'pwrPin',
        'workingDirectory': '/home/ajohnson400/research/gpt-dep/testing/depmtx', # noqa
        'hostname': 'ME04L0358GRD04',
        'cpuType': 'Intel(R) Core(TM) i7-6700T CPU @ 2.80GHz',
        'cpuMhz': 194.,
        'startDate': 'Mon Feb 19 15:39:23 2018',
        'completeDate': 'Mon Feb 19 15:39:53 2018',
    }

    expectedResdata = {
        'absKeff', 'absKinf', 'anaKeff', 'burnDays',
        'burnMaterials', 'burnMode', 'burnStep', 'burnup',
        'colKeff', 'geomAlbedo', 'impKeff', 'nubar', 'minMacroxs',
    }

    expectedKeff = array(
        [[9.91938E-01, 0.00145], [1.81729E-01, 0.00240]])
    expectedDays = array([[0.00000E+00], [5.00000E+00]])

    expectedInfExp = {
        'infAbs', 'infCapt', 'infChid', 'infChip', 'infChit',
        'infDiffcoef', 'infFiss', 'infFissFlx', 'infFlx',
        'infInvv', 'infKappa', 'infKinf', 'infMicroFlx',
        'infNsf', 'infNubar', 'infRabsxs', 'infRemxs',
        'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5',
        'infS6', 'infS7', 'infScatt0', 'infScatt1',
        'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5',
        'infScatt6', 'infScatt7', 'infTot', 'infTranspxs',
    }
    expectedUnivgcData = {
        'cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY',
        'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
        'cmmTranspxsY', 'cmmTranspxsZ',
    }
    expectedCMM = array([2.23062E-01, 6.55491E-01])
    expectedCMMunc = array([0.00144, 0.03837])
    expectedMicroGroups = (
        array([1.00000E-11, 5.00000E-09, 1.00000E-08,
               1.50000E-08, 2.00000E-08, 2.50000E-08,
               3.00000E-08, 3.50000E-08, 4.20000E-08,
               5.00000E-08, 5.80000E-08, 6.70000E-08,
               8.00000E-08, 1.00000E-07, 1.40000E-07,
               1.80000E-07, 2.20000E-07, 2.50000E-07,
               2.80000E-07, 3.00000E-07, 3.20000E-07,
               3.50000E-07, 4.00000E-07, 5.00000E-07,
               6.25000E-07, 7.80000E-07, 8.50000E-07,
               9.10000E-07, 9.50000E-07, 9.72000E-07,
               9.96000E-07, 1.02000E-06, 1.04500E-06,
               1.07100E-06, 1.09700E-06, 1.12300E-06,
               1.15000E-06, 1.30000E-06, 1.50000E-06,
               1.85500E-06, 2.10000E-06, 2.60000E-06,
               3.30000E-06, 4.00000E-06, 9.87700E-06,
               1.59680E-05, 2.77000E-05, 4.80520E-05,
               7.55014E-05, 1.48728E-04, 3.67262E-04,
               9.06898E-04, 1.42510E-03, 2.23945E-03,
               3.51910E-03, 5.50000E-03, 9.11800E-03,
               1.50300E-02, 2.47800E-02, 4.08500E-02,
               6.74300E-02, 1.11000E-01, 1.83000E-01,
               3.02500E-01, 5.00000E-01, 8.21000E-01,
               1.35300E+00, 2.23100E+00, 3.67900E+00,
               6.06550E+00, 2.00000E+01]))
    expectedGroups = array(
        [1.00000E+37, 6.25000E-07, 0.00000E+00])
    expectedInfVals = array([2.46724E+18, 2.98999E+17])
    expectedInfUnc = array([0.00115, 0.00311])
    expectedStates = (('0', 0.0, 0, 0.0), ('0', 500, 1, 5.0))

    def setUp(self):
        self.file = getFile('pwr_filter_res.m')
        # universe id, burnup, step, days
        with rc:
            rc['serpentVersion'] = '2.1.29'
            self.reader = ResultsReader(self.file)
            self.reader.read()


class TestFilterResultsNoBurnup(TesterCommonResultsReader):
    """
    Test the ability to read a file with no BU steps.

    Expected outcome:
        1. test_varsMatchSettings:
                        Results read are equal to results set
        2. test_metadata:
                        metadata is filtered
        3. test_resdata:
                        resdata is filtered
        4. test_universes:
                        univ is filtered
    """

    HAS_BURNUP = False
    expVarSettings = {
        'VERSION', 'COMPILE_DATE', 'DEBUG', 'TITLE',
        'CONFIDENTIAL_DATA', 'INPUT_FILE_NAME',
        'WORKING_DIRECTORY', 'HOSTNAME', 'CPU_TYPE',
        'CPU_MHZ', 'START_DATE', 'COMPLETE_DATE',
        'GC_UNIVERSE_NAME', 'MICRO_NG', 'MICRO_E', 'MACRO_NG',
        'MACRO_E', 'INF_MICRO_FLX', 'INF_KINF', 'INF_FLX',
        'INF_FISS_FLX', 'TOT', 'CAPT', 'ABS', 'FISS', 'NSF',
        'NUBAR', 'KAPPA', 'INVV', 'TRANSPXS', 'DIFFCOEF',
        'RABSXS', 'REMXS', 'SCATT0', 'SCATT1', 'SCATT2',
        'SCATT3', 'SCATT4', 'SCATT5', 'SCATT6', 'SCATT7',
        'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',
        'CHIT', 'CHIP', 'CHID', 'CMM_TRANSPXS',
        'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y', 'CMM_TRANSPXS_Z',
        'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X', 'CMM_DIFFCOEF_Y',
        'CMM_DIFFCOEF_Z', 'ANA_KEFF', 'IMP_KEFF', 'COL_KEFF',
        'ABS_KEFF', 'ABS_KINF', 'GEOM_ALBEDO',
        'BURN_MATERIALS', 'BURN_MODE', 'BURN_STEP', 'BURNUP',
        'BURN_DAYS', 'COEF_IDX', 'COEF_BRANCH', 'COEF_BU_STEP',
    }

    expectedMetadata = {
        'version': 'Serpent 2.1.30',
        'compileDate': 'Apr  4 2018 08:55:27',
        'debug': 0,
        'title': 'UO2 PIN MODEL',
        'confidentialData': 0,
        'inputFileName': 'pwr',
        'workingDirectory': '/gpfs/pace1/project/me-kotlyar/dkotlyar6/Research/Serpent_test/FP_test', # noqa
        'hostname': 'rich133-c36-10-l.pace.gatech.edu',
        'cpuType': 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz',
        'cpuMhz': 184549409.0,
        'startDate': 'Mon May 14 11:20:06 2018',
        'completeDate': 'Mon May 14 11:20:36 2018',
    }

    expectedResdata = {
        'absKeff', 'absKinf', 'anaKeff', 'colKeff',
        'geomAlbedo', 'impKeff', 'nubar',
    }

    expectedKeff = array([1.15295E+00, 0.00094])
    expectedDays = array([])

    expectedInfExp = {
        'infAbs', 'infCapt', 'infChid', 'infChip', 'infChit',
        'infDiffcoef', 'infFiss', 'infFissFlx', 'infFlx',
        'infInvv', 'infKappa', 'infKinf', 'infMicroFlx',
        'infNsf', 'infNubar', 'infRabsxs', 'infRemxs',
        'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5',
        'infS6', 'infS7', 'infScatt0', 'infScatt1',
        'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5',
        'infScatt6', 'infScatt7', 'infTot', 'infTranspxs',
    }
    expectedUnivgcData = {
        'cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY',
        'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
        'cmmTranspxsY', 'cmmTranspxsZ',
    }
    expectedCMM = array([1.80522E-01, 4.44568E-01])
    expectedCMMunc = array([0.00181, 0.01952])
    expectedMicroGroups = (
        array([1.00000E-11, 5.00000E-09, 1.00000E-08,
               1.50000E-08, 2.00000E-08, 2.50000E-08,
               3.00000E-08, 3.50000E-08, 4.20000E-08,
               5.00000E-08, 5.80000E-08, 6.70000E-08,
               8.00000E-08, 1.00000E-07, 1.40000E-07,
               1.80000E-07, 2.20000E-07, 2.50000E-07,
               2.80000E-07, 3.00000E-07, 3.20000E-07,
               3.50000E-07, 4.00000E-07, 5.00000E-07,
               6.25000E-07, 7.80000E-07, 8.50000E-07,
               9.10000E-07, 9.50000E-07, 9.72000E-07,
               9.96000E-07, 1.02000E-06, 1.04500E-06,
               1.07100E-06, 1.09700E-06, 1.12300E-06,
               1.15000E-06, 1.30000E-06, 1.50000E-06,
               1.85500E-06, 2.10000E-06, 2.60000E-06,
               3.30000E-06, 4.00000E-06, 9.87700E-06,
               1.59680E-05, 2.77000E-05, 4.80520E-05,
               7.55014E-05, 1.48728E-04, 3.67262E-04,
               9.06898E-04, 1.42510E-03, 2.23945E-03,
               3.51910E-03, 5.50000E-03, 9.11800E-03,
               1.50300E-02, 2.47800E-02, 4.08500E-02,
               6.74300E-02, 1.11000E-01, 1.83000E-01,
               3.02500E-01, 5.00000E-01, 8.21000E-01,
               1.35300E+00, 2.23100E+00, 3.67900E+00,
               6.06550E+00, 2.00000E+01]))
    expectedGroups = array(
        [1.00000E+37, 6.25000E-07, 0.00000E+00])
    expectedInfVals = array([8.71807E+14, 4.80974E+13])
    expectedInfUnc = array([0.00097, 0.00121])
    expectedStates = (('0', 0, 0, 0), ('0', 0, 0, 0))

    def setUp(self):
        self.file = getFile('pwr_noBU_res.m')
        # universe id, Idx, Idx, Idx
        with rc:
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            self.reader = ResultsReader(self.file)
            self.reader.read()


class TestResultsNoBurnNoGcu(TestFilterResultsNoBurnup):
    """Test with no group constant data present in the file."""

    HAS_UNIV = False

    def setUp(self):
        self.file = NO_BU_GCU_FILE
        with rc:
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            self.reader = ResultsReader(self.file)
            self.reader.read()


class NoUniverseTester(Serp2129Helper):
    """Read a file ith burnup but no universes"""

    def setUp(self):
        filep = getFile("pwr_noUniv_res.m")
        self.reader = ResultsReader(filep)
        self.reader.read()

    def test_noUniverse(self):
        expectedBurnup = array([
            [0.00000E+00, 0.00000E+00],
            [5.00000E+02, 5.00260E+02]])
        expectedAbsKeff = array([
            [9.91938E-01, 0.00145],
            [1.81729E-01, 0.00240]])
        self.assertEqual(0, len(self.reader.universes))
        assert_array_equal(expectedBurnup, self.reader.resdata['burnup'])
        assert_array_equal(expectedAbsKeff, self.reader.resdata['absKeff'])


class RestrictedResultsReader(Serp2129Helper):
    """Class that restricts the variables read from the results file"""

    expectedInfFlux_bu0 = TestReadAllResults.expectedInfVals
    expectedAbsKeff = TestReadAllResults.expectedKeff
    dataFile = "pwr_res.m"

    def _testUnivFlux(self, reader):
        univ = reader.getUniv('0', index=0)
        assert_array_equal(self.expectedInfFlux_bu0, univ.get("infFlx"))

    def test_justFlux(self):
        """Restrict the variables to gcu inf flux and verify their values"""
        with rc:
            rc['xs.variableExtras'] = ["INF_FLX", ]
            r = readDataFile(self.dataFile)
        self._testUnivFlux(r)

    def test_xsGroups(self):
        """Restrict the variables groups to gc-meta to obtain flux and test."""
        with rc:
            rc['xs.variableGroups'] = ['gc-meta', ]
            r = readDataFile(self.dataFile)
        self._testUnivFlux(r)

    def test_fluxAndKeff(self):
        """Restrict to two unique parameters and verify their contents."""
        with rc:
            rc['xs.variableExtras'] = ['ABS_KEFF', 'INF_FLX']
            r = readDataFile(self.dataFile)
        self._testUnivFlux(r)
        assert_array_equal(self.expectedAbsKeff, r.resdata['absKeff'])


del TesterCommonResultsReader, Serp2129Helper


class ResPlotTester(TestCase):

    @classmethod
    def setUpClass(cls):
        with rc:
            rc['xs.variableExtras'] = [
                'ABS_KEFF',
                'TOT_CPU_TIME',
                'BURN_DAYS',
                'BURNUP',
                'BURN_STEP',
            ]
            cls.reader = ResultsReader(getFile('InnerAssembly_res.m'))
            cls.reader.read()

    @plotTest
    def test_singlePlot(self):
        """Test the plot capabilities of the ResultsReader"""
        ax = self.reader.plot('absKeff', sigma=3)
        plotAttrTest(
            self, ax, xlabel=RESULTS_PLOT_XLABELS['burnDays'],
            ylabel="absKeff$ \\pm 3\\sigma$",
        )

        ax.clear()
        newLabel = 'Multiplication factor'
        self.reader.plot('burnup', {'absKeff': newLabel}, ax=ax, sigma=0,
                         logx=True)
        plotAttrTest(
            self, ax, ylabel=newLabel, xscale='log',
            xlabel=RESULTS_PLOT_XLABELS['burnup'],
        )
        # plot two quantities
        ax.clear()
        self.reader.plot('burnStep', ['absKeff', 'totCpuTime'], ax=ax,
                         sigma=0, ylabel="ylabel")
        plotAttrTest(
            self, ax, xlabel=RESULTS_PLOT_XLABELS['burnStep'],
            ylabel="ylabel", legendLabels=['absKeff', 'totCpuTime'],
        )

    @plotTest
    def test_rightPlot(self):
        """Test plotting on left and right y axis"""
        left, right = self.reader.plot('absKeff', sigma=0, right='totCpuTime')
        plotAttrTest(
            self, left, ylabel='absKeff',
            legendLabels=['absKeff', 'totCpuTime [right]'],
        )
        plotAttrTest(
            self, right, ylabel='totCpuTime',
        )


class ResADFTester(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reader = ResultsReader(ADF_FILE)
        cls.reader.read()

    def test_adf(self):
        """Verify the storage of ADF data"""
        univ = self.reader.getUniv('0', index=0)
        self.assertTrue(type(univ.infExp['infKinf']) is float)
        self.assertEqual(1.15306, univ.infExp['infKinf'])
        self.assertEqual(0.00127, univ.infUnc['infKinf'])
        self.assertTrue(type(univ.gc['dfSurface']) is str)
        self.assertEqual('ADF', univ.gc['dfSurface'])
        self.assertTrue(type(univ.gc['dfSym']) is int)
        self.assertEqual(1, univ.gc['dfSym'])
        self.assertTrue(type(univ.gc['dfVolume']) is float)
        self.assertEqual(4.62250E+02, univ.gc['dfVolume'])
        assert_array_equal(
            array([2.15000E+01, 2.15000E+01, 2.15000E+01, 2.15000E+01]),
            univ.gc['dfSurfArea'])
        assert_array_equal(array([
            1.19014E+15, 1.99543E+14, 1.19014E+15, 1.99543E+14,
            1.19014E+15, 1.99543E+14, 1.19014E+15, 1.99543E+14]),
            univ.gc['dfSurfInCurr'])
        self.assertTrue('dfSurfArea' not in univ.gcUnc)
