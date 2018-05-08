"""Test the microXS reader."""

import os
import unittest

import numpy

from serpentTools.settings import rc
from serpentTools.tests import TEST_ROOT
from serpentTools.parsers import MdxReader
from serpentTools.messages import SerpentToolsException

class _MicroXSTesterHelper(unittest.TestCase):
    """Test case to share setUpClass for testing Results Reader"""
    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'ref_mdx.m')
        with rc:
            rc['microxs.getFY'] = True  # do not store fission yields
            rc['microxs.getXS'] = True
            rc['microxs.getFlx'] = True
            cls.reader = MdxReader(cls.file)
        cls.reader.read()

class MicroXSTester(_MicroXSTesterHelper):
    """Class for testing the mdx reader."""

    def test_raiseError(self):
        """Verify that the reader raises an error for unexpected EOF"""
        badFile = os.path.join(TEST_ROOT, 'bad_mdx_file.m')
        with open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(str(_line))
        badReader = MdxReader(badFile)
        with self.assertRaises(SerpentToolsException):
            badReader.read()
        os.remove(badFile)

    def test_univ(self):
        """Test the expected number of universes."""
        expectedUniv = {'0'}
        expectedKeys = set(expectedUniv)
        actualKeys = set(self.reader.microXS.keys())
        self.assertSetEqual(expectedKeys, actualKeys)

    def test_xsdata(self):
        """Test the xs storage for the reader."""

        univ = '0'
        expectedXSdata = {(10010, 102, 0), (982490, 18, 0 ), (982510, 102, 0),
                            (982510, 16, 0), (982510, 17, 0), (982510, 18, 0),
                            (40090, 107, 0)}

        expectedValue = [3.09753E-05, 3.33901E-05,
                           3.57054E-05, 3.70926E-05, 3.61049E-05, 3.39464E-05,
                           3.39767E-05, 3.98315E-05, 5.38962E-05, 7.96923E-05,
                           1.18509E-04, 1.73915E-04, 2.54571E-04, 3.38540E-04,
                           4.52415E-04, 5.98190E-04, 7.69483E-04, 1.04855E-03,
                           1.31149E-03, 1.67790E-03, 2.15195E-03, 2.70125E-03,
                           3.44635E-03, 5.04611E-03]

        expectedKeys = set(expectedXSdata)
        actualKeys = set(self.reader.microXS[univ].keys())
        self.assertSetEqual(expectedKeys, actualKeys)

        numpy.testing.assert_equal(self.reader.microXS[univ][(10010, 102, 0)],
                                   expectedValue)

    def test_fluxdata(self):
        """Test flux and uncertainties for the reader."""

        univ = '0'
        expectedValue = [1.60327E+00, 1.59830E+00, 1.59005E+00, 1.57731E+00,
                         1.55586E+00, 1.54909E+00, 1.54820E+00, 1.53829E+00,
                         1.55250E+00, 1.54046E+00, 1.54549E+00, 1.55092E+00,
                         1.54549E+00, 1.53785E+00, 1.54761E+00, 1.54864E+00,
                         1.53520E+00, 1.52489E+00, 1.49595E+00, 1.51506E+00,
                         1.50824E+00, 1.50808E+00, 1.48335E+00, 1.45860E+00]

        expectedUnc = [0.00351, 0.00086, 0.00052, 0.00025, 0.00023, 0.00020,
                       0.00013, 0.00015, 0.00011, 0.00013, 0.00011, 0.00012,
                       0.00015, 0.00016, 0.00012, 0.00019, 0.00018, 0.00026,
                       0.00023, 0.00032, 0.00045, 0.00094, 0.00115, 0.00285]

        numpy.testing.assert_equal(self.reader.fluxRatio[univ], expectedValue)
        numpy.testing.assert_equal(self.reader.fluxUnc[univ], expectedUnc)

    def test_fydata(self):
        """Test fission yields for the reader."""

        parent = 922350
        energy = 2.53000E-08
        fp = 531350
        excpectedIndYield = numpy.array([2.92737E-02])
        excpectedCumYield = numpy.array([6.28187E-02])
        actualIndYield, actualCumYield = self.reader.getFY(parent, energy, fp)
        numpy.testing.assert_equal(excpectedIndYield, actualIndYield)
        numpy.testing.assert_equal(excpectedCumYield, actualCumYield)


if __name__ == '__main__':
    unittest.main()