"""
Class for testing the DepletionSampler

File Descriptions
-----------------

*. ``bwr_0`` and ``bwr_1`` are identical input files with
   different seeds. The detectors are defined exactly the same.
*. ``bwr_badInventory`` has a different nuclide inventory
   than ``bwr_0``, which would create data matrices such as ``adens``
   of different sizes, breaking the sampling routines
*. ``bwr_longT`` has a much longer final burn step, but equal number
   of burnup steps.
*. ``bwr_missingT`` is missing the final burnup step

"""
from unittest import TestCase

from numpy import where, fabs, ndarray
from numpy.testing import assert_allclose

from serpentTools.messages import MismatchedContainersError, critical
from serpentTools.data import getFile
from serpentTools.parsers.depletion import DepletionReader
from serpentTools.samplers.depletion import DepletionSampler

from tests import computeMeansErrors, TestCaseWithLogCapture

_testFileNames = {'0', '1', 'badInventory', 'longT', 'missingT'}
DEP_FILES = {key: getFile('bwr_{}_dep.m'.format(key))
             for key in _testFileNames}


class DepletionSamplerFailTester(TestCaseWithLogCapture):

    def test_badInventory(self):
        """Verify an error is raised for files with dissimilar isotopics"""
        self._mismatchedFiles(DEP_FILES['badInventory'])
        self.assertMsgInLogs("ERROR", DEP_FILES['badInventory'], partial=True)

    def test_missingTimeSteps(self):
        """Verify an error is raised if length of time steps are dissimilar"""
        self._mismatchedFiles(DEP_FILES['missingT'])
        self.assertMsgInLogs("ERROR", DEP_FILES['missingT'], partial=True)

    def _mismatchedFiles(self, badFilePath,
                         errorType=MismatchedContainersError):
        files = [badFilePath, DEP_FILES['0']]
        with self.assertRaises(errorType):
            DepletionSampler(files)


class DepletedSamplerTester(TestCase):
    """
    Class that reads two similar files and validates the averaging
    and uncertainty propagation.
    """

    def setUp(self):
        self.reader0 = DepletionReader(DEP_FILES['0'])
        self.reader0.read()
        self.reader1 = DepletionReader(DEP_FILES['1'])
        self.reader1.read()
        self.sampler = DepletionSampler([DEP_FILES[x] for x in ('0', '1')])

    def test_depSamplerValidCalcs(self):
        """
        Run through all variables and materials and check error propagation
        and averaging.
        """
        errMsg = "{varN} {qty} for material {matN}"
        for name, material in self.sampler.iterMaterials():
            for varName, varData in material.data.items():
                r0 = self.reader0.materials[name].data[varName]
                r1 = self.reader1.materials[name].data[varName]
                samplerUnc = material.uncertainties[varName]
                expectedMean, expectedStd = computeMeansErrors(r0, r1)
                for qty, actual, expected in zip(('mean', 'uncertainty'),
                                                 (varData, samplerUnc),
                                                 (expectedMean, expectedStd)):
                    msg = errMsg.format(qty=qty, varN=varName, matN=material)
                    try:
                        assert_allclose(actual, expected, err_msg=msg,
                                        rtol=1E-5)
                    except AssertionError as ae:
                        critical("\nMaterial {} - value {}".format(
                            name, varName))
                        for aRow, eRow in zip(actual, expected):
                            critical('Actual:   {}'.format(aRow))
                            critical('Expected: {}'.format(eRow))
                            den = aRow.copy()
                            if isinstance(den, ndarray):
                                den[where(den == 0)] = 1
                            else:
                                den = den or 1
                            rDiff = (fabs(aRow - eRow)
                                     / den)
                            critical('Relative: {}'.format(rDiff))

                        raise ae

    def test_getitem(self):
        """Verify the getitem method for extracting materials."""
        with self.assertRaises(KeyError):
            self.sampler['this should fail']
        for name, mat in self.sampler.materials.items():
            fromGetItem = self.sampler[name]
            self.assertIs(fromGetItem, mat, msg=name)
