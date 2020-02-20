"""
Utilties for assisting with plots
"""
from matplotlib import pyplot
from matplotlib.axes import Axes
from matplotlib.colors import Normalize, LogNorm

from serpentTools.messages import warning
from serpentTools.utils.docstrings import magicPlotDocDecorator


__all__ = [
    'DETECTOR_PLOT_LABELS',
    'DEPLETION_PLOT_LABELS',
    'RESULTS_PLOT_XLABELS',
    'formatPlot',
    'addColorbar',
    'setAx_xlims',
    'setAx_ylims',
    'normalizerFactory',
    'placeLegend',
    'inferAxScale'
]

LEGEND_KWARGS = {
    'above': {'bbox_to_anchor': (0., 1.02, 1., 1.02),
              'loc': 3, 'mode': 'expand'},
    'right': {'bbox_to_anchor': (1.02, 1),
              'loc': 2}
}
"""
Settings for modifying the position of the legend
source: `<https://matplotlib.org/users/legend_guide.html>`_
"""


DEPLETION_PLOT_LABELS = {
    'adens': r'Atom density $[\#/b-cm]$',
    'mdens': r'Mass density $[g/cm^3]$',
    'a': r'Activity $[Bq]$',
    'h': r'Decay heat $[W]$',
    'sf': r'Spontaneous fission rate $[\#/s]$',
    'gsrc': r'Photon emission rate $[\#/s]$',
    'ingTox': 'Ingestion toxicity $[Sv]$',
    'inhTox': 'Inhalation toxicity $[Sv]$',
    'days': 'Time $[d]$',
    'burnup': 'Burnup $[MWd/kgU]$',
}

DETECTOR_PLOT_LABELS = {
    'energy': 'Energy [MeV]',
    'time': 'Time [s]',
}
for dim in ['x', 'y', 'z']:
    DETECTOR_PLOT_LABELS[dim] = "{} Position [cm]".format(dim.capitalize())
    DETECTOR_PLOT_LABELS[dim + 'mesh'] = DETECTOR_PLOT_LABELS[dim]


_DET_LABEL_INDEXES = {
    'reaction', 'material', 'cell', 'universe', 'lattice',
}
# bins that increment by integer indices and reflect discrete quantities,
# unlike energy inidices

for key in _DET_LABEL_INDEXES:
    DETECTOR_PLOT_LABELS[key] = key.capitalize() + " Index"

del _DET_LABEL_INDEXES

RESULTS_PLOT_XLABELS = {
    'burnup': DEPLETION_PLOT_LABELS['burnup'],
    'burnDays': DEPLETION_PLOT_LABELS['days'],
    'burnStep': "Burnup step",
}


@magicPlotDocDecorator
def formatPlot(
    ax,
    xlabel=None,
    ylabel=None,
    logx=False,
    logy=False,
    loglog=False,
    title=None,
    legend=True,
    legendcols=1,
    axkwargs=None,
    legendkwargs=None,
):
    """
    Apply a range of formatting options to the plot.

    Parameters
    ----------
    {ax}
    {xlabel}
    {ylabel}
    {loglog}
    {logx}
    {logy}
    title : str, optional
        Title to apply to this axes object
    {legend}
    legendcols : int, optional
        Number of columns to apply to the legend, if applicable
    axkwargs : dict, optional
        Additional keyword arguments to be passed to
        :meth:`matplotlib.axes.Axes.set`. Values like ``xlabel``,
        ``ylabel``, ``xscale``, ``yscale``, and title will be respected,
        even though they are also arguments to this function
    legendkwargs : dict, optional
        Additional keyword arguments to be passed to
        :meth:`matplotlib.axes.Axes.legend`. Values like ``title``
        and ``ncol`` will be respected.

    Returns
    -------
    {rax}

    Raises
    ------
    TypeError
        If the ``ax`` argument is not an instance of
        :py:class:`matplotlib.pyplot.axes.Axes`

    """

    if not isinstance(ax, Axes):
        raise TypeError("Expected {} got {}".format(type(Axes), type(ax)))

    axkwargs = {} if axkwargs is None else axkwargs

    if logx is None:
        logx = inferAxScale(ax, 'x')
    if logy is None:
        logy = inferAxScale(ax, 'y')

    if loglog or logx:
        axkwargs.setdefault("xscale", "log")
    if loglog or logy:
        axkwargs.setdefault("yscale", "log")

    if xlabel:
        axkwargs.setdefault("xlabel", xlabel)
    if ylabel:
        axkwargs.setdefault("ylabel", ylabel)
    if title:
        axkwargs.setdefault("title", title)

    ax.set(**axkwargs)

    if not legend and legend is not None:
        return ax

    # format the legend
    legendkwargs = {} if legendkwargs is None else legendkwargs
    legendkwargs.setdefault("ncol", legendcols)

    ax = placeLegend(ax, legend, **legendkwargs)

    return ax


def inferAxScale(ax, dim):
    lims = getattr(ax, 'get_{}lim'.format(dim))()
    mn = min(lims)
    mx = max(lims)
    if not mn:
        return mx > 100
    if mn < 0:
        return mx > 10
    return abs(mx / mn) > 100


