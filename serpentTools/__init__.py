import os

ROOT_DIR = os.path.dirname(__file__)

from serpentTools import settings

# List TODOS/feature requests here for now
# Compatability
# TODO: Python 2 support
# TODO: Test compatibility with earlier numpy releases
# Usage/scripting
# TODO: Update rc with dictionary
# TODO: Update rc with yaml file into dictionary
# TODO: Capture materials with underscores for depletion

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

settings.messages.info('Using version {}'.format(__version__))
