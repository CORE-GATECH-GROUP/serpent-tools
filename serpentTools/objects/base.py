"""
Collection of base classes from which other objects inherit.
"""
from abc import ABCMeta, abstractmethod

from six import add_metaclass

from serpentTools.settings import rc
from serpentTools.messages import info, debug, warning
from serpentTools.plot import (
        plot, magicPlotDocDecorator, formatPlot, cartMeshPlot)

class NamedObject(object):
    """Class for named objects like materials and detectors."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.name)


@add_metaclass(ABCMeta)
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

    @abstractmethod
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
        :py:meth:`~serpentTools.objects.containers.Detector.slice`
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
        * :py:meth:`~serpentTools.objects.containers.Detector.spectrumPlot`
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
        * :py:meth:`~serpentTools.objects.containers.Detector.slice`
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


