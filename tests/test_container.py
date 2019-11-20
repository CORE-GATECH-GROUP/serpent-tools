"""Test the container object. """

from unittest import TestCase
from itertools import product

from numpy import arange, ndarray, float64
from numpy.testing import assert_array_equal
from serpentTools.objects.containers import HomogUniv
from serpentTools.messages import SerpentToolsException

from tests import compareDictOfArrays

NUM_GROUPS = 5


class _HomogUnivTestHelper(TestCase):
    """Class that runs the tests for the two sub-classes

    Subclasses will differ in how the ``mat`` data
    is arranged. For one case, the ``mat`` will be a
    2D matrix.
    """

    def setUp(self):
        self.univ, vec, mat = self.getParams()
        groupStructure = arange(NUM_GROUPS + 1)
        testK = vec[0]
        # Data definition
        rawData = {'B1_1': vec, 'B1_AS_LIST': list(vec),
                   'INF_1': vec, 'INF_S0': mat, 'CMM_TRANSP_X': vec,
                   'INF_KEFF': testK, 'B1_KINF': testK, 'IMP_KEFF': testK,
                   'INF_KINF': testK}
        attrs = {'MACRO_E': groupStructure}
        # Partial dictionaries
        self.b1Unc = self.b1Exp = {
            'b11': vec, 'b1AsList': list(vec), 'b1Kinf': testK,
        }
        self.infUnc = self.infExp = {
            'inf1': vec, 'infS0': mat, 'infKeff': testK, 'infKinf': testK,
        }
        self.gcUnc = self.gc = {'cmmTranspX': vec, 'impKeff': testK}
        self.expAttrs = {'groups': groupStructure, 'numGroups': NUM_GROUPS}
        # Use addData
        for key, value in attrs.items():
            self.univ.addData(key, value)
        for key, value in rawData.items():
            self.univ.addData(key, value, uncertainty=False)
            self.univ.addData(key, value, uncertainty=True)

    def test_getB1Exp(self):
        """ Get Expected vales from B1 dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.b1Exp:
            d[kk] = self.univ.get(kk, False)
        compareDictOfArrays(self.b1Exp, d, 'Error in b1 values at {key}')

    def test_getB1Unc(self):
        """ Get Expected vales and associated uncertainties from B1 dictionary
        """
        d = {}
        # Comparison
        for kk in self.univ.b1Exp:
            d[kk] = self.univ.get(kk, True)[1]
        compareDictOfArrays(self.b1Unc, d,
                            'Error in b1 uncertainties at {key}')

    def test_getInfExp(self):
        """ Get Expected vales from Inf dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.infExp:
            d[kk] = self.univ.get(kk, False)
        compareDictOfArrays(self.infExp, d,
                            'Error in infinite values at {key}')

    def test_getInfUnc(self):
        """ Get Expected vales and associated uncertainties from Inf dictionary
        """
        d = {}
        # Comparison
        for kk in self.univ.infUnc:
            d[kk] = self.univ.get(kk, True)[1]
        compareDictOfArrays(self.infUnc, d,
                            'Error in infinite uncertainties at {key}')

    def test_attributes(self):
        """ Get metaData from corresponding dictionary"""
        for key, value in self.expAttrs.items():
            actual = getattr(self.univ, key)
            if isinstance(value, ndarray):
                assert_array_equal(value, actual, err_msg=key)
            else:
                self.assertEqual(value, actual, msg=key)

    def test_getBothInf(self):
        """
        Verify that the value and the uncertainty are returned if the
        flag is passed.
        """
        expected, uncertainties = {}, {}
        for key in self.infExp.keys():
            value, unc = self.univ.get(key, True)
            expected[key] = value
            uncertainties[key] = unc
        compareDictOfArrays(self.infExp, expected, 'infinite values')
        compareDictOfArrays(self.infUnc, uncertainties,
                            'infinite uncertainties')


class VectoredHomogUnivTester(_HomogUnivTestHelper):
    """Class for testing HomogUniv that does not reshape scatter matrices"""

    def getParams(self):
        univ, vec, mat = getParams()
        self.assertFalse(univ.reshaped)
        return univ, vec, mat


