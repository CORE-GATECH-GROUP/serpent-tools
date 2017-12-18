"""
Custom-built containers for storing data from serpent outputs

Contents
--------
:py:class:`~serpentTools.objects.containers.HomogUniv`
:py:class:`~serpentTools.objects.containers.BranchContainer
:py:class:`~serpentTools.objects.containers.Detector`

"""
from collections import OrderedDict
import six

from numpy import empty, arange, unique, log, divide
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection

from serpentTools.objects import SupportingObject, NamedObject
from serpentTools.messages import warning, SerpentToolsException, debug


class HomogUniv(SupportingObject):
    """
    Class for storing homogenized universe specifications and retrieving them

    Parameters
    ----------
    container: serpentTools.objects.readers.BaseReader or
        serpentTools.objects.containers.BranchContainer
        Object to which this universe is attached
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

    def __init__(self, container, name, bu, step, day):
        SupportingObject.__init__(self, container)
        self.name = name
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
        variableName = SupportingObject._convertVariableName(variableName)
        if not isinstance(uncertainty, bool):
            raise TypeError('The variable uncertainty has type %s.\n ...'
                            'It should be boolean.', type(uncertainty))
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


MESH_DATA_OPTS = {'T', 'abs', 'rel'}
"""Make mesh plot of tally data, absolute or relative uncertainty"""

DET_COLS = ('value', 'energy', 'universe', 'cell', 'material', 'lattice',
            'reaction', 'zmesh', 'ymesh', 'xmesh', 'tally', 'error', 'scores')
"""Name of the columns of the data"""

class Detector(NamedObject):
    """
    Class to store detector data.

    Parameters
    ----------
    parser: :py:class:`~serpentTools.parsers.detector.DetectorReader`
        Detector reader that created this detector
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
        Reshaped relative error data corresponsing to bins used
    scores: None or numpy.array
        Reshaped array of tally scores. SERPENT 1 only
    """

    def __init__(self, parser, name):
        NamedObject.__init__(self, parser, name)
        self.bins = None
        self.tallies = None
        self.errors = None
        self.scores = None
        self.grids = {}
        self.__reshaped = False
        self.indexes = None

    def __len__(self):
        if self.bins is not None:
            return self.bins.shape[0]
        return 0

    def __str__(self):
        return 'Detector {}'.format(self.name)

    def addTallyData(self, bins):
        """Add and, possibly clean, tally data."""
        self.indexes = OrderedDict()
        self.__reshaped = False
        self.bins = bins

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
        for index, indexName in enumerate(DET_COLS):
            if 0 < index < 10:
                uniqueVals = unique(self.bins[:, index])
                if len(uniqueVals) > 1:
                    self.indexes[indexName] = uniqueVals
                    shape.append(len(uniqueVals))
        self.tallies = self.bins[:, 10].reshape(shape)
        self.errors = self.bins[:, 11].reshape(shape)
        if self.bins.shape[1] == 13:
            self.scores = self.bins[:, 12].reshape(shape)
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

        See Also
        --------
        https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
        """
        if not self.__reshaped:
            raise SerpentToolsException(
                'Slicing requires detector to be reshaped')
        workMap = {'tallies': self.tallies, 'errors': self.errors,
                'scores': self.scores}
        if data not in workMap:
            raise KeyError(
                'Slicing function only works with the following data arguments:'
                '\n{}'.format(', '.join(workMap.keys())))
        work = workMap[data]
        if work is None:
            raise SerpentToolsException(
                '{} data for detector {} is None. Cannot perform slicing'
                .format(data, self.name))
        return work[self.getSlices(fixed)]

    def getSlices(self, fixed):
        """
        Return a list of slice operators for each axis in reshaped data

        Parameters
        ----------
        fixed: dict
            Dictionary where keys are strings pointing to dimensions in
        """
        keys = set(fixed.keys())
        slices = []
        for key in self.indexes:
            if key in keys:
                slices.append(fixed[key] - 1)
                keys.remove(key)
            else:
                slices.append(slice(0, len(self.indexes[key])))
        if any(keys):
            warning('Could not find arguments in index that match the following'
                    ' requested slice keys: {}'.format(', '.join(keys)))
        return slices
    
    @property
    def E(self):
        """Energy mesh for this detector"""
        if 'E' not in self.grids:
            self.grids['E'] = None
        if self.grids['E'] is None:
            raise SerpentToolsException(
                'Energy mesh for {} has not been set'.format(self.name))
        return self.grids['E']

    @property
    def X(self):
        """X mesh for this detector."""
        if 'X' not in self.grids:
            self.grids['X'] = None
        if self.grids['X'] is None:
            raise SerpentToolsException(
                'X mesh for {} has not been set'.format(self.name))
        return self.grids['X']

    @property
    def Y(self):
        """Y grid for this detector."""
        if 'Y' not in self.grids:
            self.grids['Y'] = None
        if self.grids['Y'] is None:
            raise SerpentToolsException(
                'Y mesh for {} has not been set'.format(self.name))
        return self.grids['Y']

    @property
    def Z(self):
        """Z grid for this detector."""
        if 'Z' not in self.grids:
            self.grids['Z'] = None
        if self.grids['Z'] is None:
            raise SerpentToolsException(
                'Z mesh for {} has not been set'.format(self.name))
        return self.grids['Z']

    @property
    def T(self):
        """Vector of the detector tallies."""
        if self.bins is None:
            raise SerpentToolsException(
                'Detector data for {} has not been loaded'.format(self.name)
            )
        return self.bins[:, 10]

    @property
    def U(self):
        """Vector of the tally uncertainties."""
        if self.bins is None:
            raise SerpentToolsException(
                'Detector data for {} has not been loaded'.format(self.name)
            )
        return self.bins[:, 11]

    def spectrumPlot(self, fixed=None, ax=None, normalize=True, yLabel=None,
                     steps=True, xscale='log', yscale='lin', sigma=3):
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
        yLabel: str or None
            Custom label for y axis. Defaults to 'Tally data +/- sigma'
        steps: bool
            Plot tally as constant inside bin
        xscale: str
            Scale to apply to x axis
        yscale: str
            Scale to apply to y axis
        sigma: int
            Level of confidence to apply to errors. Use for no error bars

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
        slice
        getSlices
        """
        if not len(self.tallies.shape) == 1 and fixed is None:
            raise SerpentToolsException(
                'Tally data is not a one-dimensional matrix. Need constraining '
                'aguments in fixed dictionary'
            )
        slicedTallies = self.slice(fixed, 'tallies')
        if not len(slicedTallies.shape) == 1:
            raise SerpentToolsException(
                'Sliced data must be one-dimensional for spectrum plot, not {}'
                .format(slicedTallies.shape)
            )
        if errors:
            slicedErrors = 3 * self.slice(fixed, 'errors') * slicedTallies
            if normalize:
                warning('Propagation of uncertainty through normalization not '
                        'complete yet')
        if normalize:
            lethBins = log(divide(self.E[:, -1], self.E[:, 0]))
            slicedTallies = divide(slicedTallies, lethBins)
            slicedTallies = slicedTallies / slicedTallies.max()
        ax = ax or pyplot.axes()
        drawstyle = 'steps-post' if steps else None
        if errors:
            ax.errorbar(self.E[:, 0], slicedTallies, yerr=slicedErrors,
                        drawstyle=drawstyle)
        else:
            ax.plot(self.E[:, 0], slicedTallies, drawstyle=drawstyle)
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)

        return ax

    def __verifyPlotGrid__(self, expected, gridType):
        if self.bins.shape[0] != expected:
            return ('Detector {} has {} bins, not the expected {}. This '
                    'function expects the number of detector bins to '
                    'equal to the number of {} meshes'.
                format(self.name, self.bins.shape[0], expected, gridType))

    def __errorPlot__(self, x, ax, steps, xLabel, yLabel):
        """Shortcut for error bar plotting and labeling"""
        ax = ax or pyplot.axes()
        drawstyle = 'steps-post' if steps else None
        yLabel = yLabel or r'Tally data $\pm$ {} $\sigma$'.format(self.sigma)
        ax.errorbar(x, self.T, self.U, drawstyle=drawstyle, label=self.name)
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        return ax

    def linePlot(self, gridType, ax=None, steps=False, yLabel=None,
                 xLabel=None):
        """
        Plot the tally data for a single mesh.

        Parameters
        ----------
        gridType: str
            Which mesh to plot data against
        ax: pyplot.Axes or None
            Ax on which to plot the data
        yLabel: str or None
            Custom label for y axis. Defaults to 'Tally data +/- sigma'
        xLabel: str or None
            Custom label for x axis. Defaults to 'Bin position [cm]'
        steps: bool
            Plot tally as constant inside bin

        Returns
        -------
        ax: pyplot.Axes
            Axes on which the data was plotted

        Raises
        ------
        SerpentToolsException
            if number of rows in data not equal to
            number of spatial meshes

        See Also
        --------
        spectrumPlot

        """
        if gridType == 'E':
            return self.spectrumPlot(ax, yLabel, steps)

        if gridType.upper() not in self.grids:
            raise KeyError('Detector {} does not have mesh data of type {}'
                           .format(self.name, gridType))
        gridData = self.grids[gridType.upper()]
        errMsg = self.__verifyPlotGrid__(gridData.shape[0], gridType)
        if errMsg:
            raise messages.SerpentToolsException(errMsg)

        # plot using lower bounds if step plot
        # otherwise use center value
        x = gridData[:, 0 if steps else -1]

        xLabel = xLabel or 'Bin position [cm]'
        ax = self.__errorPlot__(x, ax, steps, xLabel, yLabel)

        return ax

    def plot(self, ax=None, steps=False, yLabel=None, xLabel=None):
        """
        Simple plot of tally data over bins.

        Parameters
        ----------
        ax: pyplot.Axes or None
            Ax on which to plot the data
        steps: bool
            Plot values as constant inside of bin if True
        yLabel: str or None
            Label to add to y axis
        xLabel: str or None
            Label to add to x axis

        Returns
        -------
        ax: pyplot.Axes
            Axes on which the figure was plotted
        """
        return (self.__errorPlot__(
            arange(len(self.T)), ax, steps, xLabel or 'Bin', yLabel))

    def meshPlot(self, dim1, dim2, data='T', ax=None, addcbar=True):
        """
        Plot tally data as a function of two mesh dimensions

        Parameters
        ----------
        dim1: str
            Primary dimension - will correspond to x-axis on plot
        dim2: str
            Secondary dimension - will correspond to y-axis on plot
        data: str
            Color meshes from tally data or uncertainties
        ax: axes or None
            Axes on which to plot the data

        Returns
        -------
        ax: pyplot.Axes
            Ax on which the data was plotted

        Raises
        ------
        SerpentToolsException if the mesh type is not supported
        """
        if len(data) == 1:
            data = data.upper()
        if data not in MESH_DATA_OPTS:
            raise messages.SerpentToolsException(
                'Mesh data type {} not supported. Please select '
                'one of the following: {}'
                    .format(data, ', '.join(MESH_DATA_OPTS)))
        grid1, grid2, patches = self.makeMeshPatches(dim1, dim2, data)
        if ax is None:
            fig, ax = pyplot.subplots(1, 1)
        else:
            fig = pyplot.gcf() if addcbar else None

        ax.add_collection(patches)

        if addcbar:
            fig.colorbar(patches, ax=ax)

        ax.set_xlim((grid1[:, 0].min(), grid1[:, 1].max()))
        ax.set_ylim((grid2[:, 0].min(), grid2[:, 1].max()))
        return ax

    def makeMeshPatches(self, dim1, dim2, data='T'):
        """
        Create a patch collection of mesh data.

        Parameters
        ----------
        dim1: str
            Primary dimension - will correspond to x-axis on plot
        dim2: str
            Secondary dimension - will correspond to y-axis on plot
        data: str
            Color meshes from tally data or uncertainties

        Returns
        -------
        PatchCollection
            collection of mesh patches

        Raises
        ------
        KeyError
            If requested dimensions are not in grid
        SerpentToolsException
            - If the total number of meshes is not equal to the total number of
            detector bins
            - If the grids do not easily conform to a plotting routine

        """
        dim1 = dim1.upper()
        dim2 = dim2.upper()
        for d in (dim1, dim2):
            if d not in self.grids:
                raise KeyError('Detector {} does not have mesh data of type {}'
                               .format(self.name, d))
        xGrid = self.grids[dim1]
        yGrid = self.grids[dim2]
        numPatches = xGrid.shape[0] * yGrid.shape[0]

        errMsg = self.__verifyPlotGrid__(numPatches, dim1 + '-' + dim2)
        if errMsg:
            raise messages.SerpentToolsException(errMsg)

        patches = empty(numPatches, dtype=object)
        messages.debug('Building {} patches for {} meshPlot'
                       .format(numPatches, self.name))
        if dim1 in ('X', 'Y', 'Z') and dim2 in ('X', 'Y', 'Z'):
            patches = self.__cartPatches__(dim1, xGrid, dim2, yGrid, data,
                                           patches)
        else:
            raise messages.SerpentToolsException(
                'Could not find easily plot routine for dimensions {} and {}'
                    .format(dim2, dim2))
        messages.debug('done')
        return xGrid, yGrid, patches

    def __cartPatches__(self, dim1, xgrid, dim2, ygrid, data, patches):
        if data == 'T':
            meshVals = self.T
        elif data == 'abs':
            meshVals = self.U
        else:
            meshVals = self.U / self.T
        dim1Col = self.__indx__[dim1]
        dim2Col = self.__indx__[dim2]
        for indx, row in enumerate(self.bins):
            dim1Indx = int(row[dim1Col] - 1)
            dim2Indx = int(row[dim2Col] - 1)
            # bounds are lower, upper, and center coordinates of mesh
            bounds1 = xgrid[dim1Indx]
            bounds2 = ygrid[dim2Indx]

            patches[indx] = (
                Rectangle((bounds1[0], bounds2[0]),
                          width=bounds1[1] - bounds1[0],
                          height=bounds2[1] - bounds2[0])
            )
        collection = PatchCollection(patches)
        collection.set_array(meshVals)
        return collection


class BranchContainer(SupportingObject):
    """
    Class that stores data for a single branch.

    The :py:class:`~serpentTools.parsers.branching.BranchingReader` stores
    branch variables and branched group constant data inside these
    container objects. These are used in turn to create
    :py:class:`~serpentTools.objects.containers.HomogUniv` objects for storing
    group constant data.

    Parameters
    ----------
    parser: serpentTools.objects.readers.BaseReader
        Parser that read the file that created this object
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

    def __init__(self, parser, branchID, branchNames, stateData):
        SupportingObject.__init__(self, parser)
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
        newUniv = HomogUniv(self, univID, burnup, burnIndex, burnDays)
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
