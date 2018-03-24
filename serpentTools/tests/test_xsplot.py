"""Test the xsplot reader."""
import os
import unittest
import numpy
import pickle

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

            Reference data is stored in expectedXS.pickle
            as a pickle
    """

    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'plut_xs0.m')
        cls.reader = XSPlotReader(cls.file)
        cls.reader.read()

    def test_allXS(self):
        """ Check XS read correctly
        The check happens by assuring binary representations of the data,
        where it matters, matches.
        """
        with open('expectedXS.pickle', 'rb') as fh:
            expectedData = pickle.load(fh)

        # reference to this object's reader's results:
        res = self.reader.xsections

        # expectedData should be exactly the same as self.xsections now!
        assert set(expectedData.keys()) == set(res.keys())
        for key in expectedData.keys():
            assert_equal(res[key].xsdata, expectedData[key].xsdata)
            assert res[key].MTdescrip == res[key].MTdescrip

            # check metadata values
            for key2 in expectedData[key].metadata.keys():
                assert all(res[key].metadata[key2] == expectedData[key].metadata[key2])


if __name__ == '__main__':
    unittest.main()
