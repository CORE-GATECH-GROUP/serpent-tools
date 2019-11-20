"""Test the detector reader."""

from os import remove
from unittest import TestCase

from collections import OrderedDict

from numpy import arange, array
from numpy.testing import assert_equal
from serpentTools.parsers import read
from serpentTools.data import getFile
from serpentTools.detectors import (
    CartesianDetector, HexagonalDetector, CylindricalDetector)

from tests import compareDictOfArrays


class DetectorHelper(TestCase):
    """ Class that assists setting up and testing readers"""

    @classmethod
    def setUpClass(cls):
        cls.reader = read(cls.FILE_PATH, 'det')
        cls.detectors = cls.reader.detectors

    def test_loadedDetectors(self):
        """Verify that all anticipated detectors are loaded."""
        expectedNames = set(self.EXPECTED_DETECTORS.keys())
        actualNames = set(self.reader.detectors.keys())
        self.assertSetEqual(
            expectedNames, actualNames,
            msg="Failure reading detectors from {}".format(self.FILE_PATH))
        for name, cls in self.EXPECTED_DETECTORS.items():
            actualDet = self.detectors[name]
            self.assertIsInstance(
                actualDet, cls, msg="{} is {}, should be {}: - {}"
                .format(name, actualDet.__class__.__name__, cls,
                        self.FILE_PATH))

    def test_detectorGrids(self):
        """Verify that all grids are loaded."""
        baseMsg = "Key: {key}"
        for detName, gridDict in self.EXPECTED_GRIDS.items():
            msg = baseMsg + "  Reading: " + self.__class__.__name__
            actualGrids = self.detectors[detName].grids
            compareDictOfArrays(
                gridDict, actualGrids, testCase=self, fmtMsg=msg)

    def test_detectorIndex(self):
        """Verify that the detector tally index is properly constructed."""
        for detName, expectedIndex in self.EXPECTED_INDEXES.items():
            actualIndex = self.detectors[detName].indexes
            self.assertEqual(actualIndex, expectedIndex)

    def test_detectorSlice(self):
        """Verify that the detector slicing is working well."""
        for detName, params in self.SLICING.items():
            fixed = params['fixed']
            expectedTallies = params['tallies']
            expectedErrors = params['errors']
            detector = self.detectors[detName]
            tallies = detector.slice(fixed)
            errors = detector.slice(fixed, data='errors')
            for expected, actual, what in zip(
                    (expectedTallies, expectedErrors),
                    (tallies, errors), ('tallies', 'errors')):
                assert_equal(expected, actual,
                             err_msg="Detector {} {}\nFixed: {}"
                             .format(detName, what, fixed))

    def test_iterDets(self):
        """Verify the iterDets method is functional."""
        for name, det in self.reader.iterDets():
            self.assertIn(name, self.reader.detectors, msg=name)
            self.assertIs(det, self.reader.detectors[name], msg=name)

    def test_getitem(self):
        """Verify the getitem method for extracting detectors."""
        for name, det in self.reader.detectors.items():
            fromGetItem = self.reader[name]
            self.assertIs(fromGetItem, det, msg=name)
        with self.assertRaises(KeyError):
            self.reader['this should fail']


class CartesianDetectorTester(DetectorHelper):
    """
    Class to test the detector reader.

    Detectors:

        1. xyFissionCapt: 5x5 xy mesh of the problem with two
           reactions: U-235 fission and capture
    """

    FILE_PATH = getFile('ref_det0.m')
    DET_NAME = 'xyFissionCapt'
    EXPECTED_DETECTORS = {
        DET_NAME: CartesianDetector
    }
    _EXPECTED_GRIDS = {
        'X': array([
            [-1.95000E+00, - 1.17000E+00, - 1.56000E+00],
            [- 1.17000E+00, - 3.90000E-01, - 7.80000E-01],
            [- 3.90000E-01, 3.90000E-01, 2.22045E-16],
            [3.90000E-01, 1.17000E+00, 7.80000E-01],
            [1.17000E+00, 1.95000E+00, 1.56000E+00]
        ]),
        'Z': array([[-1.00000E+37, 1.00000E+37, 0.00000E+00]])
    }
    _EXPECTED_GRIDS['Y'] = _EXPECTED_GRIDS['X']
    EXPECTED_GRIDS = {
        DET_NAME: _EXPECTED_GRIDS
    }
    _INDEXES = ("reaction", "ymesh", "xmesh")
    EXPECTED_INDEXES = {DET_NAME: _INDEXES}

    SLICING = {DET_NAME: {
        'fixed': {'reaction': 0},
        'tallies': array([
            [2.55119E-01, 2.55077E-01, 2.53685E-01, 2.55592E-01, 2.58450E-01],
            [2.54101E-01, 2.53408E-01, 2.56666E-01, 2.55375E-01, 2.52936E-01],
            [2.56006E-01, 2.51002E-01, 2.55479E-01, 2.52002E-01, 2.54708E-01],
            [2.54957E-01, 2.53399E-01, 2.48180E-01, 2.52915E-01, 2.53914E-01],
            [2.58394E-01, 2.50217E-01, 2.59642E-01, 2.54025E-01, 2.57076E-01],
        ]),
        'errors': array([
            [0.01445, 0.01063, 0.01190, 0.01193, 0.01334],
            [0.01006, 0.00916, 0.01240, 0.00933, 0.01002],
            [0.01317, 0.01187, 0.01386, 0.01120, 0.01171],
            [0.01081, 0.00885, 0.01127, 0.00893, 0.01161],
            [0.01250, 0.01121, 0.01460, 0.01142, 0.01219],
        ]),
    },
    }

    def test_sharedPlot(self):
        """Verify that the same axes object is returned on subsequent plots
        """
        det = self.detectors[self.DET_NAME]
        # plot along two reactions with no axes call
        # ensure that returned objects are equal
        ax0 = det.plot(fixed={'reaction': 0, 'ymesh': 0})
        ax1 = det.plot(fixed={'reaction': 1, 'ymesh': 0})
        self.assertTrue(ax0 is ax1)


