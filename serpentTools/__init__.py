from serpentTools import settings
from serpentTools.settings.loaders import UserSettingsLoader


class MasterSettingsLoader(UserSettingsLoader):
    """Main settings object that controls all operations."""

    def __init__(self):
        self._loaded = False
        UserSettingsLoader.__init__(self, None)
        self._loaded = True

    def __setitem__(self, key, value):
        if self._loaded:
            self.setValue(key, value)
        else:
            UserSettingsLoader.__setitem__(self, key, value)

    def __repr__(self):
        return '<Master settings loader>'

rc = MasterSettingsLoader()

from serpentTools import parsers
from serpentTools import tests


# List TODOS/feature requests here for now
# Messages/Errors
# TODO: Add verbosity control
# TODO: Add specific exceptions and warnings
# Compatability
# TODO: Python 2 support
# TODO: Test compatability with earlier numpy  releases
# Pythonicness/cleanliness
# TODO: Better rc importing and usage
# TODO: Remove need to specify all settings as a default setting object
# Usage/scripting
# TODO: Update rc with dictionary
# TODO: Update rc with yaml file into dictionary
# TODO: Capture materials with underscores for depletion
