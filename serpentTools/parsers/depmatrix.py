"""
Improved processing of depletion matrix files
"""
import re
from six.moves import range

from numpy import empty, empty_like, longfloat, zeros

from serpentTools.parsers.base import BaseReader, SparseReaderMixin
from serpentTools.messages import SerpentToolsException


NDENS_REGEX = re.compile(r'N\d\(\s*([\d]+).*=\s+([\d\.E\+-]+)')
# matches index and quantity for N0 and N1 vectors
ZAI_REGEX = re.compile(r'ZAI\(\s*(\d+)\).*=\s+(-?\d+)')
# matches index and name for ZAI vector
DEPMTX_REGEX = re.compile(r'A\(\s*(\d+),\s*(\d+)\)\s+=\s+([\dE\.\+-]+)')
# matches row and column index, as well as value
SIZE_REGEX = re.compile(r'A\s+=\s+zeros\((\d+),\s+(\d+)\)')


class DepmtxReader(BaseReader, SparseReaderMixin):
    """
    Reader for processing depletion matrix files

    Attributes
    ----------
    deltaT: float
        Length of depletion interval
    n0: :class:`numpy.ndarray`
        Vector of original isotopics
    zai: :class:`numpy.ndarray`
        Integer vector of isotope ZAI (zzaaai) identifiers
    depmtx: :class:`numpy.ndarray` or :class:`scipy.sparse.csc_matrix`
        Depletion matrix for this material. Will be sparse if
        ``scipy`` is installed and the sparse-engine option
        is either not specified (``None``) during :meth:`read`
        or passed as ``True``.
    n1: :class:`numpy.ndarray`
        Vector for isotopics after depletion
    """

    def __init__(self, filePath, sparse=None):
        BaseReader.__init__(self, filePath, 'depmtx')
        SparseReaderMixin.__init__(self, sparse)
        self.deltaT = None
        self.n0 = None
        self.n1 = None
        self.zai = None
        self.depmtx = None

    @property
    def sparse(self):
        return SparseReaderMixin.checkSparse(self)

    def _precheck(self):
        with open(self.filePath) as stream:
            line = stream.readline().strip()
        if line[:4] != 't = ':
            raise SerpentToolsException(
                "File does not appear to be a depmtx file")

    def _postcheck(self):
        pass

    def _getMatch(self, line, regex, desc):
        match = regex.search(line)
        if match is not None:
            return match
        raise SerpentToolsException(
            "Depmtx reader failed to match {} from {}:\n{}"
            .format(desc, self.filePath, line))

    def _read(self):
        tempN0 = {}
        with open(self.filePath) as stream:
            line = stream.readline()
            self.deltaT = float(line.split()[-1][:-1])

            # process initial isotopics
            line = stream.readline()
            match = self._getMatch(line, NDENS_REGEX, 'n0 vector')
            line = _parseIsoBlock(stream, tempN0, match, line, NDENS_REGEX)
            numIso = len(tempN0)
            self.n0 = empty(numIso, dtype=longfloat)
            for index in range(numIso):
                self.n0[index] = tempN0.pop(index)

            self.n1 = empty_like(self.n0)
            self.zai = empty_like(self.n0, dtype=int)

            match = self._getMatch(line, ZAI_REGEX, 'zai vector')
            line = _parseIsoBlock(stream, self.zai, match, line, ZAI_REGEX)

            match = self._getMatch(line, SIZE_REGEX, 'matrix size')
            matrixSize = [int(xx) for xx in match.groups()]

            if self.__sparse:
                line = self.__processSparseMatrix(stream, matrixSize)
            else:
                line = self.__processDenseMatrix(stream, matrixSize)

            match = self._getMatch(line, NDENS_REGEX, 'n1 vector')
            _parseIsoBlock(stream, self.n1, match, line, NDENS_REGEX)

    def __processDenseMatrix(self, stream, matrixSize):
        self.depmtx = zeros(matrixSize, dtype=longfloat)
        line = stream.readline()
        match = self._getMatch(line, DEPMTX_REGEX, 'depletion matrix')
        while match:
            row, col = [int(xx) - 1 for xx in match.groups()[:2]]
            value = longfloat(match.groups()[2])
            self.depmtx[row, col] = longfloat(value)
            line = stream.readline()
            match = DEPMTX_REGEX.search(line)
        return line

    def __processSparseMatrix(self, stream, matrixSize):
        from scipy.sparse import csc_matrix
        from serpentTools.parsers.sparseReader import SparseCSCStreamProcessor

        cscProcessor = SparseCSCStreamProcessor(
            stream, DEPMTX_REGEX, longfloat)
        line = cscProcessor.process()
        self.depmtx = csc_matrix(
            (cscProcessor.data[:, 0], cscProcessor.indices,
             cscProcessor.indptr), dtype=longfloat, shape=matrixSize)

        return line


def _parseIsoBlock(stream, storage, match, line, regex):
    """Read through the N0, N1 block and add data to storage"""
    while match:
        vals = match.groups()
        indx = int(vals[0])
        ndens = float(vals[1])
        storage[indx - 1] = ndens
        line = stream.readline()
        match = re.match(regex, line)
    return line


def readDepmtx(filePath, sparse=True):
    """
    Simple entry point to obtain data from depletion matrix files

    Parameters
    ----------
    filePath: str
        Path of file to be read
    sparse: bool
        If this is ``True``, attempt to construct a sparse depletion matrix,
        rather than a dense matrix. Requires ``scipy``. If ``scipy`` is not
        installed, a full matrix will be returned

    Returns
    -------
    dt: float
        Length of depletion interval
    n0: :class:`numpy.ndarray`
        1D vector of initial isotopics. Ordered according to ``zai`` vector
    zai: :class:`numpy.ndarray`
        1D vector of ``ZZAAAI`` isotope identifiers
    A: :class:`numpy.ndarray` or :class:`scipy.sparse.csc_matrix`
        Depletion matrix governing decay/production of isotopics. Will be
        a sparse matrix if ``sparse`` was passed as ``True`` and ``scipy``
        is installed.
    n1: :class:`numpy.ndarray`
        1D vector of isotopics after depletion event.
    """
    reader = DepmtxReader(filePath, sparse=sparse)
    reader.read()
    return (
        reader.deltaT,
        reader.n0,
        reader.zai,
        reader.depmtx,
        reader.n1,
    )
