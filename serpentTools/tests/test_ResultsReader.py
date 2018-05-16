"""Test the results reader."""

import os
import unittest

import numpy

import six

from serpentTools.settings import rc
from serpentTools.tests import TEST_ROOT
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
        """Verify that the reader raises error when no results exist in the file"""
        badFile = os.path.join(TEST_ROOT, 'bad_results_file.m')
        with open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(str(_line))
        badReader = ResultsReader(badFile)
        with self.assertRaises(SerpentToolsException):
            badReader.read()
        os.remove(badFile)

    def test_noUniverses(self):
        """Verify that the reader raises an error if no universes are stored on the file"""
        univFile = os.path.join(TEST_ROOT, 'pwr_res_noUniv.m')
        univReader = ResultsReader(univFile)
        with self.assertRaises(SerpentToolsException):
            univReader.read()

class TestGetUniv(unittest.TestCase):
    """
    Test the getUniv method.

    Tests:
        1. test_allVarsNone: burnup, index and timeDays are all set to None
        2. test_nonPostiveIndex: index is zero or negative
        3. test_noUnivState: define ('0',bu,idx,days) a non-existing state
        4. test_validUniv: test that a valid universe state contains proper data

    Raises  SerpentToolsException
                    All variables are set to None
            KeyError
                    index is non-positive
                    no universe state exist in the reader
    """
    def setUp(self):
        self.file = os.path.join(TEST_ROOT, 'pwr_res.m')
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            self.reader = ResultsReader(self.file)
            self.reader.read()
        self.expectedinfValAbs = numpy.array([1.05040E-02, 1.23260E-01])

    def test_allVarsNone(self):
        """Verify that the reader raises error when no time parameters are given"""
        with self.assertRaises(SerpentToolsException):
            self.reader.getUniv('0', burnup=None, index=None, timeDays=None)

    def test_nonPostiveIndex(self):
        """Verify that the reader raises error when the time index is not positive"""
        with self.assertRaises(KeyError):
            self.reader.getUniv('0', burnup=None, index=0, timeDays=None)

    def test_noUnivState(self):
        """Verify that the reader raises error when the state tuple does not exist"""
        with self.assertRaises(KeyError):
            self.reader.getUniv('0', burnup=50, index=10, timeDays=5)

    def test_validUniv(self):
        """Verify that the reader raises error when the state tuple does not exist"""
        xsDict = self.reader.getUniv('0', burnup=0.0, index=1, timeDays=0.0)
        numpy.testing.assert_equal(xsDict.infExp['infAbs'],
                                   self.expectedinfValAbs)

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
        self.assertSetEqual(self.expVarSettings, self.reader.settings['variables'])

    def test_metadata(self):
        """Verify that user-defined metadata is properly stored."""
        expectedKeys = set(self.expectedMetadata)
        actualKeys = set(self.reader.metadata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        for key, expectedValue in six.iteritems(self.expectedMetadata):
            if isinstance(expectedValue, str):
                self.assertSetEqual(set(self.reader.metadata[key]),
                                       set(expectedValue))
            else:
                numpy.testing.assert_equal(self.reader.metadata[key],
                                       expectedValue)

    def test_resdata(self):
        """Verify that user-defined metadata is properly stored."""
        expectedKeys = self.expectedResdata
        actualKeys = set(self.reader.resdata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        numpy.testing.assert_equal(self.reader.resdata['absKeff'],
                                   self.expectedKeff)
        try:
            numpy.testing.assert_equal(self.reader.resdata['burnDays'],
                                   self.expectedDays)
        except:
            numpy.testing.assert_equal([], self.expectedDays)

    def test_universes(self):
        """Verify that results for all the states ('univ', bu, buIdx, days) exist.
            Verify that the containers for each state are properly created
            and that the proper information is stored, e.g. infExp keys and values"""
        expSt0 = self.expectedStates[0]
        actualStates = set(self.reader.universes.keys())
        self.assertSetEqual(set(self.expectedStates), actualStates)   # check that all states are read
        self.assertSetEqual(set(self.reader.universes[expSt0].infExp.keys()),
                            self.expectedInfExp)
        self.assertSetEqual(set(self.reader.universes[expSt0].metadata.keys()),
                            self.expectedUnivMetaData)
        numpy.testing.assert_equal(self.reader.universes[expSt0].infExp['infAbs'],
                                   self.expectedinfValAbs)
        numpy.testing.assert_equal(self.reader.universes[expSt0].infUnc['infAbs'],
                                   self.expectedinfUncAbs)


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
        self.file = os.path.join(TEST_ROOT, 'pwr_res.m')
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

        self.expVarSettings = set({'VERSION', 'COMPILE_DATE', 'DEBUG', 'TITLE',
                    'CONFIDENTIAL_DATA', 'INPUT_FILE_NAME', 'WORKING_DIRECTORY',
                    'HOSTNAME', 'CPU_TYPE', 'CPU_MHZ', 'START_DATE', 'COMPLETE_DATE',
                    'GC_UNIVERSE_NAME', 'MICRO_NG', 'MICRO_E', 'MACRO_NG',
                    'MACRO_E', 'INF_MICRO_FLX','INF_KINF', 'INF_FLX',
                    'INF_FISS_FLX', 'TOT', 'CAPT', 'ABS', 'FISS', 'NSF',
                    'NUBAR', 'KAPPA', 'INVV', 'TRANSPXS', 'DIFFCOEF', 'RABSXS',
                    'REMXS', 'SCATT0', 'SCATT1', 'SCATT2', 'SCATT3', 'SCATT4',
                    'SCATT5', 'SCATT6', 'SCATT7', 'S0', 'S1', 'S2', 'S3', 'S4',
                    'S5', 'S6', 'S7', 'CHIT', 'CHIP', 'CHID', 'CMM_TRANSPXS',
                    'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y', 'CMM_TRANSPXS_Z',
                    'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X', 'CMM_DIFFCOEF_Y',
                    'CMM_DIFFCOEF_Z', 'ANA_KEFF', 'IMP_KEFF', 'COL_KEFF',
                    'ABS_KEFF', 'ABS_KINF', 'GEOM_ALBEDO', 'BURN_MATERIALS',
                    'BURN_MODE', 'BURN_STEP', 'BURNUP', 'BURN_DAYS',
                    'COEF_IDX', 'COEF_BRANCH', 'COEF_BU_STEP'})

        self.expectedMetadata = {'version': 'Serpent 2.1.29',
                            'compileDate': 'Jan  4 2018 17:22:46',
                            'debug': [0.],
                            'title': 'pwr pin',
                            'confidentialData': [0.],
                            'inputFileName': 'pwrPin',
                            'workingDirectory': '/home/ajohnson400/research/gpt-dep/testing/depmtx',
                            'hostname': 'ME04L0358GRD04',
                            'cpuType': 'Intel(R) Core(TM) i7-6700T CPU @ 2.80GHz',
                            'cpuMhz': [194.],
                            'startDate': 'Mon Feb 19 15:39:23 2018',
                            'completeDate': 'Mon Feb 19 15:39:53 2018'}

        self.expectedResdata = set(['absKeff', 'absKinf', 'anaKeff', 'burnDays', 'burnMaterials', 'burnMode', 'burnStep',
                           'burnup', 'colKeff', 'geomAlbedo', 'impKeff', 'nubar'])

        self.expectedKeff = numpy.array([[9.91938E-01, 0.00145],[1.81729E-01, 0.00240]])
        self.expectedDays = numpy.array([[0.00000E+00], [5.00000E+00]])

        self.expectedInfExp= set(['infAbs', 'infCapt', 'infChid', 'infChip', 'infChit', 'infDiffcoef', 'infFiss', 'infFissFlx',
                           'infFlx', 'infInvv', 'infKappa', 'infKinf', 'infMicroFlx', 'infNsf', 'infNubar', 'infRabsxs',
                           'infRemxs', 'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5', 'infS6', 'infS7',
                           'infScatt0', 'infScatt1', 'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5', 'infScatt6',
                           'infScatt7', 'infTot', 'infTranspxs'])
        self.expectedUnivMetaData = set(['cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY', 'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                            'cmmTranspxsY', 'cmmTranspxsZ', 'macroE', 'macroNg', 'microE', 'microNg'])
        self.expectedinfValAbs = numpy.array([1.05040E-02, 1.23260E-01])
        self.expectedinfUncAbs = numpy.array([0.00482, 0.00202])


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
        self.file = os.path.join(TEST_ROOT, 'pwr_res_filter.m')
        # universe id, burnup, step, days
        with rc:
            rc['serpentVersion'] = '2.1.29'
            self.expectedStates = (('0', 0.0, 1, 0.0), ('0', 500, 2, 5.0))
            self.reader = ResultsReader(self.file)
            self.reader.read()

        self.expVarSettings = set()

        self.expectedMetadata = {'version': 'Serpent 2.1.29',
                            'compileDate': 'Jan  4 2018 17:22:46',
                            'debug': [0.],
                            'title': 'pwr pin',
                            'confidentialData': [0.],
                            'inputFileName': 'pwrPin',
                            'workingDirectory': '/home/ajohnson400/research/gpt-dep/testing/depmtx',
                            'hostname': 'ME04L0358GRD04',
                            'cpuType': 'Intel(R) Core(TM) i7-6700T CPU @ 2.80GHz',
                            'cpuMhz': [194.],
                            'startDate': 'Mon Feb 19 15:39:23 2018',
                            'completeDate': 'Mon Feb 19 15:39:53 2018'}

        self.expectedResdata = set(['absKeff', 'absKinf', 'anaKeff', 'burnDays', 'burnMaterials', 'burnMode', 'burnStep',
                           'burnup', 'colKeff', 'geomAlbedo', 'impKeff', 'nubar', 'minMacroxs'])

        self.expectedKeff = numpy.array([[9.91938E-01, 0.00145],[1.81729E-01, 0.00240]])
        self.expectedDays = numpy.array([[0.00000E+00], [5.00000E+00]])

        self.expectedInfExp= set(['infAbs', 'infCapt', 'infChid', 'infChip', 'infChit', 'infDiffcoef', 'infFiss', 'infFissFlx',
                           'infFlx', 'infInvv', 'infKappa', 'infKinf', 'infMicroFlx', 'infNsf', 'infNubar', 'infRabsxs',
                           'infRemxs', 'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5', 'infS6', 'infS7',
                           'infScatt0', 'infScatt1', 'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5', 'infScatt6',
                           'infScatt7', 'infTot', 'infTranspxs'])
        self.expectedUnivMetaData = set(['cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY', 'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                            'cmmTranspxsY', 'cmmTranspxsZ', 'macroE', 'macroNg', 'microE', 'microNg'])
        self.expectedinfValAbs = numpy.array([1.05040E-02, 1.23260E-01])
        self.expectedinfUncAbs = numpy.array([0.00482, 0.00202])


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
        self.file = os.path.join(TEST_ROOT, 'pwr_res_noBU.m')
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

        self.expVarSettings = set({'VERSION', 'COMPILE_DATE', 'DEBUG', 'TITLE',
                    'CONFIDENTIAL_DATA', 'INPUT_FILE_NAME', 'WORKING_DIRECTORY',
                    'HOSTNAME', 'CPU_TYPE', 'CPU_MHZ', 'START_DATE', 'COMPLETE_DATE',
                    'GC_UNIVERSE_NAME', 'MICRO_NG', 'MICRO_E', 'MACRO_NG',
                    'MACRO_E', 'INF_MICRO_FLX','INF_KINF', 'INF_FLX',
                    'INF_FISS_FLX', 'TOT', 'CAPT', 'ABS', 'FISS', 'NSF',
                    'NUBAR', 'KAPPA', 'INVV', 'TRANSPXS', 'DIFFCOEF', 'RABSXS',
                    'REMXS', 'SCATT0', 'SCATT1', 'SCATT2', 'SCATT3', 'SCATT4',
                    'SCATT5', 'SCATT6', 'SCATT7', 'S0', 'S1', 'S2', 'S3', 'S4',
                    'S5', 'S6', 'S7', 'CHIT', 'CHIP', 'CHID', 'CMM_TRANSPXS',
                    'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y', 'CMM_TRANSPXS_Z',
                    'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X', 'CMM_DIFFCOEF_Y',
                    'CMM_DIFFCOEF_Z', 'ANA_KEFF', 'IMP_KEFF', 'COL_KEFF',
                    'ABS_KEFF', 'ABS_KINF', 'GEOM_ALBEDO', 'BURN_MATERIALS',
                    'BURN_MODE', 'BURN_STEP', 'BURNUP', 'BURN_DAYS',
                    'COEF_IDX', 'COEF_BRANCH', 'COEF_BU_STEP'})

        self.expectedMetadata = {'version': 'Serpent 2.1.30',
                            'compileDate': 'Apr  4 2018 08:55:27',
                            'debug': [0.],
                            'title': 'UO2 PIN MODEL',
                            'confidentialData': [0.],
                            'inputFileName': 'pwr',
                            'workingDirectory': '/gpfs/pace1/project/me-kotlyar/dkotlyar6/Research/Serpent_test/FP_test',
                            'hostname': 'rich133-c36-10-l.pace.gatech.edu',
                            'cpuType': 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz',
                            'cpuMhz': [184549409.0],
                            'startDate': 'Mon May 14 11:20:06 2018',
                            'completeDate': 'Mon May 14 11:20:36 2018'}

        self.expectedResdata = set(['absKeff', 'absKinf', 'anaKeff', 'colKeff', 'geomAlbedo', 'impKeff', 'nubar'])

        self.expectedKeff = numpy.array([1.15295E+00, 0.00094])
        self.expectedDays = numpy.array([])

        self.expectedInfExp= set(['infAbs', 'infCapt', 'infChid', 'infChip', 'infChit', 'infDiffcoef', 'infFiss', 'infFissFlx',
                           'infFlx', 'infInvv', 'infKappa', 'infKinf', 'infMicroFlx', 'infNsf', 'infNubar', 'infRabsxs',
                           'infRemxs', 'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5', 'infS6', 'infS7',
                           'infScatt0', 'infScatt1', 'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5', 'infScatt6',
                           'infScatt7', 'infTot', 'infTranspxs'])
        self.expectedUnivMetaData = set(['cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY', 'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                            'cmmTranspxsY', 'cmmTranspxsZ', 'macroE', 'macroNg', 'microE', 'microNg'])
        self.expectedinfValAbs = numpy.array([9.16972E-03, 8.66231E-02])
        self.expectedinfUncAbs = numpy.array([0.00090, 0.00129])


del TesterCommonResultsReader

if __name__ == '__main__':
    unittest.main()
