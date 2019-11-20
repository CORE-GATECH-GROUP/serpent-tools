"""
Class for testing the detector sampler

File Descriptions
-----------------

*. ``bwr_0`` and ``bwr_1`` are identical input files with
   different seeds. The detectors are defined exactly the same.
*. ``bwr_noxy`` is the same file as ``bwr_0`` with the
   ``xymesh`` detector completely removed. All spatial and energy grid
   data is removed from this file as well
*. ``bwr_smallxy`` has the same detector definitions as
   ``bwr_0``, except the spatial grid for ``xymesh`` is smaller.

.. note::

    The relative error tolerances must be low, :math:`O(1)`, because the
    absolute error values themselves are low. In writing these tests,
    a relative error of 1E-2 resulted in a 5% difference between
    error quantities, which are all :math:`O(1E-3)`. A tight absolute
    tolerance can still be achieved.

"""
from numpy import square, sqrt
from numpy.testing import assert_allclose
from serpentTools.messages import MismatchedContainersError
from serpentTools.data import getFile
from serpentTools.parsers.detector import DetectorReader
from serpentTools.samplers.detector import DetectorSampler

from tests import TestCaseWithLogCapture

_DET_FILES = {
    'bwr0': 'bwr_0',
    'bwr1': 'bwr_1',
    'noxy': 'bwr_noxy',
    'smallxy': 'bwr_smallxy'
}
DET_FILES = {key: getFile(val + '_det0.m')
             for key, val in _DET_FILES.items()}

SQRT2 = sqrt(2)

TOLERANCES = {
    'errors': {'atol': 1E-16, 'rtol': 1},
    'tallies': {'atol': 0, 'rtol': 1E-7}
}


class DetSamplerTester(TestCaseWithLogCapture):
    """
    Tester that looks for errors in mismatched detector files
    and validates the averaging and uncertainty propagation
    """

    def _checkContents(self):
        single = set(self.singleReader.detectors.keys())
        sampler = set(self.sampler.detectors.keys())
        self.assertSetEqual(single, sampler)

    @classmethod
    def setUpClass(cls):
        cls.singleReader = DetectorReader(DET_FILES['bwr0'])
        cls.singleReader.read()
        cls.sampler = DetectorSampler(
            [DET_FILES['bwr{}'.format(d)] for d in (0, 1)])

    def setUp(self):
        self._checkContents()
        TestCaseWithLogCapture.setUp(self)

    def test_properlyAveraged(self):
        """Validate the averaging for two unique detector files"""
        r0 = self.singleReader
        r1 = DetectorReader(DET_FILES['bwr1'])
        r1.read()
        for detName in self.sampler.detectors:
            expectedTallies, expectedErrors = (_getExpectedAverages(
                r0.detectors[detName], r1.detectors[detName]))
            uniq = self.sampler.detectors[detName]
            assert_allclose(uniq.tallies, expectedTallies, err_msg='tallies',
                            **TOLERANCES['tallies'])
            assert_allclose(uniq.errors, expectedErrors, err_msg='errrors',
                            **TOLERANCES['errors'])

    def test_missingDetectors(self):
        """Verify that an error is raised if detectors are missing"""
        files = [getFile(fp)
                 for fp in ['bwr_0_det0.m', 'bwr_noxy_det0.m']]
        self._raisesMisMatchError(files)
        self.assertMsgInLogs("ERROR", "detectors: Parser files", partial=True)

    def test_differentSizedDetectors(self):
        """Verify that an error is raised if detector shapes are different"""
        files = [getFile(fp)
                 for fp in ['bwr_0_det0.m', 'bwr_smallxy_det0.m']]
        self._raisesMisMatchError(files)
        self.assertMsgInLogs(
            "ERROR", "shape: Parser files",
            partial=True)

    def _raisesMisMatchError(self, files):
        with self.assertRaises(MismatchedContainersError):
            DetectorSampler(files)

    def test_getitem(self):
        """Verify the getitem method for retrieving detectors works."""
        for name, det in self.sampler.detectors.items():
            fromGetItem = self.sampler[name]
            self.assertIs(det, fromGetItem, msg=name)
        with self.assertRaises(KeyError):
            self.sampler['this should fail']


def _getExpectedAverages(d0, d1):
    tallies = 0.5 * (d0.tallies + d1.tallies)
    errors = 0.5 * sqrt(square(d0.errors) + square(d1.errors))

    return tallies, errors
