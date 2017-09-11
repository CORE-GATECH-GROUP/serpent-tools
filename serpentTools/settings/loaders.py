"""File dedicated to loading and updating settings."""

import os

import yaml
from dict_digger import dig


ROOT = os.path.dirname(__file__)


class WalkableDictionary(dict):
    """Dictionary with a recursive walk method."""

    def __init__(self, data):
        dict.__init__(self, data)
        self._items = None

    def yieldKeys(self, currentLevel=None, previousKeys=None):
        previousKeys = previousKeys or []
        currentLevel = currentLevel or dict(self)
        if isinstance(currentLevel, dict):
            for key, value in currentLevel.items():
                if isinstance(value, dict):
                    for d in self.yieldKeys(value, previousKeys + [key]):
                        yield d
                else:
                    yield previousKeys + [key]
        else:
            yield previousKeys

    def digItems(self):
        """Yield keys and values, like ``dict.items`` but recursive!"""
        for keys in self.yieldKeys():
            yield keys, dig(self, *keys)

    def _establishNests(self, keys, nestedDict=None):
        currentLevel = nestedDict if nestedDict is not None else self
        for path in keys:
            if path not in currentLevel:
                currentLevel[path] = {}
            currentLevel = currentLevel[path]
        return currentLevel

    def __len__(self):
        if self._items is None:
            self._items = len(list(self.yieldKeys()))
        return self._items

    @staticmethod
    def _getPathFromName(varName):
        return varName.split('.') if isinstance(varName, str) else varName


class DefaultSettingsLoader(WalkableDictionary):
    """Base class for loading all the default settings."""

    def __init__(self):
        self.masterFile = os.path.join(ROOT, 'masterSettings.yaml')
        self.__locked__ = False
        WalkableDictionary.__init__(self, self._loadDefaults())
        self.__locked__ = True

    def __repr__(self):
        return '<DefaultSettings at {}>'.format(id(self))

    def _loadDefaults(self):
        """Load the master settings."""
        with open(self.masterFile) as mFile:
            return yaml.load(mFile)

    def __setitem__(self, key, value):
        if self.__locked__:
            raise TypeError('{} is locked. Cannot set values.'.format(self))
        WalkableDictionary.__setitem__(self, key, value)

    def getDefault(self, name):
        keys = self._getPathFromName(name)
        setting = dig(self, *keys)
        if setting is None:
            raise KeyError('Could not find DefaultSetting for {}'.format(name))
        if isinstance(setting, dict):
            return setting
        return setting.default

    def yieldKeysAndDefault(self):
        """Yield the path to a specific setting, the setting name and value."""
        for path in self.yieldKeys():
            yield '.'.join(path), self.getDefault(path)


class DefaultSetting(object):
    """Store a single setting."""

    def __init__(self, name, default, description, options=None):
        self.name = name
        self.description = description
        self.options = set(options) if options else set()
        self.default = default

    def __repr__(self):
        return '<DefaultSetting {}: value: {}>'.format(self.name, self.default)

    @property
    def varType(self):
        return type(self.default)

    def verifyValue(self, value):
        """
        Return true if a value corresponds to the default type and options

        Parameters
        ----------
        value: value to be tested

        Returns
        -------
        True if the value can be used. False otherwise
        """
        if not isinstance(value, self.varType):
            return False
        if hasattr(self, 'options'):
            listVals = [value] if not isinstance(value, list) else value
            return any([val in self.options for val in listVals])
        return True


class UserSettingsLoader(WalkableDictionary):
    """Class that stores the settings requested by the user."""

    def __init__(self, updatedSettings=None):
        WalkableDictionary.__init__(self, {})
        self._defaults = DefaultSettingsLoader()
        if updatedSettings is not None:
            self._checkVarNames(WalkableDictionary(updatedSettings))
        self.updateSettings(updatedSettings)

    def setValue(self, name, value):
        """
        Set the value of a specific setting.

        Parameters
        ----------
        name: str or list
            Name of the setting or list of keys pointing towards the setting
            i.e. ``'readers.depletion.metadataKeys'`` or
            ``['readers', 'depletion', 'metadataKeys']``
        value: value to set

        Raises
        ------
        KeyError
            if the value does not match the schema set by the Default setting
        """
        keys = self._getPathFromName(name)
        default = dig(self._defaults, *keys)
        settingName = keys.pop(-1)
        settingLevel = self._establishNests(keys)
        if default.verifyValue(value):
            settingLevel[settingName] = value
        else:
            optStr = ('' if not hasattr(default, 'options') else
                      '\nOptions: {}'.format(
                          [str(opt) for opt in default.options]))
            raise KeyError('Value {v}\n for setting {n} is does not meet the '
                           'allowable criteria: \nType: {t}{o}'
                           .format(v=value, n=name, o=optStr,
                                   t=default.varType))

    def updateSettings(self, updateSettingsDict):
        """
        Update the settings for this run.

        Parameters
        ----------
        updateSettingsDict: dict
            nested settings, i.e. ::

                settings = {
                    'reader': {
                        'depletion': {
                            'metadataKeys': ['ZAI']
                            }
                        }
                    }
        """

        for keys, defaultSetting in self._defaults.digItems():
            existingValue = dig(updateSettingsDict, *keys)
            self.setValue(keys, (existingValue if existingValue is not None
                                 else defaultSetting.default))

    def getValue(self, name):
        """
        Return the value of the setting found at ``name``.

        Parameters
        ----------
        name: str or list
            Name of the setting or list of keys pointing towards the setting
            i.e. ``'readers.depletion.metadataKeys'`` or
            ``['readers', 'depletion', 'metadataKeys']``

        Returns
        -------
        leaf: object
            Whatever is at the end of the path specified by name

        Raises
        ------
        KeyError:
            if nothing is at the end of the path
        """
        path = self._getPathFromName(name)
        value = dig(self, *path)
        if value is None:
            raise KeyError('No value for setting {} found.'.format(name))
        return value

    def _checkVarNames(self, walkableUpdate: WalkableDictionary):
        for keys in walkableUpdate.yieldKeys():
            try:
                dig(self._defaults, *keys, fail=True)
            except (KeyError, IndexError):
                name = '.'.join(keys)
                raise KeyError('Setting {} not found in defaults.'.format(name))

    def getReaderSettings(self, readerLevel):
        """
        Get all module-wide and reader-specific settings.

        Parameters
        ----------
        readerLevel: str
            Name of the specific reader. Must be a key in the ``readers``
            settings dictionary

        Returns
        -------
        rSettings: dict
            Single level dictionary with ``settingName: settingValue`` pairs

        Raises
        ------
        KeyError:
            If the reader name is not located in the ``readers`` settings
            dictionary
        """
        if readerLevel not in self['readers']:
            readerOpts = [key for key, value in self.digItems()
                          if isinstance(value, dict)]
            raise KeyError("Could not find reader named {} in settings.\n"
                           "Options: {}"
                           .format(readerLevel, ', '.join(readerOpts)))
        rSettings = {}
        for fullName, value in self.digItems():
            nameChunks = self._getPathFromName(fullName)
            if nameChunks[0] != 'readers':
                continue
            if (len(nameChunks) == 2  # settings for all readers
                    or (len(nameChunks) == 3) and nameChunks[1] == readerLevel):
                rSettings[nameChunks[-1]] = value
        return rSettings
