"""Tests for the settings loaders."""
from os import remove
from unittest import TestCase

import yaml
import six

from serpentTools import settings
from serpentTools.tests.utils import TestCaseWithLogCapture


class DefaultSettingsTester(TestCase):
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


class RCTester(TestCase):
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
        """Verify that a set of extras is given if that is the only argument.
        """
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
                    'CMM_TRANSPXS_Z', 'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X',
                    'CMM_DIFFCOEF_Y', 'CMM_DIFFCOEF_Z', 'hello',
                    'TOT_CPU_TIME', 'RUNNING_TIME', 'INIT_TIME',
                    'PROCESS_TIME',
                    'TRANSPORT_CYCLE_TIME', 'BURNUP_CYCLE_TIME',
                    'BATEMAN_SOLUTION_TIME', 'MPI_OVERHEAD_TIME',
                    'ESTIMATED_RUNNING_TIME', 'CPU_USAGE',
                    'TRANSPORT_CPU_USAGE', 'OMP_PARALLEL_FRAC'}
        with self.rc as tempRC:
            tempRC['xs.variableExtras'] = extras
            tempRC['xs.variableGroups'] = groupNames
            actual = tempRC.expandVariables()
        self.assertSetEqual(expected, actual)


class ConfigLoaderTester(TestCaseWithLogCapture):
    """Class to test loading multiple setttings at once, i.e. config files"""

    @classmethod
    def setUpClass(cls):
        cls.configSettings = {
            'branching.floatVariables': ['Bhi', 'Tlo'],
            'verbosity': 'warning',
            'depletion.materials': ['fuel*'],
            'depletion.materialVariables': ['ADENS', 'MDENS']
        }
        cls.nestedSettings = {
            'branching': {
                'floatVariables':
                    cls.configSettings['branching.floatVariables']
            },
            'depletion': {
                'materials': cls.configSettings['depletion.materials'],
                'materialVariables':
                    cls.configSettings['depletion.materialVariables']
            },
            'verbosity': cls.configSettings['verbosity']
        }
        cls.files = {'singleLevel': 'singleLevelConf.yaml',
                     'nested': 'nestedConf.yaml',
                     'badNested': 'badNestedConf.yaml'}
        cls.rc = settings.UserSettingsLoader()

    def _writeTestRemoveConfFile(self, settings, filePath, expected, strict):
        with open(filePath, 'w') as out:
            yaml.dump(settings, out)
        with self.rc:
            self.rc.loadYaml(filePath, strict)
            for key, value in six.iteritems(expected):
                if isinstance(value, list):
                    self.assertListEqual(value, self.rc[key])
                else:
                    self.assertEqual(value, self.rc[key])
        remove(filePath)

    def test_loadSingleLevelConfig(self):
        """Test loading settings from a non-nested config file"""
        self._writeTestRemoveConfFile(self.configSettings,
                                      self.files['singleLevel'],
                                      self.configSettings, True)

    def test_loadNestedConfig(self):
        """Test loading settings from a nested config file"""
        self._writeTestRemoveConfFile(self.nestedSettings,
                                      self.files['nested'],
                                      self.configSettings, True)

    def test_loadNestedNonStrict(self):
        """Test loading settings with errors but non-strict error handling"""
        badSettings = {'bad setting': False}
        badSettings.update(self.nestedSettings)
        self._writeTestRemoveConfFile(badSettings, self.files['nested'],
                                      self.configSettings, False)
        self.assertMsgInLogs("ERROR", "bad setting", partial=True)


if __name__ == '__main__':
    from unittest import main
    main()
