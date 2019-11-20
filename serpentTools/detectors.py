"""
Module containing classes for storing detector data.

``SERPENT`` is capable of producing detectors, or tallies from MCNP,
with a variety of bin structures. These include, but are not limited to,
material regions, reaction types, energy bins, spatial meshes, and
universe bins.

The detectors contained in this module are tasked with storing such
data and proving easy access to the data, as well as the underlying
bins used to define the detector.

Detector Types
--------------

* :class:`~serpentTools.objects.detectors.Detector`
* :class:`~serpentTools.objects.detectors.CartesianDetector`
* :class:`~serpentTools.objects.detectors.HexagonalDetector`
* :class:`~serpentTools.objects.detectors.CylindricalDetector`
* :class:`~serpentTools.objects.detectors.SphericalDetector`
"""

from math import sqrt, pi
from warnings import warn
from numbers import Real
from collections.abc import Mapping

from numpy import (
    unique, empty, inf, hstack, arange, log, divide, asfortranarray,
    ndarray, asarray,
)
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
from matplotlib.pyplot import gca

from serpentTools.messages import (
    warning, SerpentToolsException, error, BAD_OBJ_SUBJ,
    debug,
)
from serpentTools.objects.base import NamedObject
from serpentTools.plot import plot, cartMeshPlot
from serpentTools.utils import (
    magicPlotDocDecorator, formatPlot, setAx_xlims, setAx_ylims,
    addColorbar, normalizerFactory, DETECTOR_PLOT_LABELS,
    compareDictOfArrays,
)
from serpentTools.utils.compare import getLogOverlaps
from serpentTools.io.hooks import matlabHook

__all__ = ['Detector', 'CartesianDetector', 'HexagonalDetector',
           'CylindricalDetector', 'SphericalDetector']