class HexagonalDetectorTester(DetectorHelper):
    """
    Class for testing the hexagonal detectors
    """
    FILE_PATH = getFile('hexplot_det0.m')
    EXPECTED_DETECTORS = {
        'hex2': HexagonalDetector,
        'hex3': HexagonalDetector,
    }
    _INDEXES = ("ycoord", "xcoord")
    EXPECTED_INDEXES = {'hex2': _INDEXES}
    EXPECTED_INDEXES['hex3'] = EXPECTED_INDEXES['hex2']

    EXPECTED_GRIDS = {
        'hex2': {
            'COORD': array([
                [-3.000000E+00, -1.732051E+00], [-2.500000E+00, -8.660254E-01],
                [-2.000000E+00, 0.000000E+00], [-1.500000E+00, 8.660254E-01],
                [-1.000000E+00, 1.732051E+00], [-2.000000E+00, -1.732051E+00],
                [-1.500000E+00, -8.660254E-01], [-1.000000E+00, 0.000000E+00],
                [-5.000000E-01, 8.660254E-01], [0.000000E+00, 1.732051E+00],
                [-1.000000E+00, -1.732051E+00], [-5.000000E-01, -8.660254E-01],
                [0.000000E+00, 0.000000E+00], [5.000000E-01, 8.660254E-01],
                [1.000000E+00, 1.732051E+00], [0.000000E+00, -1.732051E+00],
                [5.000000E-01, -8.660254E-01], [1.000000E+00, 0.000000E+00],
                [1.500000E+00, 8.660254E-01], [2.000000E+00, 1.732051E+00],
                [1.000000E+00, -1.732051E+00], [1.500000E+00, -8.660254E-01],
                [2.000000E+00, 0.000000E+00], [2.500000E+00, 8.660254E-01],
                [3.000000E+00, 1.732051E+00],
            ]),
            'Z': array([[0, 0, 0]]),
        }
    }

    # Hex grid for type 3 detector, given the same parameters as a type 2
    # contains the same coordinates, with the x and y values swapped
    EXPECTED_GRIDS['hex3'] = {
        'Z': EXPECTED_GRIDS['hex2']['Z'],
        'COORD': EXPECTED_GRIDS['hex2']['COORD'][:, ::-1],
    }

    SLICING = {
        'hex2': {
            'fixed': {'ycoord': 1},
            'tallies': array([0.181565, 0.186038, 0.193088, 0.195448,
                              0.195652]),
            'errors': array([0.02561, 0.0259, 0.02525, 0.02104, 0.02101]),
        },
        'hex3': {
            'fixed': None,
            'tallies': array([
                [0.172245, 0.185047, 0.183986, 0.188593, 0.181429],
                [0.187389, 0.189741, 0.189085, 0.195592, 0.19357],
                [0.188575, 0.189483, 0.19107, 0.190542, 0.19633],
                [0.199519, 0.196765, 0.196656, 0.193902, 0.186121],
                [0.191783, 0.187015, 0.187476, 0.182367, 0.175803],
            ]),
            'errors': array([
                [0.02523, 0.02492, 0.01933, 0.02428, 0.02403],
                [0.02212, 0.0286, 0.02614, 0.02321, 0.01673],
                [0.01913, 0.0226, 0.01927, 0.021, 0.02622],
                [0.02301, 0.01718, 0.02042, 0.02583, 0.02797],
                [0.02167, 0.02281, 0.02397, 0.02289, 0.02602],
            ])
        },
    }


