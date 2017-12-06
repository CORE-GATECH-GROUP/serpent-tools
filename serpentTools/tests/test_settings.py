"""Tests for the settings loaders."""
import unittest

from serpentTools import settings
from serpentTools.messages import deprecated, willChange


class DefaultSettingsTester(unittest.TestCase):
    """Class to test the functionality of the master loader."""

    @classmethod
    def setUpClass(cls):
        cls.defaultLoader = settings.DefaultSettingsLoader()
        cls.testSetting = 'depletion.metadataKeys'
        cls.testSettingExpected = ['ZAI', 'NAMES', 'DAYS', 'BU']
        cls.testSettingMethod = cls.assertListEqual

    def test_getDefault(self):
        """Verify the default settings loader properly retrives defaults."""
        self.testSettingMethod(self._getLoaderSetting(self.testSetting),
                               self.testSettingExpected)

    def test_cannotChangeDefaults(self):
        """Verify the default settings loader is locked after creation."""
        with self.assertRaises(KeyError):
            self.defaultLoader['this'] = 'should fail'

    def _getLoaderSetting(self, setting):
        return self.defaultLoader[setting].default


class RCTester(unittest.TestCase):
    """Class to test the functionality of the scriptable settings manager."""

    @classmethod
    def setUpClass(cls):
        cls.rc = settings.UserSettingsLoader()
        cls.rc['depletion.metadataKeys'] = ['ZAI']

    def test_failAtNonexistentSetting(self):
        """Verify that the loader will not load a nonexistent setting."""
        with self.assertRaises(KeyError):
            self.rc['bad setting'] = False

    def test_failAtBadSetting_options(self):
        """Verify that the loader will raise an error for bad options."""
        with self.assertRaises(KeyError):
            self.rc['depletion.metadata'] = ['this should fail']

    def test_failAtBadSettings_type(self):
        """Verify that the loader will raise an error for bad type."""
        with self.assertRaises(TypeError):
            self.rc['depletion.processTotal'] = 'this should fail'

    def test_returnReaderSettings(self):
        """Verify the correct reader settings can be retrieved."""
        readerName = 'depletion'
        expected = {
            'metadataKeys': ['ZAI'],
            'materialVariables': [],
            'materials': [],
            'processTotal': True,
        }
        actual = self.rc.getReaderSettings(readerName)
        self.assertDictEqual(expected, actual)

    def test_readerWithUpdatedSettings(self):
        """Verify the settings passed to the reader reflect the update."""
        from serpentTools.parsers.depletion import DepletionReader
        with settings.rc as tempRC:
            tempRC['depletion.metadataKeys'] = ['ZAI']
            reader = DepletionReader('None')
        self.assertTrue(reader.settings['metadataKeys'] == ['ZAI'])

    def test_expandExtras(self):
        """Verify that a set of extras is given if that is the only argument."""
        extras = ['hello', 'testing']
        with self.rc as tempRC:
            tempRC['xs.variableExtras'] = extras
            expected = set(extras)
            actual = tempRC.expandVariables()
        self.assertSetEqual(expected, actual)

    def test_fullExtend(self):
        """Verify that the variable expansion return the correct variables"""
        groupNames = ['times', 'diffusion']
        extras = ['hello']
        expected = {'CMM_TRANSPXS', 'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y',
                    'CMM_TRANSPXS_Z', 'CMM_DIFFCOEFF', 'CMM_DIFFCOEFF_X',
                    'CMM_DIFFCOEFF_Y', 'CMM_DIFFCOEFF_Z', 'hello',
                    'TOT_CPU_TIME', 'RUNNING_TIME', 'INIT_TIME', 'PROCESS_TIME',
                    'TRANSPORT_CYCLE_TIME', 'BURNUP_CYCLE_TIME',
                    'BATEMAN_SOLUTION_TIME', 'MPI_OVERHEAD_TIME',
                    'ESTIMATED_RUNNING_TIME', 'CPU_USAGE',
                    'TRANSPORT_CPU_USAGE', 'OMP_PARALLEL_FRAC'}
        with self.rc as tempRC:
            tempRC['xs.variableExtras'] = extras
            tempRC['xs.variableGroups'] = groupNames
            actual = tempRC.expandVariables()
        self.assertSetEqual(expected, actual)


class MessagingTester(unittest.TestCase):
    """Class to test the messaging framework."""

    def test_futureDecorator(self):
        """Verify that the future decorator doesn't break"""

        @willChange('This function will be updated in the future, '
                    'but will still exist')
        def demoFuture(x, val=5):
            return x + val

        self.assertEqual(7, demoFuture(2))
        self.assertEqual(7, demoFuture(2, 5))

    def test_depreciatedDecorator(self):
        """Verify that the depreciated decorator doesn't break things"""

        @deprecated('this nonexistent function')
        def demoFunction(x, val=5):
            return x + val

        self.assertEqual(7, demoFunction(2))
        self.assertEqual(7, demoFunction(2, 5))


if __name__ == '__main__':
    unittest.main()