class Detector(NamedObject):
    """Class for storing detector data with multiple bins

    For detectors with spatial meshes, including rectilinear,
    hexagonal, cylindrical, or spherical meshes, refer to companion
    classes :class:`serpentTools.CartesianDetector`,
    :class:`serpentTools.HexagonalDetector`,
    :class:`serpentTools.CylindricalDetector`, or
    :class:`serpentTools.SphericalDetector`

    If simply the tally bins are available, it is recommended
    to use the :meth:`fromTallyBins` class method. This will
    reshape the data and separate the mean tally [second to last
    column] and relative errors [last column].

    Parameters
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray, optional
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray, optional
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray, optional
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : iterable of string, optional
        Iterable naming the bins that correspond to reshaped
        :attr:`tally` and :attr:`errors`.
    grids : dict, optional
        Supplemental grids that may be supplied to this detector,
        including energy points or spatial coordinates.

    Attributes
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray or None
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray or float or None
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray or float or None
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : tuple or None
        Iterable naming the bins that correspond to reshaped
        :attr:`tally` and :attr:`errors`. The tuple
        ``(energy, ymesh, xmesh)`` indicates that :attr:`tallies`
        should have three dimensions corresponding to various
        energy, y-position, and x-position bins. Must be set
        after :attr:`tallies` or :attr:`errors` and agree with
        the shape of each
    grids : dict
        Dictionary containing grid information for binned quantities like
        energy or time.
    energy : numpy.ndarray or None
        Potential underlying energy grid in MeV. Will be ``(n_ene, 3)``, where
        ``n_ene`` is the number of values in the energy grid. Each
        row ``energy[j]`` will be the low point, high point, and mid point
        of the energy bin ``j``.

    Raises
    ------
    ValueError
        If some spatial grid is found in ``indexes`` during creation. This
        class is ill-suited for these problems. Refer to the companion
        classes mentioned above.
    IndexError
        If the shapes of ``bins``, ``tallies``, and ``errors`` are inconsistent
    """

    DET_COLS = (
        'value', 'time', 'energy', 'universe', 'cell', 'material', 'lattice',
        'reaction', 'zmesh', 'ymesh', 'xmesh', 'tally', 'error')

    _CBAR_LABELS = {
        'tallies': 'Tally data',
        'errors': 'Relative Uncertainty',
    }

    def __init__(self, name, bins=None, tallies=None, errors=None,
                 indexes=None, grids=None):
        NamedObject.__init__(self, name)
        self._bins = None
        self._tallies = None
        self._errors = None
        self.bins = bins
        self.tallies = tallies
        self.errors = errors
        self._indexes = None
        if indexes is not None:
            self.indexes = indexes
        self.grids = grids

    @property
    def bins(self):
        return self._bins

    @bins.setter
    def bins(self, value):
        if value is None:
            self._bins = None
            return

        # Coerce to numpy array, check shape
        # Ensure data is ordered columnwise,  and
        # the array owns the underlying data
        bins = asfortranarray(value).copy()
        if len(bins.shape) != 2 or (
                len(bins.shape) == 2 and bins.shape[1] not in {12, 13}):
            raise ValueError(
                "Data does not appear to be Serpent 2 detector data. Shape "
                "should be (N, 12) or (N, 13), is {}".format(bins.shape))

        # Check that this is not a Serpent 1 detector
        if bins[0, -3] != 1:
            raise ValueError(
                "Data does not appear to be Serpent 2 detector data. Appears "
                "to have a scores column, indicated unsupported Serpent 1 "
                "data: {}.".format(bins[0]))

        self._bins = bins

    @property
    def tallies(self):
        return self._tallies

    @tallies.setter
    def tallies(self, tallies):
        if tallies is None:
            self._tallies = tallies
            return

        if not isinstance(tallies, (Real, ndarray)):
            raise TypeError("Tallies must be array or scalar, not {}".format(
                type(tallies)))

        if self._tallies is None:
            self._tallies = tallies
            return

        # Handle scalar / single values arrays
        # TODO Kind of clunky. Maybe a dedicated ScalarDetector?

        if isinstance(tallies, Real):
            if isinstance(self._tallies, Real):
                self._tallies = tallies
            else:
                raise TypeError("Tallies are current array, not scalar")
        else:
            if isinstance(self._tallies, Real):
                raise TypeError("Tallies are currently scalar, nor array")
            if tallies.shape != self._tallies.shape:
                raise IndexError(
                    "Shape of tally data is not consistent. Should be {}, "
                    "is {}".format(self._tallies.shape, tallies.shape))
            self._tallies = tallies

    @property
    def errors(self):
        return self._errors

    @errors.setter
    def errors(self, errors):
        if errors is None:
            self._errors = errors
            return

        if not isinstance(errors, (Real, ndarray)):
            raise TypeError(
                "Tallies must be array or scalar, not {}".format(type(errors)))

        if self._errors is None:
            self._errors = errors
            return

        # Handle scalar / single values arrays
        # TODO Kind of clunky. Maybe a dedicated ScalarDetector?

        if isinstance(errors, Real):
            if isinstance(self._errors, Real):
                self._errors = errors
            else:
                raise TypeError("Tallies are current array, not scalar")
        else:
            if isinstance(self._errors, Real):
                raise TypeError("Tallies are currently scalar, nor array")
            if errors.shape != self._errors.shape:
                raise IndexError(
                    "Shape of tally data is not consistent. Should be {}, "
                    "is {}".format(self._errors.shape, errors.shape))
            self._errors = errors

    @property
    def energy(self):
        return self.grids.get("E")

    @property
    def grids(self):
        return self._grids

    @grids.setter
    def grids(self, grids):
        if grids is None:
            self._grids = {}
        else:
            if not isinstance(grids, Mapping):
                raise TypeError(
                    "Grids must be Mapping type, not {}".format(type(grids)))
            self._grids = grids

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, ix):
        if self._tallies is None:
            if self._errors is None:
                raise AttributeError("Tally and error attributes not set")
            nItems = len(self._errors.shape)
        else:
            nItems = len(self._tallies.shape)
        if len(ix) != nItems:
            raise ValueError(
                "Expected {} items for indexes, got {}".format(
                    nItems, len(ix)))
        self._indexes = tuple(ix)

    @classmethod
    def fromTallyBins(cls, name, bins, grids=None):
        """Create a detector instance from 2D detector data

        Parameters
        ----------
        name : str
            Name of this detector
        bins : numpy.ndarray
            2D array taken from Serpent. Expected to have
            either 12 or 13 columns, where the latter indicates
            a time bin has been added.
        grids : dict, optional
            Dictionary of underlying energy, space, and/or time data.

        Returns
        -------
        Detector

        Raises
        ------
        ValueError
            If the tally data does not appear to be Serpent 2 tally data

        """
        bins = asfortranarray(bins)
        if len(bins.shape) != 2:
            raise ValueError(
                "Array does not appear to be Serpent tally data. Shape is {}, "
                "should be 2D".format(bins.shape))

        if bins.shape[1] not in (12, 13):
            raise ValueError(
                "Array does not appear to be Serpent tally data. Expected 12 "
                " or 13 columns, not {}".format(bins.shape[1]))

        if grids is None:
            grids = {}
        elif not isinstance(grids, Mapping):
            raise TypeError("Grid data is not dictionary-like")

        det = cls(name, bins=bins, grids=grids)

        tallies, errors, indexes = det.reshapedBins()

        det.tallies = tallies
        det.errors = errors
        det.indexes = indexes

        return det

    def reshapedBins(self):
        """Obtain multi-dimensional tally, error, and index data

        Returns
        -------
        tallies : numpy.ndarray
            Potentially multi-dimensional array corresponding to
            tally data along each bin index
        errors : numpy.ndarray
            Potentially multi-dimensional array corresponding to
            tally relative error along each bin index
        indexes : list of str
            Ordering of named bin information, e.g. ``"xmesh"``,
            ``"energy"``, corresponding to axis in ``tallies`` and ``errors``

        Examples
        --------

        A detector is created with a single bin with two bins values.
        These could represent tallying two different reaction rates

        >>> import numpy
        >>> from serpentTools import Detector
        >>> bins = numpy.ones((2, 12))
        >>> bins[1, 0] = 2
        >>> bins[1, 4] = 2
        >>> bins[:, -2:] = [
        ...     [5.0,  0.1],
        ...     [10.0, 0.2]]
        >>> det = Detector("reshape", bins=bins)
        >>> tallies, errors, indexes = det.reshapedBins()
        >>> tallies
        array([5.0, 10.0])
        >>> errors
        array([0.1, 0.2])
        >>> indexes
        ["reaction", ]

        """
        assert self.bins is not None, "No bin data present on {}".format(self)

        if self.bins.shape[0] == 1:
            return self.bins[0, -2], self.bins[0, -1], {}

        shape = []
        indexes = []

        # See if the time column has been inserted
        nameStart = 2 if self.bins.shape[1] == 12 else 1
        for colIx, indexName in enumerate(self.DET_COLS[nameStart:-2],
                                          start=1):
            uniqueVals = unique(self.bins[:, colIx])
            if len(uniqueVals) > 1:
                indexes.append(indexName)
                shape.append(len(uniqueVals))

        tallies = self.bins[:, -2].reshape(shape)
        errors = self.bins[:, -1].reshape(shape)

        return tallies, errors, indexes

    def slice(self, fixed, data='tallies'):
        """
        Return a view of the reshaped array where certain axes are fixed

        Parameters
        ----------
        fixed: dict
            dictionary to aid in the restriction on the multidimensional
            array. Keys correspond to the various grids present in
            :attr:`indexes` while the values are used to
        data: {'tallies', 'errors'}
            Which data set to slice

        Returns
        -------
        :class:`numpy.ndarray`
            View into the respective data where certain dimensions
            have been removed

        Raises
        ------
        AttributeError
            If ``data`` is not supported

        """
        if data not in {"tallies", "errors"}:
            raise AttributeError(
                'Data argument {} not in allowed options'
                '\ntallies, errors')
        work = getattr(self, data)
        if work is None:
            raise AttributeError("{} not setup on {}".format(data, self))
        if not fixed:
            return work
        return work[self._getSlices(fixed)]

    def _getSlices(self, fixed):
        """
        Return a list of slice operators for each axis in reshaped data

        Parameters
        ----------
        fixed: dict or None
            Dictionary where keys are strings pointing to dimensions in
        """
        if fixed is None:
            return (slice(None), ) * len(self.indexes)

        keys = set(fixed)
        slices = tuple()
        for key in self.indexes:
            if key in keys:
                slices += fixed[key],
                keys.remove(key)
            else:
                slices += slice(None),
        if any(keys):
            warning(
                'Could not find arguments in index that match the following'
                ' requested slice keys: {}'.format(', '.join(keys)))
        return slices

    def _getPlotGrid(self, qty):
        grids = self.grids.get(qty[0].upper())
        if grids is not None:
            return hstack((grids[:, 0], grids[-1, 1]))
        nItems = self.tallies.shape[self.indexes.index(qty)]
        return arange(nItems + 1)

    def _getPlotXData(self, qty, ydata):
        binIndex = arange(len(ydata))
        xlabel = DETECTOR_PLOT_LABELS.get(qty, 'Bin Index')
        if qty is None:
            return binIndex, xlabel
        xdata = self.grids.get(qty[0].upper())
        if xdata is not None:
            return xdata[:, 0], xlabel
        return binIndex, xlabel

    def _compare(self, other, lower, upper, sigma):
        myShape = self.tallies.shape
        otherShape = other.tallies.shape
        if myShape != otherShape:
            error("Detector tallies do not have identical shapes"
                  + BAD_OBJ_SUBJ.format('tallies', myShape, otherShape))
            return False
        similar = compareDictOfArrays(self.grids, other.grids, 'grids',
                                      lower=lower, upper=upper)

        similar &= getLogOverlaps('tallies', self.tallies, other.tallies,
                                  self.errors, other.errors, sigma,
                                  relative=True)
        return similar

    @magicPlotDocDecorator
    def spectrumPlot(self, fixed=None, ax=None, normalize=True, xlabel=None,
                     ylabel=None, steps=True, logx=True, logy=False,
                     loglog=False, sigma=3, labels=None, legend=None, ncol=1,
                     title=None, **kwargs):
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
        :class:`~serpentTools.SerpentToolsException`
            if number of rows in data not equal to
            number of energy groups

        See Also
        --------
        * :meth:`slice`
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
            slicedErrors = slicedErrors.reshape(slicedTallies.shape)
            slicedErrors *= slicedTallies
        else:
            slicedErrors = None
        ax = plot(lowerE, slicedTallies, ax=ax, labels=labels,
                  yerr=slicedErrors, **kwargs)
        if ylabel is None:
            ylabel = 'Tally data'
            ylabel += ' normalized per unit lethargy' if normalize else ''
            ylabel += r' $\pm{}\sigma$'.format(sigma) if sigma else ''

        if legend is None and labels:
            legend = True
        ax = formatPlot(ax, loglog=loglog, logx=logx, ncol=ncol,
                        xlabel=xlabel or "Energy [MeV]", ylabel=ylabel,
                        legend=legend, title=title)
        return ax

    @magicPlotDocDecorator
    def plot(self, xdim=None, what='tallies', sigma=None, fixed=None, ax=None,
             xlabel=None, ylabel=None, steps=False, labels=None, logx=False,
             logy=False, loglog=False, legend=None, ncol=1, title=None,
             **kwargs):
        """
        Simple plot routine for 1- or 2-D data

        Parameters
        ----------
        xdim: str, optional
            Plot the data corresponding to changing this bin,
            e.g. ``"energy"``. Must exist in :attr:`indexes`
        what: {'tallies', 'errors'}
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
        :class:`~serpentTools.SerpentToolsException`
            If data contains more than 2 dimensions
        AttributeError
            If plot data or :attr:`indexes` set up.

        See Also
        --------
        * :meth:`slice`
        * :meth:`spectrumPlot`
          better options for plotting energy spectra
        """

        if xdim is not None and fixed and self.indexes is None:
            raise AttributeError(
                "indexes not setup. Unsure how to slice and plot")

        if sigma and what == "errors":
            raise ValueError("Refusing to plot error bars on uncertainties")

        data = self.slice(fixed, what)
        if len(data.shape) > 2:
            raise SerpentToolsException(
                'Data must be constrained to 1- or 2-D, not {}'
                .format(data.shape))
        elif len(data.shape) == 1:
            data = data.reshape(data.size, 1)

        if sigma:
            yerr = (self.slice(fixed, 'errors').reshape(data.shape)
                    * data * sigma)
        else:
            yerr = None

        xdata, autoX = self._getPlotXData(xdim, data)
        xlabel = xlabel or autoX
        ylabel = ylabel or "Tally data"
        ax = ax or gca()

        if steps:
            kwargs.setdefault("drawstyle", "steps-post")

        ax = plot(xdata, data, ax, labels, yerr, **kwargs)

        if legend is None and labels:
            legend = True

        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy, ncol=ncol,
                        xlabel=xlabel, ylabel=ylabel, legend=legend,
                        title=title)
        return ax

    @magicPlotDocDecorator
    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, cbarLabel=None, logColor=False, xlabel=None,
                 ylabel=None, logx=False, logy=False, loglog=False,
                 title=None, thresh=None, **kwargs):
        """
        Plot tally data as a function of two bin types on a cartesian mesh.

        Parameters
        ----------
        xdim: str
            Primary dimension - will correspond to x-axis on plot
        ydim: str
            Secondary dimension - will correspond to y-axis on plot
        what: {'tallies', 'errors'}
            Color meshes from tally data or uncertainties
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
        {mthresh}
        cbarLabel: str
            Label to apply to colorbar. If not given, infer from ``what``
        {kwargs} :py:func:`~matplotlib.pyplot.pcolormesh`

        Returns
        -------
        {rax}

        Raises
        ------
        :class:`serpentTools.SerpentToolsException`
            If data to be plotted, with or without constraints, is not 1D
        KeyError
            If ``fixed`` is given and ``xdim`` or ``ydim`` are contained
            in ``fixed``
        AttributeError
            If the data set by ``what`` not in the allowed selection
        ValueError
            If the data contains negative quantities and ``logColor`` is
            ``True``

        See Also
        --------
        * :meth:`slice`
        * :func:`matplotlib.pyplot.pcolormesh`
        """
        if fixed:
            if xdim in fixed:
                raise KeyError("Cannot constrain {} and use as x data for "
                               "plot".format(xdim))
            if ydim in fixed:
                raise KeyError("Cannot constrain {} and use as y data for "
                               "plot".format(ydim))
        data = self.slice(fixed, what)
        if len(data.shape) != 2:
            raise SerpentToolsException(
                'Data must be 2D for mesh plot, currently is {}.\nConstraints:'
                '{}'.format(data.shape, fixed)
            )
        xgrid = self._getPlotGrid(xdim)
        ygrid = self._getPlotGrid(ydim)
        if data.shape != (ygrid.size - 1, xgrid.size - 1):
            data = data.T
        if cbarLabel is None:
            cbarLabel = self._CBAR_LABELS[what]
        ax = cartMeshPlot(
            data, xgrid, ygrid, ax, cmap, logColor,
            cbarLabel=cbarLabel, thresh=thresh, **kwargs)
        if xlabel is None:
            xlabel = DETECTOR_PLOT_LABELS.get(xdim, xdim)
        if ylabel is None:
            ylabel = DETECTOR_PLOT_LABELS.get(ydim, ydim)
        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy,
                        xlabel=xlabel, ylabel=ylabel,
                        title=title)
        return ax

    def _gather_matlab(self, reconvert):
        """Gather bins and grids for exporting to matlab"""

        converter = deconvert if reconvert else prepToMatlab

        data = {
            converter(self.name, 'bins'): self.bins,
        }

        for key, value in self.grids.items():
            data[converter(self.name, key)] = value

        return data