class CylindricalDetectorTester(DetectorHelper):
    """Class that tests the cylindrical detector reader."""

    FILE_PATH = getFile('radplot_det0.m')
    DET_NAME = 'rad1'
    EXPECTED_DETECTORS = {
        DET_NAME: CylindricalDetector,
    }
    _EXPECTED_GRIDS = {
        'R': array([
            [0.00000E+00, 1.50000E+00, 7.50000E-01],
            [1.50000E+00, 3.00000E+00, 2.25000E+00],
            [3.00000E+00, 4.50000E+00, 3.75000E+00],
            [4.50000E+00, 6.00000E+00, 5.25000E+00],
            [6.00000E+00, 7.50000E+00, 6.75000E+00]
        ]),
        'PHI': array([
            [0.00000E+00, 1.57000E+00, 7.85000E-01],
            [1.57000E+00, 3.14000E+00, 2.35500E+00],
            [3.14000E+00, 4.71000E+00, 3.92500E+00],
            [4.71000E+00, 6.28000E+00, 5.49500E+00]
        ]),
        'Z': array([[0.00000E+00, 0.00000E+00, 0.00000E+00]])
    }
    EXPECTED_GRIDS = {DET_NAME: _EXPECTED_GRIDS}
    _INDEXES = ("phi", "rmesh")
    EXPECTED_INDEXES = {DET_NAME: _INDEXES}

    SLICING = {
        DET_NAME: {
            'fixed': {'rmesh': 2},
            'tallies': array([0.0341559, 0.032754, 0.0332801, 0.0326715]),
            'errors': array([0.04018, 0.04582, 0.0467, 0.04346]),
        },
    }


TEST_SUB_CLASSES = {CartesianDetectorTester, HexagonalDetectorTester,
                    CylindricalDetectorTester}


COMBINED_OUTPUT_FILE = 'combinedDets_det0.m'
SINGLE_TALLY_FILE = "single_det0.m"


def setUpModule():
    """
    Setup the test fixture for test.

    Combine all output files from standalone tests into one file.
    This will be used by a combined reader to demonstrate that the
    DetectorReader can handle files with a mixed bag of detectors.
    """
    with open(COMBINED_OUTPUT_FILE, 'w') as out:
        for subCls in TEST_SUB_CLASSES:
            with open(subCls.FILE_PATH) as subFile:
                out.write(subFile.read())
    with open(SINGLE_TALLY_FILE, 'w') as out:
        out.write("""
DETone = [
    1    1    1    1    1    1    1    1    1    1  8.19312E+17 0.05187
];""")


def tearDownModule():
    """Remove any test files created for this module."""
    remove(COMBINED_OUTPUT_FILE)
    remove(SINGLE_TALLY_FILE)


class CombinedDetTester(DetectorHelper):
    """
    Class that reads and tests from an output file with many detector types.
    """

    FILE_PATH = COMBINED_OUTPUT_FILE
    EXPECTED_GRIDS = {}
    EXPECTED_DETECTORS = {}
    EXPECTED_INDEXES = {}
    SLICING = {}
    for cls in TEST_SUB_CLASSES:
        EXPECTED_GRIDS.update(cls.EXPECTED_GRIDS)
        EXPECTED_INDEXES.update(cls.EXPECTED_INDEXES)
        EXPECTED_DETECTORS.update(cls.EXPECTED_DETECTORS)
        SLICING.update(cls.SLICING)


del DetectorHelper


class SingleTallyTester(TestCase):
    """Test storing detector data with a single tally"""

    def setUp(self):
        self.detector = read(SINGLE_TALLY_FILE, 'det').detectors['one']

    def test_singleTally(self):
        """Test the conversion of a single tally to floats, not arrays"""
        self.assertTrue(isinstance(self.detector.tallies, float))
        self.assertTrue(isinstance(self.detector.errors, float))
        self.assertEqual(self.detector.tallies, 8.19312E17)
        self.assertEqual(self.detector.errors, 0.05187)


class TimeBinnedDetectorTester(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reader = read(getFile('time_det0.m'), 'det')
        cls.timeDet = cls.reader['FP']

    def test_timeDetector(self):
        """Verify a simple time-binned detector is processed properly"""
        self.assertEqual(1, len(self.timeDet.grids),
                         msg=', '.join(self.timeDet.grids.keys()))
        self.assertTrue("T" in self.timeDet.grids)
        expTallies = array([9.99978E-01, 2.24379E-05])
        expErrors = array([0.00002, 1.0])
        expTimeGrid = array([
            [0.00000E+00, 2.50000E-05, 1.25000E-05],
            [2.50000E-05, 5.00000E-05, 3.75000E-05],
        ])
        assert_equal(self.timeDet.tallies, expTallies)
        assert_equal(self.timeDet.errors, expErrors)
        assert_equal(self.timeDet.grids['T'], expTimeGrid)
