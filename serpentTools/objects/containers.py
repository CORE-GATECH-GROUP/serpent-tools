import six

from numpy import empty
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection

from serpentTools.objects import SupportingObject, NamedObject
from serpentTools.settings import messages


class HomogUniv(SupportingObject):
    """Class for:
    (1) Storing universe number and, optionally,
    burnup, day, bu step provided by results and branching readers
    (2) Adding and get variables.

    Public methods
    ----------
    -set(VariableName,VariableValue,**kwargs)
    -get(VariableName,** kwargs)

    Attributes
    ----------
    -name: name of the universe
    -bu:   burnup value
    -step: temporal step
    -day:  depletion day

    """

    def __init__(self, container, name, bu, step, day):
        """ Class Initializer. Each universe is defined  uniquely
        in terms of the attributes mentioned in the docstring. The input
        container refers to the name of the parser (branching/results reader).
        """
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

    def set(self, variablename, variablevalue, uncertainty=False):
        """
        Parameters
        ----------
        variablename:   Variable Name
        variablevalue:  Variable Expected Value
        uncertainty:    Boolean Variable- set to True in order to retrieve the
                        uncertainty associated to the expected values
        """

        # 1. Check the input type
        variablename = SupportingObject._convertVariableName(variablename)
        if not isinstance(uncertainty, bool):
            raise messages.error("Uncertainty must be a boolean variable")
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variablename, uncertainty)
        # 3. Check if variable is already present. Then set the variable.
        if variablename in setter:
            messages.warning('The variable will be overwritten')
        setter[variablename] = variablevalue

    def get(self, variablename, uncertainty=False):

        # 1. Check the input values
        variablename = SupportingObject._convertVariableName(variablename)
        if not isinstance(uncertainty, bool):
            raise messages.error("Uncertainty must be a boolean variable")
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variablename, uncertainty)
        # 3. Return the value of the variable
        x = setter.get(variablename)
        if not uncertainty:
            return x
        else:
            dx = setter.get(variablename)
            return x, dx

    def _lookup(self, variablename, uncertainty):

        if "inf" in variablename:
            if not uncertainty:
                return self.infExp
            else:
                return self.infUnc
        elif "b1" in variablename:
            if not uncertainty:
                return self.b1Exp
            else:
                return self.b1Unc

        messages.error('Neither inf, nor b1 in the string')


DETECTOR_INDICES = {
    'E': (1, 1),
    'X': (9, 9),
    'Y': (8, 8),
    'Z': (7, 7),
    'T': (10, 10),
    'U': (11, 11),
}
"""Indices for various quantities for serpent 1 and 2 - zero offset"""


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
        Tallies from the detector file
    grids: dict
        Dictionary with additional data describing energy grids or mesh points

    """

    def __init__(self, parser, name, settings):
        NamedObject.__init__(self, parser, name)
        self.sigma = settings['sigma']
        versionIndx = 0 if settings['version'][0] == '1' else 1
        self.__indx__ = {key: value[versionIndx]
                         for key, value in six.iteritems(DETECTOR_INDICES)}
        self.bins = None
        self.grids = {}

    def __len__(self):
        if self.bins is not None:
            return self.bins.shape[0]
        return 0

    def __str__(self):
        return 'Detector {}'.format(self.name)

    def addTallyData(self, bins):
        """Add and, possibly clean, tally data."""
        self.bins = bins
        self.bins[:, self.__indx__['U']] = (
            bins[:, self.__indx__['U']] * bins[:, self.__indx__['T']] *
            self.sigma)

    @property
    def E(self):
        """Energy mesh for this detector"""
        if 'E' not in self.grids:
            self.grids['E'] = None
        if self.grids['E'] is None:
            raise messages.SerpentToolsException(
                'Energy mesh for {} has not been set'.format(self.name))
        return self.grids['E']

    @property
    def X(self):
        """X mesh for this detector."""
        if 'X' not in self.grids:
            self.grids['X'] = None
        if self.grids['X'] is None:
            raise messages.SerpentToolsException(
                'X mesh for {} has not been set'.format(self.name))
        return self.grids['X']

    @property
    def Y(self):
        """Y grid for this detector."""
        if 'Y' not in self.grids:
            self.grids['Y'] = None
        if self.grids['Y'] is None:
            raise messages.SerpentToolsException(
                'Y mesh for {} has not been set'.format(self.name))
        return self.grids['Y']

    @property
    def Z(self):
        """Z grid for this detector."""
        if 'Z' not in self.grids:
            self.grids['Z'] = None
        if self.grids['Z'] is None:
            raise messages.SerpentToolsException(
                'Z mesh for {} has not been set'.format(self.name))
        return self.grids['Z']

    @property
    def T(self):
        """Vector of the detector tallies."""
        if self.bins is None:
            raise messages.SerpentToolsException(
                'Detector data for {} has not been loaded'.format(self.name)
            )
        return self.bins[:, self.__indx__['T']]

    @property
    def U(self):
        """Vector of the tally uncertainties."""
        if self.bins is None:
            raise messages.SerpentToolsException(
                'Detector data for {} has not been loaded'.format(self.name)
            )
        return self.bins[:, self.__indx__['U']]

    def spectrumPlot(self, ax=None, yLabel=None, steps=True):
        """
        Quick plot of the detector value as a function of energy.

        Parameters
        ----------
        ax: pyplot.Axes or None
            Ax on which to plot the data
        yLabel: str or None
            Custom label for y axis. Defaults to 'Tally data +/- sigma'
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
            number of energy groups
        """
        energies = self.E[:, 0] if steps else self.E[:, -1]

        errMsg = self.__verifyPlotGrid__(self.E.shape[0], 'energy')
        if errMsg:
            raise messages.SerpentToolsException(errMsg)

        ax = self.__errorPlot__(energies, ax, steps, 'Energy [eV]', yLabel)
        ax.set_xscale('log')
        ax.set_yscale('log')

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

    def meshPlot(self, dim1, dim2, ax=None, addcbar=True):
        """
        Plot tally data as a function of two mesh dimensions

        Parameters
        ----------
        dim1: str
            Primary dimension - will correspond to x-axis on plot
        dim2: str
            Secondary dimension - will correspond to y-axis on plot
        ax: axes or None

        Returns
        -------
        ax: pyplot.Axes
            Ax on which the data was plotted
        """
        grid1, grid2, patches = self.makeMeshPatches(dim1, dim2)
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

    def makeMeshPatches(self, dim1, dim2):
        """
        Create a patch collection of mesh data.

        Parameters
        ----------
        dim1: str
            Primary dimension - will correspond to x-axis on plot
        dim2: str
            Secondary dimension - will correspond to y-axis on plot

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
            patches = self.__cartPatches__(dim1, xGrid, dim2, yGrid, patches)
        else:
            raise messages.SerpentToolsException(
                'Could not find easily plot routine for dimensions {} and {}'
                .format(dim2, dim2))
        messages.debug('done')
        return xGrid, yGrid, patches

    def __cartPatches__(self, dim1, xgrid, dim2, ygrid, patches):
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
        collection.set_array(self.T)
        return collection
