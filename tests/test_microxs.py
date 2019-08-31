"""Test the microXS reader."""

import os
import unittest

import numpy

from serpentTools.settings import rc
from serpentTools.data import getFile
from serpentTools.parsers import MicroXSReader
from serpentTools.messages import SerpentToolsException


class TestBadFile(unittest.TestCase):
    """
    Test bad files.

    Tests:
        1. test_noResults: file with no results
    Raises SerpentToolsException
    """

    def test_noResults(self):
        """Verify that an error is raised when no results exist in the file"""
        badFile = 'bad_results_file.m'
        with open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(str(_line))
        badReader = MicroXSReader(badFile)
        with self.assertRaises(SerpentToolsException):
            badReader.read()
        os.remove(badFile)


class TestMicroXSReader(unittest.TestCase):
    """
    Class functionality tests for the micro xs reader.

    Tests:

        1. test_emptyAttributes:
                        check that some results are
                        collected.
        2. test_univNum:
                        check that the number of universes
                        is correct.
        3. test_fluxdata:
                        Check that flux ratios and
                        uncertainties are properly stored
        4. test_fydata:
                        Check that fission yields values
                        are properly stored
        5. test_geyFY*
                        Check the getFY method implemented
                        to obtain fission yields for a specific
                        parent, energy and fission product.
            Raises SerpentToolsException:
                        non-existing parent or fission product
        5.1 test_getFYnoParent:
                        Check that an error is raised
                        for a non-existing parent
                        e.g., 911110
        5.2 test_getFYnoEnergy:
                        Check that the closes fission yield
                        is obtained for a non-existing energy
        5.3 test_getFYnoDaughter:
                        Check that an error is raised
                        for a non-existing daughter (fission product)
                        e.g., 555550
        6. test_getXS*
                        Check the getXS method implemented
                        to obtain cross-sections for a specific
                        isotope and reaction. Returns empty list
                        for non existing isotope and reaction
            Raises SerpentToolsException:
                        non-existing universe or wrong
                        isotope formatting
        6.1 test_getXSnoUniv:
                        Check that an error is raised
                        for a non-existing universe
        6.2 test_getXSisotopeFormat:
                        Check that an error is raised
                        for a wrong isotope format
                        e.g., 92235000
        6.3 test_getXSkeys:
                        Check that the (isotope, reaction, isomeric)
                        tuple are properly stored
        6.4 test_getXSvals:
                        Check that the group cross-sections
                        are properly stored
        6.5 test_getXSnoVals:
                        Check that an error is raised
                        for a non-existing (isotope, reaction, isomeric)
    """

    @classmethod
    def setUpClass(cls):
        cls.file = getFile('ref_mdx0.m')
        with rc:
            rc['microxs.getFY'] = True
            rc['microxs.getXS'] = True
            rc['microxs.getFlx'] = True
            cls.reader = MicroXSReader(cls.file)
            cls.reader.read()

    def test_emptyAttributes(self):
        """Verify that variables are not all empty"""
        mdxFile = getFile('ref_noXS_mdx0.m')
        with rc:
            rc['microxs.getFY'] = False  # do not store fission yields
            mdxReader = MicroXSReader(mdxFile)
            with self.assertRaises(SerpentToolsException):
                mdxReader.read()

    def test_univNum(self):
        """Test the expected number of universes."""
        expectedKeys = set('0')
        actualKeys = set(self.reader.xsVal.keys())
        self.assertSetEqual(expectedKeys, actualKeys)

    def test_fluxdata(self):
        """Test that flux ratios and uncertainties are properly stored."""
        univ = '0'
        expectedValue = numpy.array(
            [1.60327E+00, 1.59830E+00, 1.59005E+00, 1.57731E+00,
             1.55586E+00, 1.54909E+00, 1.54820E+00, 1.53829E+00,
             1.55250E+00, 1.54046E+00, 1.54549E+00, 1.55092E+00,
             1.54549E+00, 1.53785E+00, 1.54761E+00, 1.54864E+00,
             1.53520E+00, 1.52489E+00, 1.49595E+00, 1.51506E+00,
             1.50824E+00, 1.50808E+00, 1.48335E+00, 1.45860E+00])

        expectedUnc = numpy.array(
            [0.00351, 0.00086, 0.00052, 0.00025, 0.00023, 0.00020,
             0.00013, 0.00015, 0.00011, 0.00013, 0.00011, 0.00012,
             0.00015, 0.00016, 0.00012, 0.00019, 0.00018, 0.00026,
             0.00023, 0.00032, 0.00045, 0.00094, 0.00115, 0.00285])

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
        numpy.testing.assert_equal(excpectedIndYield, actualIndYield,
                                   err_msg='Independent fission yields are not'
                                           ' matching')
        numpy.testing.assert_equal(excpectedCumYield, actualCumYield,
                                   err_msg='Independent fission yields are not'
                                           ' matching')

    def test_getFYnoParent(self):
        """getFY method should raise exception due to non-existing parent."""
        with self.assertRaises(SerpentToolsException):
            self.reader.getFY(500000, 2.53000E-08, 531350)

    def test_getFYnoEnergy(self):
        """getFY method retrieves fission yields for non-existing energy."""
        # closest energy check
        actualIndYield, actualCumYield = self.reader.getFY(922350, 1E-05,
                                                           531350)
        excpectedIndYield = numpy.array([2.92737E-02])
        excpectedCumYield = numpy.array([6.28187E-02])
        numpy.testing.assert_equal(excpectedIndYield, actualIndYield)
        numpy.testing.assert_equal(excpectedCumYield, actualCumYield)

    def test_getFYnoDaughter(self):
        """getFY method should raise exception due to non-existing daughter."""
        with self.assertRaises(SerpentToolsException):
            self.reader.getFY(922350, 1E-05, 9999)

    def test_getXSnoUniv(self):
        """getXS method: non-existing universe."""
        with self.assertRaises(SerpentToolsException):
            self.reader.getXS('2', 982490, 18, 0)

    def test_getXSisotopeFormat(self):
        """getXS method: wrong isotope formatting."""
        with self.assertRaises(SerpentToolsException):
            vals, unc = self.reader.getXS('0', 5000000, 18, 0)

    def test_getXSkeys(self):
        """getXS method: all isotopes, reactions and isomeric are stored."""
        univ = '0'
        expectedXSdata = {(10010, 102, 0), (982490, 18, 0), (982510, 102, 0),
                          (982510, 16, 0), (982510, 17, 0), (982510, 18, 0),
                          (40090, 107, 0)}
        expectedKeys = set(expectedXSdata)
        actualKeys = set(self.reader.xsVal[univ].keys())
        self.assertSetEqual(expectedKeys, actualKeys)

    def test_getXSvals(self):
        """getXS method: cross-sections and uncertainties."""
        expectedValue = numpy.array([3.09753E-05, 3.33901E-05,
                                     3.57054E-05, 3.70926E-05, 3.61049E-05,
                                     3.39464E-05,
                                     3.39767E-05, 3.98315E-05, 5.38962E-05,
                                     7.96923E-05,
                                     1.18509E-04, 1.73915E-04, 2.54571E-04,
                                     3.38540E-04,
                                     4.52415E-04, 5.98190E-04, 7.69483E-04,
                                     1.04855E-03,
                                     1.31149E-03, 1.67790E-03, 2.15195E-03,
                                     2.70125E-03,
                                     3.44635E-03, 5.04611E-03])
        expectedUnc = numpy.array(
            [0.00011, 0.00002, 0.00001, 0.00000, 0.00000, 0.00000,
             0.00000, 0.00001, 0.00001, 0.00002, 0.00002, 0.00002,
             0.00002, 0.00001, 0.00001, 0.00002, 0.00002, 0.00003,
             0.00002, 0.00003, 0.00004, 0.00005, 0.00017, 0.00069])
        actualVal, actualUnc = self.reader.getXS('0', 10010, 102, 0)
        numpy.testing.assert_equal(actualVal, expectedValue)
        numpy.testing.assert_equal(actualUnc, expectedUnc)

    def test_getXSnoVals(self):
        """getXS method: non-existing cross-sections."""
        with self.assertRaises(SerpentToolsException):
            self.reader.getXS('0', 10050, 205, 0)


if __name__ == '__main__':
    unittest.main()
