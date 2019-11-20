"""
Test the branching collector
"""

from unittest import TestCase

from numpy import ones, array, arange, nan
from numpy.testing import assert_array_equal
from serpentTools.xs import BranchCollector
from serpentTools.data import readDataFile


class _BranchTestHelper(TestCase):
    """Helper class for testing branched collectors"""

    @classmethod
    def setUpClass(cls):
        cls.reader = readDataFile('demo.coe')


class CollectedHelper(_BranchTestHelper):
    """
    Class that helps test the ability to set attributes on branched objects
    """

    XS_MAP = {
        ('nom', 'nom'): {  # branch
            'infTot': {  # group constant
                0: {  # burnup
                    "0": array([2.10873E-01, 2.23528E-01]),  # univ: value
                    "20": array([2.10868E-01, 1.22701E-01]),
                },
                1: {
                    "0": array([2.08646E-01, 0.00000E+00]),
                    "20": array([2.08083E-01, 0.00000E+00]),
                },
            },
            'b1Diffcoef': {
                0: {
                    "0": array([1.80449E+00, 1.97809E+00]),
                    "20": array([1.80519E+00, 0.00000E+00]),
                },
            },
        },
        ('B750', 'FT1200'): {
            'infTot': {
                0: {
                    "0": array([3.13772E-01, 5.41505E-01]),
                    "20": array([3.13711E-01, 5.41453E-01]),
                },
                1: {
                    "0": array([3.11335E-01, 6.09197E-01]),
                    "20": array([3.11729E-01, 8.37580E-01]),
                },
            },
            'b1Diffcoef': {
                0: {
                    "0": array([1.75127E+00, 8.63097E-01]),
                    "20": array([1.75206E+00, 8.62754E-01]),
                },
            },
        },
    }

    XS_ERR_MSG = """
Pert: {p}
Group constant: {g}
Universe: {u}
Burnup: {b}""".strip()

    ORIG_PERTS = ("BOR", "TFU")

    def collect(self):
        """Return the collector after collecting group constants"""
        collector = BranchCollector(self.reader)
        collector.collect(self.ORIG_PERTS)
        return collector

    def getGroupConstant(self, pertVals, univID, gcKey, burnup, msg):
        """Return the stored group constant"""
        try:
            val = self._getGroupConstant(pertVals, univID, gcKey, burnup)
        except KeyError:
            raise KeyError(msg)
        except IndexError:
            raise IndexError(msg)
        return val

    def _getGroupConstant(self, pertVals, univID, gcKEy, burnup):
        raise NotImplementedError

    def _getBurnupIndex(self, burnup):
        bmask = self.testObj.burnups == burnup
        if not bmask.any():
            raise IndexError(burnup)
        return bmask.argsort()[-1]

    def _getPertIndex(self, perts):
        generator = (self.testObj.states[i].index(v)
                     for i, v in enumerate(perts))
        return tuple(generator)

    def compareGroupConstant(self, expGC, pertVals, univID, gcKey, burnup):
        msg = self.XS_ERR_MSG.format(p=pertVals, g=gcKey, u=univID, b=burnup)
        actual = self.getGroupConstant(pertVals, univID, gcKey, burnup, msg)
        if actual is nan:
            return  # avoid comparing different universes
        assert_array_equal(actual, expGC, err_msg=msg)

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

    def test_xsTables(self):
        """Verify that group constants are placed correctly"""
        # dig through the XS_MAP
        for pertKey, pertMap in self.XS_MAP.items():
            for gcKey, gcMap in pertMap.items():
                for burnup, burnMap in gcMap.items():
                    for univID, expGC in burnMap.items():
                        self.compareGroupConstant(
                            expGC, pertKey, univID, gcKey, burnup)


class BranchCollectorTester(CollectedHelper):
    """Class that tests the branching collector"""

    def setUp(self):
        self.collector = self.collect()
        self.testObj = self.collector

    def _getGroupConstant(self, pertVals, univID, gcKey, burnup):
        xsTable = self.collector.xsTables[gcKey]
        univIndex = self.collector.univIndex.index(univID)
        burnupIndex = self._getBurnupIndex(burnup)
        pertIndexes = self._getPertIndex(pertVals)
        # current xsTable structure:
        # univ, <perts>, burnup
        index = (univIndex, ) + pertIndexes + (burnupIndex, )
        return xsTable[index]


class BranchUnivTester(CollectedHelper):
    """Class that tests the branch universe object"""

    def setUp(self):
        col = self.collect()
        self.universe = col.universes[col.univIndex[0]]
        self.testObj = self.universe

    def _getGroupConstant(self, pertVals, univID, gcKey, burnup):
        if univID != self.universe.univID:
            return nan
        xsTable = self.universe.xsTables[gcKey]
        burnupIndex = self._getBurnupIndex(burnup)
        pertIndex = self._getPertIndex(pertVals)
        # data is stored as
        # <perturbations>, burnup
        return xsTable[pertIndex + (burnupIndex, )]


class UnknownPertCollectorTester(BranchCollectorTester):
    """Helper for creating BranchCollectors without perturbations"""

    def collect(self):
        collector = BranchCollector(self.reader)
        collector.collect()
        return collector

    def setUp(self):
        BranchCollectorTester.setUp(self)
        self.assertTrue(
            len(self.collector.perturbations) == len(self.ORIG_PERTS),
            msg="Failed to infer correct perturbations"
        )


class CollectorFromFileTester(UnknownPertCollectorTester):
    """Test the collection of the data using the fromFile method"""

    def collect(self):
        """Overwrite to use the fromFile method"""
        collector = BranchCollector.fromFile(self.reader.filePath)
        return collector


del CollectedHelper


class BareBranchContainerTester(_BranchTestHelper):
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
