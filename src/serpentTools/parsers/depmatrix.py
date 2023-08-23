"""
Improved processing of depletion matrix files
"""
import re

from numpy import empty, empty_like, longfloat, zeros

from serpentTools.parsers.base import BaseReader, SparseReaderMixin
from serpentTools.messages import SerpentToolsException
from serpentTools.utils import magicPlotDocDecorator, formatPlot


NDENS_REGEX = re.compile(r'N\d\(\s*([\d]+).*=\s+([\d\.E\+-]+)')
# matches index and quantity for N0 and N1 vectors
ZAI_REGEX = re.compile(r'ZAI\(\s*(\d+)\).*=\s+(-?\d+)')
# matches index and name for ZAI vector
DEPMTX_REGEX = re.compile(r'A\(\s*(\d+),\s*(\d+)\)\s+=\s+([\dE\.\+-]+)')
# matches row and column index, as well as value
SIZE_REGEX = re.compile(r'A\s+=\s+zeros\((\d+),\s+(\d+)\)')


DENS_PLOT_WHAT_VALS = [
    'both', 'n0', 'n1', 'initial', 'final',
]


class DepmtxReader(BaseReader, SparseReaderMixin):
    """
    Reader for processing depletion matrix files

    Parameters
    ----------
    filePath: str
        Path to file to be read
    sparse: bool or ``None``
        Use :term:`scipy` sparse matrices if ``True``. If
        passed as ``None``, only use sparse if :term:`scipy`
        is installed

    Attributes
    ----------
    deltaT: float
        Length of depletion interval
    n0: :class:`numpy.ndarray`
        Vector of original isotopics
    zai: :class:`numpy.ndarray`
        Integer vector of isotope ZAI (zzaaai) identifiers
    depmtx: :class:`numpy.ndarray` or
        Depletion matrix for this material. Will be
        :class:`scipy.sparse.csc_matrix` if
        :term:`scipy` is installed and the sparse-engine option
        is either not specified (``None``) during :meth:`read`
        or passed as ``True``. Otherwise, will be a
        :class:`numpy.ndarray`
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

            if self.sparse:
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
        from serpentTools.parsers.base import CSCStreamProcessor

        cscProcessor = CSCStreamProcessor(
            stream, DEPMTX_REGEX, longfloat)
        line = cscProcessor.process()
        self.depmtx = csc_matrix(
            (cscProcessor.data[:, 0], cscProcessor.indices,
             cscProcessor.indptr), dtype=longfloat, shape=matrixSize)

        return line

    @magicPlotDocDecorator
    def plotDensity(self, what='both', ax=None, logx=False, logy=True,
                    loglog=None, legend=None, title=None, labels=None,
                    markers=None, xlabel=None, ylabel=None,
                    ylim=None):
        """
        Plot initial, final, or both number densities.

        Parameters
        ----------
        what: str
            Concentrations to plot.

                1. ``'both'``: plot initial and final
                2. ``'n0'`` or ``'initial'``: only initial
                3. ``'n1'`` or ``'final'``: only final
        {ax}
        {logx}
        {logy}
        {loglog}
        {legend}
        {title}
        labels: None or str or list of strings
            Labels to apply to concentration plot(s). If given, must have
            length equal to the number of quantities plotted, e.g.
            plotting both concentrations and passing a single string
            for ``labels`` is not allowed
        markers: None or str or list of strings
            Markers to apply to each plot. Must be a valid
            ``matplotlib`` marker such as ``'o'``, ``'>'``, etc.
            If given, the number of markers given must equal the
            number of quantities to plot.
        {xlabel}
        {ylabel}
        ylim: None or float or list of floats
            If a single value is given, set the lower y-axis limit to
            this value. If two values are given, set the upper and
            lower y-axis limits to this value

        Returns
        -------
        {rax}
        """
        from matplotlib.pyplot import gca
        ax = gca() if ax is None else ax
        if what == 'both':
            plotAttrs = [self.n0, self.n1]
        elif what in ['n0', 'initial']:
            plotAttrs = self.n0,
        elif what in ['n1', 'final']:
            plotAttrs = self.n1,
        else:
            raise ValueError(
                "Value of {} not understood. Please pass one of {}"
                .format(what, ' '.join(DENS_PLOT_WHAT_VALS)))

        if isinstance(labels, str):
            labels = labels,
        elif labels is None:
            if len(plotAttrs) == 2:
                labels = ('Initial', 'Final')
            else:
                labels = (None, )
        if len(labels) != len(plotAttrs):
            raise ValueError(
                "Number of labels {} not equal to number of quantities "
                "to plot {}".format(len(labels), len(plotAttrs)))

        if isinstance(markers, str):
            markers = markers,
        elif markers is None:
            markers = ['x'] if len(plotAttrs) == 1 else ['o', 'x']

        if len(markers) != len(plotAttrs):
            raise ValueError(
                "Number of markers {} not equal to number of quantities "
                "to plot {}".format(len(markers), len(plotAttrs)))

        for qty, label, marker in zip(plotAttrs, labels, markers):
            ax.plot(self.zai, qty, 'o', marker=marker, label=label)

        if ylim is not None:
            ax.set_ylim(ylim)

        ylabel = r"Atomic Density $[\#/b-cm]$" if ylabel is None else ylabel

        formatPlot(ax, legend=legend, title=title, logx=logx, logy=logy,
                   loglog=loglog,
                   xlabel="Isotope ZAI" if xlabel is None else xlabel,
                   ylabel=ylabel,
                   )
        return ax

    def _gather_matlab(self, reconvert):
        out = {'t': self.deltaT}
        if reconvert:
            out['N0'] = self.n0
            out['N1'] = self.n1
            out['ZAI'] = self.zai
        else:
            out['n0'] = self.n0
            out['n1'] = self.n1
            out['zai'] = self.zai
        if self.sparse:
            out['A'] = self.depmtx.toarray()
        else:
            out['A'] = self.depmtx
        return out


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
