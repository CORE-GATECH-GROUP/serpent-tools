"""
Base module for readers.

Contains the abstract base class upon which all readers
are built.
"""

from abc import ABC, abstractmethod
import re
from collections.abc import Callable

from numpy import array
from serpentTools.messages import info
from serpentTools.settings import rc
from serpentTools.objects.base import BaseObject
from serpentTools.utils import checkScipy


class BaseReader(ABC, BaseObject):
    """Parent class from which all parsers will inherit.

    Parameters
    ----------
    filePath: str
        path pointing towards the file to be read
    readerSettingsLevel: str or list
        type of reader. Determines which settings to obtain
    """

    def __init__(self, filePath, readerSettingsLevel):
        self.filePath = filePath
        self.metadata = {}
        if isinstance(readerSettingsLevel, str):
            self.settings = rc.getReaderSettings(readerSettingsLevel)
        else:
            self.settings = {}
            for level in readerSettingsLevel:
                self.settings.update(rc.getReaderSettings(level))

    def __str__(self):
        return '<{} reading {}>'.format(self.__class__.__name__, self.filePath)

    def read(self):
        """The main method for reading that not only parses data, but also
        runs pre and post checks.
        """
        info("Reading {}".format(self.filePath))
        self._precheck()
        self._read()
        info("  - done")
        self._postcheck()

    @abstractmethod
    def _read(self):
        """Read the file and store the data.

        :warning:

            This read function has not been implemented yet

        """
        pass

    @abstractmethod
    def _precheck(self):
        """Pre-checking, e.g., make sure Serpent did not
        exit abnormally, or disk ran out of space while parsing.
        """
        pass

    @abstractmethod
    def _postcheck(self):
        """Make sure data looks reasonable. Could possibly check for
        negative cross sections, negative material densitites, etc (which
        can happen if using the reprocessing interface incorrectly).
        """
        pass


class MaterialReader(BaseReader):
    """Parent class for files that store materials."""

    def __init__(self, filePath, readerSettingsLevel):
        BaseReader.__init__(self, filePath, readerSettingsLevel)
        self.materials = {}


class XSReader(BaseReader):
    """Parent class for the branching and results reader"""

    def __init__(self, filePath, readerSettingsLevel):
        BaseReader.__init__(self, filePath, ['xs', readerSettingsLevel])
        self.settings['variables'] = rc.expandVariables()
        self.settings.pop('variableGroups')
        self.settings.pop('variableExtras')

    def _checkAddVariable(self, variableName):
        """Check if the data for the variable should be stored"""
        # no variables given -> get all
        if not any(self.settings['variables']):
            return True
        # explicitly named
        if variableName in self.settings['variables']:
            return True
        if (self.settings['getB1XS'] and variableName.replace('B1_', '') in
                self.settings['variables']):
            return True
        if (self.settings['getInfXS'] and variableName.replace('INF_', '') in
                self.settings['variables']):
            return True
        return False


class SparseReaderMixin(object):
    """
    Helper class for working with files containing sparse matrices

    Matrices may or may not be sparse, depending upon the value of
    ``sparse`` passed to the constructor and if :term:`scipy` is
    installed.

    Paramters
    ---------
    sparse: bool or ``None``
        Flag to store sparse matrices or full matrices.
        If ``None``, use full only if :term:`scipy` is not installed.
        Otherwise use full arrays. If ``sparse`` is ``True``, then
        sparse matrices will be used only if :term:`scipy` is installed

    Raises
    ------
    ImportError:
        If :term:`scipy` is not installed and ``sparse`` was passed as
        ``True``.
    """

    def __init__(self, sparse):
        HAS_SCIPY = checkScipy()
        if sparse is None:
            self.__sparse = HAS_SCIPY
        elif sparse is True and not HAS_SCIPY:
            raise ImportError(
                "scipy not installed and required for sparse support")
        else:
            self.__sparse = bool(sparse)

    def checkSparse(self):
        """
        Return ``True`` if the object is configured for sparse support
        """
        return self.__sparse is True


class CSCStreamProcessor(object):
    """
    Read through a block of text and produce sparse matrices

    .. note::

        Rows and columns matched by ``regex`` will be reduced
        by one prior to storage. Since we primarily interact
        with one-indexed MATLAB arrays, we need to convert
        the indices to something :term:`numpy` can properly
        understand

    Paramters
    ---------
    stream: IO stream from an opened file
        Object with a ``readline`` function that returns
        the next line of text to be read
    regex: str or compiled regular expression
        Regular expression that matches the following:

            0. Row of matrix
            1. Column of matrix
            2. Values to be added into resulting matrix.

        All values in ``match.groups()[2:]`` will be converted to
        ``datatype`` and appended into :attr:`data`. The rows and columns
        are used to populate  :attr:`indices` and :attr:`indptr` vectors
    datatype: object
        Data type of the numeric values of this matrix.

    Attributes
    ----------
    data: :class:`numpy.ndarray`
        Column matrix of all values matched by ``regex`` after first
        two positions. Each columns can be used to build a sparse
        matrix with :attr:`indices` and :attr:`indptr`
    indices: :class:`numpy.ndarray`
        CSC-format indices pointer array
    indptr: :class:`numpy.ndarray`
        CSC-format index pointer array. Row indices for column ``i`` are stored
        in ``indices[indptr[i]:indptr[i + 1]]``. Values for column ``i`` are
        stored in ``data[indptr[i]:intptr[i + 1]]``.
    line: str
        Last line read after calling :meth:`process`. Will be the first
        non-empty line that does not match the passed regular expression

    See Also
    --------
    * :class:`scipy.sparse.csc_matrix`
    """

    def __init__(self, stream, regex, dtype=float):
        self._stream = stream
        if isinstance(regex, str):
            self._regex = re.compile(regex)
        elif (
                not hasattr(regex, 'search')
                or not isinstance(regex.search, Callable)
        ):
            raise AttributeError(
                "Passed regular expression does not have search method")
        else:
            self._regex = regex
        self.dtype = dtype
        self.data = []
        self.indices = []
        self.indptr = [0, ]
        self.line = None
        self._curCol = 0
        self._colItems = 0

    def step(self):
        self.line = self._stream.readline().strip()
        return self.line

    def _processGroups(self, groups):
        row, col = [int(xx) - 1 for xx in groups[:2]]
        while col > self._curCol:
            self.__progressIndptr()
        values = tuple(self.dtype(xx) for xx in groups[2:])
        self.indices.append(row)
        self._colItems += 1
        self.data.append(values)

    def process(self):
        line = self.step()
        match = self._regex.search(line)
        self._curCol = 0
        self._colItems = 0
        while match is not None:
            self._processGroups(match.groups())
            match = self._regex.search(self.step())
        self.__wrapUp()
        return self.line

    def __progressIndptr(self):
        self.indptr.append(self.indptr[self._curCol] + self._colItems)
        self._colItems = 0
        self._curCol += 1

    def __wrapUp(self):
        self.__progressIndptr()
        del self._curCol, self._colItems
        self.data = array(self.data, order="F")
        self.indices = array(self.indices)
        self.indptr = array(self.indptr)
