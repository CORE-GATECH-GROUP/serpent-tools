"""Tests for the settings loaders."""
import unittest

import serpentTools
from serpentTools.settings.loaders import (
    DefaultSettingsLoader, UserSettingsLoader, WalkableDictionary)


class WalkableDictionaryTester(unittest.TestCase):
    """Class that tests the walkable dictionary"""

    @classmethod
    def setUpClass(cls):
        cls.ref = {
            'item0': {
                'item0_0': [1, 2, 3],
                'item0_1': {
                    'item0_1_0': True
                },
            },
            'item1': 3.14159
        }
        cls.walkable = WalkableDictionary(cls.ref)

    def test_len(self):
        """Verify the number of items in the dictionary is correct"""
        self.assertEqual(len(self.walkable), 3)


class MasterSettingsTester(unittest.TestCase):
    """Class to test the functionality of the master loader."""

    @classmethod
    def setUpClass(cls):
        cls.defaultLoader = DefaultSettingsLoader()
        cls.testSetting = 'readers.depletion.metadataKeys'
        cls.testSettingExpected = ['ZAI', 'NAMES', 'DAYS', 'BU']
        cls.testSettingMethod = cls.assertListEqual

    def test_getDefault_listPath(self):
        """
        Verify the default settings loader can retrieve settings properly
        from list of keys.
        """
        self.testSettingMethod(
            self._getLoaderSetting(self.testSetting.split('.')),
            self.testSettingExpected)

    def test_getDefault_stringPath(self):
        """
        Verify the default settings loader can retrieve settings properly
        from a string path.
        """
        self.testSettingMethod(self._getLoaderSetting(self.testSetting),
                               self.testSettingExpected)

    def test_cannotChangeDefaults(self):
        """Verify the default settings loader is locked after creation."""
        with self.assertRaises(TypeError):
            self.defaultLoader['this'] = 'should fail'

    def _getLoaderSetting(self, setting):
        return self.defaultLoader.getDefault(setting)


class UserSettingsTester(unittest.TestCase):
    """Class to test the methods of updating the user settings."""

    @classmethod
    def setUpClass(cls):
        goodSettings = {
            'readers':
                {'depletion': {'metadataKeys': ['ZAI']}
                 }
        }
        cls.loader = UserSettingsLoader(goodSettings)

    def test_getByVariableName(self):
        """Verify that the loader can access the variable by name."""
        self.assertListEqual(['ZAI'], self.loader.getValue(
            'readers.depletion.metadataKeys'))

    def test_getByVariablePath(self):
        """Verify that the loader can access the variable by path."""
        self.assertListEqual(['ZAI'], self.loader.getValue(
            ['readers', 'depletion', 'metadataKeys']))

    def test_failAtNonexistentSetting(self):
        """Verify that the loader will not load a nonexistent setting."""
        nonExistentSettings = {
            'readers': {
                'badParser': False
            }
        }
        with self.assertRaises(KeyError):
            UserSettingsLoader(nonExistentSettings)

    def test_failAtBadSetting_options(self):
        """Verify that the loader will raise an error for bad options."""
        malformedSettings = {
            'readers': {
                'depletion': {
                    'metadataKeys': ['fail on metadataKeys'],  # not in options
                }
            }
        }
        with self.assertRaises(KeyError):
            UserSettingsLoader(malformedSettings)

    def test_failAtBadSettings_type(self):
        """Verify that the loader will raise an error for bad type."""
        malformedSettings = {
            'readers': {
                'depletion': {
                    'materialVariables': 'fail on materialVariables'  # bad type
                }
            }
        }
        with self.assertRaises(KeyError):
            UserSettingsLoader(malformedSettings)

    def test_returnReaderSettings(self):
        """Verify the correct reader settings can be retrieved."""
        readerName = 'depletion'
        expected = {
            'metadataKeys': ['ZAI'],
            'materialVariables': ['VOLUME', 'ADENS', 'MDENS', 'BURNUP'],
            'materials': []
        }
        actual = self.loader.getReaderSettings(readerName)
        self.assertDictEqual(expected, actual)


class RCTester(unittest.TestCase):
    """Class to test the funcitonality of the scriptable settings manager."""

    @classmethod
    def setUpClass(cls):
        cls.rc = serpentTools.rc


if __name__ == '__main__':
    unittest.main()
