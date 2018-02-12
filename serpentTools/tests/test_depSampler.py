"""
Class for testing the DepletionSampler
"""
import unittest
from os import path

from six import iteritems
from numpy import where, fabs
from numpy.testing import assert_allclose

from serpentTools.messages import MismatchedContainersError
from serpentTools.parsers.depletion import DepletionReader
from serpentTools.samplers.depletion import DepletionSampler
from serpentTools.tests import TEST_ROOT, computeMeansErrors

_testFileNames = {'0', '1', 'badInventory', 'longT', 'missingT'}
DEP_FILES = {key: path.join(TEST_ROOT, 'bwr_{}_dep.m'.format(key))
             for key in _testFileNames}


class DepletionSamplerFailTester(unittest.TestCase):

    def test_badInventory(self):
        """Verify an error is raised for files with dissimilar isotopics"""
        self._mismatchedFiles(DEP_FILES['badInventory'])

    def test_missingTimeSteps(self):
        """Verify an error is raised if length of time steps are dissimilar"""
        self._mismatchedFiles(DEP_FILES['missingT'])

    def _mismatchedFiles(self, badFilePath,
                         errorType=MismatchedContainersError):
        files = [badFilePath, DEP_FILES['0']]
        with self.assertRaises(errorType):
            DepletionSampler(files)


class DepletedSamplerTester(unittest.TestCase):
    """
    Class that reads two similar files and validates the averaging
    and uncertainty propagation.
    """

    def setUp(self):
        self.reader0 = DepletionReader(DEP_FILES['0'])
        self.reader0.read()
        self.reader1 = DepletionReader(DEP_FILES['0'])
        self.reader1.read()
        self.sampler = DepletionSampler([DEP_FILES[x] for x in ('0', '1')])

    def test_depSamplerValidCalcs(self):
        """
        Run through all variables and materials and check error propagation
        and averaging.
        """
        errMsg = "{varN} {qty} for material {matN}"
        for name, material in self.sampler.iterMaterials():
            for varName, varData in iteritems(material.data):
                r0 = self.reader0.materials[name].data[varName]
                r1 = self.reader1.materials[name].data[varName]
                samplerUnc = material.uncertainties[varName]
                expectedMean, expectedStd = computeMeansErrors(r0, r1)
                for qty, actual, expected in zip(('mean', 'uncertainty'),
                                                 (varData, samplerUnc),
                                                 (expectedMean, expectedStd)):
                    msg = errMsg.format(qty=qty, varN=varName, matN=material)
                    try:
                        assert_allclose(actual, expected, err_msg=msg)
                    except AssertionError as ae:
                        for aRow, eRow in zip(actual, expected):
                            print('Actual:   ', aRow)
                            print('Expected: ', eRow)
                            den = aRow.copy()
                            den[where(den == 0)] = 1
                            rDiff = (fabs(aRow - eRow)
                                     / den)
                            print('Relative: ', rDiff)

                        raise ae


if __name__ == '__main__':
    unittest.main()
