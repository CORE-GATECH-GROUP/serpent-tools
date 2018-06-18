"""
Module for loading reference and example data files
"""

from os.path import join, dirname, exists, abspath

_DATA_ROOT = abspat(dirname(__file__))


def getFile(path):
    """
    Retrieve the path to one of the reference or example files

    Parameters
    ----------
    path: str
        Identifier for this file. Typically the name of the file 
        without any additional directory information

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

