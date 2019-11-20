"""
Custom-built containers for storing data from serpent outputs

Contents
--------
* :class:`~serpentTools.objects.containers.HomogUniv`
* :class:`~serpentTools.objects.containers.BranchContainer`

"""
from itertools import product
from collections import namedtuple

from matplotlib import pyplot
from numpy import arange, hstack, ndarray, zeros_like

from serpentTools.settings import rc
from serpentTools.objects.base import NamedObject
from serpentTools.utils import (
    convertVariableName,
    getKeyMatchingShapes,
    logDirectCompare,
    getLogOverlaps,
    compareDocReplacer,
    compareDocDecorator,
    magicPlotDocDecorator,
    formatPlot,
    inferAxScale,
)

from serpentTools.objects.base import (DEF_COMP_LOWER,
                                       DEF_COMP_UPPER, DEF_COMP_SIGMA)
from serpentTools.messages import (
    warning,
    SerpentToolsException,
    info,
    critical,
    error,
)

SCATTER_MATS = set()
SCATTER_ORDERS = 8

for xsSpectrum, xsType in product({'INF', 'B1'},
                                  {'S', 'SP'}):
    SCATTER_MATS.update({'{}_{}{}'.format(xsSpectrum, xsType, xx)
                        for xx in range(SCATTER_ORDERS)})

HOMOG_VAR_TO_ATTR = {
    'MICRO_E': 'microGroups', 'MICRO_NG': 'numMicroGroups',
    'MACRO_E': 'groups', 'MACRO_NG': 'numGroups'}

__all__ = (
    'HomogUniv', 'BranchContainer', "UnivTuple"
)

UnivTuple = namedtuple("UnivTuple", ["universe", "burnup", "step", "days"])

try:
    UnivTuple.__doc__ = """Convenient identifier for universes

Properties can be accessed by position or by attribute name.
The latter is preferable as it will be consistent across
potential API changes

Attributes
----------
universe : str
    Universe from Serpent input
burnup : float or None
    Burnup for this universe [MWd/kgU]
step : int
    Burnup step
days : float or None
    Burnup day

Example
-------

>>> x = UnivTuple("0", 0.1, 1, 10.0)
>>> x.universe
"0"
>>> x[0] == x.universe
True

"""
except AttributeError:
    # Can't set docs for namedtuples in PY2
    pass


