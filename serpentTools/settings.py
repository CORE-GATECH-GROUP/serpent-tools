"""Settings to yield control to the user."""
import os
import six

import yaml

from serpentTools import ROOT_DIR
from serpentTools import messages

__all__ = ['defaultSettings', 'rc']

defaultSettings = {
    'branching.areUncsPresent': {
        'default': False,
        'type': bool,
        'description': "True if the values in the .coe file contain "
                       "uncertainties"
    },
    'branching.intVariables': {
        'default': [],
        'description': 'Name of state data variables to convert to integers '
                       'for each branch',
        'type': list
    },
    'branching.floatVariables': {
        'default': [],
        'description': 'Names of state data variables to convert to floats '
                       'for each branch',
        'type': list
    },
    'depletion.metadataKeys': {
        'default': ['ZAI', 'NAMES', 'DAYS', 'BU'],
        'options': 'default',
        'description': 'Non-material data to store, i.e. zai, isotope names, '
                       'burnup schedule, etc.',
        'type': list
    },
    'depletion.materialVariables': {
        'default': [],
        'description': 'Names of variables to store. '
                       'Empty list -> all variables.',
        'type': list
    },
    'depletion.materials': {
        'default': [],
        'description': 'Names of materials to store. '
                       'Empty list -> all materials.',
        'type': list
    },
    'depletion.processTotal': {
        'default': True,
        'description': 'Option to store the depletion data from the TOT block',
        'type': bool
    },
    'detector.names': {
        'default': [],
        'description': 'List of detectors to store. Empty list -> store all '
                       'detectors',
        'type': list
    },
    'verbosity': {
        'default': 'info',
        'options': messages.LOG_OPTS,
        'type': str,
        'description': 'Set the level of errors to be shown.',
        'updater': messages.updateLevel
    },
    'serpentVersion': {
        'default': '2.1.29',
        'options': ['2.1.29'],
        'description': 'Version of SERPENT',
        'type': str
    },
    'xs.getInfXS': {
        'default': True,
        'description': 'If true, store the infinite medium cross sections.',
        'type': bool
    },
    'xs.getB1XS': {
        'default': True,
        'description': 'If true, store the critical leakage cross sections.',
        'type': bool
    },
    'xs.variableGroups': {
        'default': [],
        'description': ('Name of variable groups from variables.yaml to be '
                        'expanded into SERPENT variable to be stored'),
        'type': list
    },
    'xs.variableExtras': {
        'default': [],
        'description': 'Full SERPENT name of variables to be read',
        'type': list
    }
}


class DefaultSetting(object):
    """Store a single setting."""

    def __init__(self, name, default, varType, description, options, updater):
        self.name = name
        self.description = description
        self.default = default
        self.type = varType
        self.options = options
        self.updater = updater

    def __repr__(self):
        return '<DefaultSetting {}: value: {}>'.format(self.name, self.default)

    def validate(self, value):
        """Return True if the value matches the default scheme.

        Parameters
        ----------
        value:
            value to be tested

        Returns
        -------
        bool
            if the value can be used

        Raises
        ------
        TypeError
            If the value is of an incorrect type
        KeyError
            If the value does not correspond to one of the acceptable options
        """
        if not isinstance(value, self.type):
            raise TypeError('Setting {} should be of type {}, not {}'
                            .format(self.name, self.type, type(value)))
        if self.options:
            listVals = [value] if not isinstance(value, list) else value
            inOptions = any([val in self.options for val in listVals])
            if not inOptions:
                opts = ', '.join([str(option) for option in self.options])
                raise KeyError('Setting {} is {} and not one of the allowed '
                               'options: {}'
                               .format(self.name, value, opts))
        return True


class DefaultSettingsLoader(dict):
    """Base class for loading all the default settings."""

    def __init__(self):
        self.__locked__ = False
        dict.__init__(self, self._load())
        self.__locked__ = True

    @staticmethod
    def _load():
        """Load the default setting objects."""
        defaults = {}
        for name, value in defaultSettings.items():
            if 'options' in value:
                options = (value['default'] if value['options'] == 'default'
                else value['options'])
            else:
                options = None
            settingsOptions = {'name': name,
                               'default': value['default'],
                               'varType': value['type'],
                               'options': options,
                               'description': value['description'],
                               'updater': value.get('updater', None)
                               }
            defaults[name] = DefaultSetting(**settingsOptions)
        return defaults

    def __setitem__(self, key, value):
        if self.__locked__:
            raise KeyError('Default settings cannot be updated once set.')
        self[key] = value

    def retrieveDefaults(self):
        """Return a dictionary with the default settings."""
        return {key: setting.default for key, setting in self.items()}

    def validateSetting(self, name, value):
        """Validate the setting.

        Parameters
        ----------
        name: str
            Full name of the setting
        value: value to be set

        Raises
        ------
        KeyError
            If the value is not one of the allowable options or if the
            setting does not match an existing setting
        TypeError
            If the value is not of the correct type
        """
        if name not in self:
            raise KeyError('Setting {} does not exist'.format(name))
        self[name].validate(value)


