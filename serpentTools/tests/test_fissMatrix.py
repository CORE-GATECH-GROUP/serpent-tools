""" Test the fission matrix reader"""

import os
import unittest

import numpy as np
from numpy.testing import assert_equal

from serpentTools.parsers.fissionMatrix import FissionMatrixReader as fm
from serpentTools.tests import TEST_ROOT


class FissionMatrixReaderTester(unittest.TestCase):
    """
    Class to test the fission matrix reader
    """

    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'ref_fmtx0.m')
        cls.reader = fm(cls.file)
        cls.reader.read()
        cls.reader.fMatEig()

    def test_fissMatRead(self):
        """ Tests the fission matrix reader capability by comparing the
        actual fission matrix to the expected one"""
        # Expected
        expFissMat = np.array(
            [[1.035650, 2.255560e-01, 1.318140e-03, 0, 0, 0, 0, 0, 0, 0],
             [1.211410e-01, 1.066340, 1.731440e-01, 1.011310e-03, 0, 0, 0, 0,
              0, 0],
             [7.903190e-04, 1.343050e-01, 1.066410, 1.602970e-01, 9.410140e-04,
              9.573390e-06, 0, 0, 0, 0],
             [8.596380e-06, 8.440010e-04, 1.407740e-01, 1.066410, 1.537120e-01,
              9.119450e-04, 1.131590e-05, 0, 0, 0],
             [0, 1.002020e-05, 8.699140e-04, 1.457250e-01, 1.066110,
              1.492560e-01, 8.797270e-04, 1.015890e-05, 0, 0],
             [0, 0, 9.412230e-06, 8.823790e-04, 1.496460e-01, 1.066160,
              1.451350e-01, 8.696570e-04, 9.819360e-06, 0],
             [0, 0, 0, 1.025920e-05, 9.092420e-04, 1.545690e-01, 1.065620,
              1.404340e-01, 8.272110e-04, 9.880880e-06],
             [0, 0, 0, 0, 9.982500e-06, 9.508460e-04, 1.608650e-01, 1.065580,
              1.341560e-01, 7.895490e-04],
             [0, 0, 0, 0, 0, 0, 1.018420e-03, 1.729290e-01, 1.066310,
              1.213040e-01],
             [0, 0, 0, 0, 0, 0, 0, 1.277340e-03, 2.251600e-01, 1.036870]])
        # Compare
        actualFissMat = self.reader.fMat
        assert_equal(actualFissMat, expFissMat)

    def test_fissMatUncRead(self):
        """ Tests the fission matrix reader capability by comparing the
        actual fission uncertainty matrix to the expected one"""
        # Expected
        expFissMatUnc = np.array(
            [[4.56147e-04, 1.21818e-03, 1.81398e-02, 0, 0, 0, 0, 0, 0, 0],
             [1.15886e-03, 2.80155e-04, 9.23410e-04, 1.20657e-02, 0, 0, 0, 0,
              0, 0],
             [1.11279e-02, 9.28056e-04, 2.14946e-4, 8.00396e-04, 8.98881e-03,
              9.42335e-02, 0, 0, 0, 0],
             [9.26119e-02, 9.43784e-03, 7.35529e-04, 1.91504e-04, 7.14059e-04,
              9.10074e-03, 8.27339e-02, 0, 0, 0],
             [0, 8.32101e-02, 9.08811e-03, 6.79719e-04, 1.80452e-04,
              6.45687e-04, 8.35152e-03, 7.87173e-02, 0, 0],
             [0, 0, 7.83537e-02, 8.83504e-03, 7.07904e-04, 1.91159e-04,
              6.97895e-04, 8.65997e-03, 8.89029e-02, 0],
             [0, 0, 0, 8.57217e-02, 9.31878e-03, 7.60185e-04, 1.86095e-04,
              7.51217e-04, 9.42279e-03, 8.49569e-02],
             [0, 0, 0, 0, 9.35977e-02, 8.62418e-03, 7.82455e-04, 2.15360e-04,
              8.38525e-04, 1.06983e-02],
             [0, 0, 0, 0, 0, 0, 1.21988e-02, 9.19816e-04, 2.67952e-04,
              1.15123e-03],
             [0, 0, 0, 0, 0, 0, 0, 1.60677e-02, 1.23419e-03, 4.40292e-04]])
        # Compare
        actualFissMatUnc = self.reader.fMatU
        assert_equal(actualFissMatUnc, expFissMatUnc)

    def test_FissMatEig(self):
        """ Tests eigenmode calculation and normalization
        is carried out correctly """
        # Expected eigenvalue and eigenmode
        expFissMat = np.array(
            [[1.035650, 2.255560e-01, 1.318140e-03, 0, 0, 0, 0, 0, 0, 0],
             [1.211410e-01, 1.066340, 1.731440e-01, 1.011310e-03, 0, 0, 0, 0,
              0, 0],
             [7.903190e-04, 1.343050e-01, 1.066410, 1.602970e-01, 9.410140e-04,
              9.573390e-06, 0, 0, 0, 0],
             [8.596380e-06, 8.440010e-04, 1.407740e-01, 1.066410, 1.537120e-01,
              9.119450e-04, 1.131590e-05, 0, 0, 0],
             [0, 1.002020e-05, 8.699140e-04, 1.457250e-01, 1.066110,
              1.492560e-01, 8.797270e-04, 1.015890e-05, 0, 0],
             [0, 0, 9.412230e-06, 8.823790e-04, 1.496460e-01, 1.066160,
              1.451350e-01, 8.696570e-04, 9.819360e-06, 0],
             [0, 0, 0, 1.025920e-05, 9.092420e-04, 1.545690e-01, 1.065620,
              1.404340e-01, 8.272110e-04, 9.880880e-06],
             [0, 0, 0, 0, 9.982500e-06, 9.508460e-04, 1.608650e-01, 1.065580,
              1.341560e-01, 7.895490e-04],
             [0, 0, 0, 0, 0, 0, 1.018420e-03, 1.729290e-01, 1.066310,
              1.213040e-01],
             [0, 0, 0, 0, 0, 0, 0, 1.277340e-03, 2.251600e-01, 1.036870]])
        expEigVal, expEigMode = np.linalg.eig(expFissMat)
        expEigMode = expEigMode / np.sum(expEigMode[:, 0])
        expDomEigVal = expEigVal[0]
        expDomEigVec = expEigMode[:, 0]
        # Compare
        assert_equal(self.reader.eigValVec, expEigVal)
        assert_equal(self.reader.eigVecMat, expEigMode)
        assert_equal(self.reader.domEigVal, expDomEigVal)
        assert_equal(self.reader.domEigVec, expDomEigVec)

    def test_ReadNegativeValue(self):
        """ Value error if negative values are read"""
        fmtxRead = fm('neg_fmtx0.m')
        with self.assertRaises(ValueError):
            _ = fmtxRead.read()

    def test_DimsConsistencyError(self):
        """ Value error if fission matrix is square"""
        fmtxRead = fm('refrect_fmtx0.m')
        with self.assertRaises(ValueError):
            _ = fmtxRead.read()

    def test_DimsZeroError(self):
        """ Value error if fission matrix has zero dimensions"""
        fmtxRead = fm('refzero_fmtx0.m')
        with self.assertRaises(ValueError):
            _ = fmtxRead.read()

    def test_EigenNumber(self):
        """ ValueError if it the Eigenmode number is not consistent"""
        with self.assertRaises(ValueError):
            _ = self.reader.eigVecPlot(78)
        with self.assertRaises(ValueError):
            _ = self.reader.eigVecPlot(-2)


if __name__ == '__main__':
    unittest.main()
