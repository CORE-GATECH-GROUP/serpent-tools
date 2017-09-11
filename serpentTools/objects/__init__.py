"""Objects used to support the parsing."""

import numpy
from matplotlib import pyplot


class _SupportingObject(object):
    """
    Base supporting object.

    Parameters
    ----------
    container: Some parser from :py:mod:`~serpentTools.parsers`
        Container that created this object
    name: str
        Name of this specific object, e.g. material name, detector name, etc.

    """

    def __init__(self, container, name):
        self._container = container
        self.name = name
        self._filePath = container.filePath

    def __repr__(self):
        return '<{} {} from {}>'.format(self.__class__.___name__,
                                        self.name, self._filePath)

    def __getattr__(self, item):
        """Search for the item in the containers metadata."""
        if item in self._container.metadata:
            return self._container.metadata[item]
        raise AttributeError('{} has object has not atribute \'{}\''
                             .format(self, item))

    @staticmethod
    def _convertVariableName(variable):
        """Converta a SERPENT variable to camelCase."""
        lowerSplits = [item.lower() for item in variable.split('_')]
        if len(lowerSplits) == 1:
            return lowerSplits[0]
        else:
            return lowerSplits[0] + ''.join([item.capitalize()
                                             for item in lowerSplits[1:]])


class DepletedMaterial(_SupportingObject):
    """
    Class for storing material data from ``_dep.m`` files.

    Parameters
    ----------
    parser: :py:class:`~serpentTools.parsers.depletion.DepletionReader`
        Parser that found this material.
        Used to obtain file metadata like isotope names and burnup
    name: str
        Name of this material
    """

    def __init__(self, parser, name):
        _SupportingObject.__init__(self, parser, name)
        self._varData = {}

    def __getattr__(self, item):
        """
        Allows the user to get items like ``zai`` and ``adens``
        with ``self.zai`` and ``self.adens``, respectively."""
        if item in self._varData:
            return self._varData[item]
        return _SupportingObject.__getattr__(self, item)

    def __getitem__(self, item):
        if item not in self._varData:
            if item not in self._container.metadata:
                raise KeyError('{} has no item {}'.format(self, item))
            return self._container.metadata[item]
        return self._varData[item]

    def addData(self, variable, rawData):
        """
        Add data straight from the file onto a variable.

        Parameters
        ----------
        variable: str
            Name of the variable directly from ``SERPENT``
        rawData: list
            List of strings corresponding to the raw data from the file
        """
        scratch = []
        rawData = [rawData] if isinstance(rawData, str) else rawData
        for line in rawData:
            if line:
                scratch.append([float(item) for item in line.split()])
        newName = self._convertVariableName(variable)
        self._varData[newName] = numpy.array(scratch)

    def _getXY(self, xUnits, yUnits, timePoints, isotopes):
        allX = self[xUnits]
        allY = self[yUnits]
        if timePoints:
            colIndices = numpy.where(allX == timePoints)
            xVals = allX[colIndices]
        else:
            colIndices = None
            xVals = allX
        if allY.shape[0] == 1:  # vector
            yVals = allY[colIndices] if colIndices else allY
            return xVals, yVals
        rowIndices = self._getIsoID(isotopes)
        yVals = numpy.empty((len(rowIndices), xVals.size), dtype=float)
        for yId, rowId in enumerate(rowIndices):
            yVals[yId, :] = (allY[rowId][colIndices] if colIndices
                             else allY[rowId, :])
        return xVals, yVals

    def _getIsoID(self, isotopes):
        """Return the row indices that correspond to specfic isotopes."""
        if not isotopes:
            return numpy.array(list(range(len(self.zai))), dtype=int)
        rowIDs = numpy.empty_like(isotopes, dtype=int)
        for indx, isotope in enumerate(isotopes):
            rowIDs[indx] = self.zai.index(isotope)
        return rowIDs

    def plot(self, x, y, xPoints=None, zai=None, ax=None):
        if 'zai' not in self._container.metadata:
            raise KeyError('Need zai to be processed by {} in order to make '
                           'meaningful plots.'.format(self._container))
        xVals, yVals = self._getXY(x, y, xPoints, zai)
        ax = ax or pyplot.subplots(1, 1)[1]
        labels = zai or [None]
        for row in range(yVals.shape[0]):
            ax.plot(xVals, yVals[row], label=labels[row])

        return ax
