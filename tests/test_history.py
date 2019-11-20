"""
File for testing the history reader
"""

import unittest

from numpy import array
from numpy.testing import assert_array_equal

from serpentTools.parsers.history import HistoryReader
from serpentTools.data import getFile

TEST_FILE = getFile('bwr_his0.m')
NUM_INACTIVE = 20
NUM_CYCLES = 119

EXPECTED_ARRAYS_SHAPE = {
    'time': (NUM_CYCLES, 1),
    'entrSwg': (NUM_CYCLES, 12),
    'transportCpuUsage': (NUM_CYCLES, 3),
    'impKeff': (NUM_CYCLES, 3),
    'entrSpt': (NUM_CYCLES, 12),
    'iterVal': (NUM_CYCLES, 3),
    'anaKeff': (NUM_CYCLES, 9),
    'transportRuntime': (NUM_CYCLES, 6),
    'meanPopWgt': (NUM_CYCLES, 3),
    'meanPopSize': (NUM_CYCLES, 3),
    'colKeff': (NUM_CYCLES, 3)
}

_EXPECTED_ARRAY_HEADS = {
    'transportRuntime':
        [[3.48000E-01, 3.48000E-01, 0.00000, 1.39410E+00, 1.39410E+00,
         0.00000],
         [3.66000E-01, 3.57000E-01, 0.02521, 1.46339E+00, 1.42875E+00,
          0.02425],
         [3.28000E-01, 3.47333E-01, 0.03160, 1.31302E+00, 1.39017E+00,
          0.03126],
         [3.37000E-01, 3.44750E-01, 0.02372, 1.34830E+00, 1.37971E+00,
          0.02353],
         [3.41000E-01, 3.44000E-01, 0.01855, 1.36298E+00, 1.37636E+00,
          0.01843]],
    'transportCpuUsage':
        [[4.00962E+00, 4.00962E+00, 0.00000],
         [3.99595E+00, 4.00278E+00, 0.00171],
         [3.99948E+00, 4.00168E+00, 0.00102],
         [3.99652E+00, 4.00039E+00, 0.00079],
         [4.00562E+00, 4.00144E+00, 0.00067]],
    'meanPopWgt':
        [[1.00000E+04, 1.00000E+04, 0.00000],
         [1.07090E+04, 1.03545E+04, 0.03424],
         [9.74700E+03, 1.01520E+04, 0.02836],
         [1.00670E+04, 1.01308E+04, 0.02021],
         [1.01490E+04, 1.01344E+04, 0.01565]],
    'meanPopSize':
        [[1.00000E+04, 1.00000E+04, 0.00000],
         [1.07090E+04, 1.03545E+04, 0.03424],
         [9.74700E+03, 1.01520E+04, 0.02836],
         [1.00670E+04, 1.01308E+04, 0.02021],
         [1.01490E+04, 1.01344E+04, 0.01565]],
    'impKeff':
        [[1.05261E+00, 1.05261E+00, 0.00000],
         [1.05097E+00, 1.05179E+00, 0.00078],
         [1.05135E+00, 1.05164E+00, 0.00047],
         [1.04230E+00, 1.04931E+00, 0.00225],
         [1.05954E+00, 1.05135E+00, 0.00261]],
    'iterVal':
        [[0., 0., 0., ]] * 5,
    'anaKeff':
        [[1.00000E+00, 1.00000E+00, 0.00000, 1.06665E+00, 1.06665E+00,
          0.00000, 0.00000E+00, 0.00000E+00, 0.00000],
         [1.07090E+00, 1.03545E+00, 0.03424, 1.03357E+00, 1.05011E+00,
          0.01575, 7.73574E-03, 3.86787E-03, 1.00000],
         [1.04381E+00, 1.03824E+00, 0.01990, 1.03915E+00, 1.04646E+00,
          0.00977, 7.74916E-03, 5.16163E-03, 0.50000],
         [1.05080E+00, 1.04138E+00, 0.01435, 1.05253E+00, 1.04798E+00,
          0.00705, 8.71343E-03, 6.04958E-03, 0.33547],
         [1.06646E+00, 1.04639E+00, 0.01205, 1.04790E+00, 1.04796E+00,
          0.00546, 5.28116E-03, 5.89590E-03, 0.26790]],
    'colKeff':
        [[1.05246E+00, 1.05246E+00, 0.00000],
         [1.05532E+00, 1.05389E+00, 0.00136],
         [1.05706E+00, 1.05495E+00, 0.00127],
         [1.05377E+00, 1.05465E+00, 0.00094],
         [1.06782E+00, 1.05729E+00, 0.00259]],
    'entrSwg':
        [[6.47677E-01, 6.47677E-01, 0.00000, 9.79166E-01, 9.79166E-01,
          0.00000, 9.78336E-01, 9.78336E-01, 0.00000, 6.89820E-17,
          6.89820E-17, 0.00000],
         [6.57808E-01, 6.52743E-01, 0.00776, 9.95959E-01, 9.87562E-01,
          0.00850, 9.97957E-01, 9.88146E-01, 0.00993, 6.10491E-14,
          3.05590E-14, 0.99774],
         [6.59162E-01, 6.54883E-01, 0.00553, 9.97680E-01, 9.90935E-01,
          0.00596, 9.97288E-01, 9.91193E-01, 0.00649, 0.00000E+00,
          2.03727E-14, 0.99831],
         [6.59557E-01, 6.56051E-01, 0.00429, 9.98106E-01, 9.92728E-01,
          0.00458, 9.98673E-01, 9.93063E-01, 0.00495, 0.00000E+00,
          1.52795E-14, 0.99850],
         [6.58416E-01, 6.56524E-01, 0.00340, 9.98760E-01, 9.93934E-01,
          0.00374, 9.96685E-01, 9.93787E-01, 0.00390, 8.29854E-14,
          2.88207E-14, 0.62361]],
    'entrSpt':
        [[6.47677E-01, 6.47677E-01, 0.00000, 9.79166E-01, 9.79166E-01,
          0.00000, 9.78336E-01, 9.78336E-01, 0.00000, 6.89820E-17,
          6.89820E-17, 0.00000],
         [6.57808E-01, 6.52743E-01, 0.00776, 9.95959E-01, 9.87562E-01,
          0.00850, 9.97957E-01, 9.88146E-01, 0.00993, 0.00000E+00,
          3.44910E-17, 1.00000],
         [6.59162E-01, 6.54883E-01, 0.00553, 9.97680E-01, 9.90935E-01,
          0.00596, 9.97288E-01, 9.91193E-01, 0.00649, 0.00000E+00,
          2.29940E-17, 1.00000],
         [6.59557E-01, 6.56051E-01, 0.00429, 9.98106E-01, 9.92728E-01,
          0.00458, 9.98673E-01, 9.93063E-01, 0.00495, 0.00000E+00,
          1.72455E-17, 1.00000],
         [6.58416E-01, 6.56524E-01, 0.00340, 9.98760E-01, 9.93934E-01,
          0.00374, 9.96685E-01, 9.93787E-01, 0.00390, 0.00000E+00,
          1.37964E-17, 1.00000]],
    'time':
        [[2.46000E+00],
         [2.82900E+00],
         [3.16000E+00],
         [3.50000E+00],
         [3.84300E+00]],
}
_EXPECTED_ARRAY_TAILS = {
    'meanPopWgt':
        [[9.86700E+03, 1.00013E+04, 0.00156],
         [9.94500E+03, 1.00007E+04, 0.00154],
         [9.97000E+03, 1.00004E+04, 0.00153],
         [1.01230E+04, 1.00016E+04, 0.00152],
         [1.01330E+04, 1.00030E+04, 0.00151]],
    'time':
        [[4.61110E+01],
         [4.64550E+01],
         [4.67840E+01],
         [4.71380E+01],
         [4.74700E+01]],
    'impKeff':
        [[1.04949E+00, 1.05277E+00, 0.00075],
         [1.04799E+00, 1.05272E+00, 0.00074],
         [1.05134E+00, 1.05271E+00, 0.00073],
         [1.05870E+00, 1.05277E+00, 0.00073],
         [1.03628E+00, 1.05260E+00, 0.00074]],
    'anaKeff':
        [[1.04605E+00, 1.05209E+00, 0.00114, 1.03361E+00, 1.04488E+00,
          0.00110, 6.43472E-03, 7.03436E-03, 0.02013],
         [1.04029E+00, 1.05197E+00, 0.00113, 1.03475E+00, 1.04477E+00,
          0.00109, 6.61469E-03, 7.02999E-03, 0.01994],
         [1.03717E+00, 1.05182E+00, 0.00113, 1.04006E+00, 1.04472E+00,
          0.00108, 6.59834E-03, 7.02554E-03, 0.01976],
         [1.04993E+00, 1.05180E+00, 0.00112, 1.05328E+00, 1.04481E+00,
          0.00107, 8.90417E-03, 7.04471E-03, 0.01969],
         [1.06389E+00, 1.05192E+00, 0.00111, 1.02674E+00, 1.04463E+00,
          0.00108, 4.80910E-03, 7.02213E-03, 0.01982]],
    'colKeff':
        [[1.06764E+00, 1.05372E+00, 0.00108],
         [1.04992E+00, 1.05369E+00, 0.00107],
         [1.05298E+00, 1.05368E+00, 0.00106],
         [1.03877E+00, 1.05353E+00, 0.00106],
         [1.03357E+00, 1.05332E+00, 0.00107]],
    'iterVal':
        [[0] * 3] * 5,
    'meanPopSize':
        [[9.86700E+03, 1.00013E+04, 0.00156],
         [9.94500E+03, 1.00007E+04, 0.00154],
         [9.97000E+03, 1.00004E+04, 0.00153],
         [1.01230E+04, 1.00016E+04, 0.00152],
         [1.01330E+04, 1.00030E+04, 0.00151]],
    'transportRuntime':
        [[3.90000E-01, 3.88947E-01, 0.00185, 1.55888E+00, 1.55614E+00,
          0.00187],
         [3.41000E-01, 3.88448E-01, 0.00224, 1.35878E+00, 1.55409E+00,
          0.00228],
         [3.27000E-01, 3.87814E-01, 0.00276, 1.30847E+00, 1.55156E+00,
          0.00278],
         [3.51000E-01, 3.87439E-01, 0.00290, 1.40381E+00, 1.55005E+00,
          0.00293],
         [3.29000E-01, 3.86848E-01, 0.00325, 1.31852E+00, 1.54771E+00,
          0.00327]],
    'transportCpuUsage':
        [[4.00058E+00, 3.99992E+00, 0.00010],
         [3.98895E+00, 3.99980E+00, 0.00010],
         [4.00825E+00, 3.99989E+00, 0.00010],
         [3.99468E+00, 3.99983E+00, 0.00010],
         [4.00330E+00, 3.99987E+00, 0.00010]],
    'entrSpt':
        [[6.58590E-01, 6.58821E-01, 0.00012, 9.97428E-01, 9.97832E-01,
          0.00008, 9.98427E-01, 9.97970E-01, 0.00008, 0.00000E+00,
          2.83189E-17, 0.16096],
         [6.58858E-01, 6.58821E-01, 0.00011, 9.98707E-01, 9.97841E-01,
          0.00008, 9.96596E-01, 9.97956E-01, 0.00008, 6.89820E-17,
          2.87425E-17, 0.15761],
         [6.58848E-01, 6.58821E-01, 0.00011, 9.97079E-01, 9.97833E-01,
          0.00008, 9.97895E-01, 9.97955E-01, 0.00008, 6.89820E-17,
          2.91574E-17, 0.15442],
         [6.58291E-01, 6.58816E-01, 0.00011, 9.99022E-01, 9.97845E-01,
          0.00008, 9.97083E-01, 9.97946E-01, 0.00008, 0.00000E+00,
          2.88598E-17, 0.15475],
         [6.57703E-01, 6.58805E-01, 0.00011, 9.98895E-01, 9.97856E-01,
          0.00008, 9.96939E-01, 9.97936E-01, 0.00008, 0.00000E+00,
          2.85683E-17, 0.15508]],
    'entrSwg':
        [[6.58590E-01, 6.58821E-01, 0.00012, 9.97428E-01, 9.97832E-01,
          0.00008, 9.98427E-01, 9.97970E-01, 0.00008, 4.10443E-14,
          2.86384E-14, 0.14590],
         [6.58858E-01, 6.58821E-01, 0.00011, 9.98707E-01, 9.97841E-01,
          0.00008, 9.96596E-01, 9.97956E-01, 0.00008, 0.00000E+00,
          2.83401E-14, 0.14627],
         [6.58848E-01, 6.58821E-01, 0.00011, 9.97079E-01, 9.97833E-01,
          0.00008, 9.97895E-01, 9.97955E-01, 0.00008, 0.00000E+00,
          2.80480E-14, 0.14663],
         [6.58291E-01, 6.58816E-01, 0.00011, 9.99022E-01, 9.97845E-01,
          0.00008, 9.97083E-01, 9.97946E-01, 0.00008, 0.00000E+00,
          2.77617E-14, 0.14698],
         [6.57703E-01, 6.58805E-01, 0.00011, 9.98895E-01, 9.97856E-01,
          0.00008, 9.96939E-01, 9.97936E-01, 0.00008, 0.00000E+00,
          2.74813E-14, 0.14733]],
}

