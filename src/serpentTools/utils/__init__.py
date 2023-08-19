"""
Commonly used functions and utilities
"""
from distutils.version import StrictVersion

from serpentTools.utils.core import *  # noqa
from serpentTools.utils.docstrings import *  # noqa
from serpentTools.utils.compare import *  # noqa
from serpentTools.utils.plot import *  # noqa


def checkScipy(version=None):
    """Return ``True`` if the given version of :term:`scipy` is installed"""
    try:
        import scipy
    except ImportError:
        return False
    if version is None:
        return True
    return StrictVersion(scipy.__version__) >= StrictVersion(version)
