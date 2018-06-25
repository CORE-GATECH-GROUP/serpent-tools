"""Class to test the read commands from serpentTools.parsers"""
from os import path
import unittest

import six

from numpy import array
from numpy.testing import assert_array_equal

from serpentTools.messages import SerpentToolsException
from serpentTools.parsers import depmtx, inferReader, read
from serpentTools.data import getFile


class DepmtxTester(unittest.TestCase):
    """Class that tests the depletion matrix reader."""

    @classmethod
    def setUpClass(cls):
        cls.filePath = getFile('depmtx_ref.m')
        cls.numIso = 74
        (cls.time, cls.n0, cls.zai, cls.decMat, cls.n1) = depmtx(cls.filePath)

    def test_depmtxBadRead(self):
        """Verify the reader will not progress if the file is missing"""
        with self.assertRaises(IOError):
            depmtx('veryBadFile')

    def test_correctSizes(self):
        """Verify that all arrays are of the correct size"""
        N = self.numIso
        self.assertTupleEqual(self.n0.shape, (N, 1), 'initial isotpics')
        self.assertTupleEqual(self.decMat.shape, (N, N), 'decay matrix')
        self.assertTupleEqual(self.zai.shape, (N, ), 'zai vector')
        self.assertTupleEqual(self.n1.shape, (N, 1), 'final isotopics')

    def test_correctSlices(self):
        """Verify that the first and last few elements are correctly captured"""

        assert_array_equal(self.n0[:5], array(
            [[1.173442217504030343064509202267E-07],
             [6.107569078762340004851731368926E-12],
             [7.480538061277827561791279780104E-13],
             [7.524067572800136379093002835802E-16],
             [1.661130197369227900614564647189E-34]]
        ), err_msg='first five elements of n0')
        assert_array_equal(self.n0[-5:], array(
            [[1.456340924238686170077029955405E-09],
             [2.054873740352017655319549760407E-02],
             [2.108367055387284252194156353166E-07],
             [9.841801952371811001202615665146E-12],
             [8.052266563002563381135156316475E-16]]
        ), err_msg='last five elements of n0')
        assert_array_equal(self.zai[:10], array(
            ['-1', '10010', '10020', '10030', '20030', '20040', '30060',
             '30070', '40090', '50100']), 'first 10 elements of zai')
        decMat = self.decMat.A if hasattr(self.decMat, 'A') else self.decMat
        assert_array_equal(decMat[:3, :2], array(
            [[0, 0],
             [0, -1.500972704886488647503396416401E-12],
             [0, 1.500972704886488647503396416401E-12]]
        ), err_msg='dec[:3, :2]')
        assert_array_equal(decMat[-3:, -1], array(
            [2.166500765256806589294628619590E-14,
             8.673595631793918327440743302798E-12,
             -3.205752291225075667717126458572E-09]
        ), err_msg='dec[-3:, -1')
        assert_array_equal(self.n1[:5], array(
            [[1.173401055965248730759983657700E-07],
             [6.032533164919816465405638995097E-12],
             [7.311813300199797851742243369471E-13],
             [5.713459203264517940166721276285E-16],
             [1.514082744495717618511653374904E-34]]
        ), err_msg='first five elements of n1')
        assert_array_equal(self.n1[-5:], array(
            [[1.448384117008583481585383264604E-09],
             [2.054873733404119148793220972493E-02],
             [2.108922382983142802931309477132E-07],
             [9.823435767284427578223342980928E-12],
             [8.030354784613487489140522453118E-16]]
        ), err_msg='last five elements of n1')


class TestReaderInfer(unittest.TestCase):
    """Test the functionality of the read and inferReader functions"""

    def test_nonCallableReader(self):
        """
        Verify that an error is raised if the reader is non string nor callable
        """
        with self.assertRaises(AssertionError):
            read('dummyFP', None)

    def test_exceptionUnsupportedReader(self):
        """Verify an exception is raised for bad reader string"""
        with self.assertRaises(SerpentToolsException):
            read('dummyFP', 'this won\'t work')

    def test_inferReader(self):
        """Verify the correct readers are returned for given files"""
        from serpentTools.parsers import (
            BumatReader, BranchingReader, DepletionReader, DetectorReader,
            ResultsReader,
            FissionMatrixReader)
        expectedClasses = {
            'test.bumat99': BumatReader, 'test.coe': BranchingReader,
            'test_dep.m': DepletionReader, 'test_det99.m': DetectorReader,
            'test_res.m': ResultsReader, 'test_fmtx99.m': FissionMatrixReader,
            'test_res': None, 'test.coe_dep.m': DepletionReader
        }
        for fileP, expectedReader in six.iteritems(expectedClasses):
            if expectedReader is None:
                with self.assertRaises(SerpentToolsException):
                    inferReader(fileP)
            else:
                actual = inferReader(fileP)
                self.assertIs(expectedReader, actual,
                              'File path: {}\nExpected: {}\nActual: {}'
                              .format(fileP, str(expectedReader), str(actual))
                              )


if __name__ == '__main__':
    unittest.main()
