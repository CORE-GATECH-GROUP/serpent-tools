"""Test the depletion file."""
import os
import unittest

import numpy

from serpentTools.settings import rc
from serpentTools.tests import TEST_ROOT
from serpentTools.parsers.depletion import DepletionReader


class _DepletionTestHelper(unittest.TestCase):
    """Base class to setup the depletion reader and material tests."""

    @classmethod
    def setUpClass(cls):
        filePath = os.path.join(TEST_ROOT, 'ref_dep.m')
        cls.rc = rc
        with cls.rc as tempRC:
            tempRC['depletion.processTotal'] = True
            tempRC['depletion.materials'] = ['fuel', ]
            tempRC['depletion.materialVariables'] = [
                'BURNUP', 'ADENS', 'ING_TOX']
            cls.reader = DepletionReader(filePath)
        cls.reader.read()


class DepletionTester(_DepletionTestHelper):
    """Class that tests the functionality of the depletion reader."""

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
                numpy.testing.assert_equal(self.reader.metadata[key],
                                           expectedValue)

    def test_ReadMaterials(self):
        """Verify the reader stored the correct materials."""
        expectedMaterials = ['fuel']
        for material in expectedMaterials:
            with self.subTest():
                self.assertIn(material, self.reader.materials)


class DepletedMaterialTester(_DepletionTestHelper):
    """Class that tests the functionality of the DepletedMaterial class"""

    @classmethod
    def setUpClass(cls):
        _DepletionTestHelper.setUpClass()
        cls.material = cls.reader.materials['fuel']
        cls.requestedDays = [0.0, 0.5, 1.0, 5.0, 10.0, 25.0, 50.0]
        cls.fuelBU = cls.material.burnup

    def test_materials(self):
        """Verify the materials are read in properly."""
        self.assertIn('fuel', self.reader.materials)
        expectedAdens = numpy.array([
            [0.00000E+00, 2.44791E-10, 1.07741E-09, 7.54422E-09, 1.54518E-08,
             2.45253E-08, 3.05523E-08, 3.98843E-08, 4.28827E-08, 4.37783E-08,
             4.46073E-08, 4.58472E-08, 4.73590E-08, 4.84031E-08],
            [0.00000E+00, 3.92719E-09, 5.62744E-09, 6.09339E-09, 6.14629E-09,
             6.05726E-09, 6.14402E-09, 6.13795E-09, 6.10821E-09, 6.13674E-09,
             6.18320E-09, 6.18233E-09, 6.08629E-09, 6.35706E-09],
            [5.58287E-04, 5.57764E-04, 5.57298E-04, 5.55440E-04, 5.53500E-04,
             5.51257E-04, 5.48871E-04, 5.41946E-04, 5.35434E-04, 5.24946E-04,
             5.14643E-04, 4.95299E-04, 4.78407E-04, 4.58932E-04],
            [0.00000E+00, 1.63219E-08, 6.37555E-08, 4.71450E-07, 1.11725E-06,
             2.08488E-06, 3.13490E-06, 6.42737E-06, 9.58635E-06, 1.44874E-05,
             1.90933E-05, 2.73021E-05, 3.42000E-05, 4.11589E-05],
            [0.00000E+00, 9.58524E-34, 6.02782E-33, 6.83433E-32, 2.06303E-31,
             5.02500E-31, 1.07151E-30, 4.79600E-30, 1.75720E-29, 1.46446E-28,
             3.98274E-28, 1.04091E-27, 3.12542E-27, 6.72465E-27],
            [0.00000E+00, 2.90880E-14, 5.57897E-14, 1.62569E-13, 2.75249E-13,
             4.06673E-13, 5.46031E-13, 9.58962E-13, 1.35027E-12, 1.99694E-12,
             2.64702E-12, 3.90487E-12, 5.05218E-12, 6.43096E-12],
            [6.88332E-02, 6.88337E-02, 6.88341E-02, 6.88357E-02, 6.88374E-02,
             6.88394E-02, 6.88415E-02, 6.88476E-02, 6.88535E-02, 6.88632E-02,
             6.88729E-02, 6.88917E-02, 6.89087E-02, 6.89291E-02],
        ])
        expectedIngTox = numpy.array([
            [0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00],
            [0.00000E+00, 3.56712E+07, 5.11147E+07, 5.53470E+07, 5.58276E+07,
             5.50189E+07, 5.58069E+07, 5.57517E+07, 5.54817E+07, 5.57408E+07,
             5.61628E+07, 5.61549E+07, 5.52826E+07, 5.77420E+07],
            [1.68091E+00, 1.67934E+00, 1.67793E+00, 1.67234E+00, 1.66650E+00,
             1.65974E+00, 1.65256E+00, 1.63171E+00, 1.61210E+00, 1.58053E+00,
             1.54951E+00, 1.49126E+00, 1.44041E+00, 1.38177E+00],
            [0.00000E+00, 7.63264E+00, 2.98141E+01, 2.20465E+02, 5.22464E+02,
             9.74958E+02, 1.46598E+03, 3.00564E+03, 4.48288E+03, 6.77478E+03,
             8.92865E+03, 1.27673E+04, 1.59930E+04, 1.92472E+04],
            [0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00],
            [0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00],
            [5.22355E+01, 1.16651E+09, 1.10827E+09, 1.25209E+09, 1.44102E+09,
             1.49595E+09, 1.66322E+09, 1.80206E+09, 1.79453E+09, 1.79100E+09,
             1.80188E+09, 1.75346E+09, 1.60021E+09, 1.89771E+09],
        ])
        self.assertListEqual(self.material.zai,
                             self.reader.metadata['zai'])
        numpy.testing.assert_equal(self.material.adens, expectedAdens)
        numpy.testing.assert_equal(self.material.ingTox, expectedIngTox)

    def test_getXY_burnup_full(self):
        """
        Verify the material can produce the full burnup vector through getXY.
        """
        actual, _days = self.material.getXY('days', 'burnup', )
        numpy.testing.assert_equal(actual, self.fuelBU)

    def test_getXY_burnup_slice(self):
        """Verify depletedMaterial getXY correctly slices a vector."""
        actual = self.material.getXY('days', 'burnup', self.requestedDays)
        expected = [0.0E0, 1.90317E-2, 3.60163E-2, 1.74880E-1, 3.45353E-01,
                    8.49693E-01, 1.66071E0]
        numpy.testing.assert_equal(actual, expected)

    def test_getXY_adens(self):
        """Verify depletedMaterial getXY can return a requested subsection."""
        names = ['Xe135', 'U235', 'lost']
        expected = numpy.array([
            [0.00000E+00, 3.92719E-09, 5.62744E-09, 6.14629E-09, 6.14402E-09,
             6.10821E-09, 6.18320E-09],
            [5.58287E-04, 5.57764E-04, 5.57298E-04, 5.53500E-04, 5.48871E-04,
             5.35434E-04, 5.14643E-04],
            [0.00000E+00, 2.90880E-14, 5.57897E-14, 2.75249E-13, 5.46031E-13,
             1.35027E-12, 2.64702E-12],
        ], float)
        actual = self.material.getXY('days', 'adens', names=names,
                                     timePoints=self.requestedDays)
        numpy.testing.assert_allclose(actual, expected, rtol=1E-4)

    def test_getXY_adensAndTime(self):
        """Verify correct atomic density and time slice are returned."""
        actualAdens, actualDays = self.material.getXY('days', 'adens',
                                                      names=['Xe135'])
        numpy.testing.assert_equal(actualDays, self.reader.metadata['days'])

    def test_getXY_raisesError_badTime(self):
        """Verify that a ValueError is raised for non-present requested days."""
        badDays = [-1, 0, 50]
        with self.assertRaises(KeyError):
            self.material.getXY('days', 'adens', timePoints=badDays)

    def test_fetchData(self):
        """Verify that key errors are raised when bad data are requested."""
        with self.assertRaises(KeyError):
            _ = self.material['fake units']


if __name__ == '__main__':
    unittest.main()
