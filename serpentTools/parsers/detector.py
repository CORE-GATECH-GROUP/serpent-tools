"""Parser responsible for reading the ``*det<n>.m`` files"""

from six import iteritems
from numpy import asfortranarray, empty

from serpentTools.engines import KeywordParser
from serpentTools.objects.detectors import Detector
from serpentTools.parsers.base import BaseReader
from serpentTools.messages import error, debug, warning
from serpentTools.settings import rc

class DetectorReader(BaseReader):
    """
    Parser responsible for reading and working with detector files.

    Parameters
    ----------
    filePath: str
        path to the depletion file

    Attributes
    ----------
    {attrs:s}
    """
    docAttrs = """detectors: dict
        Dictionary where key, value pairs correspond to detector names
        and their respective :class:`~serpentTools.objects.containers.Detector`
        representations."""
    __doc__ = __doc__.format(attrs=docAttrs)

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'detector')
        self.detectors = {}
        if not self.settings['names']:
            self._loadAll = True
        else:
            self._loadAll = False
        self.__numCols = 13 if rc['serpentVersion'][0] == '1' else 12

    def iterDets(self):
        for name, detector in iteritems(self.detectors):
            yield name, detector

    def _read(self):
        """Read the file and store the detectors."""
        keys = ['DET']
        separators = ['\n', '];']
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

    def _addDetector(self, chunk, detName, binType):
        if binType is None:
            data = empty(shape=(len(chunk), self.__numCols))
        else:
            data = empty(shape=(len(chunk), len(chunk[0].split())))
        for indx, line in enumerate(chunk):
            data[indx] = [float(xx) for xx in line.split()]
        if detName not in self.detectors:
            # new detector, this data is the tallies
            detector = Detector(detName)
            detector.addTallyData(data)
            self.detectors[detName] = detector
            debug('Adding detector {}'.format(detName))
            return
        # detector has already been defined, this must be a mesh
        detector = self.detectors[detName]
        detector.grids[binType] = asfortranarray(data)
        debug('Added bin data {} to detector {}'
              .format(binType, detName))

    def _precheck(self):
        """ Count how many detectors are in the file."""
        with open(self.filePath) as fh:
            for line in fh:
                sline = line.split()
                if not sline:
                    continue
                elif 'DET' in sline[0]:
                    return
        error("No detectors found in {}".format(self.filePath))

    def _postcheck(self):
        if not self.detectors:
            warning("No detectors stored from file {}".format(self.filePath))
