""" Custom-built containers for storing data from serpent outputs

Contents
--------
:py:class:`~serpentTools.objects.containers.HomogUniv`
:py:class:`~serpentTools.objects.containers.BranchContainer
:py:class:`~serpentTools.objects.containers.Detector`

"""
from collections import OrderedDict

from matplotlib import pyplot

from numpy import array, arange, unique, log, divide, ones_like, hstack

from serpentTools.plot import cartMeshPlot, plot, magicPlotDocDecorator
from serpentTools.objects import NamedObject, convertVariableName
from serpentTools.messages import warning, SerpentToolsException, debug

DET_COLS = ('value', 'energy', 'universe', 'cell', 'material', 'lattice',
            'reaction', 'zmesh', 'ymesh', 'xmesh', 'tally', 'error', 'scores')
"""Name of the columns of the data"""


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
    bu: float
        burnup value
    step: float
        temporal step
    day: float
        depletion day
    infExp: dict
        Expected values for infinite medium group constants
    infUnc: dict
        Relative uncertainties for infinite medium group constants
    b1Exp: dict
        Expected values for leakage corrected group constants
    b1Unc: dict
        Relative uncertainties for leakage-corrected group constants
    metadata: dict
        Other values that do not not conform to inf/b1 dictionaries
    """

    def __init__(self, name, bu, step, day):
        NamedObject.__init__(self, name)
        self.bu = bu
        self.step = step
        self.day = day
        # Dictionaries:
        self.b1Exp = {}
        self.infExp = {}
        self.b1Unc = {}
        self.infUnc = {}
        self.metadata = {}

    def addData(self, variableName, variableValue, uncertainty=False):
        """
        Sets the value of the variable and, optionally, the associate s.d.

        .. warning::

            This method will overwrite data for variables that already exist

        Parameters
        ----------
        variableName: str
            Variable Name
        variableValue:
            Variable Value
        uncertainty: bool
            Set to ``True`` in order to retrieve the
            uncertainty associated to the expected values

        Raises
        ------
        TypeError
            If the uncertainty flag is not boolean

        """

        # 1. Check the input type
        variableName = convertVariableName(variableName)
        if not isinstance(uncertainty, bool):
            raise TypeError('The variable uncertainty has type {}, '
                            'should be boolean.'.format(type(uncertainty)))
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variableName, uncertainty)
        # 3. Check if variable is already present. Then set the variable.
        if variableName in setter:
            warning("The variable {} will be overwritten".format(variableName))
        setter[variableName] = variableValue

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
            Associated uncertainty

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
        if setter is self.metadata:
            warning('No uncertainty is associated to metadata')
            return x
        setter = self._lookup(variableName, True)
        if variableName not in setter:
            raise KeyError(
                "Variable {} absent from uncertainty dictionary".format(
                    variableName))
        dx = setter.get(variableName)
        return x, dx

    def _lookup(self, variableName, uncertainty):
        if "inf" in variableName:
            if not uncertainty:
                return self.infExp
            else:
                return self.infUnc
        elif "b1" in variableName:
            if not uncertainty:
                return self.b1Exp
            else:
                return self.b1Unc
        else:
            return self.metadata


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
                     sigma=3, labels=None, **kwargs):
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
        if loglog or logx:
            ax.set_xscale('log')
        if loglog or logy:
            ax.set_yscale('log')
        ax.set_xlabel(xlabel or 'Energy [MeV]')
        ylabel = ylabel or 'Tally data' + (' normalized per unit lethargy'
                                             if normalize else '')
        ax.set_ylabel(ylabel)

        return ax
    
    @magicPlotDocDecorator
    def plot(self, xdim=None, what='tallies', sigma=None, fixed=None, ax=None,
             xlabel=None, ylabel=None, steps=False, labels=None, 
             logx=False, logy=False, loglog=False, **kwargs):
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
        if xdim is not None:
            if xdim in self.indexes:
                xdata = self.indexes[xdim]
                xlabel = xlabel or xdim
            else:
                warning('Could not find key {} in indexes: Options: {}'
                        .format(xdim, ', '.join(self.indexes.keys())))
                xdata = arange(len(data))
        else:
            xdata = arange(len(data))

        ax = ax or pyplot.axes()
        
        if steps:
            if 'drawstyle' in kwargs:
                debug('Defaulting to drawstyle specified in kwargs as {}'
                      .format(kwargs['drawstyle']))
            else:
                kwargs['drawstyle'] = 'steps-post'
        ax = plot(xdata, data, ax, labels, yerr,**kwargs)
        
        if xlabel is not None:
            ax.set_xlabel(xlabel)
        if ylabel is not None:
            ax.set_ylabel(ylabel)
        if loglog or logx:
            ax.set_xscale('log')
        if loglog or logy:
            ax.set_yscale('log')
        return ax
    
    @magicPlotDocDecorator
    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None, 
                 logx=False, logy=False, loglog=False, **kwargs):
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
        ax.set_xlabel(xlabel or xdim)
        ax.set_ylabel(ylabel or ydim)
        if loglog or logx:
            ax.set_xscale('log')
        if loglog or logy:
            ax.set_yscale('log')
        return ax

    def _getGrid(self, qty):
        if qty[0].upper() in self.grids:
            grid = self.grids[qty[0].upper()]
            lowBounds = grid[:, 0]
            return hstack((lowBounds, grid[-1, 1]))
        if qty not in self.indexes:
            raise KeyError("No index {} found on detector. Bin indexes: {}"
                           .format(qty, ', '.join(self.indexes.keys())))
        bins = self.indexes[qty]
        return hstack((bins, len(bins)))


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

    def __init__(self, filePath, branchID, branchNames, stateData):
        self.filePath = filePath
        self.branchID = branchID
        self.stateData = stateData
        self.universes = {}
        self.branchNames = branchNames
        self.__orderedUniverses = None
        self.__keys = set()

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
        The additional arguments help track when the data for this
        universe were created.

        .. warning::

            This method will overwrite data for universes that already exist

        Parameters
        ----------
        univID: int or str
            Identifier for this universe
        burnup: float or int
            Value of burnup [MWd/kgU]
        burnIndex: int
            Point in the depletion schedule
        burnDays: int or float
            Point in time

        Returns
        -------
        newUniv: serpentTools.objects.containers.HomogUniv
        """
        newUniv = HomogUniv(univID, burnup, burnIndex, burnDays)
        key = tuple(
            [univID, burnup, burnIndex] + ([burnDays] if burnDays else []))
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
        univ: serpentTools.objects.containers.HomogUniv
            Requested Universe

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
