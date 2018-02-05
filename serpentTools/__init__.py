import os

ROOT_DIR = os.path.dirname(__file__)

from serpentTools.parsers import read
from serpentTools import messages
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

messages.info('Using version {}'.format(__version__))
