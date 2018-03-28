"""
Package dedicated for reading ``SERPENT`` output files

The :py:func:`serpentTools.parsers.read` function uses
the following string arguments to infer the type of reader
to be used.


"""
from os import path
import re

import six

from numpy import zeros, empty, empty_like, array, longfloat

try:
    from scipy.sparse import csc_matrix

    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    csc_matrix = array

from serpentTools.messages import warning, SerpentToolsException, info, debug
from serpentTools.parsers.depletion import DepletionReader
from serpentTools.parsers.branching import BranchingReader
from serpentTools.parsers.detector import DetectorReader
from serpentTools.parsers.bumat import BumatReader
from serpentTools.parsers.results import ResultsReader
from serpentTools.parsers.fissionMatrix import FissionMatrixReader
from serpentTools.parsers.history import HistoryReader

READERS = {
    'dep': DepletionReader,
    'branch': BranchingReader,
    'det': DetectorReader,
    'results': ResultsReader,
    'fission': FissionMatrixReader,
    'bumat': BumatReader,
    'history': HistoryReader
}

REGEXES = {
    r'(.*_dep\.m)': DepletionReader,
    r'(.*\.coe)': BranchingReader,
    r'(.*_det\d+\.m)': DetectorReader,
    r'(.*_res\.m)': ResultsReader,
    r'(.*_fmtx\d+\.m)': FissionMatrixReader,
    r'(.*\.bumat\d+)': BumatReader,
    r'(.*_his\d+\.m)': HistoryReader
}

__all__ = ['READERS', 'read', 'depmtx', 'inferReader', 'REGEXES',
           'DepletionReader', 'BranchingReader', 'DetectorReader',
           'BumatReader', 'ResultsReader', 'FissionMatrixReader']


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
            info('Inferred reader for {}: {}'
                 .format(filePath, reader.__name__))
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
        assert callable(reader), (
                'Reader {} is not callable'.format(str(reader)))
        loader = reader
    returnedFromLoader = loader(filePath)
    returnedFromLoader.read()
    return returnedFromLoader


def depmtx(fileP):
    """
    Read the contents of the ``depmtx`` file and return contents

    .. note::

        If ``scipy`` is not installed, matrix ``A`` will be full.
        This can cause some warnings or errors if sparse or
        non-sparse solvers are used.

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

    tRegex = re.compile(r't\s+=\s+([\d\.E\+-]+)')
    nDensRegex = re.compile(r'N\d\(\s*([\d]+).*=\s+([\d\.E\+-]+)')
    # matches index and quantity for N0 and N1 vectors
    zaiRegex = re.compile(r'ZAI\(\s*[\d]+\).*=\s+(-?\d+)')
    # matches index and name for ZAI vector
    matrixRegex = re.compile(r'A\(\s*(\d+),\s*(\d+)\)\s+=\s+([\dE\.\+-]+)')
    # matrix row, column, and decay constant for A matrix
    failMsg = 'File {} is ill-formed for depmtx reader\nLine: '.format(fileP)

    if not HAS_SCIPY:
        warning('Decay matrix will be returned as full matrix')

    with open(fileP) as f:
        line = f.readline()
        tMatch = re.match(tRegex, line)
        if not tMatch:
            raise SerpentToolsException(failMsg + line)
        t = float(tMatch.groups()[0])
        line = f.readline()

        nMatch = re.match(nDensRegex, line)
        if not nMatch:
            raise SerpentToolsException(failMsg + line)

        n0Storage, line, numIso = _parseIsoBlock(f, {}, nMatch, line,
                                                 nDensRegex)
        debug('Found {} isotopes for file {}'.format(numIso, fileP))
        n0 = empty((numIso, 1), dtype=longfloat)
        for indx, v in six.iteritems(n0Storage):
            n0[indx] = v

        zai = []
        zMatch = re.match(zaiRegex, line)
        if not zMatch:
            raise SerpentToolsException(failMsg + line)
        while zMatch:
            zai.append(zMatch.groups()[0])
            line = f.readline()
            zMatch = re.match(zaiRegex, line)

        if len(zai) != n0.size:
            debug('Stopping at line -' + line)
            raise SerpentToolsException(
                'Did not obtain equal isotopes in ZAI vector [{}] as in N0 '
                'vector [{}]'.format(len(zai), n0.size)
            )

        line = f.readline()
        aMatch = re.match(matrixRegex, line)
        if not aMatch:
            raise SerpentToolsException(failMsg + line)

        a = zeros((numIso, numIso), dtype=longfloat)

        while aMatch:
            row, col, const = aMatch.groups()
            a[int(row) - 1, int(col) - 1] = float(const)
            line = f.readline()
            aMatch = re.match(matrixRegex, line)

        n1 = empty_like(n0)
        nMatch = re.match(nDensRegex, line)
        n1, line, items = _parseIsoBlock(f, n1, nMatch, line, nDensRegex)
        if items != numIso:
            debug('Stopping at line -' + line)
            raise SerpentToolsException(
                'Did not obtain equal isotopes in N1 vector [{}] as in N0 '
                'vector [{}]'.format(items, numIso)
            )

        return t, n0, array(zai), csc_matrix(a) if HAS_SCIPY else a, n1


def _parseIsoBlock(stream, storage, match, line, regex):
    """Read through the N0, N1 block and add data to storage"""
    items = 0
    while match:
        items += 1
        vals = match.groups()
        indx = int(vals[0])
        ndens = float(vals[1])
        storage[indx - 1] = ndens
        line = stream.readline()
        match = re.match(regex, line)
    return storage, line, items
