
import re
from numpy import array

class SparseCSCStreamProcessor(object):
    """
    Read through a block of text and produce sparse matrices

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
    *. :class:`scipy.sparse.csc_matrix`
    """

    def __init__(self, stream, regex, dtype=float):
        self._stream = stream
        if not (isinstance(regex, re.Pattern)):
            self._regex = re.compile(regex)
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
