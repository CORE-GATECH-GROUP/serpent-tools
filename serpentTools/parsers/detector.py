"""Parser responsible for reading the ``*det<n>.m`` files"""

from six import iteritems
from numpy import empty

from serpentTools.utils import str2vec
from serpentTools.utils.compare import getKeyMatchingShapes
from serpentTools.engines import KeywordParser
from serpentTools.objects.detectors import detectorFactory
from serpentTools.parsers.base import BaseReader
from serpentTools.messages import error, debug, warning, SerpentToolsException
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
        and their respective :class:`~serpentTools.objects.detector.Detector`
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

    def __getitem__(self, name):
        """Retrieve a detector from :attr:`detectors`"""
        return self.detectors[name]

    def iterDets(self):
        """Yield name, detector pairs by iterating over :attr:`detectors`."""
        for name, detector in iteritems(self.detectors):
            yield name, detector

    def _read(self):
        """Read the file and store the detectors."""
        recentName = None
        lenRecent = 0
        recentGrids = {}
        keys = ['DET']
        separators = ['\n', '];']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                name, data = cleanDetChunk(chunk)
                if recentName is None or name[:lenRecent] != recentName:
                    if recentName is not None:
                        self.__processDet(recentName, recentGrids)
                    recentName = name
                    lenRecent = len(name)
                    recentGrids = {'tally': data}
                    continue
                gridName = name[lenRecent:]
                recentGrids[gridName] = data
            self.__processDet(recentName, recentGrids)

    def __processDet(self, name, grids):
        """Add this detector with it's grid data to the reader."""
        if not self._loadAll and name in self.settings['names']:
            debug("Skipping detector {} due to setting <detector.names>"
                  .format(name))
            return
        if name in self.detectors:
            raise KeyError("Detector {} already stored on reader"
                           .format(name))
        self.detectors[name] = detectorFactory(name, grids)

    def _precheck(self):
        """ Count how many detectors are in the file."""
        with open(self.filePath) as fh:
            for line in fh:
                sline = line.split()
                if not sline:
                    continue
                if 'DET' in sline[0]:
                    return
        error("No detectors found in {}".format(self.filePath))

    def _postcheck(self):
        if not self.detectors:
            warning("No detectors stored from file {}".format(self.filePath))

    def _compare(self, other, lower, upper, sigma):
        """Compare two detector readers."""
        similar = len(self.detectors) == len(other.detectors)

        commonKeys = getKeyMatchingShapes(self.detectors, other.detectors,
                                          'detectors')
        similar &= len(commonKeys) == len(self.detectors)

        for detName in sorted(commonKeys):
            myDetector = self[detName]
            otherDetector = other[detName]
            similar &= myDetector.compare(otherDetector, lower, upper, sigma)
        return similar


def cleanDetChunk(chunk):
    """
    Return the name of the detector [grid] and the array of data.

    Parameters
    ----------
    chunk: list
        Chunk of text from the output file pertaining to this section.
        Should begin with ``DET<name>[<grid>] = [`` with
        array data on the subsequent lines

    Returns
    -------
    str:
        Name of the detector including grid characters
    numpy.ndarray:
        Array containing numeric data from the chunk

    Raises
    ------
    SerpentToolsException:
        If the name of the detector could not be determined
    """
    if chunk[0][:3] != 'DET':
        raise SerpentToolsException(
            "Could not determine name of detector from chunk: {}"
            .format(chunk[0]))
    leader = chunk.pop(0)
    name = leader.split()[0][3:]
    if chunk[-1][:2] == '];':
        chunk.pop(-1)
    nCols = len(chunk[0].split())
    data = empty((len(chunk), nCols), order='F')
    for indx, row in enumerate(chunk):
        data[indx] = str2vec(row)
    return name, data
