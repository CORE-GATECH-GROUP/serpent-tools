"""
Commonly used functions and utilities
"""
try:
    import scipy  # noqa
    __HAS_SCIPY = True
except ImportError:
    __HAS_SCIPY = False

from serpentTools.utils.core import *  # noqa
from serpentTools.utils.docstrings import *  # noqa
from serpentTools.utils.compare import *  # noqa
from serpentTools.utils.plot import *  # noqa


def hasScipy():
    """Return ``True`` if :term:`scipy` is installed."""
    return __HAS_SCIPY is True
