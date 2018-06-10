"""
Module containing classes for storing detector data.

``SERPENT`` is capable of producing detectors, or tallies from MCNP,
with a variety of bin structures. These include, but are not limited to,
material regions, reaction types, energy bins, spatial meshes, and
universe bins.

The detectors contained in this module are tasked with storing such
data and proving easy access to the data, as well as the underlying
bins used to define the detector.

Detectors
---------
* :class:`~serpentTools.objects.detectors.Detector`
* :class:`~serpentTools.objects.detectors.CartesianDetector`
* :class:`~serpentTools.objects.detectors.HexagonalDetector`
* :class:`~serpentTools.objects.detectors.CylindricalDetector`
* :class:`~serpentTools.objects.detectors.SphericalDetector`
"""

from warnings import warn
from collections import OrderedDict

from six import iteritems
from numpy import unique, array

from serpentTools.utils import linkToWiki
from serpentTools.messages import warning, debug, SerpentToolsException
from serpentTools.objects.base import DetectorBase


__all__ = ['Detector', 'CartesianDetector', 'HexagonalDetector',
           'CylindricalDetector', 'SphericalDetector']


DET_COLS = ('value', 'energy', 'universe', 'cell', 'material', 'lattice',
            'reaction', 'zmesh', 'ymesh', 'xmesh', 'tally', 'error', 'scores')
"""Name of the columns of the data"""


class Detector(DetectorBase):
    docAttrs = """bins: :class:`numpy.ndarray`
        Tally data directly from ``SERPENT`` file"""
    __doc__ = """
    Class that stores data from a detector without a spatial mesh.

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    {docAttrs:s}
    {baseAttrs:s}
    """.format(params=DetectorBase.baseParams,
               docAttrs=docAttrs,
               baseAttrs=DetectorBase.baseAttrs)

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
        for index in range(1, 10):
            uniqueVals = unique(self.bins[:, index])
            if len(uniqueVals) > 1:
                indexName = self._indexName(index)
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

    def _indexName(self, indexPos):
        """Return the name of this index position"""
        if hasattr(self, '_INDEX_MAP') and indexPos in self._INDEX_MAP:
            return self._INDEX_MAP[indexPos]
        return DET_COLS[indexPos]


class CartesianDetector(Detector):
    __doc__ = """
    Class that stores detector data containing cartesian meshing.

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    {docAttrs:s}
    {baseAttrs:s}

    See Also
    --------
    {seeAlso:s}
    """.format(params=DetectorBase.baseParams, docAttrs=Detector.docAttrs,
               baseAttrs=DetectorBase.baseAttrs, seeAlso='* ' + linkToWiki(
                   'Input_syntax_manual#det_dx',
                   'Setting up a cartesian mesh detector'))
    pass


class HexagonalDetector(Detector):
    docSeeAlso = '* ' + linkToWiki('Input_syntax_manual#det_dh',
                                   'Setting up a hexagonal detector')
    docAttrs = """pitch: None or int
        Mesh size [cm]
    hexType: None or {2, 3}
        Type of hexagonal mesh.

            2. Flat face perpendicular to x-axis
            3. Flat face perpendicular to y-axis"""
    __doc__ = """
    Class that stores detecto data containing a hexagonal meshing.

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    {docAttrs:s}
    {detAttrs:s}
    {baseAttrs:s}

    See Also
    --------
    {seeAlso:s}""".format(seeAlso=docSeeAlso, docAttrs=docAttrs,
                          params=DetectorBase.baseParams,
                          detAttrs=Detector.docAttrs,
                          baseAttrs=DetectorBase.baseAttrs)

    def __init__(self, name):
        Detector.__init__(self, name)
        self.pitch = None
        self.hexType = None

    _INDEX_MAP = {
        8: 'ycoord',
        9: 'xcoord',
    }
    _NON_CART = _INDEX_MAP.values()

    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None,
                 logx=False, logy=False, loglog=False, title=None, **kwargs):
        if xdim in self._NON_CART or ydim in self._NON_CART:
            warnMeshPlot('Hexagonal', 168)
        return DetectorBase.meshPlot(self,
                                     xdim, ydim,
                                     what=what,
                                     fixed=fixed,
                                     ax=ax,
                                     cmap=cmap,
                                     logColor=logColor,
                                     xlabel=xlabel,
                                     logx=logx,
                                     logy=logy,
                                     loglog=loglog,
                                     title=title,
                                     **kwargs)

    meshPlot.__doc__ = DetectorBase.meshPlot.__doc__


