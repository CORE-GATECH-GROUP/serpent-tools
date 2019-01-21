"""
Test the branching collector
"""

from unittest import TestCase
from serpentTools.xs import BranchCollector
from serpentTools.data import readDataFile
from numpy import ones, array, arange
from numpy.testing import assert_array_equal


class BranchTestHelper(TestCase):
    """Helper class for testing branched collectors"""

    @classmethod
    def setUpClass(cls):
        cls.reader = readDataFile('demo.coe')

    def collect(self):
        """Return the collector after collecting gorup constants"""
        collector = BranchCollector(self.reader)
        collector.collect(("BOR", "TFU"), 'inf')
        return collector


class BranchAttrSetterTestHelper(BranchTestHelper):
    """
    Class that helps test the ability to set attributes on branched objects
    """

    def test_setPert(self):
        """Test the ability to change perturbations attribute"""
        lenCur = len(self.testObj.perturbations)
        goodVals = [True, ] * lenCur
        self.testObj.perturbations = goodVals
        badVals0 = [True, ] * (lenCur - 1)
        badVals1 = [True, ] * (lenCur + 1)
        with self.assertRaises(ValueError):
            self.testObj.perturbations = badVals0
        with self.assertRaises(ValueError):
            self.testObj.perturbations = badVals1

    def test_setPertStates(self):
        """Test the ability to change states attribute"""
        asNpArray = array(self.testObj.states)
        self.testObj.states = asNpArray
        badShapes = [ones(dim + 1) for dim in asNpArray.shape]
        with self.assertRaises(ValueError):
            self.testObj.states = badShapes

    def test_setAxis(self):
        """Test the ability to set the axis attribute"""
        goodAx = (None, ) * len(self.testObj.axis)
        self.testObj.axis = goodAx
        self.assertTrue(goodAx == self.testObj.axis)
        # convert to list, but axis converts back to tuple
        self.testObj.axis = list(goodAx)
        self.assertTrue(goodAx == self.testObj.axis)
        # misshapen axis object
        badAx = (None, ) * (len(goodAx) - 1)
        with self.assertRaises(ValueError):
            self.testObj.axis = badAx

    def test_setBurnup(self):
        """Test the ability to set the burnup attribute"""
        goodBurnup = arange(self.testObj.burnups.size)
        self.testObj.burnups = goodBurnup
        self.assertTrue(goodBurnup is self.testObj.burnups)
        # convert to list, but setter automatically converts to array
        self.testObj.burnups = list(goodBurnup)
        assert_array_equal(goodBurnup, self.testObj.burnups)
        badBurnup = arange(goodBurnup.size + 1)
        with self.assertRaises(ValueError):
            self.testObj.burnups = badBurnup


class BranchCollectorTester(BranchAttrSetterTestHelper):
    """Class that tests the branching collector"""

    def setUp(self):
        self.testObj = self.collect()


class BranchUnivTester(BranchAttrSetterTestHelper):
    """Class that tests the branch universe object"""

    def setUp(self):
        col = self.collect()
        self.testObj = col.universes[col.univIndex[0]]


del BranchAttrSetterTestHelper


class BareBranchContainerTester(BranchTestHelper):
    """Class for testing the pre-collected classes"""

    def test_bareBranchedContainer(self):
        """Verify that certain attributes cannot be set before collection"""
        collector = BranchCollector(self.reader)
        self._testUnsettableAttributes(
            collector, ('burnups', 'axis', 'states', 'perturbations'))

    def _testUnsettableAttributes(self, obj, attrs):
        for attr in attrs:
            with self.assertRaises(AttributeError, msg='set ' + attr):
                setattr(obj, attr, None)


if __name__ == '__main__':
    from unittest import main
    main()
