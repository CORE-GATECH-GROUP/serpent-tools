"""
Tests for testing the MATLAB conversion functions
"""

from os import remove
from unittest import TestCase, SkipTest
from numpy import arange
from numpy.testing import assert_array_equal
from serpentTools.objects import Detector
from serpentTools.utils import checkScipy
from serpentTools.io import toMatlab

HAS_SCIPY = checkScipy('1.0')


class Det2MatlabHelper(TestCase):
    """Helper class for testing detector to matlab conversion"""

    NBINS = 10
    NCOLS = 12
    # approximate some detector data
    BINS = arange(
        NCOLS * NBINS, dtype=float).reshape(NBINS, NCOLS)
    # emulate energy grid
    GRID = arange(3 * NBINS).reshape(NBINS, 3)
    GRID_KEY = 'E'

    @classmethod
    def setUpClass(cls):
        cls.detector = Detector('matlabtest')
        cls.detector.bins = cls.BINS
        cls.detector.grids[cls.GRID_KEY] = cls.GRID

    def setUp(self):
        # skip tests if scipy not installed
        if not HAS_SCIPY:
            raise SkipTest("scipy needed to test matlab conversion")

        from serpentTools.objects.detectors import deconvert, prepToMatlab
        # instance methods and/or rename them
        # potential issues sending putting many such functions in this
        # test suite

        self.converterFunc = deconvert if self.CONVERT else prepToMatlab

    def test_det2Matlab(self):
        """Test the conversion to matlab files"""
        from scipy.io import loadmat
        filePath = 'detector_{}.mat'.format(
            'conv' if self.CONVERT else 'unconv')
        toMatlab(self.detector, filePath, self.CONVERT, append=False)
        fromMatlab = loadmat(filePath)

        binsKey = self.converterFunc(self.detector.name, 'bins')
        self.assertTrue(binsKey in fromMatlab)
        assert_array_equal(fromMatlab[binsKey], self.detector.bins)

        gridKey = self.converterFunc(self.detector.name, self.GRID_KEY)
        self.assertTrue(gridKey in fromMatlab)
        assert_array_equal(fromMatlab[gridKey],
                           self.detector.grids[self.GRID_KEY])

        remove(filePath)


class ConvertedDet2MatlabTester(Det2MatlabHelper):
    """Test the process of writing detector data w/ original names"""

    CONVERT = True


class UnconvertedDet2MatlabTester(Det2MatlabHelper):
    """Test the process of writing detector data w/ custom names"""

    CONVERT = False


del Det2MatlabHelper

if __name__ == '__main__':
    from unittest import main
    main()