Detector.toMatlab = matlabHook


class CartesianDetector(Detector):
    """Class for storing detector data with Cartesian grid

    If simply the tally bins are available, it is recommended
    to use the :meth:`fromTallyBins` class method. This will
    reshape the data and separate the mean tally [second to last
    column] and relative errors [last column].

    .. note::

        In order to get full functionality from this class,
        :attr:`x`, :attr:`y`, and :attr:`z` must be set.
        All grids are expected to be ``(N, 3)`` arrays, not
        necessarily of equal shape.

    Parameters
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : dict or None
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``. Optional
    x : numpy.ndarray, optional
        Directly set the x grid
    y : numpy.ndarray, optional
        Directly set the y grid
    z : numpy.ndarray, optional
        Directly set the z grid
    grids : dict, optional
        Supplemental grids that may be supplied to this detector,
        including energy points or spatial coordinates. If spatial
        grids are not provided directly with the ``x``, ``y``, or
        ``z`` arguments, the grids will be pulled from this dictionary
        in the following manner.

        * Key ``"X"`` denotes the :attr:`x` grid
        * Key ``"Y"`` denotes the :attr:`y` grid
        * Key ``"Z"`` denotes the :attr:`z` grid

        If the keys are not present, or the grids are directly provided,
        no actions are taken.

    Attributes
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray or None
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray or None
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray or None
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : dict
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``.
    energy : numpy.ndarray or None
        Potential underlying energy grid in MeV. Will be ``(n_ene, 3)``, where
        ``n_ene`` is the number of values in the energy grid. Each
        row ``energy[j]`` will be the low point, high point, and mid point
        of the energy bin ``j``.
    x : numpy.ndarray or None
        X grid
    y : numpy.ndarray or None
        Y grid
    z : numpy.ndarray or None
        Z grid

    Raises
    ------
    ValueError
        If the values for ``x``, ``y``, and ``z`` are not 2D arrays
        with 3 columns
    """

    def __init__(self, name, bins=None, tallies=None, errors=None,
                 indexes=None, grids=None, x=None, y=None, z=None):
        Detector.__init__(self, name, bins, tallies, errors, indexes, grids)
        self._x = None
        self._y = None
        self._z = None
        x = x if x is not None else self.grids.get("X")
        y = y if y is not None else self.grids.get("Y")
        z = z if z is not None else self.grids.get("Z")
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        value = asfortranarray(value)
        if self._x is None:
            if len(value.shape) != 2 or value.shape[1] != 3:
                raise ValueError(
                    "Expected shape of x grid to be (N, 3), not {}".format(
                        value.shape))
        elif value.shape != self._x.shape:
            raise ValueError(
                "Expected shape of x grid to be {}, not {}".format(
                    value.shape, self.x.shape))
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        value = asfortranarray(value)
        if self._y is None:
            if len(value.shape) != 2 or value.shape[1] != 3:
                raise ValueError(
                    "Expected shape of y grid to be (N, 3), not {}".format(
                        value.shape))
        elif value.shape != self._y.shape:
            raise ValueError(
                "Expected shape of y grid to be {}, not {}".format(
                    value.shape, self.y.shape))
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        value = asfortranarray(value)
        if self._z is None:
            if len(value.shape) != 2 or value.shape[1] != 3:
                raise ValueError(
                    "Expected shape of z grid to be (N, 3), not {}".format(
                        value.shape))
        elif value.shape != self._z.shape:
            raise ValueError(
                "Expected shape of z grid to be {}, not {}".format(
                    value.shape, self.z.shape))
        self._z = value

    @magicPlotDocDecorator
    def meshPlot(self, xdim='x', ydim='y', what='tallies', fixed=None, ax=None,
                 cmap=None, cbarLabel=None, logColor=False, xlabel=None,
                 ylabel=None, logx=False, logy=False, loglog=False,
                 title=None, thresh=None, **kwargs):
        """
        Plot tally data as a function of two bin types on a cartesian mesh.

        Parameters
        ----------
        xdim: str
            Primary dimension - will correspond to x-axis on plot. Defaults
            to "x"
        ydim: str
            Secondary dimension - will correspond to y-axis on plot. Defaults
            to "y"
        what: {'tallies', 'errors'}
            Color meshes from tally data or uncertainties
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
        {mthresh}
        cbarLabel: str
            Label to apply to colorbar. If not given, infer from ``what``
        {kwargs} :py:func:`~matplotlib.pyplot.pcolormesh`

        Returns
        -------
        {rax}

        Raises
        ------
        :class:`serpentTools.SerpentToolsException`
            If data to be plotted, with or without constraints, is not 1D
        KeyError
            If ``fixed`` is given and ``xdim`` or ``ydim`` are contained
            in ``fixed``
        AttributeError
            If the data set by ``what`` not in the allowed selection
        ValueError
            If the data contains negative quantities and ``logColor`` is
            ``True``

        See Also
        --------
        * :meth:`slice`
        * :func:`matplotlib.pyplot.pcolormesh`
        """
        Detector.meshPlot(
            self, xdim=xdim, ydim=ydim, what=what, fixed=fixed, ax=ax,
            cmap=cmap, cbarLabel=cbarLabel, logColor=logColor, xlabel=xlabel,
            ylabel=ylabel, logx=logx, logy=logy, loglog=loglog,
            title=title, thresh=thresh, **kwargs)

    def _getPlotGrid(self, qty):
        if qty is not None and hasattr(self, qty[0]):
            grid = getattr(self, qty[0])
            if grid is not None:
                return hstack((grid[:, 0], grid[-1, 1]))
            raise AttributeError("{} not set".format(qty[0], stacklevel=2))
        return Detector._getPlotGrid(self, qty)

    def _getPlotXData(self, qty, ydata):
        if qty is not None and hasattr(self, qty[0]):
            grid = getattr(self, qty[0])
            if grid is not None:
                return grid[:, 0], DETECTOR_PLOT_LABELS.get(qty, "Bin Index")
            raise AttributeError("{} not set".format(qty[0], stacklevel=2))
        return Detector._getPlotXData(self, qty, ydata)


