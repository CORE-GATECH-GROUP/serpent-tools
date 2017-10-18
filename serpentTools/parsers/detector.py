"""Parser responsible for reading the ``*det<n>.m`` files"""

import numpy
from drewtils.parsers import KeywordParser

from serpentTools.objects.containers import Detector
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
        if not self.settings['names']:
            self._loadAll = True
        else:
            self._loadAll = False

    def read(self):
        """Read the file and store the detectors."""
        keys = ['DET']
        separators = ['\n', '];']
        messages.debug('Preparing to read {}'.format(self.filePath))
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                detString = chunk.pop(0).split(' ')[0][3:]
                if detString[:-1] in self.detectors:
                    detName = detString[:-1]
                    binType = detString[-1]
                elif detString in self.settings['names'] or self._loadAll:
                    detName = detString
                    binType = None
                else:
                    continue
                self._addDetector(chunk, detName, binType)
        messages.debug('Done reading detector file')

    def _addDetector(self, chunk, detName, binType):
        if binType is None:
            data = numpy.empty(shape=(len(chunk), NUM_COLS))
        else:
            data = numpy.empty(shape=(len(chunk), len(chunk[0].split())))
        for indx, line in enumerate(chunk):
            data[indx] = [float(xx) for xx in line.split()]
        if detName not in self.detectors:
            # new detector, this data is the tallies
            detector = Detector(self, detName)
            detector.addTallyData(data)
            self.detectors[detName] = detector
            messages.debug('Adding detector {}'.format(detName))
            return
        # detector has already been defined, this must be a mesh
        detector = self.detectors[detName]
        detector.grids[binType] = data
        messages.debug('Added bin data {} to detector {}'
                       .format(binType, detName))
