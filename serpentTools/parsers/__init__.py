"""Package dedicated for reading ``SERPENT`` output files"""
from os import path
import re

import six

from numpy import zeros, empty, empty_like, array, longfloat

try:
    from scipy.sparse import csc_matrix

    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    csr_matrix = array

from serpentTools.settings.messages import warning, SerpentToolsException, info
from serpentTools.parsers.depletion import DepletionReader
from serpentTools.parsers.branching import BranchingReader
from serpentTools.parsers.detector import DetectorReader
from serpentTools.parsers.bumat import BumatReader
from serpentTools.parsers.results import ResultsReader
from serpentTools.parsers.fissionMatrix import FissionMatrixReader

READERS = {
    'dep': DepletionReader,
    'branch': BranchingReader,
    'det': DetectorReader,
    'results': ResultsReader,
    'fission': FissionMatrixReader,
    'bumat': BumatReader
}

REGEXES = {
    r'(.*_dep\.m)': DepletionReader,
    r'(.*\.coe)': BranchingReader,
    r'(.*_det\d+\.m)': DetectorReader,
    r'(.*_res\.m)': ResultsReader,
    r'(.*_fmtx\d+\.m)': FissionMatrixReader,
    r'(.*\.bumat\d+)': BumatReader
}

__all__ = ['READERS', 'read', 'depmtx', 'inferReader', 'REGEXES']

for key in READERS:
    __all__.append(READERS[key])


def inferReader(filePath):
    """
    Attempt to infer the correct reader type.

    Parameters
    ----------
    filePath: str
        File to be read.

    Raises
    ------
    SerpentToolsException
        If a reader cannot be inferred
    """
    for reg, reader in six.iteritems(REGEXES):
        match = re.match(reg, filePath)
        if match and match.group() == filePath:
            info('Inferred reader for {}: {}'.format(filePath, reader.__name__))
            return reader
    raise SerpentToolsException(
        'Failed to infer filetype and thus accurate reader from'
        'file path {}'.format(filePath)
    )


def read(filePath, reader='infer'):
    """
    Simple entry point to read a file and obtain the processed reader.

    .. note::

        If you know the type of reader you will be using,
        it is best to either pass in the string argument,
        or directly use the appropriate reader class


    Parameters
    ----------
    filePath: str
        Path to the file to be reader
    reader: str or callable
        Type of reader to use. If a string is given, then
        the actions described below will happen. If callable,
        then that function will be used with the file
        path as the first argument.

    =============== ==========================================
    String argument Action
    =============== ==========================================
    infer           Infer the correct reader based on the file
    dep             ``DepletionReader``
    branch          ``BranchingReader``
    det             ``DetectorReader``
    results         ``ResultsReader``
    bumat           ``BumatReader``
    fission         ``FissionMatrixReader``
    =============== ==========================================

    Returns
    -------
    serpentTools.objects.readers.BaseReader
        Correct subclass corresponding to the file type

    Raises
    ------
    AttributeError
        If the object created by the reader through
        ``reader(filePath)`` does not have a ``read`` method.
    SerpentToolsException
        If the reader could not be inferred or if the requested
        reader string is not supported
    NotImplementedError
        This has the ability to load in readers that may not be
        complete, and thus the ``read`` method may raise
        this error.
    """
    if isinstance(reader, str):
        if reader == 'infer':
            loader = inferReader(filePath)
        else:
            if reader in READERS:
                loader = READERS[reader]
            else:
                raise SerpentToolsException(
                    'Reader type {} not supported'.format(reader)
                )
    else:
        assert callable(reader), 'Reader {} is not callable'.format(str(reader))
        loader = reader
    returnedFromLoader = loader(filePath)
    returnedFromLoader.read()
    return returnedFromLoader


def depmtx(fileP):
    """
    Read the contents of the ``depmtx`` file and return contents

    Parameters
    ----------
    fileP: str
        Path to depletion matrix file

    Returns
    -------
    t: float
        Length of time
    n0: numpy.ndarray
        Initial isotopic vector
    zai: numpy.array
        String identifiers for each isotope in ``n0`` and ``n1``
    a: numpy.array or scipy.sparse.csc_matrix
        Decay matrix. Will be sparse if scipy is installed
    n1: numpy.array
        Final isotopic vector
    """
    if not path.exists(fileP):
        raise IOError('Cannot find depeletion matrix file {}'.format(fileP))
    if not HAS_SCIPY:
        warning('Decay matrix will be returned as full matrix')
    with open(fileP) as f:
        t = float(f.readline().split()[-1][:-1])
        line = f.readline()
        numIso = 0
        n0Storage = {}
        while line[0] == 'N':
            numIso += 1
            vals = line.split()
            indx = int(vals[1][:-1])
            ndens = float(vals[4][:-1])
            n0Storage[indx - 1] = ndens
            line = f.readline()
        n0 = empty((numIso, 1), dtype=longfloat)
        for indx, v in n0Storage.items():
            n0[indx] = v
        zai = []
        while line[0] == 'Z':
            zai.append(line[12:-2])
            line = f.readline()

        line = f.readline()
        a = zeros((numIso, numIso), dtype=longfloat)

        while line[0] == 'A':
            vals = line.split()
            pos = [int(xx[:-1]) for xx in vals[1:3]]
            c = float(vals[-1][:-1])
            a[pos[0] - 1, pos[1] - 1] = c
            line = f.readline()
        n1 = empty_like(n0)
        while line and line[0] == 'N':
            vals = line.split()
            indx = int(vals[1][:-1])
            ndens = float(vals[4][:-1])
            n1[indx - 1] = ndens
            indx += 1
            line = f.readline()

        return t, n0, array(zai), csc_matrix(a) if HAS_SCIPY else a, n1
