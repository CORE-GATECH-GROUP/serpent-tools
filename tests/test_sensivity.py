"""
Test the sensitivity reader
"""
from unittest import TestCase, skipUnless
from collections import OrderedDict
from itertools import product
from io import BytesIO

from numpy import array, inf
from numpy.testing import assert_allclose, assert_array_equal
from serpentTools.data import getFile
from serpentTools.parsers.sensitivity import SensitivityReader

from tests import (
    plotTest, getLegendTexts, MatlabTesterHelper, compareDictOfArrays,
    HAS_SCIPY,
)

TEST_FILE = getFile('bwr_sens0.m')


class SensitivityTestHelper(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reader = SensitivityReader(TEST_FILE)
        cls.reader.read()


class SensitivityTester(SensitivityTestHelper):
    """Class for testing the sensitivity reader."""

    def test_expectedSensitivities(self):
        """Verify the sensitivity arrays are loaded correctly."""
        expected = {
            'fis2flx': array([[[
                [[-2.61375000e-01, 7.10000000e-02],  # noqa: E126
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
                'fis2flx': array([[  # noqa: E126
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
        for key, value in expected.items():
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


class SensitivityPlotTester(SensitivityTestHelper):
    """Class for testing rudimentary plot aspects of the reader."""

    ZAIS = [922350]
    RESP = 'keff'
    DEFAULT_XLABEL = "Energy [eV]"

    def _plot(self, **kwargs):
        """Shortcut for plotting."""
        return self.reader.plot(self.RESP, **kwargs)

    def _checkAxisLabels(self, ax, xlabel, ylabel, msg=None):
        self.assertEqual(ax.get_xlabel(), xlabel, msg=msg)
        self.assertEqual(ax.get_ylabel(), ylabel, msg=msg)

    @plotTest
    def test_plot_normalized(self):
        """Verify the default axis labels when normalized and with errors."""
        ax = self._plot(normalize=True, sigma=3)
        self._checkAxisLabels(ax, self.DEFAULT_XLABEL,
                              'Sensitivity per unit lethargy $\\pm3\\sigma$')

    @plotTest
    def test_plot_notNormalized_noSigma(self):
        """
        Verify the default axis labels when not normalized nor errors given.
        """
        ax = self._plot(normalize=False, sigma=0)
        self._checkAxisLabels(ax, self.DEFAULT_XLABEL,
                              'Sensitivity')

    @plotTest
    def test_plot_passLabels_noset(self):
        """Verify that the axis labels can be set to empty strings."""
        xlabel = False
        ylabel = ""
        nosetLabel = ""  # un-set matplotlib axis label
        ax = self._plot(xlabel=xlabel, ylabel=ylabel)
        self._checkAxisLabels(ax, nosetLabel, nosetLabel)

    def _generateLegendTexts(self, formatter, zais=None, mats=None,
                             perts=None):
        reader = self.reader
        zais = zais or list(reader.zais.keys())
        mats = mats or list(reader.materials.keys())
        perts = perts or list(reader.perts.keys())
        texts = []
        # match iteration order of sensitivity reader
        for z, m, p in product(zais, mats, perts):
            texts.append(formatter.format(z=z, m=m, p=p, r=self.RESP))
        return texts

    @plotTest
    def test_plot_labelFormatter(self):
        """Verify the label formatter for sensitivity plots."""
        labelFmt = "{m} {z} {p} {r}"
        ax = self._plot(labelFmt=labelFmt)
        actual = getLegendTexts(ax)
        expected = self._generateLegendTexts(labelFmt)
        self.assertListEqual(actual, expected)

    @plotTest
    def test_plot_labelFormatter_oneIso(self):
        """Verify the label formatter for sensitivity plots - pass one ZAI."""
        labelFmt = "{m} {z} {p} {r}"
        ax = self._plot(zai=922350, labelFmt=labelFmt)
        actual = getLegendTexts(ax)
        expected = self._generateLegendTexts(labelFmt, zais=[922350, ])
        self.assertListEqual(actual, expected)

    @plotTest
    def test_plot_raiseError_missingPert(self):
        """Verify that an error is raised if a bad perturbation is passed."""
        with self.assertRaises(KeyError):
            self._plot(zai=-100)

    @plotTest
    def test_plot_raiseError_missingResp(self):
        """Verify that an error is raised if a bad response is passed."""
        with self.assertRaises(KeyError):
            self.reader.plot("THIS SHOULD FAIL")


class Sens2MatlabHelper(MatlabTesterHelper, SensitivityTestHelper):
    """Base class for comparing sensitivity reader to matlab"""

    def setUp(self):
        convertIx = int(self.RECONVERT)
        self.attrMap = {
            key: value[convertIx]
            for key, value in SensitivityReader._RECONVERT_ATTR_MAP.items()}
        self.listMap = {
            key: value[convertIx]
            for key, value in SensitivityReader._RECONVERT_LIST_MAP.items()}
        self.sensFmts = SensitivityReader._RECONVERT_SENS_FMT[convertIx]
        MatlabTesterHelper.setUp(self)

    def _testGathered(self, gathered):
        """Test the contents of the gathered data"""
        # attributes
        for attr, expKey in self.attrMap.items():
            self.assertTrue(expKey in gathered, msg=expKey)
            expVal = getattr(self.reader, attr)
            actVal = gathered[expKey]
            assert_array_equal(actVal, expVal, err_msg=expKey)

        # lists -> compare against ordered dictionaries
        for attr, expKey in self.listMap.items():
            self.assertTrue(expKey in gathered, msg=expKey)
            expVal = list(getattr(self.reader, attr).keys())
            actVal = gathered[expKey]
            assert_array_equal(actVal, expVal, err_msg=expKey)

        for sensKey, expSens in self.reader.sensitivities.items():
            expEneSens = self.reader.energyIntegratedSens[sensKey]
            sensName, eneName = [fmt.format(sensKey) for fmt in self.sensFmts]
            self.assertTrue(sensName in gathered,
                            msg="{}//{}".format(sensKey, sensName))
            self.assertTrue(eneName in gathered,
                            msg="{}//{}".format(sensKey, eneName))
            actSens = gathered[sensName]
            actEneSens = gathered[eneName]
            assert_array_equal(actSens, expSens,
                               err_msg="{}//{}".format(sensKey, sensName))
            assert_array_equal(actEneSens, expEneSens,
                               err_msg="{}//{}".format(sensKey, eneName))

    def test_gatherMatlab(self):
        """Test the readers ability to gather for matlab"""
        gathered = self.reader._gather_matlab(self.RECONVERT)
        self._testGathered(gathered)

    @skipUnless(HAS_SCIPY, "SCIPY needed for this test")
    def test_toMatlab(self):
        """Verify the contents of the reader can be written to matlab"""
        from scipy.io import loadmat
        stream = BytesIO()
        self.reader.toMatlab(stream)
        gathered = loadmat(stream)
        # some vectors will be written as 2D row/column vectors
        # need to reshape them to 1D arrays
        keys = gathered.keys()
        for key in keys:
            if key[:2] == '__':  # special stuff from savemat
                continue
            value = gathered[key]
            if value.size > 1 and 1 in value.shape:
                gathered[key] = value.flatten()


class ReconvertedSens2MatlabTester(Sens2MatlabHelper):
    """Class for testing the sens - matlab conversion with original names"""
    RECONVERT = True


class UnconvertedSens2MatlabTester(Sens2MatlabHelper):
    """Class for testing the sens - matlab conversion with unconverted names"""
    RECONVERT = False


del Sens2MatlabHelper
