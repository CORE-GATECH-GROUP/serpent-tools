"""
Class to read and process a batch of similar detector files
"""
from collections import defaultdict
import warnings

from numpy import empty, square, sqrt, allclose, asarray
from matplotlib import pyplot

from serpentTools.messages import SerpentToolsException
from serpentTools.utils import magicPlotDocDecorator, formatPlot
from serpentTools.parsers.detector import DetectorReader
from serpentTools.detectors import Detector
from serpentTools.samplers.base import Sampler


class DetectorSampler(Sampler):
    """Class responsible for reading multiple detector files

    The following checks are performed to ensure that all detectors are
    of similar structure and content

        1. Each parser must have the same detectors
        2. The reshaped tally data must be of the same size for all detectors

    These tests can be skipped by settings ``<sampler.skipPrecheck>`` to be
    ``False``.

    Parameters
    ----------
    files: str or iterable
        Single file or iterable (list) of files from which to read.
        Supports file globs, ``*det0.m`` expands to all files that
        end with ``det0.m``

    Attributes
    ----------
    detectors : dict
        Dictionary of key, values pairs for detector names and corresponding
        :class:`~serpentTools.samplers.SampledDetector` instances
    files: set
        Unordered set containing full paths of unique files read
    settings: dict
        Dictionary of sampler-wide settings
    parsers: set
        Unordered set of all parsers that were successful
    map: dict
        Dictionary where key, value pairs are files and their corresponding
        parsers

    """

    def __init__(self, files):
        self.detectors = {}
        Sampler.__init__(self, files, DetectorReader)

    def __getitem__(self, name):
        """Retrieve a detector from :attr:`detectors`."""
        return self.detectors[name]

    def _precheck(self):
        self._checkParserDictKeys('detectors')
        self._checkSizes()

    def _checkSizes(self):
        sizes = None
        for parser in self.parsers:
            if sizes is None:
                sizes = {det: {} for det in parser.detectors}
            for detName, det in parser.detectors.items():
                level = sizes[detName]
                shape = det.tallies.shape
                if shape not in level:
                    level[shape] = {parser.filePath}
                else:
                    level[shape].add(parser.filePath)
        for detName, misMatches in sizes.items():
            if len(misMatches) > 1:
                self._raiseErrorMsgFromDict(misMatches, 'shape', 'detector')

    def _process(self):
        individualDetectors = defaultdict(list)
        for parser in self:
            for detName, detector in parser.iterDets():
                individualDetectors[detName].append(detector)
        for name, detList in individualDetectors.items():
            self.detectors[name] = SampledDetector.fromDetectors(
                name, detList)

    def _free(self):
        for sampledDet in self.detectors.values():
            sampledDet.free()

    def iterDets(self):
        for name, detector in self.detectors.items():
            yield name, detector


