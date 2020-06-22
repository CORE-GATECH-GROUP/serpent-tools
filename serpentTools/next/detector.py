import io
import pathlib
from collections.abc import Iterable
from warnings import warn

from serpentTools.messages import SerpentToolsException
from serpentTools.detectors import Detector, detectorFactory
from serpentTools.parsers.detector import cleanDetChunk

from ._engines import KeywordParser
from .base import SerpentFile


__all__ = ["DetectorFile", "DetectorReader"]


class DetectorFile(dict, SerpentFile):
    """Dictionary-like storage of detectors

    Inherits from :class:`dict`, but enforces that all
    values are :class:`~serpentTools.Detector` or subclasses. Therefore
    the following are allowed

    .. code::

        d.get(name, default=None)
        for k, v in d.items():
            pass
        det = d[name]
        det = d.pop(name)

    Parameters
    ----------
    args : iterable of key-value pairs or dictionary, optional
        Pre-defined iterable of detectors. Can either be an existing
        dictionary of the form ``{name: detector}``, or an iterable
        of the form ``[[name, detector], ...]``
    filename : str, optional
        Helpful identifier for the source of this data, e.g. file name
    kwargs :
        Additional way to pass detectors to the instance with
        ```DetectorFile(..., xy=<Detector>, spectrum=<Detector>)``

    Attributes
    ----------
    filename : str or None
        Identifier for the source of this data, e.g. a file name.
        A value of ``None`` indicates the filename was not passed

    See Also
    --------
    :meth:`DetectorFile.fromSerpent`

    """

    def __init__(self, *args, filename=None, **kwargs):
        dict.__init__(self)
        SerpentFile.__init__(self, filename=filename)
        self.update(*args, **kwargs)

    def __setitem__(self, key, value):
        """D[key] = :class:`~serpentTools.Detector`"""
        if not isinstance(value, Detector):
            raise TypeError(
                "Values must be {}, not {}".format(Detector, type(value))
            )
        super().__setitem__(key, value)

    def __repr__(self):
        msg = "{}{}\n{}".format(
            type(self),
            " from {}".format(self.filename) if self.filename else "",
            dict.__repr__(self),
        )
        return msg

    def update(self, *args, **kwargs):
        """Update with another mapping of detectors

        Arguments can be another :class:`DetectorFile`,
        dictionary of ``{key: <Detector>}``,
        or iterable ``[[key, <Detector>]]`` much like the
        formats expected by the constructor.
        """
        other = dict(*args, **kwargs)
        for key, value in other.items():
            if not isinstance(value, Detector):
                raise TypeError(
                    "Values must be {}, not {} for key {}".format(
                        Detector, type(value), key
                    )
                )
        super().update(other)

    @classmethod
    def fromSerpent(
        cls, source, sourcename=None, postcheck=True, strict=True, names=None,
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
        names : str or iterable of str, optional
            Names of detectors that, if found, will be processed.
            Detectors not found in ``names`` will not be included
            in the returned object

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
        return super().fromSerpent(
            source,
            sourcename=sourcename,
            postcheck=postcheck,
            strict=strict,
            names=names,
        )

    @classmethod
    def _fromSerpentStream(
        cls, stream, sourcename, postcheck, strict, names=None
    ):
        return DetectorReader(names=names).readTextStream(
            stream, sourcename=sourcename, postcheck=postcheck, strict=strict,
        )


class DetectorReader:
    """Class for reading Serpent detector files

    Creating one of these manually may not always
    be necessary. However, it can be useful if repeated
    files are to be read, as a fresh reader is created
    for each call to :meth:`DetectorFile.fromSerpent`.

    Parameters
    ----------
    names : str or iterable of str, optional
        Initial names of detectors to add to :attr:`names`

    Attributes
    ----------
    names : set of str
        Names of detectors that, if found when reading,
        should be processed. Any other detectors will not
        be processed and stored

    """

    # Update this if new detector grids are introduced
    _KNOWN_GRIDS = ("E", "X", "Y", "Z", "T", "COORD", "R", "PHI", "THETA")

    def __init__(self, names=None):
        self.names = set()
        if names is not None:
            if isinstance(names, str):
                self.names.add(names)
            elif isinstance(names, Iterable):
                self.names.update(names)
            else:
                raise TypeError(
                    "Names provided to {} must be string or iterable of string, "
                    "not {}".format(type(self), type(names))
                )

    def read(self, source, sourcename=None, postcheck=True, strict=True):
        """Process detectors from a Serpent output file

        Parameters
        ----------
        source : str or pathlib.Path or io.IOBase
            Filenames can be provided as strings or
            :class:`pathlib.Path`s and will be opened accordingly.
            Otherwise read directly from this argument
        sourcename : str, optional
            Additional descriptor of the data source. If not provided,
            and ``source`` is a string or :class:`pathlib.Path`, use
            the name of the file
        postcheck : bool, optional
            Check if any detectors have been found after reading.
            Default: True
        strict : bool, optional
            Raise errors if no detectors are found during post-read
            check. Otherwise warn if none are found. Default : True

        Returns
        -------
        DetectorFile
            Mapping of detector names and their corresponding instances.

        Raises
        ------
        SerpentToolsException
            If ``postcheck`` and ``strict`` and no detectors were found

        Warns
        -----
        UserWarning
            if ``postcheck`` and not ``strict`` and no detectors were found

        """
        if isinstance(source, str):
            with open(source, mode="r") as stream:
                return self.readTextStream(
                    stream,
                    sourcename or source,
                    postcheck=postcheck,
                    strict=strict,
                )
        elif isinstance(source, pathlib.Path):
            with source.open(mode="r") as stream:
                return self.readTextStream(
                    stream,
                    sourcename or str(source),
                    postcheck=postcheck,
                    strict=strict,
                )
        elif isinstance(source, io.BufferedIOBase):
            return self.readTextStream(
                io.TextIOWrapper(source),
                sourcename,
                postcheck=postcheck,
                strict=strict,
            )
        elif not isinstance(source, io.TextIOBase):
            raise TypeError(
                "Source must be file name (str or pathlib.Path) or "
                "readable stream of text data. Got {}".format(type(source))
            )
        return self.readTextStream(
            source, sourcename, postcheck=postcheck, strict=strict
        )

    def readTextStream(
        self, stream, sourcename=None, postcheck=True, strict=True
    ):
        """Process detectors from a stream of text data

        Differs from :meth:`read` as this method only handles
        readable :class:`io.TextIOBase` instances, like opened
        files. :meth:`read` relies on this method for processing
        of the file data, but handles more input types.

        Parameters
        ----------
        source : io.TextIOBase
            :meth:`~io.TextIOBase.readable` buffer of text data
            corresponding to a Serpent output file.
        sourcename : str, optional
            Additional descriptor of the data source. If not provided,
            and ``source`` is a string or :class:`pathlib.Path`, use
            the name of the file
        postcheck : bool, optional
            Check if any detectors have been found after reading.
            Default: True
        strict : bool, optional
            Raise errors if no detectors are found during post-read
            check. Otherwise warn if none are found. Default : True

        Returns
        -------
        DetectorFile
            Mapping of detector names and their corresponding instances.

        Raises
        ------
        SerpentToolsException
            If ``postcheck`` and ``strict`` and no detectors were found

        Warns
        -----
        UserWarning
            if ``postcheck`` and not ``strict`` and no detectors were found

        """
        if not isinstance(stream, io.TextIOBase):
            raise TypeError("Stream is not a source of text data")
        elif not stream.readable():
            raise AttributeError("Stream is not readable")

        detectors = self._read(stream, sourcename)

        if postcheck and not detectors:
            msg = "No detectors found in {}, named {}".format(
                repr(stream), sourcename
            )
            if self.names:
                msg += ". Processing detectors with names: {}".format(
                    ", ".join(self.names)
                )
            if strict:
                raise SerpentToolsException(msg)
            warn(msg)

        return detectors

    def _read(self, stream, name):
        currentName = ""
        grids = {}
        bins = None
        detectors = DetectorFile(filename=name)

        for chunk in KeywordParser(stream, ["DET"], ["\n", "];"]):
            name, data = self._clean(chunk)

            # Determine if this is a new detector
            if not currentName:
                isNewDetector = False
            elif not name.startswith(currentName):
                isNewDetector = True
            else:
                isNewDetector = not any(
                    name == "".join((currentName, g))
                    for g in self._KNOWN_GRIDS
                )

            if isNewDetector:
                if not self.names or currentName in self.names:
                    detectors[currentName] = self._detectorFactory(
                        currentName, bins, grids
                    )
                bins = data
                grids = {}
                currentName = name
            elif bins is None:
                currentName = name
                bins = data
            else:
                gridName = name[len(currentName):]
                grids[gridName] = data

        if not self.names or currentName in self.names:
            detectors[currentName] = self._detectorFactory(
                currentName, bins, grids
            )
        return detectors

    @staticmethod
    def _detectorFactory(name, bins, grids):
        return detectorFactory(name, bins, grids)

    @staticmethod
    def _clean(chunk):
        return cleanDetChunk(chunk)
