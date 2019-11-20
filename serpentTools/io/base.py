"""
Classes for converting readers and containers to other data types
"""

from abc import ABC, abstractmethod
from serpentTools.utils import checkScipy

__all__ = [
    'MatlabConverter',
]


class BaseConverter(ABC):
    """
    Base class for setting up conversion routines

    Each subclass should implement

    * ``checkContainerReq`` for checking if the container is
      capable of writing
    * ``checkImports`` for checking if the user has the required
      libraries required, at required versions
    """

    def __init__(self, container, output):
        self.checkContainerReq(container)
        self.checkImports()
        self.container = container
        self.output = output

    def checkContainerReq(self, container):
        """Ensure that the requirements to convert are met"""
        pass

    def checkImports(self):
        """Ensure that any required libraries are included"""
        pass

    @abstractmethod
    def convert(self, *args, **kwargs):
        """Perform the conversion"""
        raise NotImplementedError


class MatlabConverter(BaseConverter):
    """
    Class for assisting in writing container data to MATLAB

    Parameters
    ----------
    obj: ``serpentTools`` container
        Parser or container to be written to file
    fileP: str or file-like object
        Name of the file to write

    See Also
    --------
    * :func:`serpentTools.io.toMatlab` - high level function for
      writing to MATLAB that uses this class
    """

    def checkContainerReq(self, container):
        """Ensure that data from the container can be collected."""
        if not hasattr(container, '_gather_matlab'):
            raise NotImplementedError(
                "Gathering method not implemented for {}."
                .format(container.__class__.__name__))

    def checkImports(self):
        """Ensure that :term:`scipy` >= 1.0 is installed."""
        if not checkScipy('1.0'):
            raise ImportError("scipy >= 1.0 required")

    def convert(self, reconvert, append=True, format='5', longNames=True,
                compress=True, oned='row'):
        """
        Save contents of object to ``.mat`` file

        Parameters
        ----------
        fileP: str or file-like object
            Name of the file to write
        reconvert: bool
            If this evaluates to true, convert values back into their
            original form as they appear in the output file, e.g.
            ``MAT_TOTAL_ING_TOX``. Otherwise, maintain the ``mixedCase``
            style, ``total_ingTox``.
        append: bool
            If true and a file exists under ``output``, append to that file.
            Otherwise the file will be overwritten
        format: {'5', '4'}
            Format of file to write. ``'5'`` for MATLAB 5 to 7.2, ``'4'`` for
            MATLAB 4
        longNames: bool
            If true, allow variable names to reach 63 characters,
            which works with MATLAB 7.6+. Otherwise, maximum length is
            31 characters
        compress: bool
            If true, compress matrices on write
        oned: {'row', 'col'}:
            Write one-dimensional arrays as row vectors if
            ``oned=='row'`` (default), or column vectors

        See Also
        --------
        :func:`scipy.io.savemat`
        """
        from scipy.io import savemat
        data = self.container._gather_matlab(reconvert)
        return savemat(self.output, data, append, format, longNames,
                       compress, oned)
