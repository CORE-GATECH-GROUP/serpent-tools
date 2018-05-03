"""Test the branching reader."""

import os
import unittest

from six import iteritems

from numpy.testing import assert_allclose

from serpentTools.settings import rc
from serpentTools.tests import TEST_ROOT
from serpentTools.parsers import ResultsReader
from serpentTools.messages import SerpentToolsException


class _ResultsTesterHelper(unittest.TestCase):
    """Test case to share setUpClass for testing Results Reader"""

    @classmethod
    def setUpClass(cls):
        cls.file = os.path.join(TEST_ROOT, 'pwr_res.m')
        cls.expectedUniverses = {
            # universe id, burnup, step, days
            ('0', 0, 0, 1),('0', 500, 1, 5)
        }
        with rc:
            rc['serpentVersion'] = '2.1.29'
            rc['xs.variableGroups'] = ['gc-meta', 'xs', 'diffusion']
            rc['xs.getInfXS'] = True  # only store inf cross sections
            rc['xs.getB1XS'] = False
            cls.reader = ResultsReader(cls.file)
        cls.reader.read()


class ResultsTester(_ResultsTesterHelper):
    """Class for testing the results reader."""

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

if __name__ == '__main__':
    unittest.main()
    a = 1
