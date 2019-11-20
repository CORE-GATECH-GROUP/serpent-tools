"""Parser responsible for reading the ``*det<n>.m`` files"""

from warnings import warn
from numpy import empty

from serpentTools.utils import str2vec
from serpentTools.utils.compare import getKeyMatchingShapes
from serpentTools.engines import KeywordParser
from serpentTools.detectors import detectorFactory
from serpentTools.parsers.base import BaseReader
from serpentTools.messages import SerpentToolsException


# After py2 removal, subclass this from collections.abc.Mapping
# Gain full dictionary-like behavior by defining a few methods
class DetectorReader(BaseReader):
    """
    Parser responsible for reading and working with detector files.

    Parameters
    ----------
    filePath: str
        path to the depletion file

    Attributes
    ----------
    detectors : dict
        Dictionary where key, value pairs correspond to detector names
        and their respective :class:`~serpentTools.objects.detector.Detector`
        instances
    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'detector')
        self.detectors = {}

    def __getitem__(self, name):
        """Retrieve a detector from :attr:`detectors`"""
        return self.detectors[name]

    def __len__(self):
        return len(self.detectors)

    def __contains__(self, key):
        return key in self.detectors

    def __iter__(self):
        return iter(self.detectors)

    def iterDets(self):
        """Yield name, detector pairs by iterating over :attr:`detectors`."""
        for key, det in self.detectors.items():
            yield key, det

    def _read(self):
        """Read the file and store the detectors."""
        currentName = ""
        grids = {}
        bins = None
        with KeywordParser(self.filePath, ["DET"], ["\n", "];"]) as parser:
            for chunk in parser.yieldChunks():
                name, data = cleanDetChunk(chunk)
                if currentName and name[:len(currentName)] != currentName:
                    self._processDet(currentName, bins, grids)
                    bins = data
                    grids = {}
                    currentName = name
                elif bins is None:
                    currentName = name
                    bins = data
                else:
                    gridName = name[len(currentName):]
                    grids[gridName] = data
            self._processDet(currentName, bins, grids)

    def _processDet(self, name, bins, grids):
        """Add this detector with it's grid data to the reader."""
        if self.settings['names'] and name not in self.settings['names']:
            return
        if name in self.detectors:
            raise KeyError("Detector {} already stored on reader"
                           .format(name))
        self.detectors[name] = detectorFactory(name, bins, grids)

    def _precheck(self):
        """ Count how many detectors are in the file."""
        with open(self.filePath) as fh:
            for line in fh:
                sline = line.split()
                if not sline:
                    continue
                if 'DET' in sline[0]:
                    return
        warn("No detectors in pre-checking {}".format(self.filePath))

    def _postcheck(self):
        if not self.detectors:
            warn("No detectors stored from file {}".format(self.filePath))

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

    def _gather_matlab(self, reconvert):
        """Collect data from all detectors for exporting to matlab"""
        data = {}

        for det in self.detectors.values():
            data.update(det._gather_matlab(reconvert))

        return data


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
