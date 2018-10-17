"""Class to test the read commands from serpentTools.parsers"""
import unittest

import six

from serpentTools.messages import SerpentToolsException
from serpentTools.parsers import inferReader, read


class TestReaderInfer(unittest.TestCase):
    """Test the functionality of the read and inferReader functions"""

    def test_nonCallableReader(self):
        """
        Verify that an error is raised if the reader is non string nor callable
        """
        with self.assertRaises(AssertionError):
            read('dummyFP', None)

    def test_exceptionUnsupportedReader(self):
        """Verify an exception is raised for bad reader string"""
        with self.assertRaises(SerpentToolsException):
            read('dummyFP', 'this won\'t work')

    def test_inferReader(self):
        """Verify the correct readers are returned for given files"""
        from serpentTools.parsers import (
            BumatReader, BranchingReader, DepletionReader, DetectorReader,
            ResultsReader,
            FissionMatrixReader)
        expectedClasses = {
            'test.bumat99': BumatReader, 'test.coe': BranchingReader,
            'test_dep.m': DepletionReader, 'test_det99.m': DetectorReader,
            'test_res.m': ResultsReader, 'test_fmtx99.m': FissionMatrixReader,
            'test_res': None, 'test.coe_dep.m': DepletionReader
        }
        for fileP, expectedReader in six.iteritems(expectedClasses):
            if expectedReader is None:
                with self.assertRaises(SerpentToolsException):
                    inferReader(fileP)
            else:
                actual = inferReader(fileP)
                self.assertIs(expectedReader, actual,
                              'File path: {}\nExpected: {}\nActual: {}'
                              .format(fileP, str(expectedReader), str(actual))
                              )


if __name__ == '__main__':
    unittest.main()
