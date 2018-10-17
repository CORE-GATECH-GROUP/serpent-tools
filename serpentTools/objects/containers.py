"""
Custom-built containers for storing data from serpent outputs

Contents
--------
* :py:class:`~serpentTools.objects.containers.HomogUniv`
* :py:class:`~serpentTools.objects.containers.BranchContainer`

"""
from re import compile
from itertools import product

from six import iteritems
from matplotlib import pyplot
from numpy import array, arange, hstack, ndarray, zeros_like

from serpentTools.settings import rc
from serpentTools.objects.base import NamedObject, BaseObject
from serpentTools.utils import (
    convertVariableName,
    getKeyMatchingShapes,
    logDirectCompare,
    getLogOverlaps,
    compareDocReplacer,
    compareDocDecorator,
    magicPlotDocDecorator,
    formatPlot,
)

from serpentTools.objects.base import (DEF_COMP_LOWER,
                                       DEF_COMP_UPPER, DEF_COMP_SIGMA)
from serpentTools.messages import (
    warning,
    SerpentToolsException,
    debug,
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

__all__ = ('HomogUniv', 'BranchContainer', 'SCATTER_MATS', 'SCATTER_ORDERS')


CRIT_RE = compile('K[EI][NF]F')


def isNonNeg(value):
    """Return true if a value is None or non-negative"""
    if value is None:
        return True
    return value >= 0


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
    groups: None or :py:class:`numpy.array`
        Group boundaries from highest to lowest
    numGroups: None or int
        Number of energy groups bounded by ``groups``
    microGroups: None or :py:class:`numpy.array`
        Micro group structure used to produce group constants.
        Listed from lowest to highest

    Raises
    ------
    SerpentToolsException:
        If a negative value of burnup, step, or burnup days is passed

    """

    def __init__(self, name, bu, step, day):
        if not all(isNonNeg(xx) for xx in (bu, step, day)):
            tail = ['{}: {}'.format(valName, val)
                    for valName, val in zip(('burnup', 'index', 'days'),
                                            (bu, step, day))]
            raise SerpentToolsException(
                "Will not create universe with negative burnup\n{}"
                .format(', '.join(tail)))
        NamedObject.__init__(self, name)
        if step is not None and step == 0:
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
            extras.append('burnup: {:5.3f} MWd/kgu'.format(self.bu))
        if self.step:
            extras.append('step: {}'.format(self.step))
        if self.day is not None:
            extras.append('{:5.3f} days'.format(self.day))
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

        Makes sure all vectors, everything but keff/kinf data, are
        converted to numpy arrays. Reshapes scattering matrices
        if number of groups is known and ``xs.reshapeScatter``
        """
        if not isinstance(value, ndarray):
            value = array(value)
        if CRIT_RE.search(name):
            return value[0]
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
        dx = setter.get(variableName)
        return x, dx

    def _lookup(self, variableName, uncertainty):
        if 'inf' == variableName[:3]:
            if not uncertainty:
                return self.infExp
            return self.infUnc
        elif "b1" == variableName[:2]:
            if not uncertainty:
                return self.b1Exp
            return self.b1Unc
        return self.gcUnc if uncertainty else self.gc

    @magicPlotDocDecorator
    def plot(self, qtys, limitE=True, ax=None, logx=True, logy=True,
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
        * :py:meth:`serpentTools.objects.containers.HomogUniv.get`

        """
        qtys = [qtys, ] if isinstance(qtys, str) else qtys
        ax = ax or pyplot.axes()
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
            valD = self._lookup(key, False)
            if key not in valD:
                warning("{} not found on object. Will not plot."
                        .format(key))
                continue
            yVals = valD[key]
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
            xdata = self.__getEGrid(nbins, macroBins, microBins)
            if limitE:
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

        if legend is None:
            legend = len(qtys) > 1
        if loglog is not None:
            logx = logy = loglog
        formatPlot(ax, logx=logx, logy=logy, ncol=ncol,
                   legend=legend, xlabel=xlabel or "Energy [MeV]",
                   ylabel=ylabel)
        return ax

    def __getEGrid(self, nbins, macroBins, microBins):
        """Attempt to obtian the correct energy group for plotting."""
        if macroBins is not None and nbins == macroBins:
            return self.groups
        if microBins is not None and nbins == microBins:
            return self.microGroups
        return arange(nbins)

    def __formatLabel(self, label, key):
        mapping = {
            "{k}": key, "{u}": self.name, "{i}": self.step,
            "{b}": self.bu, "{d}": self.day
        }
        for lookF, value in iteritems(mapping):
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


class BranchContainer(BaseObject):
    """
    Class that stores data for a single branch.

    The :py:class:`~serpentTools.parsers.branching.BranchingReader` stores
    branch variables and branched group constant data inside these
    container objects. These are used in turn to create
    :py:class:`~serpentTools.objects.containers.HomogUniv` objects for storing
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
        Dictionary storing the homogenized universe objects.
        Keys are tuples of
        ``(universeID, burnup, burnIndex)``
    """
    __mismatchedBurnup = ("Was not expecting a {} value of burnup. "
                          "Expect burnup in units of {}")

    def __init__(self, filePath, branchID, branchNames, stateData):
        self.filePath = filePath
        self.branchID = branchID
        self.stateData = stateData
        self.universes = {}
        self.branchNames = branchNames
        self.__orderedUniverses = None
        self.__keys = set()
        self.__hasDays = None

    def __str__(self):
        return '<BranchContainer for {} from {}>'.format(
            ', '.join(self.branchNames), self.filePath)

    def __contains__(self, item):
        return item in self.__keys or item in self.stateData

    @property
    def orderedUniv(self):
        """Universe keys sorted by ID and by burnup"""
        if not any(self.universes):
            raise SerpentToolsException(
                'No universes stored on branch {}'.format(str(self))
            )
        if self.__orderedUniverses is None:
            self.__orderedUniverses = tuple(sorted(
                self.__keys, key=lambda tpl: (tpl[0], tpl[2])
            ))
        return self.__orderedUniverses

    def addUniverse(self, univID, burnup=0, burnIndex=0, burnDays=0):
        """
        Add a universe to this branch.

        Data for the universes are produced at specific points in time.
        The additional arguments help track of when the data for this
        universe were created.
        A negative value of ``burnup`` indicates the units on burnup are
        really ``days``. Therefore, the value of ``burnDays`` and ``burnup``
        will be swapped.

        .. warning::

            This method will overwrite data for universes that already exist

        Parameters
        ----------
        univID: int or str
            Identifier for this universe
        burnup: float or int
        """
        if self.__hasDays is None and burnup:
            self.__hasDays = burnup < 0
        if burnup < 0:
            if not self.__hasDays:
                raise SerpentToolsException(self.__mismatchedBurnup.format(
                    'negative', 'MWd/kgU'))
            burnup, burnDays = None if burnup else 0, - burnup
        else:
            if self.__hasDays and not burnDays:
                raise SerpentToolsException(self.__mismatchedBurnup.format(
                    'positive', 'days'))
            burnDays = None if burnup else 0
        newUniv = HomogUniv(univID, burnup, burnIndex, burnDays)
        key = (univID, burnup or burnDays, burnIndex)
        if key in self.__keys:
            warning('Overwriting existing universe {} in {}'
                    .format(key, str(self)))
        else:
            self.__keys.add(key)
        self.universes[key] = newUniv
        return newUniv

    def getUniv(self, univID, burnup=None, index=None):
        """
        Return a specific universe given the ID and time of interest

        If burnup and index are given, burnup is used to search

        Parameters
        ----------
        univID: int
            Unique ID for the desired universe
        burnup: float or int
            Burnup [MWd/kgU] of the desired universe
        index: int
            Point of interest in the burnup index

        Returns
        -------
        :py:class:`~serpentTools.objects.containers.HomogUniv`
            Requested universe

        Raises
        ------
        KeyError:
            If the requested universe could not be found
        SerpentToolsException:
            If neither burnup nor index are given
        """
        if burnup is None and index is None:
            raise SerpentToolsException('Burnup or index are required inputs')
        searchIndex = 2 if index is not None else 1
        searchValue = index if index is not None else burnup
        for key in self.__keys:
            if key[0] == univID and key[searchIndex] == searchValue:
                debug('Found universe that matches with keys {}'
                      .format(key))
                return self.universes[key]
        searchName = 'burnup' + ('' if index is None else ' index')
        raise KeyError(
            'Could not find a universe that matched requested universe {} and '
            '{} {}'.format(univID, searchName, searchValue))

    @property
    def hasDays(self):
        """Returns True if the burnups in the file are in units of days"""
        if self.__hasDays is None:
            raise AttributeError("Need to load at least one universe with "
                                 "non-zero burnup first.""")
        return self.__hasDays
