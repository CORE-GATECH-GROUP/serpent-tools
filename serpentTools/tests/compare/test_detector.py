"""
Test the comparison utilities for detectors
"""

from serpentTools.tests.utils import TestCaseWithLogCapture
from serpentTools import readDataFile

TEST_FILE = 'bwr_det0.m'
DET_TO_MODIFY = 'xymesh'
UNMODIFIED_DETS = [
    'spectrum',
]
# All other detectors that shall be unmodified


def compareObjs(ref, other):
    """Fixture to call identical comparisons across tests."""
    return ref.compare(other, verbosity='debug')


class DetCompareHelper(TestCaseWithLogCapture):
    """
    Helper case for testing the detector compare methods

    setUpClass:
        *. Read the ``bwr_det0.m`` file
        *. Store this reader on the class

    setUp:
        *. Read the same file, but store this reader as the
           one to mess up.
        *. Call setUp from TestCaseWithLogCapture to capture
           log messages
    """

    @classmethod
    def setUpClass(cls):
        cls.refReader = readDataFile(TEST_FILE)
        cls.refDetector = cls.refReader.detectors[DET_TO_MODIFY]

    def setUp(self):
        TestCaseWithLogCapture.setUp(self)
        self.otherReader = readDataFile(TEST_FILE)
        self.otherDetector = self.otherReader.detectors[DET_TO_MODIFY]


class DetGridsCompareTester(DetCompareHelper):
    """
    Tweak the grid structure on a detector and ensure that logs
    capture this.
    """

    GRID_FMT = "Values for {} are {}"

    def setUp(self):
        DetCompareHelper.setUp(self)
        self.gridKeys = sorted(list(self.refDetector.grids.keys()))

    def test_identicalGrids(self):
        """Verify that the inner grid compare works."""
        similar = compareObjs(self.refDetector, self.otherDetector)
        self.assertTrue(similar, msg='output from comparison')
        for gridKey in self.gridKeys:
            self.assertMsgInLogs(
                "DEBUG", self.GRID_FMT.format(gridKey, 'identical'),
                partial=True)

    def test_modifiedGrids(self):
        """Pick up on some errors due to modified grids."""
        # Changes
        # X grid unchanged
        # E grid slightly modified, but inside tolerances
        # Y grid modified to be outside tolerances
        # Z grid set to be of different shape
        # Added a bad grid that should not exist in the reference
        grids = self.otherDetector.grids
        missingKey = 'NOT PRESENT'
        grids['E'] *= 1.05
        grids['Z'] = grids['X']
        grids['Y'] *= 2
        grids[missingKey] = list(range(5))
        similar = compareObjs(self.refDetector, self.otherDetector)
        self.assertFalse(similar,
                         msg="Mismatched grids did not induce failure.")
        self.assertMsgInLogs(
            "WARNING",
            self.GRID_FMT.format('E', 'different, but within tolerances'),
            partial=True)
        self.assertMsgInLogs(
            "ERROR",
            self.GRID_FMT.format('Y', 'outside acceptable tolerances'),
            partial=True)
        self.assertMsgInLogs(
            "ERROR",
            "Z: {} - {}".format(
                self.refDetector.grids['Z'].shape,
                grids['Z'].shape),
            partial=True)
        self.assertMsgInLogs(
            'DEBUG',
            self.GRID_FMT.format('X', 'identical'),
            partial=True)


class DetectorTallyTester(DetCompareHelper):
    """Class that modifies detector tallies prior to comparisons."""

    IDENTICAL_TALLY_MSG = "Expected values for tallies are identical"
    INSIDE_CONF_MSG = "Confidence intervals for tallies overlap"
    OUTISDE_CONF_MSG = ("Values for tallies are outside acceptable "
                        "statistical limits")

    def compare(self):
        return compareObjs(self.refDetector, self.otherDetector)

    def test_unmodifiedCompare(self):
        """Verify that w/o modifications the test passes"""
        similar = self.compare()
        self.assertTrue(similar)
        self.assertMsgInLogs(
            "DEBUG", self.IDENTICAL_TALLY_MSG,
            partial=True)

    def test_withinConfIntervals(self):
        """Verify that slight differences in tallies are logged."""
        self.otherDetector.tallies *= 1.01
        similar = self.compare()
        self.assertTrue(similar)
        self.assertMsgInLogs(
            "DEBUG", self.INSIDE_CONF_MSG, partial=True)

    def test_outsideConfIntervals(self):
        """Verify that large differences in tallies are logged."""
        self.otherDetector.tallies *= 2.0
        similar = self.compare()
        self.assertFalse(similar)
        self.assertMsgInLogs(
            "ERROR", self.OUTISDE_CONF_MSG, partial=True)

if __name__ == '__main__':
    from unittest import main
    main()
