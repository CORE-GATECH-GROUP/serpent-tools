import os

ROOT_DIR = os.path.dirname(__file__)

from serpentTools.parsers import read
from serpentTools import messages

# List TODOS/feature requests here for now
# Compatibility
# TODO: Test compatibility with earlier numpy releases
# Usage/scripting
# TODO: Update rc with dictionary
# TODO: Update rc with yaml file into dictionary
# TODO: Capture materials with underscores for depletion
# TODO: Find a way to capture some or all of log messages for testing

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

messages.info('Using version {}'.format(__version__))
