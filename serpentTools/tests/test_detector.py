"""Test the detector reader."""

import os
from unittest import TestCase

from collections import OrderedDict

from six import iteritems
from numpy import arange, array
from numpy.testing import assert_equal

from serpentTools.parsers import DetectorReader
from serpentTools.objects.detectors import CartesianDetector
from serpentTools.tests import TEST_ROOT, compareDictOfArrays


def read(fileP):
    reader = DetectorReader(fileP)
    reader.read()
    return reader


class DetectorHelper(TestCase):
    """
    Class that assists setting up readers
    """

    @classmethod
    def setUpClass(cls):
        cls.reader = read(cls.FILE_PATH)
        cls.detectors = cls.reader.detectors

    def test_loadedDetectors(self):
        """Verify that all anticipated detectors are loaded"""
        expectedNames = set(self.EXPECTED_DETECTORS.keys())
        actualNames = set(self.reader.detectors.keys())
        self.assertSetEqual(
            expectedNames, actualNames,
            msg="Failure reading detectors from {}".format(self.FILE_PATH))
        for name, cls in iteritems(self.EXPECTED_DETECTORS):
            actualDet = self.detectors[name]
            self.assertIsInstance(
                    actualDet, cls, msg="{} is {}, should be {}: - {}"
                    .format(name, actualDet.__class__.__name__, cls,
                            self.FILE_PATH))

    def test_detectorGrids(self):
        """Verify that all grids are loaded"""
        baseMsg = "Key: {key}"
        for detName, gridDict in iteritems(self.EXPECTED_GRIDS):
            msg = baseMsg + "  Reading: " + self.__class__.__name__
            actualGrids = self.detectors[detName].grids
            compareDictOfArrays(
                gridDict, actualGrids, testCase=self, fmtMsg=msg)

    def test_detectorIndex(self):
        """Verify that the detector tally index is properly constructed"""
        for detName, expectedIndex in iteritems(self.EXPECTED_INDEXES):
            actualIndex = self.detectors[detName].indexes
            expectedKeys = list(expectedIndex.keys())
            actualKeys = list(actualIndex.keys())
            self.assertListEqual(actualKeys, expectedKeys)
            for key in expectedIndex:
                assert_equal(
                    actualIndex[key], expectedIndex[key],
                    err_msg="Key: {}, Detector: {}".format(key, detName))


class CartesianDetectorReaderTester(DetectorHelper):
    """
    Class to test the detector reader.

    Detectors:

        1. xyFissionCapt: 5x5 xy mesh of the problem with two
           reactions: U-235 fission and capture
    """

    __name__ = "Cartesian"

    FILE_PATH = os.path.join(TEST_ROOT, 'ref_det0.m')
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
    _INDEXES = OrderedDict([
        ['reaction', arange(2)],
        ['ymesh', arange(5)],
        ['xmesh', arange(5)],
        ])
    EXPECTED_INDEXES = {DET_NAME: _INDEXES}

    def test_detectorSlice(self):
        """Verify the slicing method"""
        refDet = self.detectors[self.DET_NAME]
        constrain = {'reaction': 0}
        expectedTallies = array([
            [2.55119E-01, 2.55077E-01, 2.53685E-01, 2.55592E-01, 2.58450E-01],
            [2.54101E-01, 2.53408E-01, 2.56666E-01, 2.55375E-01, 2.52936E-01],
            [2.56006E-01, 2.51002E-01, 2.55479E-01, 2.52002E-01, 2.54708E-01],
            [2.54957E-01, 2.53399E-01, 2.48180E-01, 2.52915E-01, 2.53914E-01],
            [2.58394E-01, 2.50217E-01, 2.59642E-01, 2.54025E-01, 2.57076E-01]
        ])
        assert_equal(refDet.slice(constrain), expectedTallies,
                     err_msg='error in expected tally slice')
        expectedErrors = array([
            [0.01445, 0.01063, 0.01190, 0.01193, 0.01334],
            [0.01006, 0.00916, 0.01240, 0.00933, 0.01002],
            [0.01317, 0.01187, 0.01386, 0.01120, 0.01171],
            [0.01081, 0.00885, 0.01127, 0.00893, 0.01161],
            [0.01250, 0.01121, 0.01460, 0.01142, 0.01219]
        ])
        assert_equal(refDet.slice(constrain, data='errors'),
                     expectedErrors, err_msg='error in expected error slice')


del DetectorHelper


if __name__ == '__main__':
    from unittest import main
    main()
