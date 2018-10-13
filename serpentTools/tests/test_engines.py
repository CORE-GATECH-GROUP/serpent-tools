"""
Tests for various sub-parsers

Included in this test suite:

    s/p/base.CSCStreamProcessor

"""

from unittest import TestCase
from io import StringIO

import re
from numpy.testing import assert_array_equal, assert_allclose
from numpy import longfloat, array, dtype

from serpentTools.parsers.base import CSCStreamProcessor


class CSCStreamTester(TestCase):
    """
    Class for testing the CSCStreamProcessor.

    Matrices are 2x2 diagonal matrices for simplicity
    Therefore the underlying indices and index pointer
    vectors can be shared across all test cases
    """

    FINAL_LINE = "THIS SHOULD BE THE FINAL LINE"

    EXP_INDPTR = array([0, 1, 2])
    EXP_INDICES = array([0, 1])

    def setUp(self):
        readable = StringIO(self.testString.lstrip() + self.FINAL_LINE)
        self.processor = CSCStreamProcessor(
            readable, self.regex, self.datatype)
        self.finalLine = self.processor.process()
        self.EXP_DATA = array(self.EXP_DATA_AS_LIST, self.datatype)

    def test_processor(self):
        """Verify the processor properly stores data in the CSC format"""
        self.assertEqual(self.finalLine, self.FINAL_LINE)
        assert_array_equal(self.processor.indptr, self.EXP_INDPTR)
        assert_array_equal(self.processor.indices, self.EXP_INDICES)
        assert_allclose(self.processor.data, self.EXP_DATA)
        # Convert a simple dtype, like float, to the numpy representation
        self.assertIs(self.processor.data.dtype, dtype(self.datatype))


class CaseOneStringBasedProcessor(object):
    """Object that reads using a string-based regular expression"""
    regex = r'A\((\d+),\s+(\d+)\)\s+=\s+([\d\.]+)'
    testString = """
A(1, 1) = 1.0;
A(2, 2) = 1.0;
"""
    EXP_DATA_AS_LIST = [
        [1.0],
        [1.0],
    ]

class CaseTwoStringBasedProcessor(object):
    """Read the second test case using a string regular expression"""
    regex = r'A\((\d+),\s+(\d+)\)\s+=\s+([\d+\.]).*=\s+([\d\.]+)'
    testString = """
A(1, 1) = 1.0; B(1, 1) = 0.05
A(2, 2) = 1.0; B(2, 2) = 0.07
"""

    EXP_DATA_AS_LIST = [
        [1.0, 0.05],
        [1.0, 0.07],
    ]


class CaseOneRegexBasedProcessor(CaseOneStringBasedProcessor):
    """Class for reading first test case using pre-compiled regex"""
    regex = re.compile(CaseOneStringBasedProcessor.regex)


class CaseTwoRegexBasedProcessor(CaseTwoStringBasedProcessor):
    """Class for reading second test case using pre-compiled regex"""
    regex = re.compile(CaseTwoStringBasedProcessor.regex)


class FloatProcessor(object):
    """Class that stores data as floats."""
    datatype = float


class LongFloatProcessor(object):
    """Class that stores data as long floats."""
    datatype = longfloat


class CaseOneStringFloatTester(
        CSCStreamTester, CaseOneStringBasedProcessor, FloatProcessor):
    """
    Class that reads the first case using a string-regex and stores as floats.
    """


class CaseOneStringLongfloatTester(
        CSCStreamTester, CaseOneStringBasedProcessor, LongFloatProcessor):
    """
    Class that reads the first case using a string-regex and stores as longfloats.
    """

class CaseTwoStringFloatTester(
        CSCStreamTester, CaseTwoStringBasedProcessor, FloatProcessor):
    """
    Class that reads the second case using a string-regex and stores as floats.
    """


class CaseTwoStringLongfloatTester(
        CSCStreamTester, CaseTwoStringBasedProcessor, LongFloatProcessor):
    """
    Class that reads the second case using a string-regex and stores as longfloats.
    """


class CaseOneRegexFloatTester(
        CSCStreamTester, CaseOneRegexBasedProcessor, FloatProcessor):
    """
    Class that reads the first case using a compiled regex and stores as floats.
    """


class CaseOneRegexLongfloatTester(
        CSCStreamTester, CaseOneRegexBasedProcessor, LongFloatProcessor):
    """
    Class that reads the first case using a compiled regex and stores as longfloats.
    """

class CaseTwoRegexFloatTester(
        CSCStreamTester, CaseTwoRegexBasedProcessor, FloatProcessor):
    """
    Class that reads the second case using a compiled regex and stores as floats.
    """


class CaseTwoRegexLongfloatTester(
        CSCStreamTester, CaseTwoRegexBasedProcessor, LongFloatProcessor):
    """
    Class that reads the second case using a compiled regex and stores as longfloats.
    """

del CSCStreamTester


if __name__ == '__main__':
    from unittest import main
    main()
