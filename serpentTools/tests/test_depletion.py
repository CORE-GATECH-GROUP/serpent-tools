"""Test the depletion file."""
import os
import unittest

from serpentTools.tests import ROOT_DIR
from serpentTools.parsers.depletion import DepletionReader


class Test_DepletionParser(unittest.TestCase):
    """Class that tests the functionality of the depletion reader."""

    @classmethod
    def setUpClass(cls):
        filePath = os.path.join(ROOT_DIR, 'ref_dep.m')
        cls.reader = DepletionReader(filePath)
        cls.reader.read()

    def test_metadata(self):
        """Test the metadata storage for the reader."""
        expectedMetadata = {
            'zai':
                ['621490', '541350', '922350', '942390', '50100', '666', '0'],
            'names':
                ['Sm149', 'Xe135', 'U235', 'Pu239', 'B10', 'lost', 'total'],
            'burnup': [0.00000E+00, 1.93360E-02, 3.86721E-02, 1.16016E-01,
                       1.93360E-01, 2.90041E-01, 3.86721E-01, 6.76762E-01,
                       9.66802E-01, 1.45020E+00, 1.93360E+00, 2.90041E+00,
                       3.86721E+00, 4.83401E+00],
            'days': [0.00000E+00, 5.00000E-01, 1.00000E+00, 3.00000E+00,
                     5.00000E+00, 7.50000E+00, 1.00000E+01, 1.75000E+01,
                     2.50000E+01, 3.75000E+01, 5.00000E+01, 7.50000E+01,
                     1.00000E+02, 1.25000E+02]
        }
        for key, expectedValue in expectedMetadata.items():
            with self.subTest(key=key):
                self.assertIn(key, self.reader.metadata)
                self.assertListEqual(self.reader.metadata[key], expectedValue)


if __name__ == '__main__':
    unittest.main()
