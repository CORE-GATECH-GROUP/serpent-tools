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
        """Test the ability to change perturbations attribute"""
        lenCur = len(self.collector.perturbations)
        goodVals = [True, ] * lenCur
        self.collector.perturbations = goodVals
        badVals0 = [True, ] * (lenCur - 1)
        badVals1 = [True, ] * (lenCur + 1)
        with self.assertRaises(ValueError):
            self.collector.perturbations = badVals0
        with self.assertRaises(ValueError):
            self.collector.perturbations = badVals1

    def test_setPertStates(self):
        """Test the ability to change states attribute"""
        asNpArray = array(self.collector.states)
        self.collector.states = asNpArray
        badShapes = [ones(dim + 1) for dim in asNpArray.shape]
        with self.assertRaises(ValueError):
            self.collector.states = badShapes


if __name__ == '__main__':
    from unittest import main
    main()