class HexagonalDetector(Detector):
    """Class for storing detector data with a hexagonal grid

    If simply the tally bins are available, it is recommended
    to use the :meth:`fromTallyBins` class method. This will
    reshape the data and separate the mean tally [second to last
    column] and relative errors [last column].

    .. note::

        In order to get full functionality from this class,
        :attr:`z`, :attr:`centers`, :attr:`pitch`, and :attr:`hexType`
        must be set.  This can be done by having ``"Z"`` and
        ``"COORDS"`` as keys in ``grids`` and passing ``pitch`` and
        ``hexType`` directly, or by setting the attributes directly.
        Z grid is expected to be ``(N, 3)`` array.

    Parameters
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray, optional
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray, optional
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray, optional
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : dict, optional
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``
    centers : numpy.ndarray, optional
        ``(N, 2)`` array with centers of each hexagonal element
    pitch : float, optional
        Center to center distance between adjacent hexagons
    hexType : {2, 3}, optional
        Integer orientation, identical to Serpent detector structure. 2
        corresponds to a hexagon with flat faces perpendicular to y-axis.
        3 corresponds to a flat faces perpendicular to x-axis
    grids : dict, optional
        Supplemental grids that may be supplied to this detector,
        including energy points or spatial coordinates.

    Attributes
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray or None
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray or None
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    pitch : float or None
        Center to center distance between hexagons. Must be set before
        calling :meth:`hexPlot`
    hexType : {2, 3} or None
        Integer orientation, identical to Serpent detector structure. 2
        corresponds to a hexagon with flat faces perpendicular to y-axis.
        3 corresponds to a flat faces perpendicular to x-axis
    errors : numpy.ndarray or None
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : dict or None
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``.
    energy : numpy.ndarray or None
        Potential underlying energy grid in MeV. Will be ``(n_ene, 3)``, where
        ``n_ene`` is the number of values in the energy grid. Each
        row ``energy[j]`` will be the low point, high point, and mid point
        of the energy bin ``j``.
    coords: numpy.ndarray or None
        Centers of hexagonal meshes in XY plane
    z : numpy.ndarray or None
        Z Grid

    """

    DET_COLS = (
        'value', 'time', 'energy', 'universe', 'cell', 'material', 'lattice',
        'reaction', 'zmesh', 'ycoord', 'xcoord', 'tally', 'error')

    def __init__(self, name, bins=None, tallies=None, errors=None,
                 indexes=None, z=None, centers=None, pitch=None, hexType=None,
                 grids=None):

        Detector.__init__(self, name, bins, tallies, errors, indexes, grids)

        if pitch is not None:
            self.pitch = pitch
        else:
            self._pitch = None

        if hexType is not None:
            self.hexType = hexType
        else:
            self._hexType = None

        self._z = None
        self._centers = None

        z = z if z is not None else self.grids.get("Z")
        if z is not None:
            self.z = z

        centers = centers if centers is not None else self.grids.get("COORD")
        if centers is not None:
            self.centers = centers

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        value = asfortranarray(value)
        if self._z is None:
            if len(value.shape) != 2 or value.shape[1] != 3:
                raise ValueError(
                    "Expected shape of z grid to be (N, 3), not {}".format(
                        value.shape))
        elif value.shape != self._z.shape:
            raise ValueError(
                "Expected shape of z grid to be {}, not {}".format(
                    value.shape, self.z.shape))
        self._z = value

    @property
    def pitch(self):
        return self._pitch

    @pitch.setter
    def pitch(self, value):
        if isinstance(value, Real):
            if value <= 0:
                raise ValueError("Pitch must be positive")
        else:
            raise TypeError(
                "Cannot set pitch to {}. Must be positive value".format(
                    type(value)))
        self._pitch = value

    @property
    def hexType(self):
        return self._hexType

    @hexType.setter
    def hexType(self, value):
        if value not in {2, 3}:
            raise ValueError(
                "Hex type must be 2 or 3, not {}".format(value))
        self._hexType = value

    @property
    def centers(self):
        return self._centers

    @centers.setter
    def centers(self, value):
        value = asarray(value)

        if self._centers is None:
            if len(value.shape) != 2 or value.shape[1] != 2:
                raise ValueError(
                    "Expected centers to have shape (N, 2), got {}".format(
                        value.shape))
        else:
            if value.shape != self._centers.shape:
                raise ValueError(
                    "Expected centers to have shape {}, got {}".format(
                        self._centers.shape, value.shape))
        self._centers = value

    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None,
                 logx=False, logy=False, loglog=False, title=None, **kwargs):
        opts = dict(what=what,
                    fixed=fixed,
                    ax=ax,
                    cmap=cmap,
                    logColor=logColor,
                    xlabel=xlabel,
                    logx=logx,
                    logy=logy,
                    loglog=loglog,
                    title=title,
                    **kwargs)
        if any(arg in {"ycoord", "xcoord"} for arg in (xdim, ydim)):
            warn("Use hexPlot if plotting xcoord vs ycoord")
            return self.hexPlot(**opts)
        return Detector.meshPlot(self, xdim, ydim, **opts)

    meshPlot.__doc__ = Detector.meshPlot.__doc__

    @magicPlotDocDecorator
    def hexPlot(self, what='tallies', fixed=None, ax=None, cmap=None,
                logColor=False, xlabel=None, ylabel=None, logx=False,
                logy=False, loglog=False, title=None, normalizer=None,
                cbarLabel=None, borderpad=2.5, **kwargs):
        """
        Create and return a hexagonal mesh plot.

        Parameters
        ----------
        what: {'tallies', 'errors'}
            Quantity to plot
        fixed: None or dict
            Dictionary of slicing arguments to pass to :meth:`slice`
        {ax}
        {cmap}
        {logColor}
        {xlabel}
        {ylabel}
        {logx}
        {logy}
        {loglog}
        {title}
        borderpad: int or float
            Percentage of total plot to apply as a border. A value of
            zero means that the extreme edges of the hexagons will touch
            the x and y axis.
        {kwargs} :class:`matplotlib.patches.RegularPolygon`

        Raises
        ------
        AttributeError
            If :attr:`pitch` and :attr:`hexType` are not set.
        """
        if self.centers is None or self.pitch is None or self.hexType is None:
            raise AttributeError("centers, pitch, and hexType not set")

        if fixed and ('xcoord' in fixed or 'ycoord' in fixed):
            raise KeyError("Refusing to restrict along one of the hexagonal "
                           "dimensions {x/y}coord")

        if not isinstance(borderpad, Real) or borderpad < 0:
            raise ValueError(
                "borderpad should be postive, not {}".format(borderpad))

        kwargs.setdefault("ec", "k")
        kwargs.setdefault("edgecolor", "k")
        alpha = kwargs.get('alpha')

        data = self.slice(fixed, what)

        ny = getattr(self, what).shape[self.indexes.index("ycoord")]
        nx = getattr(self, what).shape[self.indexes.index("xcoord")]

        if data.shape != (ny, nx):
            raise IndexError("Constrained data does not agree with hexagonal "
                             "grid structure. Coordinate grid: {}. "
                             "Constrained shape: {}"
                             .format((ny, nx), data.shape))

        patches = empty(ny * nx, dtype=object)
        values = empty(ny * nx)
        coords = self.centers

        ax = ax or gca()
        xmax, ymax = [-inf, ] * 2
        xmin, ymin = [inf, ] * 2
        radius = self.pitch / sqrt(3)
        rotation = 0 if self.hexType == 2 else (pi / 2)

        for pos, (xy, val) in enumerate(zip(coords, data.flat)):
            values[pos] = val
            h = RegularPolygon(xy, 6, radius, rotation, **kwargs)
            verts = h.get_verts()
            vmins = verts.min(0)
            vmaxs = verts.max(0)
            xmax = max(xmax, vmaxs[0])
            xmin = min(xmin, vmins[0])
            ymax = max(ymax, vmaxs[1])
            ymin = min(ymin, vmins[1])
            patches[pos] = h

        normalizer = normalizerFactory(values, normalizer, logColor,
                                       coords[:, 0], coords[:, 1])
        pc = PatchCollection(patches, cmap=cmap, alpha=alpha)
        pc.set_array(values)
        pc.set_norm(normalizer)
        ax.add_collection(pc)

        addColorbar(ax, pc, None, cbarLabel)

        formatPlot(ax, loglog=loglog, logx=logx, logy=logy,
                   xlabel=xlabel or "X [cm]",
                   ylabel=ylabel or "Y [cm]", title=title)

        setAx_xlims(ax, xmin, xmax, pad=borderpad)
        setAx_ylims(ax, ymin, ymax, pad=borderpad)

        return ax


