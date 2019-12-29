from abc import ABC, abstractmethod
from contextlib import contextmanager
from pathlib import Path
import io


class SerpentFile(ABC):
    """Abstract base class for all Serpent files

    A specific subclass should be responsible for storing data from
    a specific type of file.

    """

    @classmethod
    @abstractmethod
    def fromSerpent(cls, fileOrStream, **kwargs):
        """Return a new instance based on a file or stream

        Parameters
        ----------
        fileOrStream : str or pathlib.Path or readable
            If a string or :class:`pathlb.Path`, open the file for
            reading. Otherwise check that the object can be read by
            looking for a ``read`` and ``readline`` method.
        kwargs :
            Additional key word arguments to be passed to the
            actual processing.

        Returns
        -------
        SerpentFile
            A serpent file corresponding to the data contained in
            the file or readable stream.

        """


@contextmanager
def getStream(fileOrStream):
    """Context manager for coercing an argument to a readable type

    Parameters
    ----------
    fileOrStream : str or pathlib.Path or io.TextIOBase
        If a string or :class:`pathlib.Path`, open the file
        for reading and process. Otherwise, check that the
        object can be read by looking for a ``read`` and
        ``readline`` method.

    Yields
    ------
    io.TextIOBase
        Some readable stream that will produce either the file
        contents, in the case of string or :class:`pathlib.Path`
        arguments, or the original input stream
    """
    close = True
    if isinstance(fileOrStream, Path):
        stream = fileOrStream.open("r")
    elif isinstance(fileOrStream, str):
        stream = open(fileOrStream, "r")
    elif not isinstance(fileOrStream, io.TextIOBase):
        raise TypeError("{} does not appear to be a readable object "
                        "or file path".format(type(fileOrStream)))
    else:
        stream = fileOrStream
        close = False
    try:
        yield stream
    finally:
        if close:
            stream.close()
