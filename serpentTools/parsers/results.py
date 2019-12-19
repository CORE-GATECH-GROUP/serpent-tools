"""Parser responsible for reading the ``*res.m`` files"""
from collections import OrderedDict
from numbers import Real
import re

from numpy import array, empty, asarray
from cycler import cycler
from matplotlib import rcParams
from matplotlib.pyplot import gca

from serpentTools.settings import rc
from serpentTools.utils import convertVariableName
from serpentTools.objects.containers import HomogUniv, UnivTuple
from serpentTools.parsers.base import XSReader
from serpentTools.parsers._collections import RES_DATA_NO_UNCS
from serpentTools.objects.base import (DEF_COMP_LOWER,
                                       DEF_COMP_SIGMA, DEF_COMP_UPPER)
from serpentTools.utils import (
    str2vec,
    splitValsUncs,
    getCommonKeys,
    logDirectCompare,
    compareDocDecorator,
    getKeyMatchingShapes,
    getLogOverlaps,
    STR_REGEX,
    VEC_REGEX,
    SCALAR_REGEX,
    FIRST_WORD_REGEX,
    formatPlot,
    placeLegend,
    magicPlotDocDecorator,
    deconvertVariableName,
    RESULTS_PLOT_XLABELS,
)
from serpentTools.messages import (
    warning, SerpentToolsException,
    info,
)
from serpentTools.io import MatlabConverter


MapStrVersions = {
    '2.1.29': {
        'meta': 'VERSION ', 'rslt': 'MIN_MACROXS',
        'univ': 'GC_UNIVERSE_NAME', 'days': 'BURN_DAYS',
        'burnup': 'BURNUP', 'infxs': 'INF_', 'b1xs': 'B1_',
        'varsUnc': ['MICRO_NG', 'MICRO_E', 'MACRO_NG', 'MACRO_E'],
    },
}
MapStrVersions['2.1.30'] = MapStrVersions['2.1.29']
MapStrVersions['2.1.31'] = MapStrVersions['2.1.29']
"""
Assigns search strings for different Serpent versions
"""

METADATA_CONV = {
    int: {
        'debug',
        'confidentialData',
        'pop',
        'cycles',
        'skip',
        'batchInterval',
        'srcNormMode',
        'seed',
        'ufsMode',
        'ufsOrder',
        'neutronTransportMode',
        'photonTransportMode',
        'groupConstantGeneration',
        'b1BurnupCorrection',
        'implicitReactionRates',
        'optimizationMode',
        'reconstructMicroxs',
        'reconstructMacroxs',
        'mgMajorantMode',
        'spectrumCollapse',
        'mpiTasks',
        'ompThreads',
        'mpiReproducibility',
        'ompReproducibility',
        'shareBufArray',
        'shareRes2Array',
    },
    float: {
        'cpuMhz',
    },
}
"""
Convert items in metadata dictionary from arrays to these data types
"""

VAR_NO_CONV = {
    "DF_SURFACE",
}

DF_CONV = {
    # No uncertainty, convert to int
    int: {
        "DF_SYM",
        "DF_N_SURF",
        "DF_N_CORN",
    },
    # No uncertainty, convert to float
    float: {
        "DF_VOLUME",
    },
    # No uncertainty, convert to array of float
    str2vec: {
        "DF_SURF_AREA",
        "DF_MID_AREA",
        "DF_CORN_AREA,",
        'MICRO_NG',
        'MICRO_E',
        'MACRO_NG',
        'MACRO_E',
    },
}
"""
Functions for converting variable data to various types
"""

UNIV_K_RE = re.compile('_K[EI][NF]F')


def varTypeFactory(key):
    if key in VAR_NO_CONV:
        return lambda x: (x, None)
    for typeFunc in DF_CONV:
        # no conversion for strings
        if key in DF_CONV[typeFunc]:
            return lambda x: (typeFunc(x), None)
    # Perform array conversion, return expected values and uncertainties
    if UNIV_K_RE.search(key) is not None:
        return lambda x: str2vec(x, out=tuple)
    return lambda x: splitValsUncs(x)


__all__ = ['ResultsReader', ]


