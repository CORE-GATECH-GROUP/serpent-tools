"""Test the detector reader."""

import os
import unittest

from serpentTools.settings import rc
from serpentTools.parsers import DetectorReader
from serpentTools.tests import TEST_ROOT


class DetectorReaderTester(unittest.TestCase):
    """Class to test the detector reader."""

    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'ref_det.m')
        rc['verbosity'] = 'debug'
        cls.reader = DetectorReader(cls.file)
        cls.reader.read()
        expected = {'1', '2', '3', '4'}
        actual = set(cls.reader.detectors.keys())
        diff = expected.symmetric_difference(actual)
        assert not any(diff), (
            'Failed to load detector correctly. '
            'Incorrect detectors: {}'.format(diff))


if __name__ == '__main__':
    unittest.main()
