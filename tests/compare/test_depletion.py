"""
Test the comparisons of the depleted materials
"""

import serpentTools
from tests import TestCaseWithLogCapture

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

    def compare(self, lower=0, upper=0, sigma=0, verbosity='info'):
        raise NotImplementedError

    def test_compareIdentical(self):
        """Compare the objects against themselves for passage"""
        self.assertTrue(self.compare(0, 0, 0))

    def test_mishapenMetadata(self):
        """Verify that changes in the metadata shape fail the comparison"""
        numNames = len(self.refMaterial.names)
        self.otherMaterial.names = self.refMaterial.names[:numNames - 1]
        self.assertFalse(self.compare(0, 0, 0))

    def test_missingData(self):
        """Verify that the test fails if one object is missing data."""
        keys = list(self.refMaterial.data.keys())
        for key in keys:
            data = self.otherMaterial.data.pop(key)
            self.assertFalse(self.compare(0, 0, 0))
            self.assertMsgInLogs('ERROR', key, partial=True)

            # put things back in place
            self.handler.logMessages = {}
            self.otherMaterial.data[key] = data

    def test_minorTweakData(self):
        """Verify that the test passes after minor tweaks to data"""
        key = 'adens'
        diffInPercent = 1.
        self.otherMaterial.data[key] *= (1 + diffInPercent / 100)
        # Test by setting the lower tolerance to barely above perturbation
        self.assertTrue(self.compare(diffInPercent + 1E-6, diffInPercent * 2,
                        verbosity='info'))
        self.assertMsgInLogs("INFO", key, partial=True)
        for level in ["WARNING", "ERROR", "CRITICAL"]:
            self.assertTrue(level not in self.handler.logMessages)
        # Test again, with tighter lower tolerance and look for warning
        self.assertTrue(self.compare(diffInPercent, diffInPercent * 2,
                        verbosity='info'))
        self.assertMsgInLogs("WARNING", key, partial=True)


class DepletedMaterialComparisonTester(DepletionCompareHelper):
    """TestCase that only compares depleted materials"""

    def compare(self, lower=0, upper=0, sigma=0, verbosity='info'):
        return self.refMaterial.compare(self.otherMaterial, lower, upper,
                                        sigma, verbosity=verbosity)


class DepletionReaderComparisonTester(DepletionCompareHelper):
    """Class for comparing the reader compare method"""

    def compare(self, lower=0, upper=0, sigma=0, verbosity='info'):
        return self.refReader.compare(self.otherReader, lower, upper, sigma,
                                      verbosity=verbosity)

    def test_badMetadataShapes(self):
        """
        Verify the comparison fails early for dissimilar metadata shapes.
        """
        newVecKey = 'badMetadataKey'
        self.refReader.metadata[newVecKey] = [0, 1, 2, 3]
        self.otherReader.metadata[newVecKey] = [0, 1, 2]
        self.assertFalse(self.compare(100, 100, 100))
        self.assertMsgInLogs('ERROR', newVecKey, partial=True)
        self.refReader.metadata.pop(newVecKey)

    def test_diffMaterialDicts(self):
        """Verify the test fails if different materials are stored."""
        for key in self.otherReader.materials:
            self.otherReader.materials.pop(key)
            break
        newMaterialKey = "newMateria"
        self.otherReader.materials[newMaterialKey] = None
        self.assertFalse(self.compare())
        self.assertMsgInLogs("ERROR", key, partial=True)
        self.assertMsgInLogs("ERROR", newMaterialKey, partial=True)


del DepletionCompareHelper