class CylindricalDetector(Detector):
    docSeeAlso = "* " + linkToWiki('Input_syntax_manual#det_dn',
                                   'Setting up a curvilinear detector')
    __doc__ = """
    Class that stores detector data containing a cylindrical mesh.

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    {detAttrs:s}
    {baseAttrs:s}

    See Also
    --------
    {seeAlso:s}""".format(
        params=DetectorBase.baseParams, detAttrs=Detector.docAttrs,
        baseAttrs=DetectorBase.baseAttrs, seeAlso=docSeeAlso)

    _INDEX_MAP = {
        8: 'phi',
        9: 'rmesh'
    }

    _NON_CART = _INDEX_MAP.values()

    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None,
                 logx=False, logy=False, loglog=False, title=None, **kwargs):
        if xdim in self._NON_CART or ydim in self._NON_CART:
            warnMeshPlot('Cylindrical', 169)
        return DetectorBase.meshPlot(self,
                                     xdim, ydim,
                                     what=what,
                                     fixed=fixed,
                                     ax=ax,
                                     cmap=cmap,
                                     logColor=logColor,
                                     xlabel=xlabel,
                                     logx=logx,
                                     logy=logy,
                                     loglog=loglog,
                                     title=title,
                                     **kwargs)

    meshPlot.__doc__ = DetectorBase.meshPlot.__doc__


class SphericalDetector(Detector):
    __doc__ = """
    Class that stores detector data containing a spherical mesh.

    Paramters
    ---------
    {params:s}

    Attributes
    ----------
    {detAttrs:s}
    {baseAttrs:s}

    See Also
    --------
    {seeAlso:s}""".format(
        params=DetectorBase.baseParams, detAttrs=Detector.docAttrs,
        baseAttrs=DetectorBase.baseAttrs,
        seeAlso=CylindricalDetector.docSeeAlso)
    _INDEX_MAP = {
        7: 'theta',
        8: 'phi',
        9: 'rmesh',
    }

    _NON_CART = _INDEX_MAP.values()

    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None,
                 logx=False, logy=False, loglog=False, title=None, **kwargs):
        if xdim in self._NON_CART or ydim in self._NON_CART:
            warnMeshPlot('Spherical', 169)
        return DetectorBase.meshPlot(self,
                                     xdim, ydim,
                                     what=what,
                                     fixed=fixed,
                                     ax=ax,
                                     cmap=cmap,
                                     logColor=logColor,
                                     xlabel=xlabel,
                                     logx=logx,
                                     logy=logy,
                                     loglog=loglog,
                                     title=title,
                                     **kwargs)

    meshPlot.__doc__ = DetectorBase.meshPlot.__doc__


DET_UNIQUE_GRIDS = {
    CartesianDetector: {'X', 'Y'},
    HexagonalDetector: {"COORD"},
}


def _getDetectorType(dataDict):
    if not dataDict:
        return Detector
    for cls, uniqGrids in iteritems(DET_UNIQUE_GRIDS):
        if any([key in uniqGrids for key in dataDict]):
            return cls
    if 'R' in dataDict:
        return CylindricalDetector if 'Z' in dataDict else SphericalDetector
    return CartesianDetector if 'Z' in dataDict else Detector


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
    detCls = _getDetectorType(dataDict)
    det = detCls(name)
    det.addTallyData(tallyD)
    for gridK, value in iteritems(dataDict):
        det.grids[gridK] = value
    return det


def warnMeshPlot(plotType, ghIssue):
    msg = ("{} plotting is not fully supported yet - #{}"
           .format(plotType, ghIssue))
    warn(msg, FutureWarning)
