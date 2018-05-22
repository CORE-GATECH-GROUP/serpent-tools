""" 
Custom-built containers for storing data from serpent outputs

Contents
--------
* :py:class:`~serpentTools.objects.containers.HomogUniv`
* :py:class:`~serpentTools.objects.containers.BranchContainer`
* :py:class:`~serpentTools.objects.containers.DetectorBase`
* :py:class:`~serpentTools.objects.containers.Detector`

"""
from re import compile
from collections import OrderedDict
from itertools import product

from six import iteritems
from matplotlib import pyplot
from numpy import (array, arange, unique, log, divide, ones_like, hstack,
                   ndarray, zeros_like)

from serpentTools.settings import rc
from serpentTools.plot import (cartMeshPlot, plot, magicPlotDocDecorator,
                               formatPlot)
from serpentTools.objects import NamedObject
from serpentTools.utils import convertVariableName
from serpentTools.messages import warning, SerpentToolsException, debug, info

DET_COLS = ('value', 'energy', 'universe', 'cell', 'material', 'lattice',
            'reaction', 'zmesh', 'ymesh', 'xmesh', 'tally', 'error', 'scores')
"""Name of the columns of the data"""

SCATTER_MATS = set()
SCATTER_ORDERS = 8

for xsSpectrum, xsType in product({'INF', 'B1'},
                                  {'S', 'SP'}):
    SCATTER_MATS.update({'{}_{}{}'.format(xsSpectrum, xsType, xx)
                        for xx in range(SCATTER_ORDERS)})

HOMOG_VAR_TO_ATTR = {
    'MICRO_E': 'microGroups', 'MICRO_NG': 'numMicroGroups',
    'MACRO_E': 'groups', 'MACRO_NG': 'numGroups'}

