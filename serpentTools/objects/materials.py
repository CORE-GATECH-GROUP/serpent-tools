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

__all__ = [
    'DepletedMaterial',
]


def deprecateTimepointsWarning():
    """Warning that the use of timepoints in plots is going away"""
    from serpentTools.messages import _updateFilterAlert
    msg = ("Passing timepoints will no longer work after 0.7.0. "
           "Plots will be against all time")
    _updateFilterAlert(msg, PendingDeprecationWarning)


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

    Many of the instance attributes are shortcuts for accessing data
    in the underlying dictionary. For example, the following command
    fetch the same data::

        >>> m.data["adens"]
        >>> m["adens"]
        >>> m.adens

    With one exception: the attribute-based accessing is guaranteed to
    not raise an error if the data has not been loaded into the dictionary.
    This may be the case if a file was read using filtering settings and
    ``adens`` was not read.

    Parameters
    ----------
    name : str
        Name of this material
    metadata : dict
        Dictionary with file metadata

    Attributes
    ----------
    data : dict
        Main dictionary of arrays from the output file
    zai : list of int
        Isotopic ZZAAAI identifiers like ``922350``. Ordered like
        the rows of the data arrays
    names : list of str
        Isotope names like ``"U235"``. Ordered like the rows of the
        data arrays
    days : numpy.ndarray
        Time in days for each column in the data arrays
    burnup : numpy.ndarray or None
        Burnup vector for this specific material
    volume : numpy.ndarray or None
        Volume of this material over time
    adens : numpy.ndarray or None
        2D array of atom densities in atoms/b-cm
    mdens : numpy.ndarray or None
        2D array of mass densites in g/cm3
    activity : numpy.ndarray or None
        2D array of activities in Bq
    decayHeat : numpy.ndarray or None
        2D array of decay heats in W
    spontaneousFissionRate : numpy.ndarray or None
        2D array of spontaneous fission rate in fission per second
    photonProdRate : numpy.ndarray or None
        2D array of photon emission rate in photons per second
    ingTox : numpy.ndarray or None
        2D array of ingestion toxicity in sieverts
    inhTox : numpy.ndarray or None
        2D array of inhalation toxicity in sieverts

    """

    def __init__(self, name, metadata):
        NamedObject.__init__(self, name)
        self.data = {}
        self.zai = metadata.get('zai', None)
        self.names = metadata.get('names', None)
        self.days = metadata.get('days', None)

    def __getitem__(self, item):
        """Retrieve a value from the data dictionary"""
        return self.data[item]

    def get(self, key, default=None):
        """Retrieve a value from the dictionary, or default if not found

        Parameters
        ----------
        key : str
            Name of a quantity that may or may not exist in :attr:`data`
        default : object, optional
            Item to return if ``key`` is not found

        Returns
        -------
        object
            :class:`numpy.ndarray` if ``key`` was found, otherwise ``default``
        """
        return self.data.get(key, default)

    @property
    def burnup(self):
        return self.data.get("burnup")

    @property
    def adens(self):
        return self.data.get("adens")

    @property
    def mdens(self):
        return self.data.get("mdens")

    @property
    def volume(self):
        return self.data.get("volume")

    @property
    def activity(self):
        return self.data.get("a")

    @property
    def ingTox(self):
        return self.data.get("ingTox")

    @property
    def inhTox(self):
        return self.data.get("inhTox")

    @property
    def decayHeat(self):
        return self.data.get("h")

    @property
    def spontaneousFissionRate(self):
        return self.data.get("sf")

    @property
    def photonProdRate(self):
        return self.data.get("gsrc")

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
    """Base class for storing material data from a depleted material file

    Many of the instance attributes are shortcuts for accessing data
    in the underlying dictionary. For example, the following command
    fetch the same data::

        >>> m.data["adens"]
        >>> m["adens"]
        >>> m.adens

    With one exception: the attribute-based accessing is guaranteed to
    not raise an error if the data has not been loaded into the dictionary.
    This may be the case if a file was read using filtering settings and
    ``adens`` was not read.

    Parameters
    ----------
    name : str
        Name of this material
    metadata : dict
        Dictionary with file metadata

    Attributes
    ----------
    data : dict
        Main dictionary of arrays from the output file
    zai : list of int
        Isotopic ZZAAAI identifiers like ``922350``. Ordered like
        the rows of the data arrays
    names : list of str
        Isotope names like ``"U235"``. Ordered like the rows of the
        data arrays
    days : numpy.ndarray
        Time in days for each column in the data arrays
    burnup : numpy.ndarray or None
        Burnup vector for this specific material
    volume : numpy.ndarray or None
        Volume of this material over time
    adens : numpy.ndarray or None
        2D array of atom densities in atoms/b-cm
    mdens : numpy.ndarray or None
        2D array of mass densites in g/cm3
    activity : numpy.ndarray or None
        2D array of activities in Bq
    decayHeat : numpy.ndarray or None
        2D array of decay heats in W
    spontaneousFissionRate : numpy.ndarray or None
        2D array of spontaneous fission rate in fission per second
    photonProdRate : numpy.ndarray or None
        2D array of photon emission rate in photons per second
    ingTox : numpy.ndarray or None
        2D array of ingestion toxicity in sieverts
    inhTox : numpy.ndarray or None
        2D array of inhalation toxicity in sieverts

    """

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
    def plot(self, xUnits, yUnits=None, timePoints=None, names=None, zai=None,
             ax=None, legend=None, xlabel=None, ylabel=None, logx=False,
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
            If ``xUnits`` is given and ``yUnits`` is ``None``, then
            the plotted data will be ``xUnits`` against ``'days'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'burnup'``
        timePoints: list or None
            If given, select the time points according to those
            specified here. Otherwise, select all points

            .. deprecated:: 0.7.0
               Will plot against all time points

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
        * :func:`~serpentTools.objects.materials.DepletedMaterial.getValues`
        * :func:`matplotlib.pyplot.plot`
        * :meth:`str.format` - used for formatting labels

        Raises
        ------
        KeyError
            If x axis units are not ``'days'`` nor ``'burnup'``
        TypeError
            If both ``names`` and ``zai`` are given

        """
        if yUnits is None:
            yUnits = xUnits
            xUnits = 'days'

        if xUnits not in ('days', 'burnup'):
            raise KeyError("Plot method only uses x-axis data from <days> "
                           "and <burnup>, not {}".format(xUnits))

        if timePoints is not None:
            deprecateTimepointsWarning()
            xVals = timePoints
        else:
            xVals = self.days if xUnits == 'days' else self.burnup

        if names is None and zai is None:
            names = self.names
            zai = self.zai if names is None else None
        else:
            if isinstance(names, str):
                names = [names, ]
            if isinstance(zai, (int, str)):
                zai = [zai, ]
        yVals = self.getValues(xUnits, yUnits, xVals, names, zai)
        ax = ax or pyplot.gca()
        labels = self._formatLabel(labelFmt, names, zai)
        for row in range(yVals.shape[0]):
            ax.plot(xVals, yVals[row], label=labels[row], **kwargs)

        if xlabel is None:
            xlabel = DEPLETION_PLOT_LABELS[xUnits]
        if ylabel is None:
            ylabel = DEPLETION_PLOT_LABELS[yUnits]

        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy, legendcols=ncol,
                        xlabel=xlabel, ylabel=ylabel,
                        title=title, legend=legend)
        return ax

    def toDataFrame(self, quantity, names=None, zai=None, time="days", multiIndex=False):
        """Create a pandas DataFrame for a property of interest

        If ``names`` and ``zai`` are not provided, then the isotope
        names will be used as the columns.

        Parameters
        ----------
        quantity : str
            Either a key in :attr:`data` or the string name of an attribute
            like ``photonProdRate`` for :attr:`photonProdRate`
        names : sequence of str, optional
            Specific isotope names to obtain. Not compatible with ``zai``
        zai : sequence of int, optional
            Specific isotope zai to obtain. Not compatible with ``names``
        time : {"days", "burnup", "step"}, optional
            What array to use for the index or rows of the DataFrame.
            Defaults to using :attr:`days`, but ``"burnup"`` can be passed
            to use :attr:`burnup`, if it is present. The value of ``"step"``
            will simply create a basic index that starts at 0 and increments
            by one per row

        Returns
        -------
        pandas.DataFrame
            2D tabulated representation of the requested array. Columns
            reflect isotopes, rows represent points in time

        """
        import pandas

        if quantity in {"burnup", "volume"}:
            raise ValueError("{} does not reflect 2D isotopic data".format(
                quantity))

        if names is not None and zai is not None:
            raise ValueError("Cannot pass both isotope names and zai")

        if time == "days":
            timeIndex = pandas.Index(self.days, name="Time [d]")
        elif time == "burnup":
            bu = self.burnup
            if bu is None:
                raise AttributeError(
                    "Burnup not set on material {}".format(self.name))
            timeIndex = pandas.Index(bu, name="Burnup [MWd/kgU]")
        elif time == "step":
            timeIndex = pandas.Index(range(len(self.days)), name="Step")
        else:
            raise ValueError(
                "Index must be days, burnup, or step, not {}".format(time))

        data = self.data.get(quantity)

        if data is None:
            data = getattr(self, quantity, None)
        if data is None:
            raise AttributeError("Quantity {} not present as key in data "
                                 "or as attribute".format(quantity))

        if names is None:
            if zai is None:
                columns = pandas.Index(self.names, name="Isotope")
                isoslice = slice(None)
            else:
                isoslice = self._getRowIndices("zai", zai)
                columns = pandas.Index(
                    [self.zai[x] for x in isoslice], name="Isotope ZAI")
        else:
            isoslice = self._getRowIndices("names", names)
            columns = pandas.Index(
                [self.names[x] for x in isoslice], name="Isotopes")

        return pandas.DataFrame(
            data[isoslice].T.copy(), index=timeIndex, columns=columns)
