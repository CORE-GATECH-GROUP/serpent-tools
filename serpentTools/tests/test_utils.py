"""
Test the various utilities in serpentTools/utils.py
"""

import unittest

from numpy import arange, ndarray, array
from numpy.testing import assert_array_equal
from six import iteritems

from serpentTools.utils import convertVariableName, splitValsUncs, str2vec


class VariableConverterTester(unittest.TestCase):
    """Class for testing our variable name conversion function."""

    def test_variableConversion(self):
        """ Verify the variable name conversion function."""
        testCases = {
            "VERSION": "version",
            "INF_KINF": "infKinf",
            "ADJ_PERT_KEFF_SENS": "adjPertKeffSens"
            ,}
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
            assert_array_equal(view, copy,err_msg=msg)
            self.assertFalse(view is copy, msg=msg)

    def test_splitAtCols(self):
        """Verify that the splitValsUncs works for 2D arrays."""
        mat = self.input.reshape(2, 2)
        expectedV = array([[0], [2]])
        expectedU = array([[1], [3]])
        actualV, actualU = splitValsUncs(mat)
        assert_array_equal(expectedV, actualV, err_msg="Values")
        assert_array_equal(expectedU, actualU, err_msg="Uncertainties")


if __name__ == '__main__':
    unittest.main()

