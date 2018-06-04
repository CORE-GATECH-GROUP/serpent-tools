from collections import OrderedDict

from six import iteritems
from numpy import unique, array

from serpentTools.messages import warning, debug, SerpentToolsException
from serpentTools.objects.base import DetectorBase

DET_COLS = ('value', 'energy', 'universe', 'cell', 'material', 'lattice',
            'reaction', 'zmesh', 'ymesh', 'xmesh', 'tally', 'error', 'scores')
"""Name of the columns of the data"""


class Detector(DetectorBase):
    """
    Class that stores detector data from a single detector file

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    bins: numpy.ndarray
        Tally data directly from SERPENT file
    {attrs:s}
    """
    __doc__ = __doc__.format(params=DetectorBase.baseParams,
                             attrs=DetectorBase.baseAttrs)

    def __init__(self, name):
        DetectorBase.__init__(self, name)
        self.bins = None
        self.__reshaped = False

    def _isReshaped(self):
        return self.__reshaped

    def addTallyData(self, bins):
        """Add tally data to this detector"""
        self.__reshaped = False
        self.bins = bins
        self.reshape()

    def reshape(self):
        """
        Reshape the tally data into a multidimensional array

        This method reshapes the tally and uncertainty data into arrays
        where the array axes correspond to specific bin types.
        If a detector was set up to tally two group flux in a 5 x 5
        xy mesh, then the resulting tally data would be in a 50 x 12/13
        matrix in the original ``detN.m`` file.
        The tally data and relative error would be rebroadcasted into
        2 x 5 x 5 arrays, and the indexing information is stored in
        ``self.indexes``

        Returns
        -------
        shape: list
            Dimensionality of the resulting array

        Raises
        ------
        SerpentToolsException:
            If the bin data has not been loaded
        """
        if self.bins is None:
            raise SerpentToolsException('Tally data for detector {} has not '
                                        'been loaded'.format(self.name))
        if self.__reshaped:
            warning('Data has already been reshaped')
            return
        debug('Starting to sort tally data...')
        shape = []
        self.indexes = OrderedDict()
        for index, indexName in enumerate(DET_COLS):
            if 0 < index < 10:
                uniqueVals = unique(self.bins[:, index])
                if len(uniqueVals) > 1:
                    self.indexes[indexName] = array(uniqueVals, dtype=int) - 1
                    shape.append(len(uniqueVals))
        self.tallies = self.bins[:, 10].reshape(shape)
        self.errors = self.bins[:, 11].reshape(shape)
        if self.bins.shape[1] == 13:
            self.scores = self.bins[:, 12].reshape(shape)
        self._map = {'tallies': self.tallies, 'errors': self.errors,
                     'scores': self.scores}
        debug('Done')
        self.__reshaped = True
        return shape

class CartesianDetector(Detector):
    pass


DET_UNIQUE_GRIDS = {
    CartesianDetector: {'X', 'Y'}
}

def detectorFactory(name, dataDict):
    """
    Return a proper Detector subclass depending upon the attached grids

    Parameters
    ----------
    name: str
        Name of this specific detector.
    dataDict: dict
        Dictionary of detector data. Expects at least ``'tally'``

    Returns
    -------
    object:
        Subclass of :class:`serpentTools.objects.base.DetectorBase`
        depending on grid data passed

    Raises
    ------
    KeyError:
        If ``'tally'`` is missing from the data dictionary
    """
    tallyD = dataDict.pop('tally')
    for cls, uniqGrids in iteritems(DET_UNIQUE_GRIDS):
        if any([key in uniqGrids for key in dataDict]):
            break
    else:
        cls = CartesianDetector if 'Z' in dataDict else Detector
    det  = cls(name)
    det.addTallyData(tallyD)
    for gridK, value in iteritems(dataDict):
        det.grids[gridK] = value
    return det
