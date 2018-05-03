"""Test the container object. """

import unittest
from serpentTools.objects import containers
from serpentTools.parsers import DepletionReader


class HomogenizedUniverseTester(unittest.TestCase):
    """ Class to test the Homogenized Universe """

    @classmethod
    def setUpClass(cls):
        cls.univ = containers.HomogUniv('dummy', 0, 0, 0)
        cls.Exp = {}
        cls.Unc = {}
        # Data definition
        cls.Exp = {'B1_1': 1, 'B1_2': [1, 2], 'B1_3': [1, 2, 3],
                   'INF_1': 3, 'INF_2': [4, 5], 'INF_3': [6, 7, 8],
                   'MACRO_E': (.1, .2, .3, .1, .2, .3), 'Test_1': 'ciao'}
        cls.Unc = {'B1_1': 1e-1, 'B1_2': [1e-1, 2e-1], 'B1_3': [1e-1, 2e-1,
                                                                3e-1],
                   'INF_1': 3e-1, 'INF_2': [4e-1, 5e-1], 'INF_3': [6e-1, 7e-1,
                                                                   8e-1],
                   'MACRO_E': (.1e-1, .2e-1, .3e-1, .1e-1, .2e-1, .3e-1),
                   'Test_1': 'addio'}

        # Partial dictionaries
        cls.b1Exp = {'b11': 1, 'b12': [1, 2], 'b13': [1, 2, 3]}
        cls.b1Unc = {'b11': (1, 0.1), 'b12': ([1, 2], [.1, .2]), 'b13':
            ([1, 2, 3], [.1, .2, .3])}
        cls.infExp = {'inf1': 3, 'inf2': [4, 5], 'inf3': [6, 7, 8]}
        cls.infUnc = {'inf1': (3, .3), 'inf2': ([4, 5], [.4, .5]), 'inf3':
            ([6, 7, 8], [.6, .7, .8])}
        cls.meta = {'macroE': (.1e-1, .2e-1, .3e-1, .1e-1, .2e-1, .3e-1),
                    'test1': 'addio'}
        # Use addData
        for kk in cls.Exp:
            cls.univ.addData(kk, cls.Exp[kk], False)
        for kk in cls.Unc:
            cls.univ.addData(kk, cls.Unc[kk], True)

    def test_getB1Exp(self):
        """ Get Expected vales from B1 dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.b1Exp:
            d[kk] = self.univ.get(kk, False)
        self.assertDictEqual(self.b1Exp, d)

    def test_getB1Unc(self):
        """ Get Expected vales and associated uncertainties from B1 dictionary
        """
        d = {}
        # Comparison
        for kk in self.univ.b1Exp:
            d[kk] = self.univ.get(kk, True)
        self.assertDictEqual(self.b1Unc, d)

    def test_getInfExp(self):
        """ Get Expected vales from Inf dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.infExp:
            d[kk] = self.univ.get(kk, False)
        self.assertDictEqual(self.infExp, d)

    def test_getInfUnc(self):
        """ Get Expected vales and associated uncertainties from Inf dictionary
        """
        d = {}
        # Comparison
        for kk in self.univ.infUnc:
            d[kk] = self.univ.get(kk, True)
        self.assertDictEqual(self.infUnc, d)

    def test_getMeta(self):
        """ Get metaData from corresponding dictionary"""
        d = {}
        # Comparison
        for kk in self.univ.metadata:
            d[kk] = self.univ.get(kk, False)
        self.assertDictEqual(self.meta, d)


if __name__ == '__main__':
    unittest.main()
