"""
Classes for converting readers and containers to other data types
"""

from abc import ABCMeta, abstractmethod
from six import add_metaclass
from serpentTools.utils import checkScipy

__all__ = [
    'MatlabConverter',
    'converterRegistry',
]


converterRegistry = {}

def registerConverter(key):
    """Decorator for registering a converter for a file type"""
    def inner(convClass):
        """register this under key"""
        if key in converterRegistry:
            raise ValueError(
                "File type {} supported with {}. Please differentiate"
                .format(key, converterRegister[key].__name__))
        converterRegistry[key] = convClass
        return convClass
    return inner


@add_metaclass(ABCMeta)
class BaseConverter(object):
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


@registerConverter('mat')
class MatlabConverter(BaseConverter):
    """
    Take a container and write its contents to a ``.mat`` file
    """

    def checkContainerReq(self, container):
        if not hasattr(container, '_gather'):
            raise NotImplementedError(
                "Gathering method not implemented for {}."
                .format(container.__class__.__name__))

    def checkImports(self):
        """Ensure we have scipy"""
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
        metadata: bool or str or list of strings
            If this evaluates to true, then write all metadata to the
            file as well.
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
        data = self.container._gather(reconvert)
        return savemat(self.output, data, append, format, longNames,
                       compress, oned)
