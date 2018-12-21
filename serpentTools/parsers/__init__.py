"""
Package dedicated for reading ``SERPENT`` output files
"""
import re

import six

from serpentTools.messages import SerpentToolsException, debug, deprecated
from serpentTools.parsers.depletion import DepletionReader
from serpentTools.parsers.branching import BranchingReader
from serpentTools.parsers.detector import DetectorReader
from serpentTools.parsers.bumat import BumatReader
from serpentTools.parsers.results import ResultsReader
from serpentTools.parsers.fissionMatrix import FissionMatrixReader
from serpentTools.parsers.history import HistoryReader
from serpentTools.parsers.xsplot import XSPlotReader
from serpentTools.parsers.sensitivity import SensitivityReader
from serpentTools.parsers.microxs import MicroXSReader
from serpentTools.parsers.depmatrix import DepmtxReader, readDepmtx

READERS = {
    'dep': DepletionReader,
    'branch': BranchingReader,
    'det': DetectorReader,
    'results': ResultsReader,
    'fission': FissionMatrixReader,
    'bumat': BumatReader,
    'history': HistoryReader,
    'xsplot': XSPlotReader,
    'sensitivity': SensitivityReader,
    'microxs': MicroXSReader,
    'depmtx': DepmtxReader,
}

SUPPORTED_READER_MSG = "\n".join(
    ["{}: {}".format(key, READERS[key].__name__)
     for key in sorted(READERS.keys())]
)

REGEXES = {
    r'(.*_dep\.m)': DepletionReader,
    r'(.*\.coe)': BranchingReader,
    r'(.*_det\d+\.m)': DetectorReader,
    r'(.*_res\.m)': ResultsReader,
    r'(.*_fmtx\d+\.m)': FissionMatrixReader,
    r'(.*\.bumat\d+)': BumatReader,
    r'(.*_his\d+\.m)': HistoryReader,
    r'(.*_xs\d*\.m)': XSPlotReader,
    r'(.*_sens\d*.m)': SensitivityReader,
    r'(.*_mdx\d+\.m)': MicroXSReader,
    r'(.*depmtx_.*\.m)': DepmtxReader,
}

__all__ = ['read',
           'DepletionReader', 'BranchingReader', 'DetectorReader',
           'BumatReader', 'ResultsReader', 'FissionMatrixReader',
           'MicroXSReader',
           'DepmtxReader',
           'depmtx',
           'readDepmtx',
           ]


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
            debug('Inferred reader for {}: {}'
                  .format(filePath, reader.__name__))
            return reader
    raise SerpentToolsException(
        'Failed to infer filetype and thus accurate reader from'
        'file path {}. Pass one of the below options to ensure '
        'a specific reader:\n{}'.format(filePath, SUPPORTED_READER_MSG)
    )


def read(filePath, reader='infer'):
    """
    Simple entry point to read a file and obtain the processed reader.

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
        branch          ``BranchingReader``
        bumat           ``BumatReader``
        dep             ``DepletionReader``
        det             ``DetectorReader``
        fission         ``FissionMatrixReader``
        history         ``HistoryReader``
        microxs         ``MdxReader``
        results         ``ResultsReader``
        sensitivity     ``SensitivityReader``
        xsplot          ``XSPlotReader``
        =============== ==========================================

    Returns
    -------
    serpentTools.objects.base.BaseReader
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
                    'Reader type {} not supported. Try one of the below:\n{}'
                    .format(reader, SUPPORTED_READER_MSG)
                )
    else:
        assert callable(reader), (
            'Reader {} is not callable'.format(str(reader)))
        loader = reader
    returnedFromLoader = loader(filePath)
    returnedFromLoader.read()
    return returnedFromLoader


@deprecated("readDepmtx or DepmtxReader")
def depmtx(fileP):
    """
    Read the contents of the ``depmtx`` file and return contents

    .. deprecated:: 0.6.0
        Use either the :func:`~serpentTools.parsers.depmatrix.readDepmtx`
        or :class:`~serpentTools.parsers.depmatrix.DepmtxReader`

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
    n0: :class:`numpy.ndarray`
        Initial isotopic vector
    zai: :class:`numpy.ndarray`
        String identifiers for each isotope in ``n0`` and ``n1``
    a: :class:`numpy.ndarray` or :class:`scipy.sparse.csc_matrix`
        Decay matrix. Will be sparse if scipy is installed
    n1: :class:`numpy.ndarray`
        Final isotopic vector
    """
    t, n0, zai, a, n1 = readDepmtx(fileP)
    zai = zai.astype(str)
    n0 = n0.reshape(n0.size, 1)
    n1 = n1.reshape(n1.size, 1)
    return t, n0, zai, a, n1
