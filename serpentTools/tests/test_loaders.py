"""Tests for the settings loaders."""
import unittest

from serpentTools.settings import DefaultSettingsLoader, UserSettingsLoader


class DefaultSettingsTester(unittest.TestCase):
    """Class to test the functionality of the master loader."""

    @classmethod
    def setUpClass(cls):
        cls.defaultLoader = DefaultSettingsLoader()
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
        cls.loader = UserSettingsLoader()

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
            'verbosity': 'warning'
        }
        actual = self.loader.getReaderSettings(readerName)
        self.assertDictEqual(expected, actual)


class RCTester(unittest.TestCase):
    """Class to test the funcitonality of the scriptable settings manager."""

    @classmethod
    def setUpClass(cls):
        from serpentTools.settings import rc
        cls.rc = rc
        cls.rc['depletion.metadataKeys'] = ['ZAI']

    def test_readerWithUpdatedSettings(self):
        """Verify the settings passed to the reader reflect the update."""
        from serpentTools.parsers.depletion import DepletionReader
        reader = DepletionReader('None')
        self.assertTrue(reader.settings['metadataKeys'] == ['ZAI'])


if __name__ == '__main__':
    unittest.main()
