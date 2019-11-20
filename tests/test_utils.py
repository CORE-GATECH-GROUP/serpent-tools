"""
Test the various utilities in serpentTools/utils.py
"""

from unittest import TestCase

from numpy import arange, ndarray, array, ones, ones_like, zeros_like
from numpy.testing import assert_array_equal

from serpentTools.utils import (
    convertVariableName,
    splitValsUncs,
    str2vec,
    getCommonKeys,
    directCompare,
    getOverlaps,
    splitDictByKeys,
    DC_STAT_GOOD,
    DC_STAT_LE_LOWER,
    DC_STAT_MID,
    DC_STAT_GE_UPPER,
    DC_STAT_NOT_IDENTICAL,
    DC_STAT_NOT_IMPLEMENTED,
    DC_STAT_DIFF_TYPES,
    DC_STAT_DIFF_SHAPES,
    formatPlot,
)

from tests import plotTest, plotAttrTest


class VariableConverterTester(TestCase):
    """Class for testing our variable name conversion function."""

    def test_variableConversion(self):
        """ Verify the variable name conversion function."""
        testCases = {
            "VERSION": "version",
            "INF_KINF": "infKinf",
            "ADJ_PERT_KEFF_SENS": "adjPertKeffSens",
        }
        for serpentStyle, expected in testCases.items():
            actual = convertVariableName(serpentStyle)
            self.assertEqual(expected, actual, msg=serpentStyle)


class VectorConverterTester(TestCase):
    """Class for testing the str2vec function"""

    @classmethod
    def setUpClass(cls):
        cls.testCases = ("0 1 2 3", [0, 1, 2, 3], (0, 1, 2, 3), arange(4))

    def test_str2Arrays(self):
        """Verify that the str2vec converts to arrays."""
        expected = arange(4)
        for case in self.testCases:
            actual = str2vec(case)
            assert_array_equal(expected, actual, err_msg=case)

    def test_listOfInts(self):
        """Verify that a list of ints can be produced with str2vec."""
        expected = [0, 1, 2, 3]
        self._runConversionTest(int, expected, list)

    def test_vecOfStr(self):
        """Verify a single word can be converted with str2vec"""
        key = 'ADF'
        expected = array('ADF')
        actual = str2vec(key)
        assert_array_equal(expected, actual)

    def _runConversionTest(self, valType, expected, outType=None):
        if outType is None:
            outType = array
            compareType = ndarray
        else:
            compareType = outType
        for case in self.testCases:
            actual = str2vec(case, dtype=valType, out=outType)
            self.assertIsInstance(actual, compareType, msg=case)
            ofRightType = [isinstance(xx, valType) for xx in actual]
            self.assertTrue(all(ofRightType),
                            msg="{} -> {}, {}".format(case, actual,
                                                      type(actual)))
            self.assertEqual(expected, actual, msg=case)


class SplitValsTester(TestCase):
    """Class that tests splitValsUncs."""

    @classmethod
    def setUp(cls):
        cls.input = arange(4)

    def test_splitVals(self):
        """Verify the basic functionality."""
        expectedV = array([0, 2])
        expectedU = array([1, 3])
        actualV, actualU = splitValsUncs(self.input)
        assert_array_equal(expectedV, actualV, err_msg="Values")
        assert_array_equal(expectedU, actualU, err_msg="Uncertainties")

    def test_splitCopy(self):
        """Verfiy that a copy, not a view, is returned when copy=True"""
        viewV, viewU = splitValsUncs(self.input)
        copyV, copyU = splitValsUncs(self.input, copy=True)
        for view, copy, msg in zip(
                (viewV, viewU), (copyV, copyU), ('value', 'uncertainty')):
            assert_array_equal(view, copy, err_msg=msg)
            self.assertFalse(view is copy, msg=msg)

    def test_splitAtCols(self):
        """Verify that the splitValsUncs works for 2D arrays."""
        mat = self.input.reshape(2, 2)
        expectedV = array([[0], [2]])
        expectedU = array([[1], [3]])
        actualV, actualU = splitValsUncs(mat)
        assert_array_equal(expectedV, actualV, err_msg="Values")
        assert_array_equal(expectedU, actualU, err_msg="Uncertainties")