def normalizerFactory(data, norm, logScale, xticks, yticks):
    """
    Construct and return a :class:`~matplotlib.colors.Normalize` for this data

    Parameters
    ----------
    data : :class:`numpy.ndarray`
        Data to be plotted and normalized
    norm : None or callable or :class:`matplotlib.colors.Normalize`
        If a ``Normalize`` object, then use this as the normalizer.
        If callable, set the normalizer with
        ``norm(data, xticks, yticks)``. If not None, set the
        normalizer to be based on the min and max of the data
    logScale : bool
        If this evaluates to true, construct a
        :class:`matplotlib.colors.LogNorm` with the minimum
        set to be the minimum of the positive values.
    xticks : :class:`numpy.ndarray`
    yticks : :class:`numpy.ndarray`
        Arrays ideally corresponding to the data. Used with callable
        `norm` function.

    Returns
    --------
    :class:`matplotlib.colors.Normalize`
    or :class:`matplotlib.colors.LogNorm`
    or object:
        Object used to normalize colormaps against these data
    """
    if norm is not None:
        if isinstance(norm, Normalize):
            return norm
        elif callable(norm):
            return norm(data, xticks, yticks)
        else:
            raise TypeError("Normalizer {} not understood".format(norm))

    if logScale:
        if (data < 0).any():
            warning("Negative values will be excluded from logarithmic "
                    "colormap.")
        posData = data[data > 0]
        return LogNorm(posData.min(), posData.max())
    return Normalize(data.min(), data.max())


@magicPlotDocDecorator
def placeLegend(ax, legend, handlesAndLabels=None, **kwargs):
    """Add a legend to the axes instance.

    A legend will be drawn if at least one of the following criteria
    are met:

    1. ``legend`` is not one of the supported string legend control
       arguments that dictate where the legend should be placed
    2. More than one item has been plotted

    Parameters
    ----------
    {ax}
    {legend}
    handlesAndLabels : tuple (legend handles, labels), optional
        Exact legend handles (graphical element) and labels (string
        element) to be used in making the legend. If not provided,
        will be fetched from
        :meth:`matplotlib.axes.Axes.get_legend_handles_labels`
    kwargs : dict, optional
        Additional keyword arguments to be passed to
        :meth:`matplotlib.axes.Axes.legend`, if applicable

    Returns
    -------
    {rax}

    """
#    import pdb
#    pdb.set_trace()
    if handlesAndLabels is None:
        handles, labels = ax.get_legend_handles_labels()
    else:
        handles, labels = handlesAndLabels
    if not (handles and labels):
        return ax

    if legend is None and len(handles) == len(labels) == 1:
        return ax

    extras = LEGEND_KWARGS.get(legend, {})
    kwargs.update(extras)

    # Some plot methods support ncols=None as input argument
    # Maybe do some "smart" determination of number of columns?

    ncol = kwargs.get("ncol", None)
    if ncol is None:
        kwargs["ncol"] = 1

    ax.legend(handles, labels, **kwargs)

    return ax


def setAx_xlims(ax, xmin, xmax, pad=10):
    return _set_ax_lims(ax, xmin, xmax, True, pad)


def setAx_ylims(ax, ymin, ymax, pad=10):
    return _set_ax_lims(ax, ymin, ymax, False, pad)


_set_lim_doc = """
Set the {v} limits on an Axes object

Parameters
----------
ax : :class:`matplotlib.axes.Axes`
    Ax to be updated
{v}min : float
    Current minimum extent of {v} axis
{v}max : float
    Current maximum extent of {v} axis
pad : float, optional
    Padding, in percent, to apply to each side of
    the current min and max
"""


setAx_xlims.__doc__ = _set_lim_doc.format(v='x')
setAx_ylims.__doc__ = _set_lim_doc.format(v='y')
del _set_lim_doc


def _set_ax_lims(ax, vmin, vmax, xory, pad):
    assert pad >= 0
    func = getattr(ax, 'set_{}lim'.format('x' if xory else 'y'))
    diff = vmax - vmin
    offset = pad * diff / 100
    return func(vmin - offset, vmax + offset)


def addColorbar(ax, mappable, norm=None, cbarLabel=None):
    """
    Quick utility to add a colorbar to an axes object

    The color bar is placed adjacent to the provided
    axes argument, rather than in the provided space.

    Parameters
    ----------
    mappable : iterable
        Collection of meshes, patches, or values that are used to
        construct the colorbar.
    norm : :class:`matplotlib.colors.Normalize`, optional
        Normalizer for this plot. Can be a subclass like
        :class:`matplotlib.colors.LogNorm`
    cbarLabel : str, optional
        If given, place this as the y-label for the colorbar

    Returns
    -------
    :class:`matplotlib.colorbar.Colorbar`
        The colorbar that was added

    """
    cbar = pyplot.colorbar(mappable, ax=ax, norm=norm)
    if cbarLabel:
        cbar.ax.set_ylabel(cbarLabel)
    return cbar
