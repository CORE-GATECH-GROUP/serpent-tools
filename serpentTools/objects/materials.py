"""Classes for storing material data."""

import numpy
from matplotlib import pyplot

from serpentTools.messages import warning, debug
from serpentTools.plot import magicPlotDocDecorator, formatPlot, DEPLETION_PLOT_LABELS
from serpentTools.objects import NamedObject
from serpentTools.utils import convertVariableName


class DepletedMaterialBase(NamedObject):
    docParams = """name: str
        Name of this material
    metadata: dict
        Dictionary with file metadata"""
    docAttrs = """data: dict
        dictionary that stores all variable data
    zai: list
        Isotopic ZZAAA identifiers, e.g. 93325
    names: list
        Names of isotopes, e.g. U235
    days: :py:class:`numpy.ndarray`
        Vector of total, cumulative days of burnup for the run that
        created this material
    burnup: :py:class:`numpy.ndarray`
        Vector of total, cumulative burnup [MWd/kgU] for this specific
        material
    adens: :py:class:`numpy.ndarray`
        2D array of atomic {densStruct:s}
    mdens: :py:class:`numpy.ndarray`
        2D array of mass {densStruct:s}""".format(
        densStruct="densities where where row ``j`` corresponds to isotope "
                   "``j`` and column ``i`` corresponds to time ``i``")
    docEquiv = """    While ``adens``, ``mdens``, and ``burnup`` are 
        accessible directly with ``material.adens``, all variables read in 
        from the file can be accessed through the ``data`` dictionary::

            >>> assert material.adens is material.data['adens']
            >>> assert material.adens is material['adens']
            # The three methods are equivalent"""
    __doc__ = """
    Base class for storing material data from a depleted material file

    {equiv:s}

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    {attrs:s}

    """.format(equiv=docEquiv, params=docParams, attrs=docAttrs)

    def __init__(self, name, metadata):
        NamedObject.__init__(self, name)
        self.data = {}
        self.__burnup = None
        self.__mdens = None
        self.__adens = None
        self.zai = metadata.get('zai', None)
        self.names = metadata.get('names', None)
        self.days = metadata.get('days', None)

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
        return self.data['burnup']

    @property
    def adens(self):
        if 'adens' not in self.data:
            raise AttributeError('Atomic densities for material {} have not '
                                 'been loaded'.format(self.name))
        return self.data['adens']

    @property
    def mdens(self):
        if 'mdens' not in self.data:
            raise AttributeError('Mass densities for material {} has not been '
                                 'loaded'.format(self.name))
        return self.data['mdens']

    def _getIsoID(self, isotopes):
        """Return the row indices that correspond to specfic isotopes."""
        if not isotopes:
            return numpy.array(list(range(len(self.names))), dtype=int)
        isoList = [isotopes] if isinstance(isotopes, (str, int)) else isotopes
        rowIDs = numpy.empty_like(isoList, dtype=int)
        for indx, isotope in enumerate(isoList):
            rowIDs[indx] = self.names.index(isotope)
        return rowIDs

    def getValues(self, xUnits, yUnits, timePoints=None, names=None):
        """
        Return material variable data at specified time points and isotopes

        If the quantity ``yUnits`` corresponds to a vector in the ``data``
        dictionary, e.g. ``burnup`` or ``volume``, and not something that
        varies by isotope, then ``names`` does not have to be given

        Parameters
        ----------
        xUnits: str
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'burnup'``
        timePoints: list or None
            If given, select the time points according to those specified here.
            Otherwise, select all points
        names: str or list or None
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
        if names and self.names is None:
            raise AttributeError(
                'Isotope names not stored on DepletedMaterial '
                '{}.'.format(self.name))
        colIndices = self._getColIndices(xUnits, timePoints)
        rowIndices = self._getRowIndices(names)
        return self._slice(self.data[yUnits], rowIndices, colIndices)

    @staticmethod
    def _slice(data, rows, cols):
        if data.shape[0] == 1 or len(data.shape) == 1 or rows is None:
            yVals = data[cols]
            return yVals
        return data[:, cols][rows]

    def _checkTimePoints(self, actual, requested):
        """Return a list of all requested points in time not stored."""
        badPoints = [str(time) for time in requested if time not in actual]
        if any(badPoints):
            raise KeyError(
                'The following times were not present for material {}'
                '\n{}'.format(self.name, ', '.join(badPoints)))

    def _getColIndices(self, xUnits, timePoints):
        """Return row and column indices corresponding to isotopes and times"""
        allX = self.days if xUnits == 'days' else self.data[xUnits]
        if timePoints is None:
            return numpy.arange(len(allX), dtype=int)
        self._checkTimePoints(allX, timePoints)
        colIndices = [indx for indx, xx in enumerate(allX) if xx in timePoints]
        return colIndices

    def _getRowIndices(self, isotopes):
        """
        Return the indices in ``names`` that correspond to specific isotopes.
        """
        if not isotopes:
            return numpy.arange(len(self.names), dtype=int)
        isoList = [isotopes] if isinstance(isotopes, (str, int)) else isotopes
        rowIDs = numpy.empty_like(isoList, dtype=int)
        for indx, isotope in enumerate(isoList):
            rowIDs[indx] = self.names.index(isotope)
        return rowIDs

    def _formatLabel(self, labelFmt, names):
        if isinstance(names, str):
            names = [names]
        elif names is None:
            labels = self.names
        fmtr = labelFmt if labelFmt else '{iso}'
        labels = []
        if '{zai' in fmtr and self.zai is None:
            warning('ZAI not set for material {}. Labeling plot with isotope names'
                    .format(self.name))
            zaiLookup = self.names
        else:
            zaiLookup = self.zai
        names = names or self.names
        for name in names:
            labels.append(fmtr.format(mat=self.name, iso=name,
                          zai=zaiLookup[self.names.index(name)]))

        return labels

class DepletedMaterial(DepletedMaterialBase):
    __doc__ = DepletedMaterialBase.__doc__

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
        newName = convertVariableName(variable)
        debug('Adding {} data to {}'.format(newName, self.name))
        if isinstance(rawData, str):
            scratch = [float(item) for item in rawData.split()]
        else:
            scratch = []
            for line in rawData:
                if line:
                    scratch.append([float(item) for item in line.split()])
        self.data[newName] = numpy.array(scratch)
    
    @magicPlotDocDecorator
    def plot(self, xUnits, yUnits, timePoints=None, names=None, ax=None,
             legend=True, xlabel=None, ylabel=None, logx=False, logy=False,
             loglog=False, labelFmt=None, ncol=1, title=None, **kwargs):
        """
        Plot some data as a function of time for some or all isotopes.

        .. note::

            ``kwargs`` will be passed to the plot for all isotopes.
            If ``c='r'`` is passed, to make a plot red, then data for
            all isotopes plotted will be red and potentially very confusing.

        Parameters
        ----------
        xUnits: str
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'burnup'``
        timePoints: list or None
            If given, select the time points according to those
            specified here. Otherwise, select all points
        names: str or list or None
            If given, return y values corresponding to these isotope
            names. Otherwise, return values for all isotopes.
        {ax}
        {legend}
        {xlabel} Otherwise, use ``xUnits``
        {ylabel} Otherwise, use ``yUnits``
        {logx}
        {logy}
        {loglog}
        {matLabelFmt}
        {ncol}
        {title}

        {kwargs} :py:func:`matplotlib.pyplot.plot`

        Returns
        -------
        {rax}

        See Also
        --------
        * :py:func:`~serpentTools.objects.materials.DepletedMaterial.getValues`
        * :py:func:`matplotlib.pyplot.plot`
        * :py:meth:`str.format` - used for formatting labels

        Raises
        ------
        KeyError
            If x axis units are not ``'days'`` nor ``'burnup'``
        """
        if xUnits not in ('days', 'burnup'):
            raise KeyError("Plot method only uses x-axis data from <days> "
                           "and <burnup>, not {}".format(xUnits))
        xVals = timePoints if timePoints is not None else (
            self.days if xUnits == 'days' else self.burnup)
        yVals = self.getValues(xUnits, yUnits, xVals, names)
        ax = ax or pyplot.axes()
        labels = self._formatLabel(labelFmt, names)
        for row in range(yVals.shape[0]):
            ax.plot(xVals, yVals[row], label=labels[row], **kwargs)
        
        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy, ncol=ncol,
                        xlabel=xlabel or DEPLETION_PLOT_LABELS[xUnits],
                        ylabel=ylabel or DEPLETION_PLOT_LABELS[yUnits], 
                        title=title)
        return ax