class HomogUniv(NamedObject):
    """
    Class for storing homogenized universe specifications and retrieving them

    Parameters
    ----------
    name: str
        name of the universe
    bu: float
        burnup value
    step: float
        temporal step
    day: float
        depletion day

    Attributes
    ----------
    name: str
        name of the universe
    bu: float or int
        non-negative burnup value
    step: int
        temporal step
    day: float or int
        non-negative depletion day
    infExp: dict
        Expected values for infinite medium group constants
    infUnc: dict
        Relative uncertainties for infinite medium group constants
    b1Exp: dict
        Expected values for leakage corrected group constants
    b1Unc: dict
        Relative uncertainties for leakage-corrected group constants
    gc: dict
        Expected values for group constants that do not fit
        the ``INF_`` nor ``B1_`` pattern
    gcUnc: dict
        Relative uncertainties for group constants that do not fit
        the ``INF_`` nor ``B1_`` pattern
    reshaped: bool
        ``True`` if scattering matrices have been reshaped to square
        matrices. Otherwise, these matrices are stored as vectors.
    groups: None or :class:`numpy.array`
        Group boundaries from highest to lowest
    numGroups: None or int
        Number of energy groups bounded by ``groups``
    microGroups: None or :class:`numpy.array`
        Micro group structure used to produce group constants.
        Listed from lowest to highest

    Raises
    ------
    :class:`serpentTools.SerpentToolsException`
        If a negative value of burnup, step, or burnup days is passed

    """

    def __init__(self, name, bu, step, day):
        if not all(xx is None or xx >= 0 for xx in (bu, step, day)):
            tail = ['{}: {}'.format(valName, val)
                    for valName, val in zip(('burnup', 'index', 'days'),
                                            (bu, step, day))]
            raise SerpentToolsException(
                "Will not create universe with negative burnup\n{}"
                .format(', '.join(tail)))
        NamedObject.__init__(self, name)
        if step == 0:
            bu = bu if bu is not None else 0.0
            day = day if day is not None else 0.0
        self.bu = bu
        self.step = step
        self.day = day
        # Dictionaries:
        self.b1Exp = {}
        self.infExp = {}
        self.b1Unc = {}
        self.infUnc = {}
        self.gc = {}
        self.gcUnc = {}
        self.__reshaped = rc['xs.reshapeScatter']
        self._numGroups = None
        self.groups = None
        self.microGroups = None
        self._numMicroGroups = None

    @property
    def reshaped(self):
        return self.__reshaped

    @property
    def numGroups(self):
        if self._numGroups is None and self.groups is not None:
            self._numGroups = self.groups.size - 1
        return self._numGroups

    @numGroups.setter
    def numGroups(self, value):
        value = value if isinstance(value, int) else int(value)
        self._numGroups = value

    @property
    def numMicroGroups(self):
        if self._numMicroGroups is None and self.microGroups is not None:
            self._numMicroGroups = self.microGroups.size - 1
        return self._numMicroGroups

    @numMicroGroups.setter
    def numMicroGroups(self, value):
        value = value if isinstance(value, int) else int(value)
        self._numMicroGroups = value

    def __str__(self):
        extras = []
        if self.bu is not None:
            extras.append('burnup: {:11.5E} MWd/kgU'.format(self.bu))
        if self.day is not None:
            extras.append('{:11.5E} days'.format(self.day))
        if extras:
            extras = ': ' + ', '.join(extras)
        return '<{} {}{}>'.format(self.__class__.__name__, self.name,
                                  extras or '')

    def addData(self, variableName, variableValue, uncertainty=False):
        r"""
        Sets the value of the variable and, optionally, the associate s.d.

        .. versionadded:: 0.5.0

            Reshapes scattering matrices according to setting
            ``xs.reshapeScatter``. Matrices are of the form
            :math:`S[i, j]=\Sigma_{s,i\rightarrow j}`

        .. warning::

            This method will overwrite data for variables that already exist

        Parameters
        ----------
        variableName: str
            Variable Name
        variableValue:
            Variable Value
        uncertainty: bool
            Set to ``True`` if this data is an uncertainty

        Raises
        ------
        TypeError
            If the uncertainty flag is not boolean

        """
        if not isinstance(uncertainty, bool):
            raise TypeError('The variable uncertainty has type {}, '
                            'should be boolean.'.format(type(uncertainty)))

        value = self._cleanData(variableName, variableValue)
        if variableName in HOMOG_VAR_TO_ATTR:
            value = value if variableValue.size > 1 else value[0]
            setattr(self, HOMOG_VAR_TO_ATTR[variableName], value)
            return

        name = convertVariableName(variableName)
        # 2. Pointer to the proper dictionary
        setter = self._lookup(name, uncertainty)
        # 3. Check if variable is already present. Then set the variable.
        if name in setter:
            warning("The variable {} will be overwritten".format(name))
        setter[name] = value

    def _cleanData(self, name, value):
        """
        Return the new value to be stored after some cleaning.

        Reshapes scattering matrices if number of groups
        is known and ``xs.reshapeScatter``
        """
        ng = self.numGroups
        if self.__reshaped and name in SCATTER_MATS:
            if ng is None:
                info("Number of groups is unknown at this time. "
                     "Will not reshape variable {}"
                     .format(name))
            else:
                value = value.reshape(ng, ng, order="F")
        return value

    def get(self, variableName, uncertainty=False):
        """
        Gets the value of the variable VariableName from the dictionaries

        Parameters
        ----------
        variableName: str
            Variable Name
        uncertainty:   bool
            Boolean Variable- set to True in order to retrieve the
            uncertainty associated to the expected values

        Returns
        -------
        x:
            Variable Value
        dx:
            Associated uncertainty if ``uncertainty``

        Raises
        ------
        TypeError
            If the uncertainty flag is not boolean
        KeyError
            If the variable requested is not stored on the
            object

        See Also
        --------
        :meth:`__getitem__` to directly access data witout uncertainties

        """
        # 1. Check the input values
        if not isinstance(uncertainty, bool):
            raise TypeError('The variable uncertainty has type %s.\n ...'
                            'It should be boolean.', type(uncertainty))
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variableName, False)
        if variableName not in setter:
            raise KeyError(
                "Variable {} absent from expected value dictionary".format(
                    variableName))
        x = setter.get(variableName)
        # 3. Return the value of the variable
        if not uncertainty:
            return x
        setter = self._lookup(variableName, True)
        if variableName not in setter:
            raise KeyError(
                "Variable {} absent from uncertainty dictionary".format(
                    variableName))

        return x, setter[variableName]

    def __getitem__(self, gcname):
        """
        Return just the group constant with this name, no uncertainty

        To return data with uncertainties, or to return uncertainties,
        use :meth:`get`.
        """
        return self._lookup(gcname, False)[gcname]

    def __setitem__(self, gckey, gcvalue):
        """
        Set the expected value of gckey to be gcvalue

        No conversions are placed on the variable name. What you
        pass is what gets set.

        For uncertainties, or to convert variable
        names to ``mixedCase``, use :meth:`addData`.

        Much like a dictionary, this will overwrite existing data.
        """
        self._lookup(gckey, False)[gckey] = gcvalue

    def _lookup(self, variableName, uncertainty):
        if 'inf' == variableName[:3]:
            if uncertainty:
                return self.infUnc
            return self.infExp
        elif "b1" == variableName[:2]:
            if uncertainty:
                return self.b1Unc
            return self.b1Exp
        return self.gcUnc if uncertainty else self.gc

    @magicPlotDocDecorator
    def plot(self, qtys, limitE=True, ax=None, logx=None, logy=None,
             loglog=None, sigma=3, xlabel=None, ylabel=None, legend=None,
             ncol=1, steps=True, labelFmt=None, labels=None):
        """
        Plot homogenized data as a function of energy.

        Parameters
        ----------
        qtys: str or iterable
            Plot this or these value against energy.
        limitE: bool
            If given, set the maximum energy value to be
            that of the micro group structure. By default,
            SERPENT macro group structures can reach
            1E37, leading for a very large tail on the plots.
        {ax}
        {labels}
        {logx}
        {logy}
        {loglog}
        {sigma}
        {xlabel}
        {ylabel}
        {legend}
        {ncol}
        steps: bool
            If ``True``, plot values as constant within
            energy bins.
        {univLabelFmt}

        Returns
        -------
        {rax}

        See Also
        --------
        * :meth:`serpentTools.objects.containers.HomogUniv.get`

        """
        qtys = [qtys, ] if isinstance(qtys, str) else qtys
        ax = ax or pyplot.gca()
        onlyXS = True
        sigma = max(0, int(sigma))
        drawstyle = 'steps-post' if steps else None
        limitE = limitE and (self.groups is not None
                             and self.microGroups is not None)
        macroBins = self.numGroups + 1 if self.numGroups is not None else None
        microBins = (self.numMicroGroups + 1
                     if self.numMicroGroups is not None else None)
        labelFmt = labelFmt or "{k}"
        if limitE:
            eneCap = min(self.microGroups.max(), self.groups.max())

        if isinstance(labels, str):
            labels = [labels, ]
        if labels is None:
            labels = [labelFmt, ] * len(qtys)
        else:
            if len(labels) != len(qtys):
                raise IndexError(
                    "Need equal number of labels for plot quantities. "
                    "Given {} expected: {}".format(len(labels), len(qtys)))

        for key, label in zip(qtys, labels):
            yVals = self.__getitem__(key)
            if len(yVals.shape) != 1 and 1 not in yVals.shape:
                warning("Data for {} is not 1D. Will not plot"
                        .format(key))
                continue
            uncD = self._lookup(key, True)
            yUncs = uncD.get(key, zeros_like(yVals))

            if 'Flx' in key:
                onlyXS = False
            yVals = hstack((yVals, yVals[-1]))
            nbins = yVals.size
            yUncs = hstack((yUncs, yUncs[-1])) * yVals * sigma

            xdata, foundE = self.__getEGrid(nbins, macroBins, microBins)

            if limitE and foundE:
                xdata = xdata.copy()
                xdata[xdata.argmax()] = eneCap

            label = self.__formatLabel(label, key)

            ax.errorbar(xdata, yVals, yerr=yUncs, label=label,
                        drawstyle=drawstyle)

        if ylabel is None:
            ylabel, yUnits = (("Cross Section", "[cm$^{-1}$]") if onlyXS
                              else ("Group Constant", ""))
            sigStr = r" $\pm{}\sigma$".format(sigma) if sigma else ""
            ylabel = ' '.join((ylabel, sigStr, yUnits))

        if xlabel is None:
            xlabel = "Energy [MeV]" if foundE else "Energy Group"

        if legend is None:
            legend = len(qtys) > 1
        if loglog is not None:
            logx = logy = loglog
        else:
            if logx is None:
                logx = foundE
            if logy is None:
                logy = inferAxScale(ax, 'y')

        formatPlot(ax, logx=logx, logy=logy, ncol=ncol,
                   legend=legend, xlabel=xlabel or "Energy [MeV]",
                   ylabel=ylabel)
        return ax

    def __getEGrid(self, nbins, macroBins, microBins):
        """Return group structure that matches number of groups"""
        if macroBins is not None and nbins == macroBins:
            return self.groups, True
        if microBins is not None and nbins == microBins:
            return self.microGroups, True
        return arange(0.5, nbins + 0.5), False

    def __formatLabel(self, label, key):
        mapping = {
            "{k}": key, "{u}": self.name, "{i}": self.step,
            "{b}": self.bu, "{d}": self.day
        }
        for lookF, value in mapping.items():
            label = label.replace(lookF, str(value))
        return label

    def __bool__(self):
        """Return True if data is stored on the object."""
        attrs = {"infExp", "infUnc", "b1Exp", "b1Unc", "gc", "gcUnc",
                 "groups", "microGroups"}
        for key in attrs:
            value = getattr(self, key)
            if isinstance(value, dict) and value:
                return True
            if isinstance(value, ndarray) and value.any():
                return True
            if value:
                return True
        return False

    __nonzero__ = __bool__

    hasData = __bool__

    def _compare(self, other, lower, upper, sigma):
        similar = self.compareAttributes(other, lower, upper, sigma)
        similar &= self.compareInfData(other, sigma)
        similar &= self.compareB1Data(other, sigma)
        similar &= self.compareGCData(other, sigma)

        return similar

    @compareDocDecorator
    def compareAttributes(self, other, lower=DEF_COMP_LOWER,
                          upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA):
        """
        Compare attributes like group structure and burnup. Return the result

        Parameters
        ----------
        other: :class:`HomogUniv`
            Universe against which to compare
        {compLimits}
        {sigma}

        Returns
        -------
        bools:
            ``True`` if the attributes agree within specifications

        Raises
        ------
        {compTypeErr}
        """

        self._checkCompareObj(other)

        myMeta = {}
        otherMeta = {}

        for key in {'bu', 'step', 'groups', 'microGroups', 'reshaped'}:
            for meta, obj in zip((myMeta, otherMeta), (self, other)):
                try:
                    meta[key] = getattr(obj, key)
                except AttributeError:
                    meta[key] = None

        matchingKeys = getKeyMatchingShapes(myMeta, otherMeta, 'metadata')
        similar = len(matchingKeys) == len(myMeta)

        for key in sorted(matchingKeys):
            similar &= logDirectCompare(myMeta[key], otherMeta[key],
                                        lower, upper, key)

        return similar

    __docCompare = compareDocReplacer("""
    Return ``True`` if contents of ``{qty}Exp`` and ``{qty}Unc`` agree

    Parameters
    ----------
    other: :class:`HomogUniv`
        Object from which to grab group constant dictionaries
    {sigma}

    Returns
    bool
        If the dictionaries contain identical values with uncertainties,
        and if those values have overlapping confidence intervals
    Raises
    ------
    {compTypeErr}
    """)

    def _helpCompareGCDict(self, other, attrBase, sigma):
        """
        Method that actually compare group constant dictionaries.

        ``attrBase`` is used to find dictionaries by appending
        ``'Exp'`` and ``'Unc'`` to ``attrBase``
        """
        self._checkCompareObj(other)

        valName = (attrBase + 'Exp') if attrBase != 'gc' else 'gc'
        uncName = attrBase + 'Unc'
        try:
            myVals = getattr(self, valName)
            myUncs = getattr(self, uncName)
            otherVals = getattr(other, valName)
            otherUncs = getattr(other, uncName)
        except Exception as ee:
            critical("The following error was raised extracting {} and "
                     "{} from universes {} and {}:\n\t{}"
                     .format(valName, uncName, self, other, ee))
            return False

        keys = getKeyMatchingShapes(myVals, otherVals, valName)
        similar = len(keys) == len(myVals) == len(otherVals)

        for key in keys:
            if key not in myUncs or key not in otherUncs:
                loc = self if key in otherUncs else other
                error("Uncertainty data for {} missing from {}"
                      .format(key, loc))
                similar = False
                continue
            myVal = myVals[key]
            myUnc = myUncs[key]
            otherVal = otherVals[key]
            otherUnc = otherUncs[key]

            similar &= getLogOverlaps(key, myVal, otherVal, myUnc, otherUnc,
                                      sigma, relative=True)
        return similar

    def compareInfData(self, other, sigma):
        return self._helpCompareGCDict(other, 'inf', sigma)

    def compareB1Data(self, other, sigma):
        return self._helpCompareGCDict(other, 'b1', sigma)

    def compareGCData(self, other, sigma):
        return self._helpCompareGCDict(other, 'gc', sigma)

    compareInfData.__doc__ = __docCompare.format(qty='inf')
    compareB1Data.__doc__ = __docCompare.format(qty='b1')
    compareGCData.__doc__ = __docCompare.format(qty='gc')


