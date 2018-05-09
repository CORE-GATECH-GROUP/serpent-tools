"""Test the results reader."""

import os
import unittest

import numpy

import six

from serpentTools.settings import rc
from serpentTools.tests import TEST_ROOT
from serpentTools.parsers import ResultsReader
from serpentTools.messages import SerpentToolsException

class _ResultsTesterHelperFull(unittest.TestCase):
    """Test case to share setUpClass for testing Results Reader"""
    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'pwr_res_filter.m')
        # universe id, burnup, step, days
        cls.expectedStates = (('0', 0.0, 1, 0.0), ('0', 500, 2, 5.0))
        cls.reader = ResultsReader(cls.file)
        cls.reader.read()

class _ResultsTesterHelper(unittest.TestCase):
    """Test case to share setUpClass for testing Results Reader"""
    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'pwr_res.m')
        # universe id, burnup, step, days
        cls.expectedStates = (('0', 0.0, 1, 0.0), ('0', 500, 2, 5.0))
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['versions', 'gc-meta', 'xs',
                                       'diffusion', 'eig', 'burnup-coeff']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            cls.reader = ResultsReader(cls.file)
        cls.reader.read()

class ResultsTester(_ResultsTesterHelper):
    """Class for testing the results reader."""

    def test_raiseError(self):
        """Verify that the reader raises an error for unexpected EOF"""
        badFile = os.path.join(TEST_ROOT, 'bad_results_file.m')
        with open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(str(_line))
        badReader = ResultsReader(badFile)
        with self.assertRaises(SerpentToolsException):
            badReader.read()
        os.remove(badFile)

    def test_variables(self):
        """Verify that the correct settings and variables are obtained."""
        expected = {'VERSION', 'COMPILE_DATE', 'DEBUG', 'TITLE',
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
                    'COEF_IDX', 'COEF_BRANCH', 'COEF_BU_STEP'}
        self.assertSetEqual(expected, self.reader.settings['variables'])

    def test_metadata(self):
        """Test the metadata storage for the reader."""
        expectedMetadata = {'version': 'Serpent 2.1.29',
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
        expectedKeys = set(expectedMetadata)
        actualKeys = set(self.reader.metadata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        for key, expectedValue in six.iteritems(expectedMetadata):
            if isinstance(expectedValue, str):
                self.assertSetEqual(set(self.reader.metadata[key]),
                                       set(expectedValue))
            else:
                numpy.testing.assert_equal(self.reader.metadata[key],
                                       expectedValue)

    def test_resdata(self):
        """Test the resdata storage for the reader."""
        expectedResdata = ['absKeff', 'absKinf', 'anaKeff', 'burnDays', 'burnMaterials', 'burnMode', 'burnStep',
                           'burnup', 'colKeff', 'geomAlbedo', 'impKeff', 'nubar']

        expectedKeff =  numpy.array([[9.91938E-01, 0.00145],[1.81729E-01, 0.00240]])
        expectedDays = numpy.array([[0.00000E+00], [5.00000E+00]])
        expectedKeys = set(expectedResdata)
        actualKeys = set(self.reader.resdata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        numpy.testing.assert_equal(self.reader.resdata['absKeff'],
                                   expectedKeff)
        numpy.testing.assert_equal(self.reader.resdata['burnDays'],
                                   expectedDays)

    def test_univdata(self):
        """Verify that the correct universes and values are present."""
        expectedInfExp= ['infAbs', 'infCapt', 'infChid', 'infChip', 'infChit', 'infDiffcoef', 'infFiss', 'infFissFlx',
                           'infFlx', 'infInvv', 'infKappa', 'infKinf', 'infMicroFlx', 'infNsf', 'infNubar', 'infRabsxs',
                           'infRemxs', 'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5', 'infS6', 'infS7',
                           'infScatt0', 'infScatt1', 'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5', 'infScatt6',
                           'infScatt7', 'infTot', 'infTranspxs']
        expectedMetaData = ['cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY', 'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                            'cmmTranspxsY', 'cmmTranspxsZ', 'macroE', 'macroNg', 'microE', 'microNg']
        expectedinfValAbsSt0 = numpy.array([1.05040E-02, 1.23260E-01])
        expectedinfValAbsSt1 = numpy.array([1.01031E-02, 5.62564E-02])
        expectedinfUncAbsUn0 = numpy.array([0.00482, 0.00202])
        expectedinfUncAbsUn1 = numpy.array([0.00156, 0.00071])
        actualStates = set(self.reader.univdata.keys())
        self.assertSetEqual(set(self.expectedStates), actualStates)   # check that all states are read
        self.assertSetEqual(set(self.reader.univdata[self.expectedStates[1]].infExp.keys()),
                            set(expectedInfExp))
        self.assertSetEqual(set(self.reader.univdata[self.expectedStates[1]].metadata.keys()),
                            set(expectedMetaData))
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[0]].infExp['infAbs'],
                                   expectedinfValAbsSt0)
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[1]].infExp['infAbs'],
                                   expectedinfValAbsSt1)
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[0]].infUnc['infAbs'],
                                   expectedinfUncAbsUn0)
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[1]].infUnc['infAbs'],
                                   expectedinfUncAbsUn1)


