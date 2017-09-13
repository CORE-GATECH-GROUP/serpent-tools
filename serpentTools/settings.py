"""Settings to yield control to the user."""

defaultSettings = {
    'depletion.metadataKeys': {
        'default': ['ZAI', 'NAMES', 'DAYS', 'BU'],
        'options': 'default',
        'description': 'Non-material data to store, i.e. zai, isotope names, '
                       'burnup schedule, etc.',
        'type': list
    },
    'depletion.materialVariables': {
        'default': ['ADENS', 'MDENS', 'BURNUP'],
        'description': 'Variables to store for each depleted material.',
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
    }
}


class DefaultSetting(object):
    """Store a single setting."""

    def __init__(self, name, default, varType, description, options):
        self.name = name
        self.description = description
        self.default = default
        self.type = varType
        self.options = options

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
                opts = [str(option) for option in self.options]
                raise KeyError('Setting {} is\n{}\nand not one of the allowed '
                               'options:\n{}'
                               .format(self.name, value, opts))
        return True


class DefaultSettingsLoader(dict):
    """Base class for loading all the default settings."""

    def __init__(self):
        self.__locked__ = False
        dict.__init__(self, self._load())
        self.__locked__ = True

    def _load(self):
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
                               'description': value['description']
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
        dict.__init__(self, self._defaultLoader.retrieveDefaults())

    def __setitem__(self, key, value):
        self.setValue(key, value)

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
        dict.__setitem__(self, name, value)

    def getReaderSettings(self, readerName):
        """Get all module-wide and reader-specific settings.

        Parameters
        ----------
        readerLevel: str
            Name of the specific reader.
            Will look for settings with lead with ``readerName``, e.g.
            ``depletion.metadataKeys``

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
        self._validateReaderName(readerName)
        for setting, value in self.items():
            settingPath = setting.split('.')
            if len(settingPath) == 1:  # high level setting like verbosity
                name = settingPath[0]
            else:
                if settingPath[0] == readerName:
                    name = settingPath[1]
                else:
                    continue
            settings[name] = value
        return settings

    def _validateReaderName(self, readerName):
        """Return True if the reader name has settings."""
        readers = set([name.split('.')[0] for name in self if '.' in name])
        return readerName in readers


rc = UserSettingsLoader()
