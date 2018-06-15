"""
Test the various utilities in serpentTools/utils.py
"""

import unittest

from numpy import arange, ndarray, array, ones, ones_like, zeros_like
from numpy.testing import assert_array_equal
from six import iteritems

from serpentTools.utils import (
    convertVariableName,
    splitValsUncs,
    str2vec,
    getCommonKeys,
    directCompare,
    getOverlaps,
    )


class VariableConverterTester(unittest.TestCase):
    """Class for testing our variable name conversion function."""

    def test_variableConversion(self):
        """ Verify the variable name conversion function."""
        testCases = {
            "VERSION": "version",
            "INF_KINF": "infKinf",
            "ADJ_PERT_KEFF_SENS": "adjPertKeffSens",
            }
        for serpentStyle, expected in iteritems(testCases):
            actual = convertVariableName(serpentStyle)
            self.assertEqual(expected, actual, msg=serpentStyle)


class VectorConverterTester(unittest.TestCase):
    """Class for testing the str2vec function"""

    def setUp(self):
        self.testCases = ("0 1 2 3", [0, 1, 2, 3], (0, 1, 2, 3), arange(4))

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

    def _runConversionTest(self, valType, expected, outType=None):
        if outType is None:
            outType = array
            compareType = ndarray
        else:
            compareType = outType
        for case in self.testCases:
            actual = str2vec(case, of=valType, out=outType)
            self.assertIsInstance(actual, compareType, msg=case)
            ofRightType = [isinstance(xx, valType) for xx in actual]
            self.assertTrue(all(ofRightType),
                            msg="{} -> {}, {}".format(case, actual,
                                                      type(actual)))
            self.assertEqual(expected, actual, msg=case)


class SplitValsTester(unittest.TestCase):
    """Class that tests splitValsUncs."""

    def setUp(self):
        self.input = arange(4)

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


class CommonKeysTester(unittest.TestCase):
    """Class that tests getCommonKeys"""

    def test_goodKeys_dict(self):
        """Verify a complete set of keys is returned from getCommonKeys"""
        d0 = {1: None, '2': None, (1, 2, 3): "tuple"}
        expected = set(d0.keys())
        actual = getCommonKeys(d0, d0)
        self.assertSetEqual(expected, actual,
                            msg="Passed two dictionaries")
        actual = getCommonKeys(d0, expected)
        self.assertSetEqual(expected, actual,
                            msg="Passed dictionary and set")

    def test_getKeys_missing(self):
        """Verify that missing keys are properly notified."""
        log = []
        d0 = {1, 2, 3}
        emptyS = set()
        desc0 = "xObj0x"
        desc1 = "xObj1x"
        common = getCommonKeys(d0, emptyS, desc0, desc1, herald=log.append)
        self.assertSetEqual(emptyS, common)
        self.assertEqual(len(log), 1, msg="Failed to append warning message")
        warnMsg = log[0]
        self.assertIsInstance(warnMsg, str, msg="Log messages is not string")
        for desc in (desc0, desc1):
            errMsg = "Description {} missing from warning message\n{}"
            self.assertIn(desc, warnMsg, msg=errMsg.format(desc, warnMsg))


class DirectCompareTester(unittest.TestCase):
    """Class for testing utils.directCompare."""

    NUMERIC_ITEMS = (
        [0, 0.001],
        [1E-8, 0],
        [array([1, 1, ]), array([1, 1.0001])],
        [array([0, 1, ]), array([1, 1])],
    )
    def test_badTypes(self):
        """Verify that two objects of different types return False."""
        self.assertFalse(directCompare(1, array([1, ]), 0, 1,
                                       'badTypes'))

    def test_identicalString(self):
        """Verify that identical strings return True."""
        msg = qty = obj = 'identicalStrings'
        self.assertTrue(directCompare(obj, obj, 0, 1, qty), msg=msg)

    def test_dissimilarString(self):
        """Verify that directCompare returns False for dissimilar strings."""
        msg = qty = "dissimilarStrings"
        self.assertFalse(directCompare('item0', 'item1', 0, 1, qty),
                         msg=msg)

    def _testNumericsForItems(self, tOrF, qty, lower, upper):
        tester = self.assertTrue if tOrF else self.assertFalse
        msg = "lower: {lower}, upper: {upper}\n{}\n{}"
        for (obj0, obj1) in self.NUMERIC_ITEMS:
            tester(directCompare(obj0, obj1, lower, upper, qty),
                   msg=msg.format(obj0, obj1, lower=lower, upper=upper))

    def test_acceptableLow(self):
        """Verify that directCompare returns True for close numerics."""
        lower = 5
        upper = 1E4
        self._testNumericsForItems(True, 'acceptableLow', lower, upper)

    def test_acceptableHigh(self):
        """
        Verify that directCompare returns True for close but not quite values.
        """
        lower = 0.01
        upper = 1E4
        self._testNumericsForItems(True, 'acceptableHigh', lower, upper)

    def test_outsideTols(self):
        """Verify that directCompare returns False for values outside tolerances."""
        lower = 1E-8
        upper = 1E-8
        self._testNumericsForItems(False, 'outsideTols', lower, upper)


class OverlapTester(unittest.TestCase):
    """Class for testing the Overlapping uncertainties function."""

    _errMsg ="Sigma:{}\na0:\n{}\nu0:\n{}\na1:\n{}\nu1:\n{}" 

    def _test(self, expected, a0, a1, u0, u1, sigma):
        """Symmetric test on the data by switching the order of arguments."""
        assert_array_equal(expected, getOverlaps(a0, a1, u0, u1, sigma),
                           err_msg=self._errMsg.format(a0, u0, a1, u1, sigma))
        assert_array_equal(expected, getOverlaps(a1, a0, u1, u0, sigma),
                           err_msg=self._errMsg.format(sigma,a1, u1, a0, u0))

    def _testWithReshapes(self, expected, a0, a1, u0, u1, sigma, shape):
        """Call symmetric test twice, using reshaped arrays the second time."""
        self._test(expected, a0, a1, u0, u1, sigma)
        reshapes = [arg.reshape(*shape) for arg in [a0, a1, u0, u1]]
        self._test(expected.reshape(*shape), *reshapes, sigma)

    def test_overlapDoc(self):
        """Verify the getOverlaps works."""
        # Based on the original example
        a0 = ones(4)
        a1 = ones(4) * 0.5
        u0 = array([0, 0.2, 0.1, 0.2])
        u1 = array([1, 0.55, 0.25, 0.4])
        expected = array([True, True, False, True])
        sigma = 1
        self._testWithReshapes(expected, a0, a1, u0, u1, sigma, (2, 2))

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
        self._test(expected, vec, vec, unc, unc, 1)

    def test_overlap_identical_2D(self):
        """
        Verify that all positions are found to overlap for identical arrays.
        """
        vec, unc, expected = self._setupIdentical(8, (2, 4))
        self._test(expected, vec, vec, unc, unc, 1)

    def test_overlap_identical_3D(self):
        """
        Verify that all positions are found to overlap for identical arrays.
        """
        vec, unc, expected = self._setupIdentical(8, (2, 2, 2))
        self._test(expected, vec, vec, unc, unc, 1)


if __name__ == '__main__':
    unittest.main()