class ResultsTesterFull(_ResultsTesterHelperFull):
    """Class for testing the results reader."""

    def test_raiseError(self):
        """Verify that the reader raises an error for unexpected EOF"""
        badFile = os.path.join(TEST_ROOT, 'bad_results_file.m')
        with open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(str(_line))
        badReader = ResultsReader(badFile)
        with self.assertRaises(SerpentToolsException):
            badReader.read()
        os.remove(badFile)

    def test_variables(self):
        """Verify that the correct settings and variables are obtained."""
        expected = {}
        self.assertSetEqual(set(expected), self.reader.settings['variables'])

    def test_metadata(self):
        """Test the metadata storage for the reader."""
        expectedMetadata = {'version': 'Serpent 2.1.29',
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
        expectedKeys = set(expectedMetadata)
        actualKeys = set(self.reader.metadata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        for key, expectedValue in six.iteritems(expectedMetadata):
            if isinstance(expectedValue, str):
                self.assertSetEqual(set(self.reader.metadata[key]),
                                       set(expectedValue))
            else:
                numpy.testing.assert_equal(self.reader.metadata[key],
                                       expectedValue)

    def test_resdata(self):
        """Test the resdata storage for the reader."""
        expectedResdata = ['absKeff', 'absKinf', 'anaKeff', 'burnDays', 'burnMaterials', 'burnMode', 'burnStep',
                           'burnup', 'colKeff', 'geomAlbedo', 'impKeff', 'nubar', 'minMacroxs']

        expectedKeff =  numpy.array([[9.91938E-01, 0.00145],[1.81729E-01, 0.00240]])
        expectedDays = numpy.array([[0.00000E+00], [5.00000E+00]])
        expectedKeys = set(expectedResdata)
        actualKeys = set(self.reader.resdata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        numpy.testing.assert_equal(self.reader.resdata['absKeff'],
                                   expectedKeff)
        numpy.testing.assert_equal(self.reader.resdata['burnDays'],
                                   expectedDays)

    def test_univdata(self):
        """Verify that the correct universes and values are present."""
        expectedInfExp= ['infAbs', 'infCapt', 'infChid', 'infChip', 'infChit', 'infDiffcoef', 'infFiss', 'infFissFlx',
                           'infFlx', 'infInvv', 'infKappa', 'infKinf', 'infMicroFlx', 'infNsf', 'infNubar', 'infRabsxs',
                           'infRemxs', 'infS0', 'infS1', 'infS2', 'infS3', 'infS4', 'infS5', 'infS6', 'infS7',
                           'infScatt0', 'infScatt1', 'infScatt2', 'infScatt3', 'infScatt4', 'infScatt5', 'infScatt6',
                           'infScatt7', 'infTot', 'infTranspxs']
        expectedMetaData = ['cmmDiffcoef', 'cmmDiffcoefX', 'cmmDiffcoefY', 'cmmDiffcoefZ', 'cmmTranspxs', 'cmmTranspxsX',
                            'cmmTranspxsY', 'cmmTranspxsZ', 'macroE', 'macroNg', 'microE', 'microNg']
        expectedinfValAbsSt0 = numpy.array([1.05040E-02, 1.23260E-01])
        expectedinfValAbsSt1 = numpy.array([1.01031E-02, 5.62564E-02])
        expectedinfUncAbsUn0 = numpy.array([0.00482, 0.00202])
        expectedinfUncAbsUn1 = numpy.array([0.00156, 0.00071])
        actualStates = set(self.reader.univdata.keys())
        self.assertSetEqual(set(self.expectedStates), actualStates)   # check that all states are read
        self.assertSetEqual(set(self.reader.univdata[self.expectedStates[1]].infExp.keys()),
                            set(expectedInfExp))
        self.assertSetEqual(set(self.reader.univdata[self.expectedStates[1]].metadata.keys()),
                            set(expectedMetaData))
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[0]].infExp['infAbs'],
                                   expectedinfValAbsSt0)
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[1]].infExp['infAbs'],
                                   expectedinfValAbsSt1)
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[0]].infUnc['infAbs'],
                                   expectedinfUncAbsUn0)
        numpy.testing.assert_equal(self.reader.univdata[self.expectedStates[1]].infUnc['infAbs'],
                                   expectedinfUncAbsUn1)


if __name__ == '__main__':
    unittest.main()