__all__ = ('DET_COLS', 'HomogUniv', 'BranchContainer', 'Detector',
           'DetectorBase', 'SCATTER_MATS', 'SCATTER_ORDERS')


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
            tail = ['{}: {}'.format(name, val)
                for name, val in zip(('burnup', 'index', 'days'),
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
        elif "b1" ==  variableName[:2]:
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

class DetectorBase(NamedObject):
    """
    Base class for classes that store detector data

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    {attrs:s}
    """

    baseParams = """name: str
        Name of this detector"""
    baseAttrs = """grids: dict
        Dictionary with additional data describing energy grids or mesh points
    tallies: None or numpy.array
        Reshaped tally data to correspond to the bins used
    errors: None or numpy.array
        Reshaped relative error data corresponding to bins used
    scores: None or numpy.array
        Reshaped array of tally scores. SERPENT 1 only
    indexes: None or OrderedDict
        Collection of unique indexes for each requested bin"""
    __doc__ = __doc__.format(params=baseParams, attrs=baseAttrs)

    def __init__(self, name):
        NamedObject.__init__(self, name)
        self.tallies = None
        self.errors = None
        self.scores = None
        self.grids = {}
        self.indexes = None
        self._map = None

    def _isReshaped(self):
        raise NotImplementedError

    def slice(self, fixed, data='tallies'):
        """
        Return a view of the reshaped array where certain axes are fixed

        Parameters
        ----------
        fixed: dict
            dictionary to aid in the restriction on the multidimensional
            array. Keys correspond to the various grids present in
            ``indexes`` while the values are used to
        data: {'tallies', 'errors', 'scores'}
            Which data set to slice

        Returns
        -------
        numpy.array
            View into the respective data where certain dimensions
            have been removed

        Raises
        ------
        SerpentToolsException
            If the data has not been reshaped or is None [e.g. scores]
        KeyError
            If the data set to slice not in the allowed selection

        """
        if not self._isReshaped():
            raise SerpentToolsException(
                'Slicing requires detector to be reshaped')
        if data not in self._map:
            raise KeyError(
                'Data argument {} not in allowed options'
                '\n{}'.format(data, ', '.join(self._map.keys())))
        work = self._map[data]
        if work is None:
            raise SerpentToolsException(
                '{} data for detector {} is None. '
                'Cannot perform slicing'.format(data, self.name))
        if not fixed:
            return work
        return work[self._getSlices(fixed)]

    def _getSlices(self, fixed):
        """
        Return a list of slice operators for each axis in reshaped data

        Parameters
        ----------
        fixed: dict
            Dictionary where keys are strings pointing to dimensions in
        """
        fixed = fixed if fixed is not None else {}
        keys = set(fixed.keys())
        slices = []
        for key in self.indexes:
            if key in keys:
                slices.append(fixed[key])
                keys.remove(key)
            else:
                slices.append(slice(0, len(self.indexes[key])))
        if any(keys):
            warning(
                'Could not find arguments in index that match the following'
                ' requested slice keys: {}'.format(', '.join(keys)))
        return slices
    
    @magicPlotDocDecorator
    def spectrumPlot(self, fixed=None, ax=None, normalize=True, xlabel=None,
                     ylabel=None, steps=True, logx=True, logy=False, loglog=False, 
                     sigma=3, labels=None, legend=False, ncol=1, title=None, 
                     **kwargs):
        """
        Quick plot of the detector value as a function of energy.

        Parameters
        ----------
        fixed: None or dict
            Dictionary controlling the reduction in data
        {ax}
        normalize: bool
            Normalize quantities per unit lethargy
        {xlabel}
        {ylabel}
        steps: bool
            Plot tally as constant inside bin
        {logx}
        {logy}
        {loglog}
        {sigma}
        {labels}
        {legend}
        {ncol}
        {title}
        {kwargs} :py:func:`matplotlib.pyplot.plot` or 
            :py:func:`matplotlib.pyplot.errorbar`

        Returns
        -------
        {rax}

        Raises
        ------
        SerpentToolsException
            if number of rows in data not equal to
            number of energy groups

        See Also
        --------
        :py:meth:`~serpentTools.objects.containers.DetectorBase.slice`
        """
        slicedTallies = self.slice(fixed, 'tallies').copy()
        if len(slicedTallies.shape) > 2:
            raise SerpentToolsException(
                'Sliced data cannot exceed 2-D for spectrum plot, not '
                '{}'.format(slicedTallies.shape)
            )
        elif len(slicedTallies.shape) == 1:
            slicedTallies = slicedTallies.reshape(slicedTallies.size, 1)
        lowerE = self.grids['E'][:, 0]
        if normalize:
            lethBins = log(
                divide(self.grids['E'][:, -1], lowerE))
            for indx in range(slicedTallies.shape[1]):
                scratch = divide(slicedTallies[:, indx], lethBins)
                slicedTallies[:, indx] = scratch / scratch.max() 
        
        if steps:
            if 'drawstyle' in kwargs:
                debug('Defaulting to drawstyle specified in kwargs as {}'
                      .format(kwargs['drawstyle']))
            else:
                kwargs['drawstyle'] = 'steps-post'
        
        if sigma:
            slicedErrors = sigma * self.slice(fixed, 'errors').copy()
            slicedErrors = slicedErrors.reshape(slicedTallies.shape) * slicedTallies
        else:
            slicedErrors = None
        ax = plot(lowerE, slicedTallies, ax=ax, labels=labels, yerr=slicedErrors, **kwargs)     
        if ylabel is None:
            ylabel = 'Tally data'
            ylabel += ' normalized per unit lethargy' if normalize else ''
            ylabel += ' $\pm${}$\sigma$'.format(sigma) if sigma else ''
        
        ax = formatPlot(ax, loglog=loglog, logx=logx, ncol=ncol,
                        xlabel=xlabel or "Energy [MeV]", ylabel=ylabel, 
                        legend=legend, title=title)
        return ax
    
    @magicPlotDocDecorator
    def plot(self, xdim=None, what='tallies', sigma=None, fixed=None, ax=None,
             xlabel=None, ylabel=None, steps=False, labels=None, logx=False, 
             logy=False, loglog=False, legend=False, ncol=1, title=None,
             **kwargs):
        """
        Simple plot routine for 1- or 2-D data

        Parameters
        ----------
        xdim: None or str
            If not None, use the array under this key in ``indexes`` as
            the x axis
        what: {'tallies', 'errors', 'scores'}
            Primary data to plot
        {sigma}
        fixed: None or dict
            Dictionary controlling the reduction in data down to one dimension
        {ax}
        {xlabel} If ``xdim`` is given and ``xlabel`` is ``None``, then 
            ``xdim`` will be applied to the x-axis.
        {ylabel}
        steps: bool
            If true, plot the data as constant inside the respective bins.
            Sets ``drawstyle`` to be ``steps-post`` unless ``drawstyle``
            given in ``kwargs``
        {labels}
        {logx}
        {logy}
        {loglog}
        {legend}
        {ncol}
        {title}
        {kwargs} :py:func:`~matplotlib.pyplot.plot` or
            :py:func:`~matplotlib.pyplot.errorbar` function.

        Returns
        -------
        {rax}

        Raises
        ------
        SerpentToolsException
            If data contains more than 2 dimensions

        See Also
        --------
        * :py:meth:`~serpentTools.objects.containers.Detector.slice`
        * :py:meth:`~serpentTools.objects.containers.DetectorBase.spectrumPlot`
           better options for plotting energy spectra
        """

        data = self.slice(fixed, what)
        if len(data.shape) > 2:
            raise SerpentToolsException(
                'Data must be constrained to 1- or 2-D, not {}'.format(data.shape))
        elif len(data.shape) == 1:
            data = data.reshape(data.size, 1)

        if sigma:
            if what != 'errors':
                yerr = self.slice(fixed, 'errors').reshape(data.shape) * data * sigma
            else:
                warning(
                    'Will not plot error bars on the error plot. Data to be '
                    'plotted: {}.  Sigma: {}'.format(what, sigma))
                yerr = None
        else: 
           yerr = None

        xdata, autoX = self._getPlotXData(xdim, data)
        xlabel = xlabel or autoX
        ylabel = ylabel or "Tally data" 
        ax = ax or pyplot.axes()
        
        if steps:
            if 'drawstyle' in kwargs:
                debug('Defaulting to drawstyle specified in kwargs as {}'
                      .format(kwargs['drawstyle']))
            else:
                kwargs['drawstyle'] = 'steps-post'
        ax = plot(xdata, data, ax, labels, yerr,**kwargs)
        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy, ncol=ncol,
                        xlabel=xlabel, ylabel=ylabel, legend=legend, 
                        title=title)
        return ax

    @magicPlotDocDecorator
    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None, 
                 logx=False, logy=False, loglog=False, title=None, **kwargs):
        """
        Plot tally data as a function of two mesh dimensions

        Parameters
        ----------
        xdim: str
            Primary dimension - will correspond to x-axis on plot
        ydim: str
            Secondary dimension - will correspond to y-axis on plot
        what: {'tallies', 'errors', 'scores'}
            Color meshes from tally data, uncertainties, or scores
        fixed: None or dict
            Dictionary controlling the reduction in data down to one dimension
        {ax}
        {cmap}
        logColor: bool
            If true, apply a logarithmic coloring to the data positive 
            data
        {xlabel}
        {ylabel}
        {logx}
        {logy}
        {loglog}
        {title}
        {kwargs} :py:func:`~matplotlib.pyplot.pcolormesh`

        Returns
        -------
        {rax}

        Raises
        ------
        SerpentToolsException
            If data to be plotted, with or without constraints, is not 1D
        KeyError
            If the data set by ``what`` not in the allowed selection
        ValueError
            If the data contains negative quantities and ``logColor`` is
            ``True``

        See Also
        --------
        * :py:meth:`~serpentTools.objects.containers.DetectorBase.slice`
        * :py:func:`matplotlib.pyplot.pcolormesh`
        * :py:func:`~serpentTools.plot.cartMeshPlot`
        """
        if fixed:
            for qty, name in zip((xdim, ydim), ('x', 'y')):
                if qty in fixed:
                    raise SerpentToolsException(
                        'Requested {} dimension {} is one of the axis to be constrained. '
                        .format(name, qty))

        data = self.slice(fixed, what)
        dShape = data.shape
        if len(dShape) != 2:
            raise SerpentToolsException(
                'Data must be 2D for mesh plot, currently is {}.\nConstraints:'
                '{}'.format(dShape, fixed)
            )
        xgrid = self._getGrid(xdim)
        ygrid = self._getGrid(ydim)
        if data.shape != (ygrid.size - 1, xgrid.size - 1):
            data = data.T

        ax = cartMeshPlot(data, xgrid, ygrid, ax, cmap, logColor, **kwargs)
        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy,
                        xlabel=xlabel or xdim, ylabel=ylabel or ydim,
                        title=title)
        return ax

    def _getGrid(self, qty):
        grids = self._inGridsAs(qty)
        if grids is not None:
            lowBounds = grids[:, 0]
            return hstack((lowBounds, grids[-1, 1]))
        if qty not in self.indexes:
            raise KeyError("No index {} found on detector. Bin indexes: {}"
                           .format(qty, ', '.join(self.indexes.keys())))
        bins = self.indexes[qty]
        return hstack((bins, len(bins)))

    def _dimInGrids(self, key):
        return key[0].upper() in self.grids

    def _inGridsAs(self, qty):
        if self._dimInGrids(qty):
            return self.grids[qty[0].upper()]
        return None

    def _getPlotXData(self, qty, ydata):
        fallback = arange(len(ydata)), 'Bin Index'
        if qty is None:
            return fallback
        xdata = self._inGridsAs(qty)
        if xdata is not None:
            return xdata[:, 0], qty
        if qty in self.indexes:
            return self.indexes[qty], qty
        return fallback


class Detector(DetectorBase):
    """
    Class that stores detector data from a single detector file

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    bins: numpy.ndarray
        Tally data directly from SERPENT file
    {attrs:s}
    """
    __doc__ = __doc__.format(params=DetectorBase.baseParams,
                             attrs=DetectorBase.baseAttrs)

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
        for index, indexName in enumerate(DET_COLS):
            if 0 < index < 10:
                uniqueVals = unique(self.bins[:, index])
                if len(uniqueVals) > 1:
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


class BranchContainer(object):
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
            Value of burnup [MWd/kgU]. A negative value here indicates
            the value is really in units of days.
        burnIndex: int
            Point in the depletion schedule
        burnDays: int or float
            Point in time

        Returns
        -------
        serpentTools.objects.containers.HomogUniv
            Empty new universe

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

