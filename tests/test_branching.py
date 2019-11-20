"""Test the branching reader."""

import os
import unittest

from numpy.testing import assert_allclose

from serpentTools.settings import rc
from serpentTools.data import getFile
from serpentTools.parsers import BranchingReader
from serpentTools.objects import UnivTuple
from serpentTools.messages import SerpentToolsException


class _BranchTesterHelper(unittest.TestCase):
    """Test case to share setUpClass for testing Branching Reader"""

    @classmethod
    def setUpClass(cls):
        cls.file = getFile('ref_branch.coe')
        cls.expectedBranches = {('nom', 'nom', 'nom')}
        cls.expectedUniverses = {
            # universe id, burnup, step
            UnivTuple("0", 0, 0, None),
        }
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['gc-meta', 'xs', 'diffusion']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            cls.reader = BranchingReader(cls.file)
        cls.reader.read()


class BranchTester(_BranchTesterHelper):
    """Class for testing the branching coefficient file reader."""

    def test_variables(self):
        """Verify that the correct settings and variables are obtained."""
        expected = {'GC_UNIVERSE_NAME', 'MICRO_NG', 'MICRO_E', 'MACRO_NG',
                    'MACRO_E', 'INF_MICRO_FLX', 'INF_KINF', 'INF_FLX',
                    'INF_FISS_FLX', 'TOT', 'CAPT', 'ABS', 'FISS', 'NSF',
                    'NUBAR', 'KAPPA', 'INVV', 'TRANSPXS', 'DIFFCOEF',
                    'RABSXS', 'REMXS', 'SCATT0', 'SCATT1', 'SCATT2', 'SCATT3',
                    'SCATT4', 'SCATT5', 'SCATT6', 'SCATT7', 'S0', 'S1', 'S2',
                    'S3', 'S4', 'S5', 'S6', 'S7', 'CHIT', 'CHIP', 'CHID',
                    'CMM_TRANSPXS', 'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y',
                    'CMM_TRANSPXS_Z', 'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X',
                    'CMM_DIFFCOEF_Y', 'CMM_DIFFCOEF_Z'}
        self.assertSetEqual(expected, self.reader.settings['variables'])
        self.assertFalse(self.reader.hasUncs)

    def test_raiseError(self):
        """Verify that the reader raises an error for unexpected EOF"""
        badFile = 'bad_branching.coe'
        with open(self.file) as fObj, open(badFile, 'w') as badObj:
            for _line in range(10):
                badObj.write(fObj.readline())
        badReader = BranchingReader(badFile)
        with self.assertRaises(EOFError):
            badReader.read()
        os.remove(badFile)

    def test_branchingUniverses(self):
        """Verify that the correct universes are present."""
        for branchID, branch in self.reader.iterBranches():
            self.assertSetEqual(
                self.expectedUniverses, set(branch),
                'Branch {}'.format(branchID))


class BranchContainerTester(_BranchTesterHelper):
    """Class to test the branch container"""

    @classmethod
    def setUpClass(cls):
        _BranchTesterHelper.setUpClass()
        cls.refBranchID = ('nom', 'nom', 'nom')
        cls.refUnivKey = ("0", 0, 0, None)
        cls.refBranch = cls.reader.branches[cls.refBranchID]
        cls.refUniv = cls.refBranch[cls.refUnivKey]

    def test_loadedUniv(self):
        """Verify the reference universe has the correct data loaded"""
        assortedExpected = {
            'infKinf': [1.36460], 'infChit': [1.0, 0.0],
            'infTot': [5.3147E-1, 1.39411],
            'infS3': [9.84645E-3, -1.92215E-3, 1.36850E-4, 2.63834E-2],
            'cmmDiffcoefY': [1.56742E+00, 4.13948E-01]
        }
        for name, valList in assortedExpected.items():
            assert_allclose(self.refUniv.get(name), valList,
                            err_msg='Error in value: {}'.format(name))

    def test_containerGetUniv(self):
        """Verify the getUniv method returns the reference universe"""
        key = self.refUnivKey
        self.assertIs(self.refUniv, self.refBranch.getUniv(*key),
                      msg='Failed to return the universe given reference key')
        self.assertIs(self.refUniv,
                      self.refBranch.getUniv(*key[:2]),
                      msg='Failed to return the universe given ID and burnup')
        self.assertIs(self.refUniv,
                      self.refBranch.getUniv(key[0], index=key[2]),
                      msg='Failed to return the universe given ID and index')
        with self.assertRaises(KeyError):
            self.refBranch.getUniv(key[0], burnup=-1)
        with self.assertRaises(SerpentToolsException):
            self.refBranch.getUniv(key[0])


class BranchWithUncsTester(unittest.TestCase):
    """Tester that just tests a small file with uncertainties"""

    BRANCH_DATA = {
        'nom': {
            'infTot': [
                [4.92499E-01, 1.01767E+00],  # value
                [0.00074, 0.00072],  # uncertainty
            ],
            'infS0': [
                [0.466391, 0.0155562, 0.00128821, 0.921487],
                [0.00072, 0.00148, 0.01793, 0.00091],
            ],
        },
        'hot': {
            'infTot': [
                [4.92806E-1, 1.0168E00],  # value
                [0.00063, 0.00104],  # uncertainty
            ],
            'infS0': [
                [4.66639E-1, 1.53978E-02, 1.38727E-03, 9.20270E-01],
                [0.00062, 0.00214, 0.03073, 0.00112],
            ],
        },
    }
    BRANCH_UNIVKEY = ("0", 0, 0, None)

    def setUp(self):
        fp = getFile('demo_uncs.coe')
        self.reader = BranchingReader(fp)
        self.reader.read()

    def test_valsWithUncs(self):
        """Test that the branches and the uncertainties are present"""
        self.assertTrue(self.reader.hasUncs)
        for expKey, expSubData in self.BRANCH_DATA.items():
            self.assertTrue(expKey in self.reader.branches, msg=expKey)
            actBranch = self.reader.branches[expKey]
            self.assertTrue(self.BRANCH_UNIVKEY in actBranch,
                            msg=self.BRANCH_UNIVKEY)
            univ = actBranch[self.BRANCH_UNIVKEY]
            for gcKey, gcVals in expSubData.items():
                actData = univ.get(gcKey, True)
                for act, exp, what in zip(actData, gcVals, ['val', 'unc']):
                    assert_allclose(act, exp, err_msg='{} {} {}'.format(
                        expKey, gcKey, what))
