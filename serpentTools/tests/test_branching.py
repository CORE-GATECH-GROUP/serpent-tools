"""Test the branching reader."""

import os
import unittest

from six import iteritems

from numpy.testing import assert_allclose

from serpentTools.settings import rc
from serpentTools.tests import TEST_ROOT
from serpentTools.parsers import BranchingReader


class BranchTester(unittest.TestCase):
    """Class for testing the branching coefficient file reader."""

    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'ref_branch.txt')
        cls.expectedBranches = {('nom', 'nom', 'nom')}
        cls.expectedUniverses = {
            # universe id, burnup, step, day
            (0, 0, 1, 0),
        }
        cls.refBranchID = ('nom', 'nom', 'nom')
        cls.refUnivKey = (0, 0, 1, 0)
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['gc-meta', 'xs', 'diffusion']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            cls.reader = BranchingReader(cls.file)
        cls.reader.read()

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

    def test_raiseError(self):
        """Verify that the reader raises an error for unexpected EOF"""
        badFile = os.path.join(TEST_ROOT, 'bad_branching.txt')
        with open(self.file) as fObj, open(badFile, 'w') as badObj:
            for _line in range(5):
                badObj.write(fObj.readline())
        badReader = BranchingReader(badFile)
        with self.assertRaises(EOFError):
            badReader.read()
        os.remove(badFile)

    def test_branchingUniverses(self):
        """Verify that the correct universes are present."""
        for branchID, branch in self.reader.iterBranches():
            self.assertSetEqual(
                self.expectedUniverses, set(branch.universes),
                'Branch {}'.format(branchID))

    def test_loadedUniv(self):
        actualUniv = (
            self.reader.branches[self.refBranchID].universes[self.refUnivKey])
        assortedExpected = {
            'infKinf': [1.36460], 'infChit': [1.0, 0.0],
            'infTot': [5.3147E-1, 1.39411],
            'infS3': [9.84645E-3, -1.92215E-3, 1.36850E-4, 2.63834E-2],
            'cmmDiffcoefY': [1.56742E+00, 4.13948E-01]
        }
        for name, valList in iteritems(assortedExpected):
            assert_allclose(actualUniv.get(name), valList,
                            err_msg='Error in value: {}'.format(name))


if __name__ == '__main__':
    unittest.main()
