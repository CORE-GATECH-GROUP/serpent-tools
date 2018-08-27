"""
Test the comparisons of the depleted materials
"""

import serpentTools
from serpentTools.tests.utils import TestCaseWithLogCapture

DATA_FILE = 'ref_dep.m'
REF_MATERIAL = 'fuel'


class DepletionCompareHelper(TestCaseWithLogCapture):
    """Read the reference files for creating the readers"""

    @classmethod
    def setUpClass(cls):
        cls.refReader = serpentTools.readDataFile(DATA_FILE)
        cls.refMaterial = cls.refReader[REF_MATERIAL]

    def setUp(self):
        self.otherReader = serpentTools.readDataFile(DATA_FILE)
        self.otherMaterial = self.otherReader[REF_MATERIAL]
        TestCaseWithLogCapture.setUp(self)

    def compare(self, lower, upper, sigma):
        raise NotImplementedError

    def test_compareIdentical(self):
        """Compare the objects against themselves for passage"""
        self.assertTrue(self.compare(0, 0, 0))

    def test_mishapenMetadata(self):
        """Verify that changes in the metadata shape fail the comparison"""
        numNames = len(self.refMaterial.names)
        self.otherMaterial.names = self.refMaterial.names[:numNames - 1]
        self.assertFalse(self.compare(0, 0, 0))


class DepletedMaterialComparisonTester(DepletionCompareHelper):
    """TestCase that only compares depleted materials"""

    def compare(self, lower, upper, sigma):
        return self.refMaterial.compare(self.otherMaterial, lower, upper,
                                        sigma)


class DepletionReaderComparisonTester(DepletionCompareHelper):
    """Class for comparing the reader compare method"""

    def compare(self, lower, upper, sigma):
        return self.refReader.compare(self.otherReader, lower, upper, sigma)


del DepletionCompareHelper


if __name__ == '__main__':
    from unittest import main
    main()
