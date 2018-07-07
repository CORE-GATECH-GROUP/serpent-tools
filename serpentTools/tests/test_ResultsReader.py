"""Test the results reader."""

import os
import unittest

from numpy import array
from numpy.testing import assert_equal
from six import iteritems

from serpentTools.settings import rc
from serpentTools.data import getFile
from serpentTools.parsers import ResultsReader
from serpentTools.messages import SerpentToolsException


class TestBadFiles(unittest.TestCase):
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
        os.remove(badFile)

    def test_noUniverses(self):
        """Verify that the reader raises an error if no universes are stored on the file""" # noqa
        univFile = getFile('pwr_noUniv_res.m')
        univReader = ResultsReader(univFile)
        with self.assertRaises(SerpentToolsException):
            univReader.read()


class TestEmptyAttributes(unittest.TestCase):
    """
    Test a case, in which some results do exist in the file,
    however the read procedure assigns no results into the attributes.
    Hence metadata, resdata and universes are all empty

    Raises SerpentToolsException
    """

    def test_emptyAttributes(self):
        """Verify that the reader raises error when all attributes are empty"""
        testFile = getFile('pwr_emptyAttributes_res.m')
        with self.assertRaises(SerpentToolsException):
            with rc:
                rc['xs.variableExtras'] = ['GC_UNIVERSE_NAME']
                testReader = ResultsReader(testFile)
                testReader.read()


class TestGetUniv(unittest.TestCase):
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

    def test_nonPostiveIndex(self):
        """Verify that the reader raises error when the time index is not positive""" # noqa
        with self.assertRaises(KeyError):
            self.reader.getUniv('0', burnup=None, index=0, timeDays=None)

    def test_noUnivState(self):
        """Verify that the reader raises error when the state tuple does not exist""" # noqa
        with self.assertRaises(KeyError):
            self.reader.getUniv('0', burnup=50, index=10, timeDays=5)

    def test_validUniv(self):
        """Verify that getUniv returns the correct universe"""
        xsDict = self.reader.getUniv('0', burnup=0.0, index=1, timeDays=0.0)
        assert_equal(xsDict.infExp['infAbs'], self.expectedinfValAbs)


