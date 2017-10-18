"""Parser responsible for reading the ``*det<n>.m`` files"""
import re

import numpy
from drewtils.parsers import KeywordParser

from serpentTools.settings import messages
from serpentTools.objects.readers import BaseReader


NUM_COLS = 12
# number of columns/bins in a single detector line

__all__ = ['DetectorReader']


class DetectorReader(BaseReader):
    """
    Parser responsible for reading and working with detector files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'detector')
        self.detectors = {}
        self._detNames = self._makeDetectorNames()

    def _makeDetectorNames(self):
        names = self.settings['names'] or ['.*']
        return [re.compile(name) for name in names]

    def read(self):
        """Read the file and store the detectors."""
        keys = ['DET']
        separators = ['\n', '];']
        messages.debug('Preparing to read {}'.format(self.filePath))
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                valid = any(re.match(pattern, chunk[0])
                            for pattern in self._detNames)
                if valid:
                    self._addDetector(chunk)
        messages.debug('Done reading detector file')

    def _addDetector(self, chunk):
        detName = chunk.pop(0)
        detName = detName[:detName.index(' =')]
        detBins = numpy.empty(shape=(len(chunk), NUM_COLS))
        for indx, line in enumerate(chunk):
            detBins[indx] = [float(xx) for xx in line.split()]
        self.detectors[detName] = detBins
