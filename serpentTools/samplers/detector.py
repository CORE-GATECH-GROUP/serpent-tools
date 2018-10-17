"""
Class to read and process a batch of similar detector files
"""
from six import iteritems
from six.moves import range

from numpy import empty, empty_like, square, sqrt, sum, where
from matplotlib import pyplot

from serpentTools.messages import (MismatchedContainersError, warning,
                                   SamplerError, SerpentToolsException)
from serpentTools.utils import magicPlotDocDecorator
from serpentTools.parsers.detector import DetectorReader
from serpentTools.objects.base import DetectorBase
from serpentTools.samplers.base import (Sampler, SampledContainer,
                                        SPREAD_PLOT_KWARGS)


class DetectorSampler(Sampler):
    __doc__ = """
    Class responsible for reading multiple detector files

    The following checks are performed to ensure that all detectors are
    of similar structure and content

        1. Each parser must have the same detectors
        2. The reshaped tally data must be of the same size for all detectors

    {skip:s}

    Parameters
    ----------
    {files:s}

    Attributes
    ----------
    {detAttrs:s}
    {samplerAttrs:s}

    """.format(detAttrs=DetectorReader.docAttrs, samplerAttrs=Sampler.docAttrs,
               files=Sampler.docFiles, skip=Sampler.docSkipChecks)

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
            for detName, det in iteritems(parser.detectors):
                level = sizes[detName]
                shape = det.tallies.shape
                if shape not in level:
                    level[shape] = {parser.filePath}
                else:
                    level[shape].add(parser.filePath)
        for detName, misMatches in iteritems(sizes):
            if len(misMatches) > 1:
                self._raiseErrorMsgFromDict(misMatches, 'shape', 'detector')

    def _process(self):
        numParsers = len(self.parsers)
        for parser in self:
            for detName, detector in parser.iterDets():
                if detName not in self.detectors:
                    self.detectors[detName] = SampledDetector(detName,
                                                              numParsers)
                self.detectors[detName].loadFromContainer(detector)
        for _detName, sampledDet in self.iterDets():
            sampledDet.finalize()

    def _free(self):
        for _detName, sampledDet in self.iterDets():
            sampledDet.free()

    def iterDets(self):
        for name, detector in iteritems(self.detectors):
            yield name, detector


class SampledDetector(SampledContainer, DetectorBase):
    __doc__ = """
    Class to store aggregated detector data

    .. note ::

        :py:func:`~serpentTools.samplers.detector.SampledDetector.free`
        sets ``allTallies``, ``allErrors``, and ``allScores`` to
        ``None``. {free:s}

    Parameters
    ----------
    {detParams:s}
    numFiles: int
        Number of files that have been/will be read

    Attributes
    ----------
    {detAttrs:s}


    """.format(detAttrs=DetectorBase.baseAttrs, free=SampledContainer.docFree,
               detParams=DetectorBase.baseParams)

    def __init__(self, name, numFiles):
        SampledContainer.__init__(self, numFiles, DetectorBase)
        DetectorBase.__init__(self, name)
        self.allTallies = None
        self.allErrors = None
        self.allScores = None

    def _isReshaped(self):
        return True

    def _loadFromContainer(self, detector):
        """
        Load data from a detector

        Parameters
        ----------
        detector

        Returns
        -------

        """
        if detector.name != self.name:
            warning("Attempting to read from detector with dissimilar names: "
                    "Base: {}, incoming: {}".format(self.name, detector.name))
        if not self._index:
            self.__shape = tuple([self.N] + list(detector.tallies.shape))
            self.__allocate(detector.scores is not None)
        if self.__shape[1:] != detector.tallies.shape:
            raise MismatchedContainersError(
                "Incoming detector {} tally data shape does not match "
                "sampled shape. Base: {}, incoming: {}".format(
                    detector.name, self.__shape[1:], detector.tallies.shape))
        self.__load(detector.tallies, detector.errors, detector.scores,
                    detector.name)
        if self.indexes is None:
            self.indexes = detector.indexes
        if not self.grids:
            self.grids = detector.grids

    def __allocate(self, scoreFlag):
        self.allTallies = empty(self.__shape)
        self.allErrors = empty_like(self.allTallies)
        if scoreFlag:
            self.allScores = empty_like(self.allTallies)

    def free(self):
        self.allTallies = None
        self.allScores = None
        self.allErrors = None

    def __load(self, tallies, errors, scores, oName):
        index = self._index
        otherHasScores = scores is not None
        selfHasScores = self.allScores is not None
        if otherHasScores and selfHasScores:
            self.allScores[index, ...] = scores
        elif otherHasScores and not selfHasScores:
            warning("Incoming detector {} has score data, while base does "
                    "not. Skipping score data".format(oName))
        elif not otherHasScores and selfHasScores:
            raise MismatchedContainersError(
                "Incoming detector {} does not have score data, while base "
                "does.".format(oName)
            )
        self.allTallies[index] = tallies
        self.allErrors[index] = tallies * errors

    def _finalize(self):
        if self.allTallies is None:
            raise SamplerError(
                "Detector data has not been loaded and cannot be processed")
        N = self._index
        self.tallies = self.allTallies[:N].mean(axis=0)
        self.__computeErrors(N)

        self.scores = (self.allScores[:N].mean(
            axis=0) if self.allScores is not None else None)
        self._map = {'tallies': self.tallies, 'errors': self.errors,
                     'scores': self.scores}

    def __computeErrors(self, N):
        nonZeroT = where(self.tallies > 0)
        zeroIndx = where(self.tallies == 0)
        self.errors = sqrt(sum(square(self.allErrors), axis=0)) / N
        self.errors[nonZeroT] /= self.tallies[nonZeroT]
        self.errors[zeroIndx] = 0

    @magicPlotDocDecorator
    def spreadPlot(self, xdim=None, fixed=None, ax=None, xlabel=None,
                   ylabel=None, logx=False, logy=False, loglog=False,
                   autolegend=True):
        """
        Plot the mean tally value against all sampled detector data.

        Parameters
        ----------
        xdim: str
            Bin index to place on the x-axis
        fixed: None or dict
            Dictionary controlling the reduction in data down to one dimension
        {ax}
        {xlabel}
        {ylabel}
        {logx}
        {logy}
        {loglog}
        autolegend: bool
            If true, apply a label to this plot.

        Returns
        -------
        {rax}

        Raises
        ------
        SamplerError
            If ``allTallies`` is None, indicating this object has been
            instructed to free up data from all sampled files
        SerpentToolsException
            If data to be plotted, after applying ``fixed``, is not
            one dimensional

        """
        if self.allTallies is None:
            raise SamplerError("Data from all sampled files has been freed "
                               "and cannot be used in this plot method")
        samplerData = self.slice(fixed, 'tallies')
        slices = self._getSlices(fixed)
        if len(samplerData.shape) != 1:
            raise SerpentToolsException(
                'Data must be constrained to 1D, not {}'.format(
                    samplerData.shape))
        xdata, autoX = self._getPlotXData(xdim, samplerData)
        xlabel = xlabel or autoX
        ax = ax or pyplot.axes()
        N = self._index
        allTallies = self.allTallies.copy(order='F')
        for n in range(N):
            plotData = allTallies[n][slices]
            ax.plot(xdata, plotData, **SPREAD_PLOT_KWARGS)

        ax.plot(xdata, samplerData, label='Mean value - N={}'.format(N))
        if autolegend:
            ax.legend()
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel or "Tally Data")
        if loglog or logx:
            ax.set_xscale('log')
        if loglog or logy:
            ax.set_yscale('log')
        return ax
