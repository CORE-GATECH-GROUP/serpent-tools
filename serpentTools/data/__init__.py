"""
Module for loading reference and example data files
"""

from os.path import join, exists
from warnings import warn

from serpentTools import __path__, read

_DATA_ROOT = join(__path__[0], 'data')

__all__ = ['readDataFile', ]


def getFile(path):
    """
    Retrieve the path to one of the reference or example files

    Parameters
    ----------
    path: str
        The name of the file without any additional directory
        information

    Returns
    -------
    str:
        Path to a data file that can be read with one of
        the readers or with :func:`serpentTools.read`

    Raises
    ------
    IOError:
        If no match for ``path`` exists
    """
    fullPath = join(_DATA_ROOT, path)
    if not exists(fullPath):
        raise IOError("File matching {} does not exist".format(path))
    return fullPath


def readDataFile(path, **kwargs):
    """
    Return a reader for the data file (test or example) file.

    All additional keyword arguments will be passed to
    :func:`serpentTools.read`.

    Parameters
    ----------
    path: str
        The name of the file without any additional directory
        information

    Returns
    -------
    object
        The reader that has processed this file and stored
        all the data

    Raises
    ------
    IOError:
        If the file for ``path`` does not exist

    See Also
    --------
    * :func:`serpentTools.read`
    """
    if not exists(path):
        # assume this is a example/test file contained in this project
        filePath = getFile(path)
    else:
        _warnDataFilePurpose()
        filePath = path
    return read(filePath, **kwargs)


def _warnDataFilePurpose():
    """
    Issue a warning indicating that readDataFile is not primary read function.
    """
    warn("Please use serpentTools.read as the primary read function. "
         "readDataFile is intended for testing and example and may "
         "be changed or removed in the future.", UserWarning)
