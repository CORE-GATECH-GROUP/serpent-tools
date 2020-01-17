"""
Module for loading reference and example data files
"""

import os
from os.path import exists
import pathlib
from warnings import warn

from serpentTools import read

__all__ = ['readDataFile', ]


def getFile(path):
    """
    Retrieve the path to one of the reference or example files

    Relies on the environment variable ``SERPENT_TOOLS_DATA``
    to find the data files.

    Parameters
    ----------
    path : str
        The name of the file without any additional directory
        information

    Returns
    -------
    str
        Path to a data file that can be read with one of
        the readers or with :func:`serpentTools.read`

    Raises
    ------
    IOError
        If no match for ``path`` exists
    """
    datadir = os.environ.get("SERPENT_TOOLS_DATA")
    if datadir is None:
        raise EnvironmentError("""serpentTools.data functions rely on the
environment variable SERPENT_TOOLS_DATA to find data files. To use these
functions for testing and examples, set this environment variable""")
    fullPath = pathlib.Path(datadir) / path
    if not fullPath.is_file():
        raise FileNotFoundError(
            "Data file {} could not be found in {}".format(path, datadir))
    return str(fullPath)


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

    Examples
    --------

    Obtain a detector file from the examples

    >>> import serpentTools
    >>> d = serpentTools.readDataFile('bwr_det0.m')
    >>> d.detectors.keys()
    dict_keys(['spectrum', 'xymesh'])

    See Also
    --------
    * :func:`serpentTools.read`
    """
    if not exists(path):
        # assume this is a example/test file contained in this project
        filePath = getFile(path)
    else:
        warn("Please use serpentTools.read as the primary read function. "
             "readDataFile is intended for testing and example and may "
             "be changed or removed in the future.")
        filePath = path
    return read(filePath, **kwargs)