class CommonKeysTester(TestCase):
    """Class that tests getCommonKeys"""

    def test_goodKeys_dict(self):
        """Verify a complete set of keys is returned from getCommonKeys"""
        d0 = {1: None, '2': None, (1, 2, 3): "tuple"}
        expected = set(d0.keys())
        actual = getCommonKeys(d0, d0, 'identical dictionary')
        self.assertSetEqual(expected, actual,
                            msg="Passed two dictionaries")
        actual = getCommonKeys(d0, expected, 'dictionary and set')
        self.assertSetEqual(expected, actual,
                            msg="Passed dictionary and set")

    def test_getKeys_missing(self):
        """Verify that missing keys are properly notified."""
        log = []
        d0 = {1, 2, 3}
        emptyS = set()
        desc0 = "xObj0x"
        desc1 = "xObj1x"
        common = getCommonKeys(d0, emptyS, 'missing keys', desc0, desc1,
                               herald=log.append)
        self.assertSetEqual(emptyS, common)
        self.assertEqual(len(log), 1, msg="Failed to append warning message")
        warnMsg = log[0]
        self.assertIsInstance(warnMsg, str, msg="Log messages is not string")
        for desc in (desc0, desc1):
            errMsg = "Description {} missing from warning message\n{}"
            self.assertIn(desc, warnMsg, msg=errMsg.format(desc, warnMsg))


class DirectCompareTester(TestCase):
    """Class for testing utils.directCompare."""

    NUMERIC_ITEMS = (
        [0, 0.001],
        [1E-8, 0],
        [array([1, 1, ]), array([1, 1.0001])],
    )

    def checkStatus(self, expected, obj0, obj1, lower, upper, msg=None):
        """Wrapper around directCompare with ``args``. Pass ``kwargs`` to
        assertEqual."""
        actual = directCompare(obj0, obj1, lower, upper)
        self.assertEqual(expected, actual, msg=msg)

    def test_badTypes(self):
        """Verify that two objects of different types return -1."""
        status = DC_STAT_DIFF_TYPES
        value = 1
        for otherType in (bool, str):
            self.checkStatus(status, value, otherType(value), 0, 1,
                             msg=str(otherType))
        asIterable = [value, ]
        for otherType in (list, set, tuple, array):
            self.checkStatus(status, value, otherType(asIterable), 0, 1,
                             msg=str(otherType))

    def test_identicalString(self):
        """Verify that identical strings return 0."""
        msg = obj = 'identicalStrings'
        status = DC_STAT_GOOD
        self.checkStatus(status, obj, obj, 0, 1, msg=msg)

    def test_dissimilarString(self):
        """Verify returns the proper code for dissimilar strings."""
        msg = "dissimilarStrings"
        status = DC_STAT_NOT_IDENTICAL
        self.checkStatus(status, 'item0', 'item1', 0, 1, msg=msg)

    def _testNumericsForItems(self, status, lower, upper):
        msg = "lower: {lower}, upper: {upper}\n{}\n{}"
        for (obj0, obj1) in self.NUMERIC_ITEMS:
            self.checkStatus(status, obj0, obj1, lower, upper,
                             msg=msg.format(obj0, obj1, lower=lower,
                                            upper=upper))

    def test_acceptableLow(self):
        """Verify returns the proper code for close numerics."""
        lower = 5
        upper = 1E4
        self._testNumericsForItems(DC_STAT_LE_LOWER, lower, upper)

    def test_acceptableHigh(self):
        """Verify returns the proper code for close but not quite values."""
        lower = 0
        upper = 1E4
        self._testNumericsForItems(DC_STAT_MID, lower, upper)

    def test_outsideTols(self):
        """Verify returns the proper code for values outside tolerances."""
        lower = 1E-8
        upper = 1E-8
        self._testNumericsForItems(DC_STAT_GE_UPPER, lower, upper)

    def test_notImplemented(self):
        """Check the not-implemented cases."""
        self.checkStatus(DC_STAT_NOT_IMPLEMENTED, {'hello': 'world'},
                         {'hello': 'world'}, 0, 0,
                         msg="testing on dictionaries")

    def test_stringArrays(self):
        """Verify the function handles string arrays properly."""
        stringList = ['hello', 'world', '1', '-1']
        vec0 = array(stringList)
        self.checkStatus(DC_STAT_GOOD, vec0, vec0, 0, 0,
                         msg='Identical string arrays')
        vec1 = array(stringList)
        vec1[-1] = 'foobar'
        self.checkStatus(DC_STAT_NOT_IDENTICAL, vec0, vec1, 0, 0,
                         msg='Dissimilar string arrays')

    def test_diffShapes(self):
        """
        Verify that that directCompare fails for arrays of different shape.
        """
        vec0 = [0, 1, 2, 3, 4]
        vec1 = [0, 1]
        mat0 = [[0, 1], [1, 2]]
        mat1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.checkStatus(DC_STAT_DIFF_SHAPES, vec0, vec1, 0, 0,
                         msg="Compare two vectors.")
        self.checkStatus(DC_STAT_DIFF_SHAPES, vec0, mat0, 0, 0,
                         msg="Compare vector and array.")
        self.checkStatus(DC_STAT_DIFF_SHAPES, mat0, mat1, 0, 0,
                         msg="Compare vector and array.")


