"""Classes for storing material data."""

import numpy
from matplotlib import pyplot

from serpentTools.settings import messages
from serpentTools.objects import NamedObject


class DepletedMaterial(NamedObject):
    """
    Class for storing material data from ``_dep.m`` files.

    Parameters
    ----------
    parser: :py:class:`~serpentTools.parsers.depletion.DepletionReader`
        Parser that found this material.
        Used to obtain file metadata like isotope names and burnup
    name: str
        Name of this material

    Attributes
    ----------
    zai: numpy.array or None
        Isotope id's
    names: numpy.array or None
        Names of isotopes
    days: numpy.array or None
        Days overwhich the material was depleted
    adens: numpy.array or None
        Atomic density over time for each nuclide
    mdens: numpy.array or None
        Mass density over time for each nuclide
    burnup: numpy.array or None
        Burnup of the material over time

    """

    def __init__(self, parser, name):
        NamedObject.__init__(self, parser, name)
        self.data = {}
        self.zai = parser.metadata.get('zai', None)
        self.names = parser.metadata.get('names', None)
        self.days = parser.metadata.get('days', None)
        self.__burnup__ = None
        self.__adens__ = None
        self.__mdens__ = None

        # a series of dictionaries that define material composition over time
        # from ZAID to density value, and knowledge of one
        # variable can inform the other through the getIsoMass
        # function.
        self.data['adensDicts'] = []
        self.data['mdensDicts'] = []

    def __getitem__(self, item):
        if item not in self.data:
            raise KeyError('Key {} not found on material {}'
                           .format(item, self.name))
        return self.data[item]

    @property
    def burnup(self):
        if 'burnup' not in self.data:
            raise AttributeError('Burnup for material {} has not been loaded'
                                 .format(self.name))
        if self.__burnup__ is None:
            self.__burnup__ = self.data['burnup']
        return self.__burnup__

    @property
    def adens(self):
        if 'adens' not in self.data:
            raise AttributeError('Atomic densities for material {} have not '
                                 'been loaded'.format(self.name))
        if self.__adens__ is None:
            self.__adens__ = self.data['adens']
        return self.__adens__

    @property
    def mdens(self):
        if 'mdens' not in self.data:
            raise AttributeError('Mass densities for material {} has not been '
                                 'loaded'.format(self.name))
        if self.__mdens__ is None:
            self.__mdens__ = self.data['mdens']
        return self.__mdens__

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
        newName = self._convertVariableName(variable)
        messages.debug('Adding {} data to {}'.format(newName, self.name))
        if isinstance(rawData, str):
            scratch = [float(item) for item in rawData.split()]
        else:
            scratch = []
            for line in rawData:
                if line:
                    scratch.append([float(item) for item in line.split()])
        self.data[newName] = numpy.array(scratch)

    @messages.depreciated
    def getXY(self, xUnits, yUnits, timePoints=None, names=None):
        """Deprecated. Use getValues instead"""
        if timePoints is None:
            timePoints = self.days
            return self.getValues(xUnits, yUnits, timePoints, names), self.days
        else:
            return self.getValues(xUnits, yUnits, timePoints, names)

    def getValues(self, xUnits, yUnits, timePoints=None, names=None):
        """
        Return x values for given time, and corresponding isotope values.

        Parameters
        ----------
        xUnits: str
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'burnup'``
        timePoints: list or None
            If given, select the time points according to those specified here.
            Otherwise, select all points
        names: list or None
            If given, return y values corresponding to these isotope names.
            Otherwise, return values for all isotopes.

        Returns
        -------
        numpy.array
            Array of values.

        Raises
        ------
        AttributeError
            If the names of the isotopes have not been obtained and specific
            isotopes have been requested
        KeyError
            If at least one of the days requested is not present
        """
        if timePoints is not None:
            timeCheck = self._checkTimePoints(xUnits, timePoints)
            if any(timeCheck):
                raise KeyError('The following times were not present in file {}'
                               '\n{}'.format(self.origin,
                                             ', '.join(timeCheck)))
        if names and self.names is None:
            raise AttributeError(
                'Isotope names not stored on DepletedMaterial {}.'
                .format(self.name))
        xVals, colIndices = self._getXSlice(xUnits, timePoints)
        rowIndices = self._getIsoID(names)
        allY = self.data[yUnits]
        if allY.shape[0] == 1 or len(allY.shape) == 1:  # vector
            yVals = allY[colIndices] if colIndices else allY
        else:
            yVals = numpy.empty((len(rowIndices), len(xVals)), dtype=float)
            for isoID, rowId in enumerate(rowIndices):
                yVals[isoID, :] = (allY[rowId][colIndices] if colIndices
                                   else allY[rowId][:])
        return yVals

    def _checkTimePoints(self, xUnits, timePoints):
        valid = self.days if xUnits == 'days' else self.data[xUnits]
        badPoints = [str(time) for time in timePoints if time not in valid]
        return badPoints

    def _getXSlice(self, xUnits, timePoints):
        allX = self.days if xUnits == 'days' else self.data[xUnits]
        if timePoints is not None:
            colIndices = [indx for indx, xx in enumerate(allX)
                          if xx in timePoints]
            xVals = allX[colIndices]
        else:
            colIndices = None
            xVals = allX
        return xVals, colIndices

    def _getIsoID(self, isotopes):
        """Return the row indices that correspond to specfic isotopes."""
        # TODO: List comprehension to make rowIDs then return array
        if not isotopes:
            return numpy.array(list(range(len(self.names))), dtype=int)
        isoList = [isotopes] if isinstance(isotopes, (str, int)) else isotopes
        rowIDs = numpy.empty_like(isoList, dtype=int)
        for indx, isotope in enumerate(isoList):
            rowIDs[indx] = self.names.index(isotope)
        return rowIDs

    def plot(self, xUnits, yUnits, timePoints=None, names=None, ax=None):
        """
        Plot some data as a function of time for some or all isotopes.

        Parameters
        ----------
        xUnits: str
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'burnup'``
        timePoints: list or None
            If given, select the time points according to those
            specified here. Otherwise, select all points
        names: list or None
            If given, return y values corresponding to these isotope
            names. Otherwise, return values for all isotopes.
        ax: None or ``matplotlib axes``
            If given, add the data to this plot.
            Otherwise, create a new plot

        Returns
        -------
        ``matplotlib axes``
            Axes corresponding to the figure that was plotted

        See Also
        --------
        getXY

        """
        xVals = timePoints or self.days
        yVals = self.getValues(xUnits, yUnits, xVals, names)
        ax = ax or pyplot.axes()
        labels = names or ['']
        for row in range(yVals.shape[0]):
            ax.plot(xVals, yVals[row], label=labels[row])
        return ax