class BranchContainer(dict):
    """
    Class that stores data for a single branch.

    This container acts like a dictionary, mapping
    :class:`~serpentTools.objects.UnivTuple` to
    :class:`~serpentTools.objects.HomogUniv` corresponding
    to a specific branch state. As such, there is no
    need for the :attr:`universes` dictionary that previously
    served this purpose. However, it is provided for compatibility
    but will be removed after 0.9.0

    The :class:`~serpentTools.BranchingReader` stores
    branch variables and branched group constant data inside these
    container objects. These are used in turn to create
    :class:`~serpentTools.objects.HomogUniv` objects for storing
    group constant data.

    Parameters
    ----------
    filePath: str
        Path to input file from which this container was connected
    branchID: int
        Index for the run for this branch
    branchNames: tuple
        Name of branches provided for this universe
    stateData: dict
        key: value pairs for branch variables

    Attributes
    ----------
    stateData: dict
        Name: value pairs for the variables defined on each
        branch card
    universes: dict

        .. deprecated:: 0.8.0
           Treat this object as the universes dictionary instead
    """

    def __init__(self, filePath, branchID, branchNames, stateData):
        dict.__init__(self)
        self.filePath = filePath
        self.branchID = branchID
        self.stateData = stateData
        self.branchNames = branchNames
        self._orderedUniverses = None

    @property
    def universes(self):
        # For compatibility, remove after 0.9.0
        return self

    def __str__(self):
        return '<BranchContainer for {} from {}>'.format(
            ', '.join(self.branchNames), self.filePath)

    @property
    def orderedUniv(self):
        """Universe keys sorted by ID and by burnup"""
        if not any(self):
            raise SerpentToolsException(
                'No universes stored on branch {}'.format(str(self))
            )
        if self._orderedUniverses is None:
            self._orderedUniverses = tuple(sorted(
                self, key=lambda tpl: (tpl.universe, tpl.step)
            ))
        return self._orderedUniverses

    def __setitem__(self, key, value):
        if not isinstance(value, HomogUniv):
            raise TypeError("{} {}".format(key, type(value)))
        if not isinstance(key, UnivTuple):
            key = UnivTuple(*key)
        dict.__setitem__(self, key, value)

    def update(self, other):
        """Update with contents of another BranchContainer"""
        # Check before making any changes
        temp = {}
        for key, univ in dict(other).items():
            if not isinstance(univ, HomogUniv):
                raise TypeError("{} {}".format(key, type(univ)))
            temp[UnivTuple(*key)] = univ

        dict.update(self, temp)

    def getUniv(self, univID, burnup=None, index=None, days=None):
        """
        Return a specific universe given the ID and time of interest

        Parameters
        ----------
        univID: str
            Unique ID for the desired universe
        burnup: float, optional
            Burnup [MWd/kgU] of the desired universe
        index: int, optional
            Point of interest in the burnup index
        days : float, optional
            Point in time [d] for the desired universe

        Returns
        -------
        :class:`~serpentTools.objects.containers.HomogUniv`
            Requested universe

        Raises
        ------
        KeyError
            If the requested universe could not be found
        :class:`serpentTools.SerpentToolsException`
            If neither burnup nor index are given
        """
        if burnup is None and index is None:
            raise SerpentToolsException('Burnup or index are required inputs')

        searchKey = UnivTuple(univID, burnup, index, days)

        for key, universe in self.items():
            for uItem, sItem in zip(key, searchKey):
                if sItem is None:
                    continue
                if uItem != sItem:
                    break
            else:
                return universe
        raise KeyError(
            "Could not find a universe matching {}".format(searchKey))