class SampledDetector(Detector):
    """Class to store aggregated detector data

    Parameters
    ----------
    name : str
        Name of the detector to be sampled
    allTallies : numpy.ndarray or iterable of arrays
        Array of tally data for each individual detector
    allErrors : numpy.ndarray or iterable of arrays
        Array of absolute tally errors for individual detectors
    indexes : iterable of string, optional
        Iterable naming the bins that correspond to reshaped
        :attr:`tally` and :attr:`errors`.
    grids : dict, optional
        Additional grid information, like spatial or energy-wise
        grid information.

    Attributes
    ----------
    name : str
        Name of this detector
    tallies : numpy.ndarray
        Average of tallies from all detectors
    errors : numpy.ndarray
        Uncertainty on :attr:`tallies` after propagating uncertainty from all
        individual detectors
    deviation : numpy.ndarray
        Deviation across all tallies
    allTallies : numpy.ndarray
        Array of tally data from sampled detectors. First dimension is the
        file index ``i``, followed by the tally array for detector ``i``.
    allErrors : numpy.ndarray
        Array of uncertainties for sampled detectors. Structure is identical
        to :attr:`allTallies`
    grids : dict or None
        Dictionary of additional grid information
    indexes : tuple or None
        Iterable naming the bins that correspond to reshaped
        :attr:`tally` and :attr:`errors`. The tuple
        ``(energy, ymesh, xmesh)`` indicates that :attr:`tallies`
        should have three dimensions corresponding to various
        energy, y-position, and x-position bins. Must be set
        after :attr:`tallies` or :attr:`errors` and agree with
        the shape of each

    See Also
    --------
    :meth:`fromDetectors`

    """

    def __init__(self, name, allTallies, allErrors, indexes=None, grids=None):
        # average tally data, propagate uncertainty
        self._allTallies = allTallies
        self._allErrors = allErrors
        tallies = self.allTallies.mean(axis=0)

        # propagate absolute uncertainty
        # assume no covariance
        inner = square(allErrors).sum(axis=0)
        errors = sqrt(inner) / allTallies.shape[0]
        nz = tallies.nonzero()
        errors[nz] /= tallies[nz]

        Detector.__init__(self, name, tallies=tallies, errors=errors,
                          grids=grids, indexes=indexes)

        self._deviation = None

    @property
    def allTallies(self):
        return self._allTallies

    @allTallies.setter
    def allTallies(self, tallies):
        if tallies is None:
            self._allTallies = None
            return

        tallies = asarray(tallies)

        if self._allTallies is None:
            self._allTallies = tallies
            return

        if tallies.shape != self._allTallies.shape:
            raise ValueError("Expected shape to be {}, is {}".format(
                self._allTallies.shape, tallies.shape))

        self._allTallies = tallies

    @property
    def allErrors(self):
        return self._allErrors

    @allErrors.setter
    def allErrors(self, errors):
        if errors is None:
            self._allErrors = None
            return

        errors = asarray(errors)

        if self._allErrors is None:
            self._allErrors = errors
            return

        if errors.shape != self._allErrors.shape:
            raise ValueError("Expected shape to be {}, is {}".format(
                self._allErrors.shape, errors.shape))

        self._allErrors = errors

    @property
    def deviation(self):
        if self._deviation is not None:
            return self._deviation
        if self.allTallies is not None:
            return self.allTallies.std(axis=0)
        return None

    @deviation.setter
    def deviation(self, dev):
        if dev is None:
            self._deviation = None
            return

        dev = asarray(dev)
        if self.deviation is not None and dev.shape != self.deviation.shape:
            raise ValueError(
                "Deviation shape should be {}, is {}".format(
                    self.deviation.shape, dev.shape))
        elif self.tallies is not None and dev.shape != self.tallies.shape:
            raise ValueError(
                "Deviation shape {} incompatible with tally shape {}"
                .format(dev.shape, self.tallies.shape))
        elif (self.allTallies is not None
              and dev.shape != self.allTallies.shape[1:]):
            raise ValueError(
                "Deviation shape {} incompatible with tally shape {}"
                .format(dev.shape, self.allTallies.shape))
        self._deviation = dev

    @magicPlotDocDecorator
    def spreadPlot(self, xdim=None, fixed=None, sampleKwargs=None,
                   meanKwargs=None, ax=None, xlabel=None,
                   ylabel=None, logx=False, logy=False, loglog=False,
                   legend=True):
        """
        Plot the mean tally value against all sampled detector data.

        Parameters
        ----------
        xdim: str
            Bin index to place on the x-axis
        fixed: None or dict
            Dictionary controlling the reduction in data down to one dimension
        sampleKwargs : dict, optional
            Additional matplotlib-acceptable arguments to be passed into the
            plot when plotting data from unique runs, e.g.
            ``{"c": k, "alpha": 0.5}``.
        meanKwargs : dict, optional
            Additional matplotlib-acceptable argumentst to be used when
            plotting the mean value, e.g. ``{"c": "b", "marker": "o"}``
        {ax}
        {xlabel}
        {ylabel}
        {logx}
        {logy}
        {loglog}
        {legend}

        Returns
        -------
        {rax}

        """
        if self.allTallies is None:
            raise AttributeError(
                "allTallies is None, cannot plot all tally data")

        samplerData = self.slice(fixed, 'tallies')
        slices = self._getSlices(fixed)
        if len(samplerData.shape) != 1:
            raise SerpentToolsException(
                'Data must be constrained to 1D, not {}'.format(
                    samplerData.shape))
        xdata, autoX = self._getPlotXData(xdim, samplerData)
        xlabel = xlabel or autoX

        if sampleKwargs is None:
            sampleKwargs = {"c": "k", "alpha": 0.5, "marker": ""}
        if meanKwargs is None:
            meanKwargs = {"c": "#0173b2", "marker": "o"}

        ax = ax or pyplot.gca()
        for data in self.allTallies:
            ax.plot(xdata, data[slices], **sampleKwargs)

        ax.plot(xdata, samplerData, label='Mean value', **meanKwargs)
        formatPlot(ax, logx=logx, logy=logy, loglog=loglog, xlabel=xlabel,
                   ylabel=ylabel, legend=legend)
        return ax

    @classmethod
    def fromDetectors(cls, name, detectors):
        """
        Create a :class:`SampledDetector` from similar detectors

        Parameters
        ----------
        name : str
            Name of this detector
        detectors : iterable of :class:`serpentTools.Detector`
            Iterable that contains detectors to be averaged. These
            should be structured identically, in shape of the tally
            data and the underlying grids and indexes.

        Returns
        -------
        SampledDetector

        Raises
        ------
        TypeError
            If something other than a :class:`serpentTools.Detector` is found
        ValueError
            If tally data are not shaped consistently
        KeyError
            If some grid or index information is missing
        AttributeError
            If one detector is missing grids entirely but grids are
            present on other grids
        """
        shape = None
        indexes = None
        grids = {}
        differentGrids = set()

        for d in detectors:
            if not isinstance(d, Detector):
                raise TypeError(
                    "All items should be Detector. Found {}".format(type(d)))

            if shape is None:
                shape = d.tallies.shape
            elif shape != d.tallies.shape:
                raise ValueError(
                    "Shapes do not agree. Found {} and {}".format(
                        shape, d.tallies.shape))

            # Inspect tally structure via indexes
            if indexes is None and d.indexes is not None:
                indexes = d.indexes
            else:
                if d.indexes != indexes:
                    raise KeyError(
                        "Detector indexes do not agree. Found {} and "
                        "{}".format(d.indexes, indexes))

            # Inspect tally structure via grids
            if d.grids and not grids:
                grids = d.grids
            elif not d.grids and grids:
                raise AttributeError(
                    "Detector {} is missing grid structure".format(d))
            elif d.grids and grids:
                for key, refGrid in grids.items():
                    thisGrid = d.grids.get(key)
                    if thisGrid is None:
                        raise KeyError(
                            "Detector {} is missing {} grid".format(d, key))
                    if not allclose(refGrid, thisGrid):
                        differentGrids.add(key)

        if differentGrids:
            warnings.warn(
                "Found some potentially different grids {}".format(
                    ", ".join(differentGrids)), RuntimeWarning)

        shape = (len(detectors), ) + shape

        allTallies = empty(shape)
        allErrors = empty(shape)

        for ix, d in enumerate(detectors):
            allTallies[ix] = d.tallies
            allErrors[ix] = d.tallies * d.errors

        return cls(name, allTallies, allErrors, indexes=indexes, grids=grids)
