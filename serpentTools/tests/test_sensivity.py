"""
Test the sensitivity reader
"""
# noqa: E126
import unittest
from collections import OrderedDict

from six import iteritems
from numpy import array, inf
from numpy.testing import assert_allclose

from serpentTools.data import getFile
from serpentTools.parsers.sensitivity import SensitivityReader
from serpentTools.tests import compareDictOfArrays

TEST_FILE = getFile('bwr_sens0.m')


class SensitivityTester(unittest.TestCase):
    """Class for testing the sensitivity reader."""
    def setUp(self):
        self.reader = SensitivityReader(TEST_FILE)
        self.reader.read()

    def test_expectedSensitivities(self):
        """Verify the sensitivity arrays are loaded correctly."""
        expected = {
            'fis2flx': array([[[
                 [[-2.61375000e-01, 7.10000000e-02],
                  [-1.04396000e-01, 1.30000000e-01]],

                 [[8.14309000e-04, 1.00000000e+00],
                  [-1.89700000e-03, 1.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [0.00000000e+00, 0.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [5.08970000e-03, 6.80000000e-01]],

                 [[-3.80915000e-02, 1.50000000e-01],
                  [-3.32722000e-02, 1.50000000e-01]],

                 [[-2.24098000e-01, 7.40000000e-02],
                  [-7.40533000e-02, 1.50000000e-01]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [-2.63575000e-04, 1.00000000e+00]]],


                [[[-1.82609000e-02, 8.50000000e-01],
                  [9.13794000e-03, 1.00000000e+00]],

                 [[1.05618000e-02, 1.00000000e+00],
                  [2.10562000e-02, 1.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [0.00000000e+00, 0.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [4.73019000e-02, 4.00000000e-01]],

                 [[-2.88227000e-02, 1.30000000e-01],
                  [-7.02287000e-02, 1.10000000e-01]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [1.05040000e-02, 6.80000000e-01]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [5.04490000e-04, 1.00000000e+00]]]]]),
            'keff': array([[[
                 [[2.33920000e-01, 8.00000000e-02],
                  [8.70984000e-02, 2.10000000e-01]],

                 [[-5.39529000e-03, 7.90000000e-01],
                  [-1.93425000e-04, 1.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [0.00000000e+00, 0.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [-5.16380000e-03, 7.60000000e-01]],

                 [[-6.34126000e-02, 8.10000000e-02],
                  [-5.09998000e-02, 9.00000000e-02]],

                 [[3.02727000e-01, 6.00000000e-02],
                  [1.43519000e-01, 8.30000000e-02]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [-6.34103000e-05, 1.00000000e+00]]],


                [[[-2.55744000e-02, 4.90000000e-01],
                  [-1.08870000e-01, 4.00000000e-01]],

                 [[7.10802000e-03, 1.00000000e+00],
                  [-1.57546000e-02, 1.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [0.00000000e+00, 0.00000000e+00]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [-2.26180000e-02, 7.00000000e-01]],

                 [[-3.26824000e-02, 1.20000000e-01],
                  [-1.20262000e-01, 8.30000000e-02]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [4.75881000e-02, 1.10000000e-01]],

                 [[0.00000000e+00, 0.00000000e+00],
                  [2.17649000e-03, 5.30000000e-01]]]]])
        }
        compareDictOfArrays(expected, self.reader.sensitivities,
                            'Error in sensitivities at {key}', testCase=self)

    def test_integratedSensitivities(self):
        """Verify the energy integrated sensitivities are correct."""
        expected = {
                'fis2flx': array([[
                       [[-3.65771000e-01, 5.50000000e-02],
                        [-1.08269000e-03, 1.00000000e+00],
                        [0.00000000e+00, 0.00000000e+00],
                        [5.08970000e-03, 6.80000000e-01],
                        [-7.13637000e-02, 1.10000000e-01],
                        [-2.98151000e-01, 6.50000000e-02],
                        [-2.63575000e-04, 1.00000000e+00]],

                       [[-9.12298000e-03, 1.00000000e+00],
                        [3.16180000e-02, 1.00000000e+00],
                        [0.00000000e+00, 0.00000000e+00],
                        [4.73019000e-02, 4.00000000e-01],
                        [-9.90513000e-02, 8.80000000e-02],
                        [1.05040000e-02, 6.80000000e-01],
                        [5.04490000e-04, 1.00000000e+00]]]]),
                'keff': array([[
                       [[3.21018000e-01, 7.40000000e-02],
                        [-5.58871000e-03, 1.00000000e+00],
                        [0.00000000e+00, 0.00000000e+00],
                        [-5.16380000e-03, 7.60000000e-01],
                        [-1.14412000e-01, 5.70000000e-02],
                        [4.46246000e-01, 4.20000000e-02],
                        [-6.34103000e-05, 1.00000000e+00]],

                       [[-1.34445000e-01, 3.40000000e-01],
                        [-8.64658000e-03, 1.00000000e+00],
                        [0.00000000e+00, 0.00000000e+00],
                        [-2.26180000e-02, 7.00000000e-01],
                        [-1.52945000e-01, 7.30000000e-02],
                        [4.75881000e-02, 1.10000000e-01],
                        [2.17649000e-03, 5.30000000e-01]]]])
        }
        compareDictOfArrays(expected, self.reader.energyIntegratedSens,
                            'energy integrated sensitivities')

    def test_parameters(self):
        expected = {'nMat': 1, 'nEne': 2, 'nZai': 2, 'nPert': 7, 'latGen': 14}
        for key, value in iteritems(expected):
            actual = getattr(self.reader, key)
            self.assertEqual(value, actual,
                             msg="Parameter: {}".format(key))

    def test_energyBounds(self):
        """Verify the energy bounds are stored properly."""
        expectedBounds = array([0, 6.250E-7, 1.0E37])
        expectedLethWidths = array([inf, 9.94812E+1])
        for expected, actualStr in zip(
                (expectedBounds, expectedLethWidths),
                ('energies', 'lethargyWidths')):
            actual = getattr(self.reader, actualStr)
            assert_allclose(expected, actual, err_msg=actualStr)

    def test_perts(self):
        """Verify the ordered dictionary of perturbations is correct."""
        expected = OrderedDict([
            ('total xs', 0), ('ela scatt xs', 1), ('sab scatt xs', 2),
            ('inl scatt xs', 3), ('capture xs', 4), ('fission xs', 5),
            ('nxn xs', 6)])
        actual = self.reader.perts
        self.assertDictEqual(expected, actual)

    def test_zai(self):
        """Verify the ordered dictionary of perturbed isotopes is correct."""
        expected = OrderedDict([
            (922350, 0), (922380, 1)])
        actual = self.reader.zais
        self.assertDictEqual(expected, actual)

    def test_materials(self):
        """Verify the ordered dictionary of perturbed materials is correct."""
        expected = OrderedDict([
            ('total', 0)])
        actual = self.reader.materials
        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
