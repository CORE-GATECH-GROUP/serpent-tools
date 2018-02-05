"""
Class to read and process a batch of similar detector files
"""
from six import iteritems

from serpentTools.messages import SerpentToolsException
from serpentTools.parsers.detector import DetectorReader
from serpentTools.objects.containers import Detector
from serpentTools.samplers import Sampler


class DetectorSampler(Sampler):

    def __init__(self, files):
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
            raise SerpentToolsException(msg)

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
                raise SerpentToolsException(msg)

    def process(self):
        pass


def _makeErrorMsgFromDict(misMatches, header):
    msg = 'Files do not contain a consistent set of detectors\n'
    msg += header + ': number of files'
    for key, values in iteritems(misMatches):
        numMismatch = values if isinstance(values, int) else len(values)
        msg += '\n{}: {}'.format(key, numMismatch)
    return msg


if __name__ == '__main__':
    from shutil import copy
    from serpentTools.settings import rc
    rc.setValue('verbosity', 'warning')

    for xx in range(10):
        copy('../../examples/bwr_det0.m', 'demo_{}_det.m'.format(xx))
    s = DetectorSampler('*det.m')
    for p in s.parsers:
        print(p.detectors.keys())
