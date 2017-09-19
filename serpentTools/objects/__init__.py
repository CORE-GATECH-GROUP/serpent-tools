"""Objects used to support the parsing."""

import numpy
from matplotlib import pyplot


class _SupportingObject(object):
    """
    Base supporting object.

    Parameters
    ----------
    container: Some parser from serpentTools.parsers
        Container that created this object
    name: str
        Name of this specific object, e.g. material name, detector name, etc.

    """

    def __init__(self, container, name):
        self._container = container
        self.name = name
        self._filePath = container.filePath

    def __repr__(self):
        return '<{} {} from {}>'.format(self.whatAmI(),
                                        self.name, self._filePath)

    def whatAmI(self):
        return type(self).__name__

    def __getattr__(self, item):
        """Search for the item in the containers metadata."""
        if item in self._container.metadata:
            return self._container.metadata[item]
        raise AttributeError('{} has object has no attribute \'{}\''
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
    """Class for storing material data from ``_dep.m`` files.

    Parameters
    ----------
    parser: :py:class:`~serpentTools.parsers.depletion.DepletionReader`
        Parser that found this material.
        Used to obtain file metadata like isotope names and burnup
    name: str
        Name of this material

    Attributes
    ----------
    zai: numpy.array
        Isotope id's
    names: numpy.array
        Names of isotopes
    days: numpy.array
        Days overwhich the material was depleted
    adens: numpy.array
        Atomic density over time for each nuclide

    :note:

        These attributes only exist if the pasers was instructed to
        read in this data. I.e. if ``readers.depletion.metadataKeys``
        does not contain ``ZAI``, then this object will not have
        the ``zai`` data.

    """

    def __init__(self, parser, name):
        _SupportingObject.__init__(self, parser, name)
        self._varData = {}

    def __getattr__(self, item):
        """
        Allows the user to get items like ``zai`` and ``adens``
        with ``self.zai`` and ``self.adens``, respectively.
        """
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
        """Add data straight from the file onto a variable.

        Parameters
        ----------
        variable: str
            Name of the variable directly from ``SERPENT``
        rawData: list
            List of strings corresponding to the raw data from the file
        """
        newName = self._convertVariableName(variable)
        if isinstance(rawData, str):
            scratch = [float(item) for item in rawData.split()]
        else:
            scratch = []
            for line in rawData:
                if line:
                    scratch.append([float(item) for item in line.split()])
        self._varData[newName] = numpy.array(scratch)

    def getXY(self, xUnits, yUnits, timePoints=None, names=None):
        """Return x values for given time, and corresponding isotope values.

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
        numpy.array
            Vector of time points only if ``timePoints`` is ``None``

        Raises
        ------
        AttributeError
            If the names of the isotopes have not been obtained and specific
            isotopes have been requested
        KeyError
            If at least one of the days requested is not present
        """
        if timePoints is not None:
            returnX = False
            timeCheck = self._checkTimePoints(xUnits, timePoints)
            if any(timeCheck):
                raise KeyError('The following times were not present in file {}'
                               '\n{}'.format(self._container.filePath,
                                             ', '.join(timeCheck)))
        else:
            returnX = True
        if names and 'names' not in self._container.metadata:
            raise AttributeError('Parser {} has not stored the isotope names.'
                                 .format(self._container))
        xVals, colIndices = self._getXSlice(xUnits, timePoints)
        rowIndices = self._getIsoID(names)
        allY = self[yUnits]
        if allY.shape[0] == 1 or len(allY.shape) == 1:  # vector
            return xVals, allY[colIndices] if colIndices else allY
        yVals = numpy.empty((len(rowIndices), len(xVals)), dtype=float)
        for isoID, rowId in enumerate(rowIndices):
            yVals[isoID, :] = (allY[rowId][colIndices] if colIndices
                               else allY[rowId][:])
        if returnX:
            return yVals, xVals
        return yVals

    def _checkTimePoints(self, xUnits, timePoints):
        valid = self[xUnits]
        badPoints = [str(time) for time in timePoints if time not in valid]
        return badPoints


    def _getXSlice(self, xUnits, timePoints):
        allX = self[xUnits]
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
        """Plot some data as a function of time for some or all isotopes.

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
        xVals, yVals = self.getXY(xUnits, yUnits, timePoints, names)
        ax = ax or pyplot.subplots(1, 1)[1]
        labels = names or [None]
        for row in range(yVals.shape[0]):
            ax.plot(xVals, yVals[row], label=labels[row])

        return ax
