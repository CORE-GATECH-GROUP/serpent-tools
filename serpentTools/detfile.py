"""Detector file implementation

Responsible for storing data from detector files
"""

from collections.abc import Mapping
import warnings

from .messages import deprecated
from .detectors import Detector
from .base import SerpentFile, getStream


__all__ = ["DetectorFile"]


class DetectorFile(SerpentFile, Mapping):
    """Class for storing detector data

    Can be treated as a :class:`dict`, mapping detector
    names to their corresponding :class:`serpentTools.Detector`
    instances. Fulfills a :class:`collections.abc.Mapping`
    interface by providing :meth:`__iter__`, :meth:`__getitem__`,
    :meth:`__setitem__`, and :meth:`__len__` methods.

    .. note::

        Only :class:`serpentTools.Detector` instances can be
        assigned as values.

    Parameters
    ----------
    detectors : Mapping[str, Detector], optional
        Initial map of detector names and
        :class:`~serpentTools.Detector` instances.

    Attributes
    ----------
    detectors : dict
        Deprecated attribute for backwards compatibility. It
        is preferable to treat instances of this class as
        a dictionary

    See Also
    --------
    :meth:`fromSerpent` - Convenience method for loading data
    directly from a detector file

    """

    def __init__(self, detectors=None):
        if detectors is None:
            self._detectors = {}
        elif not isinstance(detectors, Mapping):
            raise TypeError("Expected detectors to be Mapping, not {}".format(
                type(detectors)))
        else:
            for k, v in detectors.items():
                if not isinstance(k, str):
                    raise TypeError("Keys must be strings, not {}".format(k))
                if not isinstance(v, Detector):
                    raise TypeError("Values must be {}, not {}".format(Detector, type(v)))
            self._detectors = detectors

    def __iter__(self):
        return iter(self._detectors)

    def __getitem__(self, key):
        return self._detectors[key]

    def __setitem__(self, key, value):
        if not isinstance(value, Detector):
            raise TypeError(
                "Cannot assign {} to {} as it is not a {}".format(
                    key, type(value), Detector))
        self._detectors[key] = value

    def __len__(self):
        return len(self._detectors)

    def __repr__(self):
        return "<{} with detectors {}>".format(
            self.__class__.__name__, ", ".join(sorted(self)))

    @property
    def detectors(self):
        warnings.warn(
            "{o}.detectors is deprecated in favor of operating directly "
            "on {o} like a dictionary.".format(o=self.__class__.__name__))
        return self

    @deprecated("det.items()")
    def iterDets(self):
        return self.items()

    @classmethod
    def fromSerpent(cls, fileOrStream, names=None):
        """Process detector data and create a new DetectorFile

        If no names are given, then the current value of
        ``detector.names`` will be retrived from the
        :class:`~serpentTools.settings.rc` settings manager.
        Any value given in ``names`` will take precedence over
        existing settings.

        Parameters
        ----------
        fileOrStream : str or pathlib.Path or readable
            If a string or :class:`pathlib.Path`, open the file
            for reading and process. Otherwise, check that the
            object can be read by looking for a ``read`` and
            ``readline`` method.
        names : iterable of str, optional
            Specific names of detectors, as they appear in the output
            file, to be processed. Any detector that is found that
            does appear in ``names`` will not be stored on the
            resulting :class:`DetectorFile` object

        Returns
        -------
        DetectorFile
            Instance containing all detector data found in the stream

        """
        from serpentTools.settings import rc
        from serpentTools.parsers import DetectorReader

        detFile = cls()
        names = names or rc["detector.names"]
        reader = DetectorReader(names)

        with getStream(fileOrStream) as stream:
            for det in reader.processStream(stream):
                detFile[det.name] = det

        return detFile
