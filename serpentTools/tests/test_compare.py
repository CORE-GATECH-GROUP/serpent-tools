"""
Test object-level compare methods
"""

from serpentTools.tests.utils import TestCaseWithLogCapture
from serpentTools.data import readDataFile


RES_DATA_FILE = 'pwr_res.m'
# strings that should appear in specific logging messages after formatted
# with a single value key
IDENTICAL_KEY_FMT = "for {} are identical"
OVERLAPPING_KEY_FMT = "{} overlap"
WITHIN_TOLS_KEY_FMT = "{} are different, but within tolerance"
OUTSIDE_TOLS_KEY_FMT = "{} are outside acceptable tolerances"


class ResultsCompareTester(TestCaseWithLogCapture):
    """
    Test the ResultsReader comparison methods
    """

    @classmethod
    def setUpClass(cls):
        cls.r0 = readDataFile(RES_DATA_FILE)
        cls.resultsKeys = set(cls.r0.resdata.keys())
        cls.univKeys = set()
        for univ in cls.r0.universes.values():
            cls.univKeys.update(set(univ.infExp.keys()))
            cls.univKeys.update(set(univ.b1Exp.keys()))
            cls.univKeys.update(set(univ.gc.keys()))
            break

    def setUp(self):
        self.r1 = readDataFile(RES_DATA_FILE)
        TestCaseWithLogCapture.setUp(self)

    def _runCompare(self, verbosity):
        return self.r0.compare(self.r1, verbosity=verbosity)

    def test_fullCompare(self):
        """Test the primary comparison method with no modifications."""
        out = self._runCompare('debug')
        self.assertTrue(out, msg="Result from comparison")
        self.assertMsgInLogs('DEBUG', 'Updated setting verbosity to debug')
        for resKey in self.resultsKeys:
            self.assertMsgInLogs('DEBUG', IDENTICAL_KEY_FMT.format(resKey),
                                 partial=True)

    def test_moddedResults(self):
        """
        Verify that the results comparison logs errors in modified data.
        """
        resd = self.r1.resdata
        # drastically increase one value with uncertainties
        # to ensure disagreement
        resd['anaKeff'][:, ::2] *= 2
        # slightly modify one value with uncertainties to force overlapping
        # confidence intervals, but not identical quantities
        resd['colKeff'][:, ::2] *= 1.01
        resd['colKeff'][:, 1::2] *= 1.05
        # modify a value w/o uncertainties slightly
        resd['allocMemsize'] *= 1.01
        # drastically modify a value w/o uncertainties
        resd['uresAvail'] *= -2
        out = self._runCompare('debug')
        self.assertFalse(out)
        self.assertMsgInLogs('ERROR', 'anaKeff', partial=True)
        self.assertMsgInLogs(
            'DEBUG', OVERLAPPING_KEY_FMT.format('colKeff'), partial=True)
        self.assertMsgInLogs(
            'WARNING', WITHIN_TOLS_KEY_FMT.format('allocMemsize'),
            partial=True)
        self.assertMsgInLogs(
            'ERROR', OUTSIDE_TOLS_KEY_FMT.format('uresAvail'), partial=True)


if __name__ == '__main__':
    from unittest import main
    main()
