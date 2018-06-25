import os

ROOT_DIR = os.path.dirname(__file__)

from serpentTools.parsers import *
from serpentTools.data import *
from serpentTools.samplers import *
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