class TesterCommonResultsReader(unittest.TestCase):
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

    def test_varsMatchSettings(self):
        """Verify that the obtained variables match the settings."""
        self.assertSetEqual(self.expVarSettings,
                            self.reader.settings['variables'])

    def test_metadata(self):
        """Verify that user-defined metadata is properly stored."""
        expectedKeys = set(self.expectedMetadata)
        actualKeys = set(self.reader.metadata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        for key, expectedValue in iteritems(self.expectedMetadata):
            if isinstance(expectedValue, str):
                self.assertSetEqual(set(self.reader.metadata[key]),
                                    set(expectedValue))
            else:
                assert_equal(self.reader.metadata[key], expectedValue)

    def test_resdata(self):
        """Verify that user-defined metadata is properly stored."""
        expectedKeys = self.expectedResdata
        actualKeys = set(self.reader.resdata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        assert_equal(self.reader.resdata['absKeff'], self.expectedKeff)
        try:
            assert_equal(self.reader.resdata['burnDays'], self.expectedDays)
        except:
            assert_equal([], self.expectedDays)

    def test_universes(self):
        """Verify that results for all states (univ, bu, buIdx, days) exist.
           Verify that the containers for each state are properly
           created and that the proper information is stored, e.g.
           infExp keys and values"""
        actualStates = set(self.reader.universes.keys())
        self.assertSetEqual(set(self.expectedStates), actualStates)
        expSt0 = self.expectedStates[0]
        expUniv = self.reader.universes[expSt0]
        self.assertSetEqual(set(expUniv.infExp.keys()), self.expectedInfExp)
        self.assertSetEqual(set(expUniv.gc.keys()), self.expectedUnivgcData)
        assert_equal(expUniv.infExp['infFlx'], self.expectedInfVals)
        assert_equal(expUniv.infUnc['infFlx'], self.expectedInfUnc)
        assert_equal(expUniv.gc['cmmTranspxs'], self.expectedCMM)
        assert_equal(expUniv.gcUnc['cmmTranspxs'], self.expectedCMMunc)
        assert_equal(expUniv.groups, self.expectedGroups)
        assert_equal(expUniv.microGroups, self.expectedMicroGroups)


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
    def setUp(self):
        self.file = getFile('pwr_res.m')
        # universe id, burnup, step, days
        self.expectedStates = (('0', 0.0, 1, 0.0), ('0', 500, 2, 5.0))
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            self.reader = ResultsReader(self.file)
            self.reader.read()

        self.expVarSettings = {
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

        self.expectedMetadata = {
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

        self.expectedResdata = {
                'absKeff', 'absKinf', 'anaKeff', 'burnDays',
                'burnMaterials', 'burnMode', 'burnStep', 'burnup',
                'colKeff', 'geomAlbedo', 'impKeff', 'nubar',
                }

        self.expectedKeff = array(
                [[9.91938E-01, 0.00145], [1.81729E-01, 0.00240]])
        self.expectedDays = array([[0.00000E+00], [5.00000E+00]])

        self.expectedInfExp = {
                'infAbs', 'infCapt', 'infChid', 'infChip', 'infChit',
                'infDiffcoef', 'infFiss', 'infFissFlx', 'infFlx',
                'infInvv', 'infKappa', 'infKinf', 'infMicroFlx',
                'infNsf', 'infNubar', 'infRabsxs', 'infRemxs',
                'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5',
                'infS6', 'infS7', 'infScatt0', 'infScatt1',
                'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5',
                'infScatt6', 'infScatt7', 'infTot', 'infTranspxs',
                }
        self.expectedUnivgcData = {
                'cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY',
                'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                'cmmTranspxsY', 'cmmTranspxsZ',
                }
        self.expectedCMM = array([2.23062E-01, 6.55491E-01])
        self.expectedCMMunc = array([0.00144, 0.03837])
        self.expectedMicroGroups = (
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
        self.expectedGroups = array(
                [1.00000E+37, 6.25000E-07, 0.00000E+00])
        self.expectedInfVals = array([2.46724E+18, 2.98999E+17])
        self.expectedInfUnc = array([0.00115, 0.00311])


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
    def setUp(self):
        self.file = getFile('pwr_filter_res.m')
        # universe id, burnup, step, days
        with rc:
            rc['serpentVersion'] = '2.1.29'
            self.expectedStates = (('0', 0.0, 1, 0.0), ('0', 500, 2, 5.0))
            self.reader = ResultsReader(self.file)
            self.reader.read()

        self.expVarSettings = set()

        self.expectedMetadata = {
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
                'completeDate': 'Mon Feb 19 15:39:53 2018'}

        self.expectedResdata = {
                'absKeff', 'absKinf', 'anaKeff', 'burnDays',
                'burnMaterials', 'burnMode', 'burnStep', 'burnup',
                'colKeff', 'geomAlbedo', 'impKeff', 'nubar', 'minMacroxs',
                }

        self.expectedKeff = array(
                [[9.91938E-01, 0.00145], [1.81729E-01, 0.00240]])
        self.expectedDays = array([[0.00000E+00], [5.00000E+00]])

        self.expectedInfExp = {
                'infAbs', 'infCapt', 'infChid', 'infChip', 'infChit',
                'infDiffcoef', 'infFiss', 'infFissFlx', 'infFlx',
                'infInvv', 'infKappa', 'infKinf', 'infMicroFlx',
                'infNsf', 'infNubar', 'infRabsxs', 'infRemxs',
                'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5',
                'infS6', 'infS7', 'infScatt0', 'infScatt1',
                'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5',
                'infScatt6', 'infScatt7', 'infTot', 'infTranspxs',
                }
        self.expectedUnivgcData = {
                'cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY',
                'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                'cmmTranspxsY', 'cmmTranspxsZ',
                }
        self.expectedCMM = array([2.23062E-01, 6.55491E-01])
        self.expectedCMMunc = array([0.00144, 0.03837])
        self.expectedMicroGroups = (
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
        self.expectedGroups = array(
                [1.00000E+37, 6.25000E-07, 0.00000E+00])
        self.expectedInfVals = array([2.46724E+18, 2.98999E+17])
        self.expectedInfUnc = array([0.00115, 0.00311])


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
    def setUp(self):
        self.file = getFile('pwr_noBU_res.m')
        # universe id, Idx, Idx, Idx
        self.expectedStates = (('0', 1, 1, 1), ('0', 1, 1, 1))
        with rc:
            rc['serpentVersion'] = '2.1.30'
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            self.reader = ResultsReader(self.file)
            self.reader.read()

        self.expVarSettings = {
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

        self.expectedMetadata = {
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

        self.expectedResdata = {
                'absKeff', 'absKinf', 'anaKeff', 'colKeff',
                'geomAlbedo', 'impKeff', 'nubar',
                }

        self.expectedKeff = array([1.15295E+00, 0.00094])
        self.expectedDays = array([])

        self.expectedInfExp = {
                'infAbs', 'infCapt', 'infChid', 'infChip', 'infChit',
                'infDiffcoef', 'infFiss', 'infFissFlx', 'infFlx',
                'infInvv', 'infKappa', 'infKinf', 'infMicroFlx',
                'infNsf', 'infNubar', 'infRabsxs', 'infRemxs',
                'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5',
                'infS6', 'infS7', 'infScatt0', 'infScatt1',
                'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5',
                'infScatt6', 'infScatt7', 'infTot', 'infTranspxs',
                }
        self.expectedUnivgcData = {
                'cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY',
                'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                'cmmTranspxsY', 'cmmTranspxsZ',
                }
        self.expectedCMM = array([1.80522E-01, 4.44568E-01])
        self.expectedCMMunc = array([0.00181, 0.01952])
        self.expectedMicroGroups = (
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
        self.expectedGroups = array(
                [1.00000E+37, 6.25000E-07, 0.00000E+00])
        self.expectedInfVals = array([8.71807E+14, 4.80974E+13])
        self.expectedInfUnc = array([0.00097, 0.00121])


del TesterCommonResultsReader

if __name__ == '__main__':
    unittest.main()
