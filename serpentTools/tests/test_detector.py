"""Test the detector reader."""

import os
import unittest
from collections import OrderedDict

import numpy
from numpy.testing import assert_allclose, assert_equal

from serpentTools.parsers import DetectorReader
from serpentTools.tests import TEST_ROOT


class DetectorReaderTester(unittest.TestCase):
    """
    Class to test the detector reader.

    Detectors:

        1. xyFissionCapt: 5x5 xy mesh of the problem with two
           reactions: U-235 fission and capture
    """

    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'ref_det.m')
        cls.reader = DetectorReader(cls.file)
        cls.reader.read()
        expected = {'xyFissionCapt'}
        actual = set(cls.reader.detectors.keys())
        diff = expected.symmetric_difference(actual)
        assert not any(diff), (
            'Failed to load detector correctly. '
            'Incorrect detectors: {}'.format(diff)
        )
        cls.refDet = cls.reader.detectors['xyFissionCapt']
        expectedIndexKeys = {'xmesh', 'ymesh', 'reaction'}
        diffIndexK = expectedIndexKeys.symmetric_difference(
            cls.refDet.indexes.keys())
        assert not any(diffIndexK), (
            'Unexpected index keys for detector {}: {}'.format(cls.refDet.name,
                                                               diffIndexK)
        )
        expectedGrids = {'X', 'Y', 'Z'}
        diffGrids = expectedGrids.symmetric_difference(cls.refDet.grids.keys())
        assert not any(diffGrids), (
            'Unexpected grid keys for detector {}: {}'.format(cls.refDet.name,
                                                              diffGrids)
        )

    def test_detectorGrids(self):
        """Verify that the detector grids are property constructed"""
        expectedXY = numpy.array([
            [-1.95000E+00, - 1.17000E+00, - 1.56000E+00],
            [- 1.17000E+00, - 3.90000E-01, - 7.80000E-01],
            [- 3.90000E-01, 3.90000E-01, 2.22045E-16],
            [3.90000E-01, 1.17000E+00, 7.80000E-01],
            [1.17000E+00, 1.95000E+00, 1.56000E+00]
        ])
        expectedZ = numpy.array([[-1.00000E+37, 1.00000E+37, 0.00000E+00]])
        assert_allclose(self.refDet.grids['X'], expectedXY,
                        err_msg='x grid incorrect')
        assert_allclose(self.refDet.grids['Y'], expectedXY,
                        err_msg='y grid incorrect')
        assert_allclose(self.refDet.grids['Z'], expectedZ,
                        err_msg='z grid incorrect')

    def test_detectorIndex(self):
        """Verify that the detector tally index is properly constructed"""
        expected = OrderedDict()
        expected['reaction'] = numpy.array([1, 2])
        expected['ymesh'] = numpy.array([1, 2, 3, 4, 5])
        expected['xmesh'] = numpy.array([1, 2, 3, 4, 5])
        expectedKeys = list(expected.keys())
        actualIndex = self.refDet.indexes
        actualKeys = list(actualIndex.keys())
        self.assertListEqual(actualKeys, expectedKeys)
        for key in expected:
            assert_equal(actualIndex[key], expected[key])

    def test_detectorSlice(self):
        """Verify the slicing method"""
        constrain = {'reaction': 1}
        expectedTallies = numpy.array([
            [2.55119E-01, 2.55077E-01, 2.53685E-01, 2.55592E-01, 2.58450E-01],
            [2.54101E-01, 2.53408E-01, 2.56666E-01, 2.55375E-01, 2.52936E-01],
            [2.56006E-01, 2.51002E-01, 2.55479E-01, 2.52002E-01, 2.54708E-01],
            [2.54957E-01, 2.53399E-01, 2.48180E-01, 2.52915E-01, 2.53914E-01],
            [2.58394E-01, 2.50217E-01, 2.59642E-01, 2.54025E-01, 2.57076E-01]
        ])
        assert_equal(self.refDet.slice(constrain), expectedTallies,
                     err_msg='error in expected tally slice')
        expectedErrors = numpy.array([
            [0.01445, 0.01063, 0.01190, 0.01193, 0.01334],
            [0.01006, 0.00916, 0.01240, 0.00933, 0.01002],
            [0.01317, 0.01187, 0.01386, 0.01120, 0.01171],
            [0.01081, 0.00885, 0.01127, 0.00893, 0.01161],
            [0.01250, 0.01121, 0.01460, 0.01142, 0.01219]
        ])
        assert_equal(self.refDet.slice(constrain, data='errors'),
                     expectedErrors, err_msg='error in expected error slice')


if __name__ == '__main__':
    unittest.main()
