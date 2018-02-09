"""
Class to read and process a batch of similar detector files
"""
from six import iteritems

from numpy import empty, empty_like, square, sqrt, sum, where

from serpentTools.messages import (MismatchedContainersError, warning,
                                   SamplerError)
from serpentTools.parsers.detector import DetectorReader
from serpentTools.objects.containers import DetectorBase
from serpentTools.samplers import Sampler


class DetectorSampler(Sampler):

    def __init__(self, files):
        self.detectors = {}
        Sampler.__init__(self, files, DetectorReader)

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
                self.detectors[detName].loadFromDetector(detector)
        for _detName, sampledDet in self.iterDets():
            sampledDet.finalize()
            sampledDet.free()

    def iterDets(self):
        for name, detector in iteritems(self.detectors):
            yield name, detector


class SampledDetector(DetectorBase):
    """
    Class to store aggregated detector data

    Parameters
    ----------
    name: str
        Name of this detector
    numFiles: int
        Number of files that have been/will be read

    Attributes
    ----------
    grids: dict
        Dictionary with additional data describing energy grids or mesh points
    tallies: None or numpy.array
        Tally data averaged over all detector files
    errors: None or numpy.array
        Relative error in tally data data
    scores: None or numpy.array
        Reshaped array of tally scores. SERPENT 1 only
    indexes: None or OrderedDict
        Collection of unique indexes for each requested bin
    """

    def __init__(self, name, numFiles):
        DetectorBase.__init__(self, name)
        self.N = numFiles
        self._allTallies = None
        self._allErrors = None
        self._allScores = None
        self.__index = 0
        self.__shape = None

    def _isReshaped(self):
        return True

    def loadFromDetector(self, detector):
        """
        Load data from a detector

        Parameters
        ----------
        detector

        Returns
        -------

        """
        if self.__index == self.N:
            raise SamplerError("SampledDetector {} has already loaded {} "
                               "detectors and cannot exceed this bound"
                               .format(self.name, self.N))
        if detector.name != self.name:
            warning("Attempting to read from detector with dissimilar names: "
                    "Base: {}, incoming: {}".format(self.name, detector.name))
        if not self.__index:
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
        self.__index += 1

    def __allocate(self, scoreFlag):
        self._allTallies = empty(self.__shape)
        self._allErrors = empty_like(self._allTallies)
        if scoreFlag:
            self._allScores = empty_like(self._allTallies)

    def free(self):
        self._allTallies = self._allScores = self._allErrors = None

    def __load(self, tallies, errors, scores, oName):
        index = self.__index
        otherHasScores = scores is not None
        selfHasScores = self._allScores is not None
        if otherHasScores and selfHasScores:
            self._allScores[index, ...] = scores
        elif otherHasScores and not selfHasScores:
            warning("Incoming detector {} has score data, while base does "
                    "not. Skipping score data".format(oName))
        elif not otherHasScores and selfHasScores:
            raise MismatchedContainersError(
                "Incoming detector {} does not have score data, while base "
                "does.".format(oName)
            )
        self._allTallies[index] = tallies
        self._allErrors[index] = tallies * errors

    def finalize(self):
        if self._allTallies is None:
            raise SamplerError(
                "Detector data has not been loaded and cannot be processed")
        N = self.__index
        if N != self.N:
            warning("Only {} of {} detectors have been loaded.".format(
                N, self.N))

        self.tallies = self._allTallies[:N].mean(axis=0)
        self.__computeErrors(N)

        self.scores = (self._allScores[:N].mean(
            axis=0) if self._allScores is not None else None)
        self._map = {'tallies': self.tallies, 'errors': self.errors,
                     'scores': self.scores}

    def __computeErrors(self, N):
        nonZeroT = where(self.tallies > 0)
        zeroIndx = where(self.tallies == 0)
        self.errors = sqrt(sum(square(self._allErrors), axis=0)) / N
        self.errors[nonZeroT] /= self.tallies[nonZeroT]
        self.errors[zeroIndx] = 0
