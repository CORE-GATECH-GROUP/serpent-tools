"""
Test the branching collector
"""

from unittest import TestCase
from serpentTools.xs import BranchCollector
from serpentTools.data import readDataFile
from numpy import ones, array


class BranchCollectorTester(TestCase):
    """Class that tests the branching collector"""

    @classmethod
    def setUpClass(cls):
        cls.reader = readDataFile('demo.coe')

    def setUp(self):
        self.collector = BranchCollector(self.reader)
        self.collector.collect(('BOR', 'TFU'), 'inf')

    def test_setPert(self):
        """Test the ability to change perts attribute"""
        lenCur = len(self.collector.perts)
        goodVals = [True, ] * lenCur
        self.collector.perts = goodVals
        badVals0 = [True, ] * (lenCur - 1)
        badVals1 = [True, ] * (lenCur + 1)
        with self.assertRaises(ValueError):
            self.collector.perts = badVals0
        with self.assertRaises(ValueError):
            self.collector.perts = badVals1

    def test_setPertStates(self):
        """Test the ability to change pertStates attribute"""
        asNpArray = array(self.collector.pertStates)
        self.collector.pertStates = asNpArray
        badShapes = [ones(dim + 1) for dim in asNpArray.shape]
        with self.assertRaises(ValueError):
            self.collector.pertStates = badShapes


if __name__ == '__main__':
    from unittest import main
    main()