class OverlapTester(TestCase):
    """Class for testing the Overlapping uncertainties function."""

    a0 = ones(4)
    a1 = ones(4) * 0.5
    u0 = array([0, 0.2, 0.1, 0.2])
    u1 = array([1, 0.55, 0.25, 0.4])
    expected = array([True, True, False, True])
    sigma = 1
    relative = False

    _errMsg = "Sigma:{}\na0:\n{}\nu0:\n{}\na1:\n{}\nu1:\n{}"

    def _test(self, expected, a0, a1, u0, u1, sigma, relative):
        """Symmetric test on the data by switching the order of arguments."""
        assert_array_equal(expected, getOverlaps(a0, a1, u0, u1, sigma,
                                                 relative),
                           err_msg=self._errMsg.format(a0, u0, a1, u1, sigma))
        assert_array_equal(expected, getOverlaps(a1, a0, u1, u0, sigma,
                                                 relative),
                           err_msg=self._errMsg.format(sigma, a1, u1, a0, u0))

    def _testWithReshapes(self, expected, a0, a1, u0, u1, sigma, shape,
                          relative):
        """Call symmetric test twice, using reshaped arrays the second time."""
        self._test(expected, a0, a1, u0, u1, sigma, relative)
        ra0, ra1, ru0, ru1 = [arg.reshape(*shape) for arg in [a0, a1, u0, u1]]
        self._test(expected.reshape(*shape), ra0, ra1, ru0, ru1, sigma,
                   relative)

    def test_overlap_absolute(self):
        """Verify the getOverlaps works using absolute uncertainties."""
        self._testWithReshapes(self.expected, self.a0, self.a1, self.u0,
                               self.u1, self.sigma, (2, 2), False)

    def test_overlap_relative(self):
        """Verify the getOverlaps works using relative uncertainties."""
        u0 = self.u0 / self.a0
        u1 = self.u1 / self.a1
        self._testWithReshapes(self.expected, self.a0, self.a1, u0,
                               u1, self.sigma, (2, 2), True)

    @staticmethod
    def _setupIdentical(nItems, shape=None):
        arr = arange(nItems)
        if shape is not None:
            arr = arr.reshape(*shape)
        unc = zeros_like(arr)
        expected = ones_like(arr, dtype=bool)
        return arr, unc, expected

    def test_overlap_identical_1D(self):
        """
        Verify that all positions are found to overlap for identical arrays.
        """
        vec, unc, expected = self._setupIdentical(8)
        self._test(expected, vec, vec, unc, unc, 1, False)

    def test_overlap_identical_2D(self):
        """
        Verify that all positions are found to overlap for identical arrays.
        """
        vec, unc, expected = self._setupIdentical(8, (2, 4))
        self._test(expected, vec, vec, unc, unc, 1, False)

    def test_overlap_identical_3D(self):
        """
        Verify that all positions are found to overlap for identical arrays.
        """
        vec, unc, expected = self._setupIdentical(8, (2, 2, 2))
        self._test(expected, vec, vec, unc, unc, 1, False)

    def test_overlap_badshapes(self):
        """Verify IndexError is raised for bad shapes."""
        vec = arange(4)
        mat = vec.reshape(2, 2)
        with self.assertRaises(IndexError):
            getOverlaps(vec, mat, vec, mat, 1)