class ListOfArrays(list):
    """Helper class for creating arrays by appending rows

    Parameters
    ----------
    values : numpy.ndarray, optional
        Initial row to insert into array

    Attributes
    ----------
    A : numpy.ndarray
        Array where each row ``A[i]`` is the ``i``-th row or
        sub-array that was appended
    """

    def __init__(self, values=None):
        super().__init__()
        self._shape = None
        self._dtype = None
        if values is not None:
            self.append(values)

    @property
    def A(self):
        return array(self)

    def append(self, value):
        """Append a row into the final array

        Parameters
        ----------
        value : numpy.ndarray or array-like
            Some object that can be coerced to a numpy.ndarray.
            Must have same shape and data type (e.g. float) as
            previously appended rows

        """
        value = asarray(value)
        if not self:
            self._shape = value.shape
            self._dtype = value.dtype
        elif self._shape != value.shape:
            raise ValueError(
                "Shapes do not agree: Current {} vs. incoming {}".format(
                    self._shape, value.shape))
        elif self._dtype != value.dtype:
            raise TypeError(
                "Types do not agree: Current {} vs. incoming {}".format(
                    self._dtype, value.dtype))
        super().append(value)


class ResultsReader(XSReader):
    """
    Parser responsible for reading and working with result files.

    When inspecting keys of :attr:`universes`, it is preferable to use
    an attribute based approach rather than positional. For example::

        >>> for key in res.universes:
        ...     break
        >>> key.universe
        # rather than
        >>> key[0]

    Attributes
    ------------
    metadata: dict
        Dictionary with serpent descriptive variables as keys and the
        corresponding description. Within the _res.m file this data is
        printed multiple times, but contains the same description
        and thus is stored only once. e.g., 'version': 'Serpent 2.1.29'
    resdata: dict
        Dictionary with serpent time-dependent variables as keys and the
        corresponding values. The data is unique for each burnup step.
        Some variables also contain uncertainties.
        e.g., 'absKeff': [[9.91938E-01, 0.00145],[1.81729E-01, 0.00240]]
    universes: dict
        Dictionary of universe identifiers
        :class:`~serpentTools.objects.UnivTuple` and their corresponding
        :class:`~serpentTools.objects.HomogUniv`
        objects. The keys describe a unique state:
        'universe', burnup (MWd/kg), burnup index, time (days)
        ('0', 0.0, 0, 0.0).
        Burnup indexes are zero-indexed, meaning the first
        step is index 0.

    Parameters
    ----------
    filePath: str
        path to the results file

    Raises
    ------
    :class:`~serpentTools.SerpentToolsException`:
        Serpent version is not supported,
        No universes are found in the file,
        No results are collected,
        Corrupted results

    IOError: file is unexpectedly closes while reading
    """

    __METADATA_COMP_SKIPS = {
        'title',
        'inputFileName',
        'workingDirectory',
        'startDate',
        'completeDate',
        'seed',
    }
    """Metadata keys that will not be compared."""

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'results')

        self.metadata = {}
        self.resdata = {}
        self.universes = {}

    def _read(self):
        """Read through the results file and store requested data."""

        self._counter = {'meta': 0, 'rslt': 0}
        self._univlist = []
        self._varTypeLookup = {}
        self._tempArrays = {}

        self.metadata.clear()
        self.resdata.clear()
        self.universes.clear()

        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                self._processResults(tline)

        while self._tempArrays:
            # Consume temporary arrays
            key, temp = self._tempArrays.popitem()
            value = temp.A

            # Only insert first row if no burnup present
            if value.shape[0] == 1:
                self.resdata[key] = value.reshape(value.size)
            else:
                self.resdata[key] = value

    def _processResults(self, tline):
        """Performs the main processing of the results."""
        #  Not an empty line or a comment
        if (tline.strip() and '%' not in tline and '=' in tline
                and 'idx = ' not in tline):
            self._whereAmI(tline)  # identify position in file
            # obtain the name of the variable
            varNameSer, varNamePy = self._getVarName(tline)
            if not self._checkAddVariable(varNameSer):
                return
            varType, varVals = self._getVarValues(tline)  # values to be stored
            if self._posFile == 'meta':
                self._storeMetaData(varNamePy, varType, varVals)
            if self._posFile == 'rslt':
                self._storeResData(varNamePy, varVals)
            if self._posFile == 'univ':
                self._storeUnivData(varNameSer, varVals)

    def _whereAmI(self, tline):
        """Identify the position in the file."""
        if self._keysVersion['meta'] in tline:
            self._posFile = 'meta'
            self._counter['meta'] += 1
        elif self._keysVersion['rslt'] in tline:
            self._posFile = 'rslt'
            if self._numUniv:
                self._counter['rslt'] = (
                    (self._counter['meta'] - 1) // self._numUniv + 1)
                return
            self._counter['rslt'] = self._counter['meta']
        elif self._keysVersion['univ'] in tline:
            self._posFile = 'univ'
            varType, varVals = self._getVarValues(tline)  # universe name
            self._univlist.append(varVals)

    def _storeUnivData(self, varNameSer, varVals):
        """Process universes data"""
        brState = self._getBUstate()  # obtain the branching tuple
        if brState not in self.universes:
            self.universes[brState] = HomogUniv(*brState)
        if varNameSer == self._keysVersion['univ']:
            return

        # Get variable specificy type converter
        if varNameSer not in self._varTypeLookup:
            self._varTypeLookup[varNameSer] = varTypeFactory(varNameSer)
        converter = self._varTypeLookup[varNameSer]
        values, uncertainties = converter(varVals)

        # Values without uncertainties
        self.universes[brState].addData(varNameSer, values, False)
        if uncertainties is not None:
            self.universes[brState].addData(varNameSer, uncertainties, True)

    def _storeResData(self, varNamePy, varVals):
        """Process time-dependent results data"""
        vals = str2vec(varVals)  # convert the string to float numbers

        stored = self._tempArrays.get(varNamePy)
        if stored is None:
            self._tempArrays[varNamePy] = ListOfArrays(vals)
        elif len(stored) < self._counter['rslt']:
            # append this data only once!
            try:
                stored.append(vals)
            except Exception as ee:
                raise SerpentToolsException(
                    "Error in appending {}  into {} of resdata:\n{}"
                    .format(varNamePy, vals, str(ee)))

    def _storeMetaData(self, varNamePy, varType, varVals):
        """Store general descriptive data"""
        if varType == 'string':
            self.metadata[varNamePy] = varVals
        else:  # vector or scalar
            vals = str2vec(varVals)  # convert string to floats
            self.metadata[varNamePy] = array(vals)  # overwrite existing data

    def _getBUstate(self):
        """Define unique branch state"""
        burnIdx = self._counter['rslt'] - 1
        dayVec = self._tempArrays.get(self._burnupKeys["days"])

        if dayVec is None:
            days = 0
        elif burnIdx:
            days = dayVec[-1][0]
        else:
            days = dayVec[0][0]

        burnupVec = self._tempArrays.get(self._burnupKeys["burnup"])

        if burnupVec is None:
            burnup = 0
        elif burnIdx:
            burnup = burnupVec[-1][0]
        else:
            burnup = burnupVec[0][0]

        return UnivTuple(self._univlist[-1], burnup, burnIdx, days)

    def _getVarName(self, tline):
        """Obtains the variable name and converts it to a python-style name."""
        currVar = FIRST_WORD_REGEX.search(tline)
        if currVar is not None:
            # return serpent-style and python-style names
            return currVar.group(), convertVariableName(currVar.group())

    def _getVarValues(self, tline):
        """Obtains the values of any variable."""
        strMatch = STR_REGEX.search(tline)
        vecMatch = VEC_REGEX.search(tline)
        sclMatch = SCALAR_REGEX.search(tline)
        varType, varVals = [], []
        if strMatch is not None:
            varType = 'string'
            varVals = tline[strMatch.span()[0] + 1:strMatch.span()[1] - 1]
        elif vecMatch is not None:
            varType = 'vector'
            varVals = tline[vecMatch.span()[0] + 1:vecMatch.span()[1] - 2]
        elif sclMatch is not None:
            varType = 'scalar'
            varVals = tline[sclMatch.span()[0] + 1:sclMatch.span()[1] - 2]
        return varType, varVals

    def getUniv(self, univ, burnup=None, index=None, timeDays=None):
        """
        Return a specific universe given the ID and time of interest

        Parameters
        ----------
        univ: str
            Unique str for the desired universe
        burnup: float or int, optional
            Burnup [MWd/kgU] of the desired universe
        timeDays: float or int, optional
            Time [days] of the desired universe
        index: int, optinal
            Point of interest in the burnup/days index

        Returns
        -------
        :class:`~serpentTools.objects.HomogUniv`
            Requested universe

        Raises
        ------
        KeyError:
            If the requested universe could not be found
        :class:`~serpentTools.SerpentToolsException`
            If burnup, days and index are not given
        """
        if index is None and burnup is None and timeDays is None:
            raise SerpentToolsException(
                'Burnup, time or index are required inputs')

        searchKey = UnivTuple(univ, burnup, index, timeDays)

        # check if key is exactly present

        universe = self.universes.get(searchKey)
        if universe is not None:
            return universe

        for key, universe in self.universes.items():
            for uItem, sItem in zip(key, searchKey):
                if sItem is None:
                    continue
                elif uItem != sItem:
                    break
            else:
                return universe
        raise KeyError(
            "Could not find a universe that matches {}".format(searchKey))

    def _precheck(self):
        """do a quick scan to ensure this looks like a results file."""
        serpentV = rc['serpentVersion']
        keys = MapStrVersions.get(serpentV)

        if keys is None:
            warning("SERPENT {} is not supported by the "
                    "ResultsReader".format(serpentV))
            warning("  Attemping to read anyway. Please report strange "
                    "behaviors/failures to developers.")
            keys = MapStrVersions[max(MapStrVersions)]

        self._keysVersion = keys

        self._burnupKeys = {k: convertVariableName(keys[k]) for k in {"days", "burnup"}}

        univSet = set()
        verWarning = True
        with open(self.filePath) as fid:
            if fid is None:
                raise IOError("Attempting to read on a closed file.\n"
                              "Parser: {}\nFile: {}"
                              .format(self, self.filePath))
            for tline in fid:
                if verWarning and self._keysVersion['meta'] in tline:
                    verWarning = False
                    varType, varVals = self._getVarValues(tline)  # version
                    if serpentV not in varVals:
                        warning("SERPENT {} found in {}, but version {} is "
                                "defined in settings"
                                .format(varVals, self.filePath,
                                        serpentV))
                        warning("  Attemping to read anyway. Please report "
                                "strange behaviors/failures to developers.")
                if self._keysVersion['univ'] in tline:
                    varType, varVals = self._getVarValues(tline)  # universe
                    if varVals in univSet:
                        break
                    univSet.add(varVals)  # add the new universe
            self._numUniv = len(univSet)

    def _inspectData(self):
        """ensure the parser grabbed expected materials."""
        obtainedRes = (self._counter['meta'] // self._numUniv if self._numUniv
                       else self._counter['meta'])
        if obtainedRes != self._counter['rslt']:
            raise SerpentToolsException(
                "The file {} is not complete. The reader found {} universes, "
                "{} time-points, and {} overall result points "
                .format(self.filePath, self._numUniv,
                        self._counter['rslt'], self._counter['meta']))
        if not self.resdata and not self.metadata:
            for keys, dictUniv in self.universes.items():
                if dictUniv.hasData():
                    return
            raise SerpentToolsException(
                "metadata, resdata and universes are all empty "
                "from {} and <results.expectGcu> is True"
                .format(self.filePath))

    def _postcheck(self):
        self._inspectData()
        self._cleanMetadata()
        del (self._varTypeLookup, self._burnupKeys, self._keysVersion,
             self._counter, self._univlist, self._tempArrays)

    def _compare(self, other, lower, upper, sigma):
        similar = self.compareMetadata(other)
        similar &= self.compareResults(other, lower, upper, sigma)
        similar &= self.compareUniverses(other, lower, upper, sigma)
        return similar

    @compareDocDecorator
    def compareMetadata(self, other, header=False):
        """
        Return True if the metadata (settings) are identical.

        Parameters
        ----------
        other: :class:`ResultsReader`
            Class against which to compare
        {header}

        Returns
        -------
        bool:
            If the metadata are identical

        Raises
        ------
        {compTypeErr}
        """

        self._checkCompareObj(other)
        if header:
            self._compareLogPreMsg(other, quantity='metadata')
        myKeys = set(self.metadata.keys())
        otherKeys = set(other.metadata.keys())
        similar = not any(myKeys.symmetric_difference(otherKeys))
        commonKeys = getCommonKeys(myKeys, otherKeys, 'metadata')
        skips = commonKeys.intersection(self.__METADATA_COMP_SKIPS)
        if any(skips):
            info("The following items will be skipped in the comparison\n\t{}"
                 .format(', '.join(sorted(skips))))
        for key in sorted(commonKeys):
            if key in self.__METADATA_COMP_SKIPS:
                continue
            selfV = self.metadata[key]
            otherV = other.metadata[key]
            similar &= logDirectCompare(selfV, otherV, 0., 0., key)

        return similar

    @compareDocDecorator
    def compareResults(self, other, lower=DEF_COMP_LOWER,
                       upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA,
                       header=False):
        """
        Compare the contents of the results dictionary

        Parameters
        ----------
        other: :class:`ResultsReader`
            Class against which to compare
        {compLimits}
        {sigma}
        {header}

        Returns
        -------
        bool:
            If the results data agree to given tolerances

        Raises
        ------
        {compTypeErr}
        """
        self._checkCompareObj(other)
        if header:
            self._compareLogPreMsg(other, lower, upper, sigma, 'results')
        myRes = self.resdata
        otherR = other.resdata

        commonTypeKeys = getKeyMatchingShapes(myRes, otherR, 'results')

        similar = len(commonTypeKeys) == len(myRes) == len(otherR)

        for key in sorted(commonTypeKeys):
            mine = myRes[key]
            theirs = otherR[key]
            if key in RES_DATA_NO_UNCS:
                similar &= logDirectCompare(mine, theirs, lower, upper, key)
                continue
            myVals, myUncs = splitValsUncs(mine)
            theirVals, theirUncs = splitValsUncs(theirs)
            similar &= getLogOverlaps(key, myVals, theirVals, myUncs,
                                      theirUncs, sigma, relative=True)
        return similar

    @compareDocDecorator
    def compareUniverses(self, other, lower=DEF_COMP_LOWER,
                         upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA):
        """
        Compare the contents of the ``universes`` dictionary

        Parameters
        ----------
        other: :class:`ResultsReader`
            Reader by which to compare
        {compLimits}
        {sigma}

        Returns
        -------
        bool:
            If the contents of the universes agree to given tolerances

        Raises
        ------
        {compTypeErr}
        """
        self._checkCompareObj(other)
        myUniverses = self.universes
        otherUniverses = other.universes
        keyGoodTypes = getKeyMatchingShapes(myUniverses, otherUniverses,
                                            'universes')

        similar = len(keyGoodTypes) == len(myUniverses) == len(otherUniverses)

        for univKey in keyGoodTypes:
            myUniv = myUniverses[univKey]
            otherUniv = otherUniverses[univKey]
            similar &= myUniv.compare(otherUniv, lower, upper, sigma)
        return similar

    def _cleanMetadata(self):
        """Replace some items in metadata dictionary with easier data types."""
        mdata = self.metadata
        origKeys = set(mdata.keys())
        for converter, keys in METADATA_CONV.items():
            for key in keys:
                if key in origKeys:
                    mdata[key] = converter(mdata[key])
                    origKeys.remove(key)

    @magicPlotDocDecorator
    def plot(self, x, y=None, right=None, sigma=3, ax=None, legend=None,
             ncol=None, xlabel=True, ylabel=None, logx=False, logy=False,
             loglog=False, rightlabel=None):
        """
        Plot quantities over time

        Parameters
        ----------
        x: str or iterable of strings
            ``y`` is not given, then plot these quantites against
            burnup in days. Otherwise, plot this quantity as the x
            axis with same rules as if called by ``plot('burndays', x)``.
            Burnup options are ``{'burnup', 'days', 'burnDays', 'burnStep'}``
        y: str or iterable of strings
            Quantity or quantities to plot. For all entries, only
            the first column, with respect to time, will be plotted.
            If the second column exists, and sigma is > 0, that column
            will be treated as the relative uncertainty for an
            errorbar plot. If a dictionary is passed, then plots will
            be labeled by the values of that dictionary, e.g.
            ``{'anaKeff': $k_{eff}$}`` would plot the first column of
            ``anaKeff`` with a ``LaTeX``-ready :math:`k_{eff}`
        right: str or iterable of strings
            Quantites to plot on the same plot, but with a different
            y axis and common x axis. Same rules apply as for arguments
            to ``y``. Each label will modified to have a unique identifier
            indicating the plot uses the right y-axis
        {ax}
        {sigma}
        {legend}
        {ncol}
        {xlabel}
        {ylabel}
        {logx}
        logy: bool or list or tuple
            Apply a log scale to the y-axis. If passing values to
            ``right``, this can be a two item list or tuple,
            corresponding to log-scaling the left and right axis,
            respectively.
        {loglog}
        rlabel: str or None
            If given and passing values to ``right``, use this to label
            the y-axis.

        Returns
        -------
        :class:`matplotlib.axes.Axes` or tuple of axes
            If right is not given, then only the primary axes object
            is returned. Otherwise, the primary and the "right"
            axes object are returned

        """

        # cleanup some inputs
        if y is None:
            y = x
            x = "burnDays"

        sigma = max(int(sigma), 0)

        y = self._expandPlotIterables(y)

        if right is not None:
            right = self._expandPlotIterables(right, ' [right]')

        if xlabel is True:
            xlabel = RESULTS_PLOT_XLABELS[x]

        if len(y) == 1 and ylabel is None:
            for ylabel in y.values():
                break  # just need the first one
            if sigma:
                ylabel += r'$ \pm {}\sigma$'.format(sigma)

        ax = ax or gca()

        self._plot(x, y, ax, sigma)

        if right is None:
            formatPlot(ax, logx=logx, logy=logy, loglog=loglog,
                       xlabel=xlabel, ylabel=ylabel, legend=legend,
                       ncol=ncol)
            return ax

        # plot some other quantity on the same x axis
        other = ax.twinx()

        # update color cycle to not repeat
        colors = rcParams['axes.prop_cycle'].by_key()['color']
        colors = colors[len(y):] + colors[:len(y)]
        other.set_prop_cycle(cycler('color', colors))

        self._plot(x, right, other, sigma)

        # formatting
        if logy is None or isinstance(logy, bool):
            logy = [logy, ] * 2

        if loglog is None or isinstance(loglog, bool):
            loglog = [loglog, None]

        if legend or legend is None:
            leftHandles, leftLabels = ax.get_legend_handles_labels()
            rightHandles, rightLabels = other.get_legend_handles_labels()

            placeLegend(ax, legend, ncol,
                        (leftHandles + rightHandles,
                         leftLabels + rightLabels))

        if len(right) == 1 and rightlabel is None:
            for rightlabel in right.values():
                break  # just need the first one
            if sigma:
                rightlabel += r'$ \pm {}\sigma$'.format(sigma)

        formatPlot(ax, logx=logx, logy=logy[0], loglog=loglog[0],
                   legend=False, xlabel=xlabel, ylabel=ylabel)
        formatPlot(other, logx=False, loglog=False, logy=logy[1],
                   legend=False, ylabel=rightlabel.replace(' [right]', ''))

        return ax, other

    def _plot(self, x, y, ax, sigma):
        """Simple, unformatted plot with dictionary of keys"""
        # get plot data
        xvals = self.resdata[x][:, 0]
        for resKey, label in y.items():
            ydata = self.resdata[resKey]
            if ydata.shape[0] != xvals.size and ydata.size != xvals.size:
                raise ValueError(
                    "Quantity for {} has {} time points, not {} like {}"
                    .format(resKey, ydata.shape[0], xvals.size, x))

            # grab second column for uncertainty
            if sigma and ydata.shape[1] > 1:
                ax.errorbar(xvals, ydata[:, 0], label=label,
                            yerr=ydata[:, 0] * sigma * ydata[:, 1],
                            )
            else:
                ax.errorbar(xvals, ydata[:, 0], label=label,
                            )

    @staticmethod
    def _expandPlotIterables(y, tail=''):
        if isinstance(y, str):
            return {y: "{}{}".format(y, tail)}
        elif not isinstance(y, (dict, OrderedDict)):
            return OrderedDict([[item, '{}{}'.format(item, tail)]
                                for item in y])
        return y

    def toMatlab(self, fileP, reconvert=True, append=True,
                 format='5', longNames=True, compress=True,
                 oned='row'):
        """
        Write a binary MATLAB file from the contents of this reader

        The group constant data will be presented as a multi-dimensional
        array, rather than a stacked 2D matrix. The axis are ordered
        ``burnup, universeIndex, group, value/uncertainty``

        The ordering of the universes can be found in the ``'UNIVERSES'``
        vector if ``reconvert==True``, otherwise ``'universes'``. Each
        universe ID is present in this vector, ordered to their
        position along the second axis in the matrix.

        Parameters
        ----------
        fileP: str or file-like object
            Name of the file to write
        reconvert: bool
            If this evaluates to true, convert values back into their
            original form as they appear in the output file.
        append: bool
            If true and a file exists under ``output``, append to that file.
            Otherwise the file will be overwritten
        format: {'5', '4'}
            Format of file to write. ``'5'`` for MATLAB 5 to 7.2, ``'4'`` for
            MATLAB 4
        longNames: bool
            If true, allow variable names to reach 63 characters,
            which works with MATLAB 7.6+. Otherwise, maximum length is
            31 characters
        compress: bool
            If true, compress matrices on write
        oned: {'row', 'col'}:
            Write one-dimensional arrays as row vectors if
            ``oned=='row'`` (default), or column vectors

        Examples
        --------

        >>> import serpentTools
        >>> from scipy.io import loadmat
        >>> r = serpentTools.readDataFile('pwr_res.m')
        # convert to original variable names
        >>> r.toMatlab('pwr_res.mat', True)
        >>> loaded = loadmat('pwr_res.mat')
        >>> loaded['ABS_KEFF']
        array([[0.991938, 0.00145 ],
               [0.181729, 0.0024  ]])
        >>> kinf = loaded['INF_KINF']
        >>> kinf.shape
        (2, 1, 1, 2)
        >>> kinf[:, 0, 0, 0]
        array([0.993385, 0.181451])
        >>> tot = loaded['INF_TOT']
        >>> tot.shape
        (2, 1, 2, 2)
        >>> tot[:, 0, :, 0]
        array([[0.496553, 1.21388 ],
               [0.481875, 1.30993 ]])
        # use the universes key to identify ordering of universes
        >>> loaded['UNIVERSES']
        array([0])

        Raises
        ------
        ImportError:
            If :term:`scipy` is not installed

        See Also
        --------
        * :func:`scipy.io.savemat`
        """
        converter = MatlabConverter(self, fileP)
        return converter.convert(reconvert, append, format, longNames,
                                 compress, oned)

    def _gather_matlab(self, reconvert):
        if reconvert:
            varFunc = getSerpentCaseName
            out = {
                varFunc(key): value for key, value in self.metadata.items()
            }
            out.update({
                varFunc(key): value for key, value in self.resdata.items()
            })
        else:
            out = {}
            varFunc = getMixedCaseName
            out.update(self.metadata)
            out.update(self.resdata)
        out.update(self._gather_univdata(varFunc))
        return out

    def _gather_univdata(self, func):
        numAppearances = {}

        for key in self.universes:
            if key.universe not in numAppearances:
                numAppearances[key.universe] = 1
                continue
            numAppearances[key.universe] += 1
        # check to make sure all universes appear an identical
        # number of times
        burnupVals = set(numAppearances.values())
        if len(burnupVals) != 1:
            raise SerpentToolsException(
                "Universes appear a different number of times:\n{}"
                .format(numAppearances))

        shapeStart = burnupVals.pop(), len(numAppearances)
        univOrder = tuple(sorted(numAppearances))

        univData = {func('universes'): univOrder}

        for univKey, univ in self.universes.items():

            # position in matrix
            uIndex = univOrder.index(univKey.universe)
            bIndex = univKey.step

            for expName, uncName in zip(
                    ('infExp', 'b1Exp', 'gc'), ('infUnc', 'b1Unc', 'gcUnc')):
                expD = getattr(univ, expName)
                uncD = getattr(univ, uncName)
                gatherPairedUnivData(univ, uIndex, bIndex, shapeStart, func,
                                     expD, uncD, univData)

        return univData


def getMixedCaseName(name):
    """
    Return the name of the variable used for exporting - camelCase
    """
    return name


def getSerpentCaseName(name):
    """
    Return the name of the variable used for exporting - SERPENT_CASE
    """
    return deconvertVariableName(name)


def gatherPairedUnivData(universe, uIndex, bIndex, shapeStart, convFunc,
                         expD, uncD, univData):
    """Helper function to update universe dictionary for exporting"""
    for xsKey, xsVal in expD.items():
        outKey = convFunc(xsKey)
        if outKey not in univData:
            if isinstance(xsVal, Real):
                shape = 1,
            else:  # assume array or has shape
                shape = xsVal.shape
            data = empty((shapeStart + shape + (2, )))
            univData[outKey] = data
        else:
            data = univData[outKey]
        data[bIndex, uIndex, ..., 0] = xsVal
        xsUnc = uncD.get(xsKey)
        if xsUnc is None:
            data[bIndex, uIndex, ..., 1] = 0.0
        else:
            data[bIndex, uIndex, ..., 1] = xsUnc