class CylindricalDetector(Detector):
    """Class for storing detector data with a cylindrical mesh

    If simply the tally bins are available, it is recommended
    to use the :meth:`fromTallyBins` class method. This will
    reshape the data and separate the mean tally [second to last
    column] and relative errors [last column].

    Parameters
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray, optional
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray, optional
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray, optional
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : collections.OrderedDict, optinal
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``
    grids : dict, optional
        Supplemental grids that may be supplied to this detector,
        including energy points or spatial coordinates.

    Attributes
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : collections.OrderedDict
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``.
    energy : numpy.ndarray or None
        Potential underlying energy grid in MeV. Will be ``(n_ene, 3)``, where
        ``n_ene`` is the number of values in the energy grid. Each
        row ``energy[j]`` will be the low point, high point, and mid point
        of the energy bin ``j``.

    """

    # column indices in full (time-bin included) bins matrix
    DET_COLS = (
        'value', 'time', 'energy', 'universe', 'cell', 'material', 'lattice',
        'reaction', 'zmesh', 'phi', 'rmesh', 'tally', 'error')

    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None,
                 logx=False, logy=False, loglog=False, title=None, **kwargs):
        if any(arg in {"rmesh", "phi"} for arg in (xdim, ydim)):
            warn("Cylindrical plotting is not fully supported. See GitHub "
                 "issue 169")
        return Detector.meshPlot(
            self, xdim, ydim, what=what, fixed=fixed, ax=ax, cmap=cmap,
            logColor=logColor, xlabel=xlabel, logx=logx, logy=logy,
            loglog=loglog, title=title, **kwargs)

    meshPlot.__doc__ = Detector.meshPlot.__doc__


