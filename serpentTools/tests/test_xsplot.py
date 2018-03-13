"""Test the xsplot reader."""
import os
import unittest
import numpy

from numpy.testing import assert_equal
from serpentTools.parsers import read
from serpentTools.settings import rc
from serpentTools.parsers import XSPlotReader
from serpentTools.tests import TEST_ROOT


class XSPlotTester(unittest.TestCase):
    """
    Class to test the xsplot reader.

    Cases:

        1. A file that has a "fissile", and "be" material.
            plut_xs0.m
    """

    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'plut_xs0.m')
        cls.reader = XSPlotReader(cls.file)
        cls.reader.read()
        expected = {'ummm'}

        # cast keys as set, take symmetric difference

    def test_isoXS():
        pass

    def test_matXS():
        pass

if __name__ == '__main__':
    unittest.main()
