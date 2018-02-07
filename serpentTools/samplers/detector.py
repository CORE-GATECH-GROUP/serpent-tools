"""
Class to read and process a batch of similar detector files
"""
from six import iteritems

from numpy import empty, empty_like

from serpentTools.messages import (MismatchedContainersError, warning, debug,
                                   SamplerError)
from serpentTools.parsers.detector import DetectorReader
from serpentTools.objects.containers import Detector
from serpentTools.samplers import Sampler


class DetectorSampler(Sampler):

    def __init__(self, files):
        self.detectors = {}
        Sampler.__init__(self, files, DetectorReader)

    def _precheck(self):
        self._checkPresentDetectors()
        self._checkSizes()

    def _checkPresentDetectors(self):
        matches = {}
        for parser in self.parsers:
            keys = tuple(sorted(parser.detectors.keys()))
            if keys not in matches:
                matches[keys] = 1
            else:
                matches[keys] += 1
        if len(matches) > 1:
            msg = _makeErrorMsgFromDict(
                matches, 'Detectors')
            raise MismatchedContainersError(msg)

    def _checkSizes(self):
        sizes = None
        for parser in self.parsers:
            if sizes is None:
                sizes = {det: {} for det in parser.detectors}
            for detName, det in iteritems(parser.detectors):
                level = sizes[detName]
                shape = det.tallies.shape
                if shape not in level:
                    level[shape] = {parser}
                else:
                    level[shape].add(parser)
        for detName, det in iteritems(sizes):
            if len(det) > 1:
                msg = _makeErrorMsgFromDict(
                    det, '{} shape'.format(detName)
                )
                raise MismatchedContainersError(msg)

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

    def iterDets(self):
        for name, detector in iteritems(self.detectors):
            yield name, detector


def _makeErrorMsgFromDict(misMatches, header):
    msg = 'Files do not contain a consistent set of detectors\n'
    msg += header + ': number of files'
    for key, values in iteritems(misMatches):
        numMismatch = values if isinstance(values, int) else len(values)
        msg += '\n{}: {}'.format(key, numMismatch)
    return msg


class SampledDetector(Detector):

    def __init__(self, name, numFiles):
        Detector.__init__(self, name)
        self.N = numFiles
        self.__reshaped = True
        # del self.addTallyData
        # del self.reshape
        self._allTallies = None
        self._allErrors = None
        self._allScores = None
        self.__index = 0
        self.__shape = None

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
            self.__shape = (self.N, *detector.tallies.shape)
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
        self.__index += 1

    def __allocate(self, scoreFlag):
        self._allTallies = empty(self.__shape)
        self._allErrors = empty_like(self._allTallies)
        if scoreFlag:
            self._allScores = empty_like(self._allTallies)

    def __free(self):
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
        self._allTallies[index, ...] = tallies
        self._allErrors[index, ...] = tallies * errors

    def finalize(self):
        if self._allTallies is None:
            raise SamplerError(
                "Detector data has not been loaded and cannot be processed")
        warning("Double check the error propagation")
        self.tallies = self._allTallies.mean(axis=0)
        self.errors = self._allTallies.std(axis=0)
        self.scores = (self._allScores.mean(
            axis=0) if self._allScores is not None else None)
        self.__free()


if __name__ == '__main__':
    from shutil import copy
    from serpentTools.settings import rc

    rc.setValue('verbosity', 'warning')

    for xx in range(10):
        copy('../../examples/bwr_det0.m', 'demo_{}_det.m'.format(xx))
    s = DetectorSampler('*det.m')
    for p in s.parsers:
        print(p.detectors.keys())