class SplitDictionaryTester(TestCase):
    """Class for testing utils.splitDictByKeys."""

    @classmethod
    def setUpClass(cls):
        cls.map0 = {
            'hello': 'world',
            'missingFrom1': True,
            'infKeff': arange(2),
            'float': 0.24,
            'absKeff': arange(2),
            'anaKeff': arange(6),
            'notBool': 1,
        }
        cls.map1 = {
            'hello': 'world',
            'infKeff': arange(2),
            'float': 0.24,
            'missingFrom0': True,
            'notBool': False,
            'anaKeff': arange(2),
            'absKeff': arange(2),
        }
        cls.badTypes = {'notBool': (int, bool)}
        cls.badShapes = {'anaKeff': ((6, ), (2, )), }
        cls.goodKeys = {'hello', 'absKeff', 'float', 'infKeff', }

    def callTest(self, keySet=None):
        return splitDictByKeys(self.map0, self.map1, keySet)

    def test_noKeys(self):
        """Verify that splitDictByKeys works when keySet is None."""
        m0, m1, badTypes, badShapes, goodKeys = self.callTest(None)
        self.assertSetEqual({'missingFrom0', }, m0)
        self.assertSetEqual({'missingFrom1', }, m1)
        self.assertDictEqual(self.badTypes, badTypes)
        self.assertDictEqual(self.badShapes, badShapes)
        self.assertSetEqual(self.goodKeys, goodKeys)

    def test_keySet_all(self):
        """Verify that splitDictByKeys works when keySet is all keys."""
        keys = set(self.map0.keys())
        keys.update(set(self.map1.keys()))
        keys.add('NOT IN ANY MAP')
        missing0 = set()
        missing1 = set()
        for key in keys:
            if key not in self.map0:
                missing0.add(key)
            if key not in self.map1:
                missing1.add(key)

        m0, m1, badTypes, badShapes, goodKeys = self.callTest(keys)
        self.assertSetEqual(missing0, m0)
        self.assertSetEqual(missing1, m1)
        self.assertDictEqual(self.badTypes, badTypes)
        self.assertDictEqual(self.badShapes, badShapes)
        self.assertSetEqual(self.goodKeys, goodKeys)


class PlotTestTester(TestCase):
    """Class to test the validity of the plot test utils"""
    XLABEL = "Test x label"
    YLABEL = "Test y label"

    def buildPlot(self):
        from matplotlib.pyplot import gca
        ax = gca()
        ax.plot([1, 2, 3], label=1)
        ax.legend()
        ax.set_ylabel(self.YLABEL)
        ax.set_xlabel(self.XLABEL)
        return ax

    @plotTest
    def test_plotAttrs_gca(self):
        """Test the plotAttrTest without passing an axes object"""
        self.buildPlot()
        plotAttrTest(self, xlabel=self.XLABEL, ylabel=self.YLABEL)

    @plotTest
    def test_plotAttrs_fail(self):
        """Test the failure modes of the plotAttrTest function"""
        ax = self.buildPlot()
        with self.assertRaisesRegex(AssertionError, 'xlabel'):
            plotAttrTest(self, ax, xlabel="Bad label")
        with self.assertRaisesRegex(AssertionError, 'ylabel'):
            plotAttrTest(self, ax, ylabel="Bad label")
        with self.assertRaisesRegex(AssertionError, 'xscale'):
            plotAttrTest(self, ax, xscale="log")
        with self.assertRaisesRegex(AssertionError, 'yscale'):
            plotAttrTest(self, ax, yscale="log")
        with self.assertRaisesRegex(AssertionError, 'legend text'):
            plotAttrTest(self, ax, legendLabels='bad text')
        with self.assertRaisesRegex(AssertionError, 'legend text'):
            plotAttrTest(self, ax, legendLabels=['1', '2'])
        with self.assertRaisesRegex(AssertionError, 'title'):
            plotAttrTest(self, ax, title='Bad title')

    @plotTest
    def test_formatPlot(self):
        """Test the capabilities of the formatPlot function"""
        ax = self.buildPlot()
        newX = 'new x label'
        newY = 'new y label'
        title = 'plot title'
        formatPlot(ax, xlabel=newX, ylabel=newY, loglog=True,
                   title=title)
        plotAttrTest(self, ax, xlabel=newX, ylabel=newY,
                     xscale='log', yscale='log', title=title)
