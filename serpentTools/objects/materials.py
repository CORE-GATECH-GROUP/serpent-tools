"""Classes for storing material data."""

import numpy
from matplotlib import pyplot

from serpentTools.messages import warning, debug
from serpentTools.utils import (
    magicPlotDocDecorator, formatPlot, DEPLETION_PLOT_LABELS,
    convertVariableName,
)
from serpentTools.utils.compare import (
    logDirectCompare,
    compareDictOfArrays,
)
from serpentTools.objects.base import NamedObject


class DepletedMaterialBase(NamedObject):
    docParams = """name: str
        Name of this material
    metadata: dict
        Dictionary with file metadata"""
    docAttrs = """data: dict
        dictionary that stores all variable data
    zai: list
        Isotopic ZZAAA identifiers, e.g. 93325

        .. versionchanged:: 0.5.1

            Now a list of integers, not strings

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

    def getValues(self, xUnits, yUnits, timePoints=None, names=None, zai=None):
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
        zai: str or list or None
            If given, return y values corresponding to isotopes with
            these ``ZZAAAI`` as would be present in ``self.zai``. Otherwise,
            return values for all isotopes.

            .. versionadded:: 0.5.1

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
        TypeError
            If both ``names`` and ``zai`` arguments are passed
        ValueError
            If one isotope cannot be found
        """
        if None not in (names, zai):
            raise TypeError("Cannot pass both names and zai arguments. "
                            "One must be None.")
        for attr, arg in zip(('names', 'zai'), (names, zai)):
            if arg is not None:
                if getattr(self, attr) is None:
                    raise AttributeError(
                        'Isotope {} not stored on DepletedMaterial '
                        '{}.'.format(attr, self.name))
                rowIndices = self._getRowIndices(attr, arg)
                break
        else:
            rowIndices = None
        colIndices = self._getColIndices(xUnits, timePoints)
        return self._slice(self.data[yUnits], rowIndices, colIndices)

    @staticmethod
    def _slice(data, rows, cols):
        if data.shape[0] == 1 or len(data.shape) == 1:
            yVals = data[cols]
            return data[cols]
        yVals = data[:, cols]
        if rows is None:
            return yVals
        return yVals[rows]

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

    def _getRowIndices(self, attr, isotopes):
        """
        Return indices in self.[attr] that correspond to requested isotopes
        """
        allvals = getattr(self, attr)
        isoList = [isotopes] if isinstance(isotopes, (str, int)) else isotopes
        rowIDs = numpy.empty_like(isoList, dtype=int)
        for indx, isotope in enumerate(isoList):
            if isotope not in allvals:
                raise ValueError("Could not find isotope {} {}"
                                 .format(attr, isotope))
            rowIDs[indx] = allvals.index(isotope)
        return rowIDs

    def _formatLabel(self, labelFmt, names, zai):
        """
        Return a list of the formatted labels for a plot.

        Assumes that either names or zai is not None.
        """
        fmtr = labelFmt if labelFmt else '{iso}'
        allNames = self.names
        allZai = self.zai
        for allList, key, repl in zip(
                (allNames, allZai), ('names', 'zai'), ('{iso}', '{zai}')):
            if allList is None and repl in fmtr:
                warning("Isotope {} not stored on material and requested in "
                        "labelFmt. Check setting <depletion.metadataKeys>")
                fmtr = fmtr.replace(repl, '')
        iterator = zai if names is None else names
        lookup = allZai if names is None else allNames
        labels = []
        for item in iterator:
            index = lookup.index(item)
            iso = allNames[index] if allNames else ''
            zai = allZai[index] if allZai else ''
            labels.append(fmtr.format(mat=self.name, iso=iso, zai=zai))

        return labels

    def _compare(self, other, lower, upper, sigma):
        # look for identical isotope names and
        similar = logDirectCompare(self.names, other.names, 0, 0,
                                   'isotope names')
        similar &= logDirectCompare(self.zai, other.zai, 0, 0, 'isotope ZAI')

        # test data dictionary
        # if uncertianties exist, use those
        myUncs = self.uncertainties if hasattr(self, 'uncertainties') else {}
        otherUncs = (other.uncertainties if hasattr(other, 'uncertainties')
                     else {})
        similar &= compareDictOfArrays(
            self.data, other.data, 'data', lower=lower, upper=upper,
            sigma=sigma, u0=myUncs, u1=otherUncs, relative=False)

        return similar


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
    def plot(self, xUnits, yUnits, timePoints=None, names=None, zai=None,
             ax=None, legend=True, xlabel=None, ylabel=None, logx=False,
             logy=False, loglog=False, labelFmt=None, ncol=1, title=None,
             **kwargs):
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
            If given, plot  values corresponding to these isotope
            names. Otherwise, plot values for all isotopes.
        zai: int or list or None
            If given, plot values corresponding to these
            isotope ``ZZAAAI`` values. Otherwise, plot for all isotopes

            .. versionadded:: 0.5.1

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
        TypeError
            If both ``names`` and ``zai`` are given
        """
        if xUnits not in ('days', 'burnup'):
            raise KeyError("Plot method only uses x-axis data from <days> "
                           "and <burnup>, not {}".format(xUnits))
        xVals = timePoints if timePoints is not None else (
            self.days if xUnits == 'days' else self.burnup)
        if names is None and zai is None:
            names = self.names
            zai = self.zai if names is None else None
        else:
            if isinstance(names, str):
                names = [names, ]
            if isinstance(zai, str):
                zai = [zai, ]
        yVals = self.getValues(xUnits, yUnits, xVals, names, zai)
        ax = ax or pyplot.axes()
        labels = self._formatLabel(labelFmt, names, zai)
        for row in range(yVals.shape[0]):
            ax.plot(xVals, yVals[row], label=labels[row], **kwargs)

        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy, ncol=ncol,
                        xlabel=xlabel or DEPLETION_PLOT_LABELS[xUnits],
                        ylabel=ylabel or DEPLETION_PLOT_LABELS[yUnits],
                        title=title, legend=legend)
        return ax
