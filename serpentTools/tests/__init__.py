from os import path, remove
from shutil import copy

from serpentTools import ROOT_DIR

TEST_ROOT = path.join(ROOT_DIR, 'tests')


def copyTestFiles(test, src, numFiles):
    """
    Copy a single file into multiple files with identifiable names

    Copied file format will be ``base_test_cp{n}.ext`` for source
    file ``base.ext``. No extension -> no ``.ext`` for copied files

    Parameters
    ----------
    test: str
        Name of test
    src: str
        Path to source file. Must exist
    numFiles: int
        Number of files to generate

    Returns
    -------
    set
        Names of generated files

    Raises
    ------
    OSError
        If source file does not exist
    """
    if not path.exists(src):
        raise OSError("Source file {} does not exist".format(src))
    files = set()
    if '.' in src:
        dotIndx = src.index('.')
        base = src[:dotIndx]
        ext = src[dotIndx:]
    else:
        base = src
        ext = ''
    fileFmt = base + '_{}'.format(test) + '_cp{}' + ext
    for n in range(numFiles):
        thisF = fileFmt.format(n)
        copy(src, thisF)
        files.add(thisF)
    return files


def removeTestFiles(files):
    """Shortcut to remove files in iterable ``files``"""
    for fileP in files:
        if path.isfile(fileP):
            remove(fileP)
