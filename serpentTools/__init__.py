from serpentTools import settings
rc = settings.loaders.UserSettingsLoader()
"""Settings loader that will be used for scripting and adjusting readers"""
# placed above parsers import because parsers and rely on this class

from serpentTools import parsers
from serpentTools import tests


# List TODOS/feature requests here for now
# Messages/Errors
# TODO: Add verbosity control
# TODO: Add specific exceptions and warnings
# TODO: Figure out how to capture materials with underscores for depletion
# Compatability
# TODO: Python 2 support
# TODO: Test compatability with earlier numpy  releases
# Pythonicness/cleanliness
# TODO: Better rc importing and usage
# TODO: Remove need to specify all settings as a default setting object