class SphericalDetector(Detector):
    """Class for storing detector data with multiple bins

    If simply the tally bins are available, it is recommended
    to use the :meth:`fromTallyBins` class method. This will
    reshape the data and separate the mean tally [second to last
    column] and relative errors [last column].

    Parameters
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : dict
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``. Optional
    grids : dict
        Supplemental grids that may be supplied to this detector,
        including energy points or spatial coordinates.

    Attributes
    ----------
    name : str
        Name of this detector
    bins : numpy.ndarray
        Full 2D tally data from detector file, including tallies and
        errors in last two columns
    tallies : numpy.ndarray
        Reshaped tally data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin.
    errors : numpy.ndarray
        Reshaped error data such that each dimension corresponds
        to a unique bin, such as energy or spatial bin. Note:
        this is a relative error as it would appear in the
        output file
    indexes : dict
        Dictionary mapping the bin name to its corresponding
        axis in :attr:`tallies` and :attr:`errors`, e.g.
        ``{"energy": 0}``.
    energy : numpy.ndarray or None
        Potential underlying energy grid in MeV. Will be ``(n_ene, 3)``, where
        ``n_ene`` is the number of values in the energy grid. Each
        row ``energy[j]`` will be the low point, high point, and mid point
        of the energy bin ``j``.
    """

    DET_COLS = (
        'value', 'time', 'energy', 'universe', 'cell', 'material', 'lattice',
        'reaction', 'theta', 'phi', 'rmesh', 'tally', 'error')

    def meshPlot(self, xdim, ydim, what='tallies', fixed=None, ax=None,
                 cmap=None, logColor=False, xlabel=None, ylabel=None,
                 logx=False, logy=False, loglog=False, title=None, **kwargs):
        if any(arg in {"theta", "phi", "rmesh"} for arg in (xdim, ydim)):
            warn("Spherical mesh plotting is not fully supported.")
        return Detector.meshPlot(
            self, xdim, ydim, what=what, fixed=fixed, ax=ax, cmap=cmap,
            logColor=logColor, xlabel=xlabel, logx=logx, logy=logy,
            loglog=loglog, title=title, **kwargs)

    meshPlot.__doc__ = Detector.meshPlot.__doc__


def detectorFactory(name, bins, grids=None):
    grids = {} if grids is None else grids
    if "X" in grids:
        detClass = CartesianDetector
    elif "COORD" in grids:
        detClass = HexagonalDetector
    elif "R" in grids:
        detClass = CylindricalDetector if "Z" in grids else SphericalDetector
    else:
        # fall back to base detector
        detClass = Detector
    return detClass.fromTallyBins(name, bins, grids)


def deconvert(detectorName, quantity):
    """Restore the original name of the detector data"""
    return "DET{}{}".format(
        detectorName, "" if quantity == "bins" else quantity)


def prepToMatlab(detectorName, quantity):
    """Create a name of a variable for MATLAB"""
    return detectorName + "_" + quantity