EXPECTED_ARRAY_HEADS = {key: array(value)
                        for key, value in _EXPECTED_ARRAY_HEADS.items()}

EXPECTED_ARRAY_TAILS = {key: array(value)
                        for key, value in _EXPECTED_ARRAY_TAILS.items()}

del _EXPECTED_ARRAY_HEADS, _EXPECTED_ARRAY_TAILS

#
# Validate all keys present in expected heads and tails
#
for key in EXPECTED_ARRAYS_SHAPE:
    for arrayD, arrayT in zip((EXPECTED_ARRAY_HEADS, EXPECTED_ARRAY_TAILS),
                              ('heads', 'tails')):
        assert key in arrayD, (
            'Missing {} from history {}'.format(key, arrayT))


class HistoryHelper(unittest.TestCase):
    """Helper class for setting up tests"""

    @classmethod
    def setUpClass(cls):
        cls.reader = HistoryReader(TEST_FILE)
        cls.reader.read()
        cls.arrays = cls.reader.arrays


class HistoryTester(HistoryHelper):
    """Class that is responsible for testing the history reader."""

    def test_keysArePresent(self):
        """Verify that all the correct keys are present."""
        self.assertSetEqual(set(EXPECTED_ARRAYS_SHAPE.keys()),
                            set(self.arrays.keys()),
                            msg='Mismatch in array contents')

    def test_numInactive(self):
        """Verify the correct number of inactive cycles are stored."""
        self.assertEqual(self.reader.numInactive, NUM_INACTIVE)

    def test_sizes(self):
        """Verify the arrays are of the correct size."""
        for key, shape in EXPECTED_ARRAYS_SHAPE.items():
            self.assertTupleEqual(shape, self.arrays[key].shape,
                                  msg=key)

    def test_getItem(self):
        """Verify the getitem indexing is functional."""
        for key, readerArray in self.arrays.items():
            self.assertIs(readerArray, self.reader[key], msg=key)

    def test_arrayHeads(self):
        """Verify the first few lines of each array are correct."""
        for key, expectedArray in EXPECTED_ARRAY_HEADS.items():
            numRows = expectedArray.shape[0]
            actual = self.arrays[key][:numRows]
            assert_array_equal(expectedArray, actual, err_msg=key)

    def test_arrayTails(self):
        """Verify the last few lines of each array are correct."""
        for key, expectedArray in EXPECTED_ARRAY_TAILS.items():
            numRows = expectedArray.shape[0]
            actual = self.arrays[key][-numRows:]
            assert_array_equal(expectedArray, actual, err_msg=key)

    def test_specialMethods(self):
        """Test special methods on the reader"""
        # test len
        self.assertEqual(len(self.reader), len(self.reader.arrays))
        # test contains
        badKey = 'this_shouldNotBe_present'
        self.assertFalse(badKey in self.reader)
        # test iter
        for nFound, key in enumerate(self.reader, start=1):
            self.assertTrue(key in self.reader.arrays, msg=key)
            self.assertTrue(key in self.reader, msg=key)
        self.assertEqual(nFound, len(self.reader.arrays))

    def test_iterItems(self):
        """Test the items method for yielding key, value pairs"""
        for nFound, (key, value) in enumerate(self.reader.items(), start=1):
            self.assertTrue(key in self.reader.arrays, msg=key)
            self.assertTrue(key in self.reader, msg=key)
            assert_array_equal(value, self.reader.arrays[key], err_msg=key)
            self.assertTrue(value is self.reader[key], msg=key)

        self.assertEqual(nFound, len(self.reader.arrays))


