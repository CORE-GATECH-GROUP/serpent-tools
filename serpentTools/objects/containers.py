"""
Custom-built containers for storing data from serpent outputs

Contents
--------
:py:class:`~serpentTools.objects.containers.HomogUniv`
:py:class:`~serpentTools.objects.containers.BranchContainer
:py:class:`~serpentTools.objects.containers.Detector`

"""
from collections import OrderedDict

from matplotlib import pyplot

from numpy import array, arange, unique, log, divide, ones_like

from serpentTools.plot import cartMeshPlot
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


class Detector(NamedObject):
    """
    Class to store detector data.

    Parameters
    ----------
    name: str
        Name of this detector

    Attributes
    ----------
    bins: numpy.array
        Tallies straight from the detector file
    grids: dict
        Dictionary with additional data describing energy grids or mesh points
    tallies: None or numpy.array
        Reshaped tally data to correspond to the bins used
    errors: None or numpy.array
        Reshaped relative error data corresponding to bins used
    scores: None or numpy.array
        Reshaped array of tally scores. SERPENT 1 only
    indexes: None or OrderedDict
        Collection of unique indexes for each requested bin
    """

    def __init__(self, name):
        NamedObject.__init__(self, name)
        self.bins = None
        self.tallies = None
        self.errors = None
        self.scores = None
        self.grids = {}
        self.__reshaped = False
        self.indexes = None
        self._map = None

    def __len__(self):
        if self.bins is not None:
            return self.bins.shape[0]
        return 0

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
                    self.indexes[indexName] = array(uniqueVals, dtype=int)
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

    def slice(self, fixed, data='tallies'):
        """
        Return a slice of the reshaped array where certain axes are fixed

        Parameters
        ----------
        data: {'tallies', 'errors', 'scores'}
            Which data set to slice
        fixed: dict
            dictionary to aid in the restriction on the multidimensional
            array. Keys correspond to the various grids present in
            ``indexes`` while the values are used to

        Returns
        -------
        reduced: numpy.array
            View into the respective data where certain dimensions
            have been removed

        Raises
        ------
        SerpentToolsException
            If the data has not been reshaped or is None [e.g. scores]
        KeyError
            If the data set to slice not in the allowed selection

        """
        if not self.__reshaped:
            raise SerpentToolsException(
                'Slicing requires detector to be reshaped')
        if data not in self._map:
            raise KeyError(
                'Data argument {} not in allowed options'
                '\n{}'.format(data, ', '.join(self._map.keys())))
        work = self._map[data]
        if work is None:
            raise SerpentToolsException(
                '{} data for detector {} is None. Cannot perform slicing'
                .format(data, self.name))
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
                slices.append(fixed[key] - 1)
                keys.remove(key)
            else:
                slices.append(slice(0, len(self.indexes[key])))
        if any(keys):
            warning(
                'Could not find arguments in index that match the following'
                ' requested slice keys: {}'.format(', '.join(keys)))
        return slices

    def spectrumPlot(self, fixed=None, ax=None, normalize=True, xlabel=None,
                     ylabel=None, steps=True, xscale='log', yscale='linear',
                     sigma=3, **kwargs):
        """
        Quick plot of the detector value as a function of energy.

        Parameters
        ----------
        fixed: None or dict
            Dictionary controlling the reduction in data down to one dimension
        ax: pyplot.Axes or None
            Ax on which to plot the data
        normalize: bool
            Normalize quantities per unit lethargy
        xlabel: str or None
            Label for x-axis. Defaults to 'Energy [MeV]'
        ylabel: str or None
            Label for y axis
        steps: bool
            Plot tally as constant inside bin
        xscale: {'log', 'linear'}
            Scale to apply to x axis
        yscale: {'log', 'linear'}
            Scale to apply to y axis
        sigma: int
            Level of confidence to apply to errors. Use for no error bars
        kwargs:
            Additional arguments to pass to plot command
        Returns
        -------
        ax: pyplot.Axes
            Axes on which the data was plotted

        Raises
        ------
        SerpentToolsException
            if number of rows in data not equal to
            number of energy groups

        See Also
        --------
        :py:meth:`~serpentTools.objects.containers.Detector.slice`
        """
        if not len(self.tallies.shape) == 1 and fixed is None:
            raise SerpentToolsException(
                'Tally data is not a one-dimensional matrix. '
                'Need constraining aguments in fixed dictionary'
            )
        slicedTallies = self.slice(fixed, 'tallies')
        if not len(slicedTallies.shape) == 1:
            raise SerpentToolsException(
                'Sliced data must be one-dimensional for spectrum plot, not {}'
                .format(slicedTallies.shape)
            )
        if normalize:
            lethBins = log(
                divide(self.grids['E'][:, -1], self.grids['E'][:, 0]))
            slicedTallies = divide(slicedTallies, lethBins)
            slicedTallies = slicedTallies / slicedTallies.max()
        ax = ax or pyplot.axes()
        if steps:
            if 'drawstyle' in kwargs:
                debug('Defaulting to drawstyle specified in kwargs as {}'
                      .format(kwargs['drawstyle']))
                drawstyle = kwargs.pop('drawstyle')
            else:
                drawstyle = 'steps-post'
        else:
            drawstyle = None
        if sigma:
            slicedErrors = sigma * self.slice(fixed, 'errors') * slicedTallies
            ax.errorbar(self.grids['E'][:, 0], slicedTallies,
                        yerr=slicedErrors,
                        drawstyle=drawstyle, **kwargs)
        else:
            ax.plot(self.grids['E'][:, 0], slicedTallies, drawstyle=drawstyle,
                    **kwargs)
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)
        ax.set_xlabel(xlabel or 'Energy [MeV]')
        ylabel = ylabel or 'Neutron flux' + (' normalized per unit lethargy'
                                             if normalize else '')
        ax.set_ylabel(ylabel)

        return ax

    def plot(self, xdim=None, what='tallies', sigma=None, fixed=None, ax=None,
             xlabel=None, ylabel=None, steps=False, **kwargs):
        """
        Shortcut routine for plotting 1D data

        Parameters
        ----------
        xdim: None or str
            If not None, use the array under this key in ``indexes`` as
            the x axis
        what: {'tallies', 'errors', 'scores'}
            Primary data to plot
        sigma: None or int
            If given, apply this level of confidence to absolute errors.
            If not given, then error bars will not be used
        fixed: None or dict
            Dictionary controlling the reduction in data down to one dimension
        ax: axes or None
            Axes on which to plot the data
        xlabel: None or str
            If given, apply this label to the x-axis. If ``xdim`` is given
            and ``xlabel`` is ``None``, then ``xdim`` will be applied to the
            x-axis
        ylabel: None or str
            If given, label to apply to y-axis
        steps: bool
            If true, plot the data as constant inside the respective bins.
            Sets ``drawstyle`` to be ``steps-post`` unless ``drawstyle``
            given in ``kwargs``
        kwargs: dict
            additional arguments to pass to the
            :py:func:`~matplotlib.pyplot.plot`  of
            :py:func:`~matplotlib.pyplot.errorbar` function.

        Returns
        -------
        ax: matplotlib.AxesSubplot

        Raises
        ------
        SerpentToolsException: If the data is not constrained to 1D

        See Also
        --------
        * :py:meth:`~serpentTools.objects.containers.Detector.slice`
        * :py:meth:`~serpentTools.objects.containers.Detector.spectrumPlot`
          better options for plotting energy spectra
        """
        data = self.slice(fixed, what)
        if len(data.shape) != 1:
            raise SerpentToolsException(
                'Data must be constrained to 1D, not {}'.format(data.shape))
        if sigma:
            if what != 'errors':
                errors = self.slice(fixed, 'errors') * data * sigma
            else:
                warning(
                    'Will not plot error bars on the error plot. Data to be '
                    'plotted: {}.  Sigma: {}'.format(what, sigma))
                errors = None
        else:
            errors = None
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
                drawstyle = kwargs.pop('drawstyle')
            else:
                drawstyle = 'steps-post'
        else:
            drawstyle = None
        if errors is None:
            ax.plot(xdata, data, drawstyle=drawstyle, **kwargs)
        else:
            ax.errorbar(xdata, data, yerr=errors, drawstyle=drawstyle,
                        **kwargs)
        if xlabel is not None:
            ax.set_xlabel(xlabel)
        if ylabel is not None:
            ax.set_ylabel(ylabel)
        return ax

    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, addcbar=True, xlabel=None, ylabel=None,
                 xscale='linear', yscale='linear'):
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
        ax: axes or None
            Axes on which to plot the data
        cmap: None or str
            Colormap to apply to the figure. If None, use default colormap
        addcbar: bool
            If True, add a colorbar to the figure
        xlabel: None or str
            Label to apply to x-axis. If not given, defaults to xdim
        ylabel: None or str
            Label to apply to y-axis. If not given, defaults to xdim
        xscale: {'log', 'linear'}
            Scale to apply to x-axis
        yscale: {'log', 'linear'}
            Scale to apply to y-axis

        Returns
        -------
        ax: pyplot.Axes
            Ax on which the data was plotted

        Raises
        ------
        SerpentToolsException
            If data to be plotted, with or without constraints, is 2D
        KeyError
            If the data set by ``what`` not in the allowed selection

        See Also
        --------
        :py:meth:`~serpentTools.objects.containers.Detector.slice`
        """
        data = self.slice(fixed, what)
        if len(data.shape) != 2:
            raise SerpentToolsException(
                'Data must be 2D for mesh plot, currently is {}.\nConstraints:'
                '{}'.format(data.shape, fixed)
            )
        if xdim[0].upper() in self.grids:
            xgridFull = self.grids[xdim[0].upper()]
            xgrid = xgridFull[:, 0]
            widths = xgridFull[:, 1] - xgrid
            del xgridFull
        else:
            xgrid = self.indexes[xdim] - 1
            widths = ones_like(xgrid)

        if ydim[0].upper() in self.grids:
            ygridFull = self.grids[xdim[0].upper()]
            ygrid = ygridFull[:, 0]
            heights = ygridFull[:, 1] - ygrid
            del ygridFull
        else:
            ygrid = self.indexes[ydim] - 1
            heights = ones_like(ygrid)
        if data.shape != (ygrid.size, xgrid.size):
            data = data.T

        ax = cartMeshPlot(data, xgrid, ygrid, widths, heights, ax, cmap,
                          addcbar)

        ax.set_xlabel(xlabel or xdim)
        ax.set_ylabel(ylabel or ydim)
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)

        return ax


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