class ReshapedHomogUnivTester(_HomogUnivTestHelper):
    """Class for testing HomogUniv that does reshape scatter matrices"""

    def getParams(self):
        from serpentTools.settings import rc
        with rc:
            rc.setValue('xs.reshapeScatter', True)
            univ, vec, mat = getParams()
            self.assertTrue(univ.reshaped)
        return univ, vec, mat.reshape(NUM_GROUPS, NUM_GROUPS, order="F")


class SimpleHomogUnivTester(TestCase):
    """Class for simple tests on HomogUniv objects"""

    def _wrapBadInit(self, *initArgs):
        msg = "Args: {}".format(initArgs)
        with self.assertRaises(SerpentToolsException, msg=msg):
            HomogUniv('badInit', *initArgs)

    def test_badinit(self):
        """Verify that a HomogUniv cannot be constructed with negative time"""
        self._wrapBadInit(-1, 0, None)
        self._wrapBadInit(None, None, -10.0)
        # good init
        HomogUniv('good', None, None, None)

    def test_setGet(self):
        infKey = 'infTestData'
        infVal = arange(2)
        univ = HomogUniv('setGetTest', None, None, None)
        self.assertEqual(0, len(univ.infExp), msg='Before set')
        self.assertEqual(0, len(univ.infUnc), msg='Before set')
        univ[infKey] = infVal
        self.assertEqual(1, len(univ.infExp), msg='After set')
        self.assertTrue(infKey in univ.infExp)
        self.assertEqual(0, len(univ.infUnc), msg='After set')
        self.assertIs(univ[infKey], infVal)
        with self.assertRaises(KeyError):
            univ['this should not exist']


def getParams():
    """Return the universe, vector, and matrix for testing."""
    univ = HomogUniv(300, 0, 0, 0)
    vec = arange(NUM_GROUPS)
    mat = arange(NUM_GROUPS ** 2)
    return univ, vec, mat


del _HomogUnivTestHelper


class UnivTruthTester(TestCase):
    """Class that tests the various boolean evaluations for HomogUniv"""

    def setUp(self):
        """Verify that an empty universe evalutes to False."""
        self.assertFalse(self.getUniv())

    def test_loadedUnivTrue(self):
        """Verify that universes with some data evalue to True."""
        keys = {"INF_TOT", "B1_TOT", "CMM_TRANSP_X"}
        data = arange(NUM_GROUPS)
        for uflag, key in product((True, False), keys):
            univ = self.getUniv()
            univ.addData(key, data, uflag)
            self.evalUniv(univ, msg="Key = {}, Uflag={}".format(key, uflag))
        univ = self.getUniv()
        univ.addData("MACRO_E", data)
        self.evalUniv(univ, msg="Key = MACRO_E")

    @staticmethod
    def getUniv():
        return HomogUniv('truth', 0, 0, 0)

    def evalUniv(self, univ, msg):
        """Shortcut for testing the truth of a universe."""
        self.assertTrue(univ, msg=msg)
        self.assertTrue(univ.hasData, msg=msg)


class HomogUnivIntGroupsTester(TestCase):
    """Class that ensures number of groups is stored as ints."""

    def setUp(self):
        self.univ = HomogUniv('intGroups', 0, 0, 0)
        self.numGroups = 2
        self.numMicroGroups = 4

    def test_univGroupsFromFloats(self):
        """Vefify integer groups are stored when passed as floats."""
        self.setAs(float)
        self._tester()

    def test_univGroupsFromNPFloats(self):
        """Vefify integer groups are stored when passed as numpy floats."""
        self.setAs(float64)
        self._tester()

    def _tester(self):
        for attr in {'numGroups', 'numMicroGroups'}:
            actual = getattr(self.univ, attr)
            msg = 'Attribute: {}'.format(attr)
            self.assertIsInstance(actual, int, msg=msg)
            expected = getattr(self, attr)
            self.assertEqual(expected, actual, msg=msg)

    def setAs(self, func):
        """Set the number of groups to be as specific type."""
        for attr in {'numGroups', 'numMicroGroups'}:
            expected = getattr(self, attr)
            setattr(self.univ, attr, func(expected))
