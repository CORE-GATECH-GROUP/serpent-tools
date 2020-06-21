import io
import pathlib
from abc import ABC, abstractclassmethod


class SerpentFile(ABC):
    """Most basic interface for a Serpent file

    Parameters
    ----------
    filename : str, optional
        Helpful identifier for the source of data

    Attributes
    ----------
    filename : str or None
        Name of the source of data

    """

    def __init__(self, filename=None):
        self.filename = filename

    @classmethod
    def fromSerpent(
        cls, source, sourcename=None, postcheck=True, strict=True, **kwargs
    ):
        """
        Load data from a Serpent output file

        Parameters
        ----------
        source : str or pathlib.Path or io.IOBase
            Source of Serpent output data. File names can be passed
            as either strings or :class:`pathlib.Path`s. Otherwise,
            source must be readable, e.g. support ``source.read`` and
            ``source.readline``
        sourcename : str, optional
            Alternative identifier for the source. If not provided
            and ``source`` is a string or :class:`pathlib.Path`,
            the name will reflect the name of the file
        postcheck : bool, optional
            Perform simple checks after the file has been processed.
            Default is to perform the check
        strict : bool, optional
            If simple checks fail during post-check routines,
            raise an error if ``True`` or a warning. Default is to
            raise an error
        kwargs :
            Additional keyword arguments will be passed directly to
            the concrete stream reader, implemented by each subclass.

        Returns
        -------
        SerpentFile
            Specific subclass corresponding to the file type

        Raises
        ------
        serpentTools.SerpentToolsException
            If ``postcheck``, a check fails, and ``strict``

        Warns
        -----
        UserWarning
            If ``postcheck``, a check fails, and not ``strict``

        """
        if isinstance(source, str):
            with open(source, mode="r") as stream:
                return cls._fromSerpentStream(
                    stream, sourcename or source, postcheck, strict, **kwargs
                )
        elif isinstance(source, pathlib.Path):
            with source.open(mode="r") as stream:
                return cls._fromSerpentStream(
                    stream,
                    sourcename or str(source),
                    postcheck,
                    strict,
                    **kwargs,
                )
        # Special case for binary data, e.g. zip files
        elif isinstance(source, io.BufferedIOBase):
            return cls._fromSerpentStream(
                io.TextIOWrapper(source),
                sourcename,
                postcheck,
                strict,
                **kwargs,
            )
        elif not isinstance(source, io.IOBase):
            raise TypeError(
                "Source must be string or pathlib.Path for file names, or a "
                "readable IO stream. Got {}".format(type(source))
            )
        return cls._fromSerpentStream(
            source, sourcename, postcheck, strict, **kwargs
        )

    @abstractclassmethod
    def _fromSerpentStream(
        cls, source, sourcename, postcheck, strict, **kwargs
    ):
        """Process a stream of Serpent text data.

        Source will be an :class:`io.TextIOBase`, which supports at
        least ``source.read`` and ``source.readline``. Seeking
        with ``source.seek`` might not be available in all
        cases, but can be checked with ``source.seekable``

        Other arguments correspond with their intent in
        :meth:`fromSerpent`

        """