class UserSettingsLoader(dict):
    """Class that stores the active user settings."""

    def __init__(self):
        self._defaultLoader = DefaultSettingsLoader()
        self.__inside__ = False
        self.__originals__ = {}
        dict.__init__(self, self._defaultLoader.retrieveDefaults())

    def __setitem__(self, key, value):
        self._checkStoreOriginal(key)
        self.setValue(key, value)

    def __enter__(self):
        self.__inside__ = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__inside__ = False
        for key, originalValue in self.__originals__.items():
            self[key] = originalValue
        self.__originals__ = {}

    def _checkStoreOriginal(self, key):
        if self.__inside__:
            self.__originals__[key] = self[key]

    def setValue(self, name, value):
        """Set the value of a specific setting.

        Parameters
        ----------
        name: str
            Full name of the setting
        value: value to be set

        Raises
        ------
        KeyError
            If the value is not one of the allowable options or if the
            setting does not match an existing setting
        TypeError
            If the value is not of the correct type

        """
        if name not in self:
            raise KeyError('Setting {} does not exist'.format(name))
        self._defaultLoader[name].validate(value)
        # if we've made it here, then the value is valid
        if self._defaultLoader[name].updater is not None:
            value = self._defaultLoader[name].updater(value)
        dict.__setitem__(self, name, value)
        messages.debug('Updated setting {} to {}'.format(name, value))

    def getReaderSettings(self, settingsPreffix):
        """Get all module-wide and reader-specific settings.

        Parameters
        ----------
        settingsPreffix: str or list
            Name of the specific reader.
            Will look for settings that lead with ``readerName``, e.g.
            ``depletion.metadataKeys`` or ``xs.variables``

        Returns
        -------
        dict
            Single level dictionary with ``settingName: settingValue`` pairs

        Raises
        ------
        KeyError
            If the reader name is not located in the ``readers`` settings
            dictionary
        """
        settings = {}
        settingsPreffix = ([settingsPreffix] if isinstance(settingsPreffix, str)
        else settingsPreffix)
        for setting, value in self.items():
            settingPath = setting.split('.')
            if settingPath[0] in settingsPreffix:
                name = settingPath[1]
            else:
                continue
            settings[name] = value
        if not settings:
            messages.warning('Could not obtain settings for the following '
                             'reader names: {}'
                             .format(', '.join(settingsPreffix)))
        return settings

    def expandVariables(self):
        """Extend the keyword groups into lists of serpent variables.

           Returns
           -------
           set
               Names of all variables to be scraped
           """
        keywords = self['xs.variableGroups']
        extras = self['xs.variableExtras']
        serpentVersion = self['serpentVersion']
        if not (keywords or extras):  # return empty set and don't read
            return set()
        variables = set(extras) if extras else set()
        if not keywords:
            return variables
        varFile = os.path.join(ROOT_DIR, 'variables.yaml')
        with open(varFile) as fObj:
            groups = yaml.load(fObj)
        thisVersion = groups[serpentVersion]
        baseGroups = groups['base']
        for key in keywords:
            if key in thisVersion:
                variables.update(thisVersion[key])
            elif key in baseGroups:
                variables.update(baseGroups[key])
        return variables

    def loadYaml(self, filePath, strict=True):
        """
        Update the settings based on the contents of the yaml file

        .. versionadded:: 0.2.0

        Parameters
        ----------
        filePath: str
            Path to config file
        strict: bool
            Fail at the first incorrect setting. If false, failed settings
            will not be loaded and alerts will be raised

        Raises
        ------
        KeyError or TypeError
            If settings found in the config file are not
            valid
        FileNotFound or OSError
            If the file does not exist

        """
        messages.debug('Attempting to read from {}'.format(filePath))
        with open(filePath) as yFile:
            l = yaml.safe_load(yFile)
        messages.info('Loading settings onto object with strict:{}'
                      .format(strict))

        for key, value in six.iteritems(l):
            if isinstance(value, dict):
                self.__recursiveLoad(value, strict, key)
            else:
                self.__safeLoad(key, value, strict)
        messages.info('Done')

    def __recursiveLoad(self, curLevel, strict, preset):
        for nextLevelKey, nextLevel in six.iteritems(curLevel):
            newSettingName = preset + '.' + nextLevelKey
            if isinstance(nextLevel, dict):
                self.__recursiveLoad(nextLevel, strict, newSettingName)
            else:
                self.__safeLoad(newSettingName, nextLevel, strict)

    def __safeLoad(self, key, value, strict):
        messages.debug('Attempting to set setting {} to {}'
                       .format(key, value))
        try:
            self.setValue(key, value)
        except (KeyError, TypeError) as error:
            if strict:
                raise error
            else:
                messages.error(str(error))


rc = UserSettingsLoader()
