"""Parser responsible for reading the ``*det<n>.m`` files"""

from numpy import empty

from serpentTools.utils import str2vec
from serpentTools.utils.compare import getKeyMatchingShapes
from serpentTools.engines import KeywordParser
from serpentTools.detectors import detectorFactory


class DetectorReader:
    """
    Parser responsible for reading and working with detector files.

    Parameters
    ----------
    names : iterable of str, optional
        Names of detectors to be saved, exactly as they appear in the
        output file. If not given, all detectors will be stored

    Attributes
    ----------
    names : set of str
        Names of detectors to be processed. If empty, all detectors
        will be processed

    """

    def __init__(self, names=None):
        self.names = set(names) if names else set()

    def processStream(self, stream):
        """Process the contents of an output file

        :attr:`names` is used to filter out detectors. If
        not-empty and the name of a detector does not appear
        in the list, the data is not processed.

        Parameters
        ----------
        stream : io.TextIOBase
            Readable buffer such as an opened file to be read.

        Yields
        ------
        Detector
            Each detector found in the file

        """
        currentName = ""
        grids = {}
        bins = None
        parser = KeywordParser(stream, ["DET"], ["\n", "];"])
        for chunk in parser:
            name, data = self._cleanDetChunk(chunk)
            if currentName and name[:len(currentName)] != currentName:
                det = self._processDet(currentName, bins, grids)
                if det is not None:
                    yield det
                bins = data
                grids = {}
                currentName = name
            elif bins is None:
                currentName = name
                bins = data
            else:
                gridName = name[len(currentName):]
                grids[gridName] = data
            det = self._processDet(currentName, bins, grids)
            if det is not None:
                yield det

    @staticmethod
    def _cleanDetChunk(chunk):
        """
        Return the name of the detector [grid] and the array of data.

        Parameters
        ----------
        chunk : list
            Chunk of text from the output file pertaining to this section.
            Should begin with ``DET<name>[<grid>] = [`` with
            array data on the subsequent lines

        Returns
        -------
        str
            Name of the detector including grid characters
        numpy.ndarray
            Array containing numeric data from the chunk

        Raises
        ------
        ValueError
            If the name of the detector could not be determined
        """
        if chunk[0][:3] != 'DET':
            raise ValueError(
                "Could not determine name of detector from chunk: {}"
                .format(chunk[0]))
        name = chunk[0].split()[0][3:]
        if chunk[-1][:2] == '];':
            chunk.pop()
        nCols = len(chunk[1].split())
        data = empty((len(chunk[1:]), nCols), order='F')
        for indx, row in enumerate(chunk[1:]):
            data[indx] = str2vec(row)
        return name, data

    def _processDet(self, name, bins, grids):
        """Add this detector with it's grid data to the reader."""
        if self.names and name not in self.names:
            return
        return detectorFactory(name, bins, grids)

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