class HistoryMatlabBase(HistoryHelper):
    """Base class for performing tests on the history -> matlab conversion"""

    def gather(self):
        return self.reader._gather_matlab(self.RECONVERT)

    def test_gather(self):
        """Test the ability to place data into a dictionary for exporting"""
        gathered = self.gather()
        if self.RECONVERT:
            varFunc = self.reader.ioReconvertName
        else:
            varFunc = self.reader.ioConvertName
        for origKey, actValue in self.arrays.items():
            expKey = varFunc(origKey)
            msg = "{} -> {}".format(origKey, expKey)
            self.assertTrue(expKey in gathered, msg=msg)
            assert_array_equal(gathered[expKey], actValue, err_msg=msg)

    def test_conversion(self):
        """Test the method used in name conversion for accuracy and consistency.
        """
        if self.RECONVERT:
            convFun = self.reader.ioReconvertName
        else:
            convFun = self.reader.ioConvertName
        for origKey, expKey in self.CONV_KEYS.items():
            msg = '{} -> {}'.format(origKey, expKey)
            self.assertEqual(expKey, convFun(origKey), msg=msg)


class HistMatlabConvertTester(HistoryMatlabBase):
    """Test the ability to retain camelCase names through matlab exporting"""

    RECONVERT = False

    CONV_KEYS = {
        'time': 'hisTime',
        'impKeff': 'hisImpKeff',
        'meanPopSize': 'hisMeanPopSize',
    }


class HistMatlabReconvertTester(HistoryMatlabBase):
    """Test the ability to reconvert names through matlab exporting"""

    RECONVERT = True
    CONV_KEYS = {
        'time': 'HIS_TIME',
        'impKeff': 'HIS_IMP_KEFF',
        'meanPopSize': 'HIS_MEAN_POP_SIZE',
    }


del HistoryMatlabBase
