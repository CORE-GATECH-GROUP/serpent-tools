"""Test the container object. """

import unittest

from six import iteritems
from numpy import array, arange
from numpy.testing import assert_allclose

from serpentTools.objects import containers
from serpentTools.parsers import DepletionReader


class HomogenizedUniverseTester(unittest.TestCase):
    """ Class to test the Homogenized Universe """

    @classmethod
    def setUpClass(cls):
        cls.univ = containers.HomogUniv('dummy', 0, 0, 0)
        vec = arange(5)
        mat = arange(25)
        # Data definition
        rawData = {'B1_1': vec, 'INF_1': vec, 'INF_S0': mat,
                  'MACRO_E': vec}

        # Partial dictionaries
        cls.b1Unc = cls.b1Exp = {'b11': vec}
        cls.infUnc = cls.infExp = {'inf1': vec, 'infS0': mat}
        cls.meta = {'macroE': vec}

        # Use addData
        for key, value in iteritems(rawData):
            cls.univ.addData(key, value, uncertainty=False)
            cls.univ.addData(key, value, uncertainty=True)

    def test_getB1Exp(self):
        """ Get Expected vales from B1 dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.b1Exp:
            d[kk] = self.univ.get(kk, False)
        compareDictOfArrays(self.b1Exp, d, 'b1 values')
        
    def test_getB1Unc(self):
        """ Get Expected vales and associated uncertainties from B1 dictionary
        """
        d = {}
        # Comparison
        for kk in self.univ.b1Exp:
            d[kk] = self.univ.get(kk, True)[1]
        compareDictOfArrays(self.b1Unc, d, 'b1 uncertainties')

    def test_getInfExp(self):
        """ Get Expected vales from Inf dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.infExp:
            d[kk] = self.univ.get(kk, False)
        compareDictOfArrays(self.infExp, d, 'infinite values')

    def test_getInfUnc(self):
        """ Get Expected vales and associated uncertainties from Inf dictionary
        """
        d = {}
        # Comparison
        for kk in self.univ.infUnc:
            d[kk] = self.univ.get(kk, True)[1]
        compareDictOfArrays(self.infUnc, d, 'infinite uncertainties')

    def test_getMeta(self):
        """ Get metaData from corresponding dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.metadata:
            d[kk] = self.univ.get(kk, False)
        compareDictOfArrays(self.meta, d, 'metadata')

    def test_getBothInf(self):
        """
        Verify that the value and the uncertainty are returned if the
        flag is passed.
        """
        expected, uncertainties = {}, {}
        for key in self.infExp.keys():
            value, unc = self.univ.get(key, True)
            expected[key] = value
            uncertainties[key] = unc
        compareDictOfArrays(self.infExp, expected, 'infinite values')
        compareDictOfArrays(self.infUnc, uncertainties, 
                            'infinite uncertainties')
                            


def compareDictOfArrays(expected, actualDict, dataType):
    for key, value in iteritems(expected):
        actual = actualDict[key]
        assert_allclose(value, actual, 
                err_msg="Error in {} dictionary: key={}"
                .format(dataType, key))


if __name__ == '__main__':
    unittest.main()
