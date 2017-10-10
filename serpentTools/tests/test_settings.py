"""Tests for the settings loaders."""
import unittest

from serpentTools import settings


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


class UserSettingsTester(unittest.TestCase):
    """Class to test the methods of updating the user settings."""

    @classmethod
    def setUpClass(cls):
        cls.loader = settings.UserSettingsLoader()

    def test_failAtNonexistentSetting(self):
        """Verify that the loader will not load a nonexistent setting."""
        with self.assertRaises(KeyError):
            self.loader['bad setting'] = False

    def test_failAtBadSetting_options(self):
        """Verify that the loader will raise an error for bad options."""
        with self.assertRaises(KeyError):
            self.loader['depletion.metadata'] = ['this should fail']

    def test_failAtBadSettings_type(self):
        """Verify that the loader will raise an error for bad type."""
        with self.assertRaises(TypeError):
            self.loader['depletion.processTotal'] = 'this should fail'

    def test_returnReaderSettings(self):
        """Verify the correct reader settings can be retrieved."""
        readerName = 'depletion'
        expected = {
            'metadataKeys': ['ZAI', 'NAMES', 'DAYS', 'BU'],
            'materialVariables': ['ADENS', 'MDENS', 'BURNUP'],
            'materials': [],
            'processTotal': True,
        }
        actual = self.loader.getReaderSettings(readerName)
        self.assertDictEqual(expected, actual)


class RCTester(unittest.TestCase):
    """Class to test the functionality of the scriptable settings manager."""

    @classmethod
    def setUpClass(cls):
        cls.rc = settings.rc
        cls.rc['depletion.metadataKeys'] = ['ZAI']

    def test_readerWithUpdatedSettings(self):
        """Verify the settings passed to the reader reflect the update."""
        from serpentTools.parsers.depletion import DepletionReader
        reader = DepletionReader('None')
        self.assertTrue(reader.settings['metadataKeys'] == ['ZAI'])


class VariableExtenderTester(unittest.TestCase):
    """Class to test the functionality of the keyword extender."""

    def test_returnExtras(self):
        """Verify that a set of extras is given if that is the only argument."""
        extras = ['hello', 'testing']
        expected = set(extras)
        actual = settings.extendVariableGroups('2.1.29', None, extras)
        self.assertSetEqual(expected, actual)

    def test_fullExtend(self):
        groupNames = ['times', 'diffusion']
        extras = {'hello'}
        expected = {'CMM_TRANSPXS', 'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y',
                    'CMM_TRANSPXS_Z', 'CMM_DIFFCOEFF', 'CMM_DIFFCOEFF_X',
                    'CMM_DIFFCOEFF_Y', 'CMM_DIFFCOEFF_Z', 'hello',
                    'TOT_CPU_TIME', 'RUNNING_TIME', 'INIT_TIME', 'PROCESS_TIME',
                    'TRANSPORT_CYCLE_TIME', 'BURNUP_CYCLE_TIME',
                    'BATEMAN_SOLUTION_TIME', 'MPI_OVERHEAD_TIME',
                    'ESTIMATED_RUNNING_TIME', 'CPU_USAGE',
                    'TRANSPORT_CPU_USAGE', 'OMP_PARALLEL_FRAC'}
        actual = settings.extendVariableGroups('2.1.29', groupNames, extras)
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
