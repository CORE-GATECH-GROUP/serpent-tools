"""
Utilties for assisting with plots
"""
from matplotlib.axes import Axes
from matplotlib.colors import Normalize, LogNorm

from serpentTools.messages import warning
from serpentTools.utils.docstrings import magicPlotDocDecorator


__all__ = [
    'DETECTOR_PLOT_LABELS',
    'DEPLETION_PLOT_LABELS',
    'formatPlot',
    'addColorbar',
    'setAx_xlims',
    'setAx_ylims',
    'normalizerFactory',
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
    'days': 'Burnup $[d]$',
    'burnup': 'Burnup $[MWd/kgU]$',
}

DETECTOR_PLOT_LABELS = {
    'energy': 'Energy [MeV]',
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


PLOT_FORMAT_DEFAULTS = {
    'xlabel': None, 'ylabel': None, 'legend': True,
    'loglog': None, 'logy': None, 'logx': None,
    'ncol': 1, 'title': None}


@magicPlotDocDecorator
def formatPlot(ax, **kwargs):
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
    {legend}
    {ncol}
    {title}

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
    loglog = kwargs.get('loglog', PLOT_FORMAT_DEFAULTS['loglog'])
    logx = kwargs.get('logx', PLOT_FORMAT_DEFAULTS['logx'])
    logy = kwargs.get('logy', PLOT_FORMAT_DEFAULTS['logy'])
    xlabel = kwargs.get('xlabel', PLOT_FORMAT_DEFAULTS['xlabel'])
    ylabel = kwargs.get('ylabel', PLOT_FORMAT_DEFAULTS['ylabel'])
    legend = kwargs.get('legend', PLOT_FORMAT_DEFAULTS['legend'])
    title = kwargs.get('title', PLOT_FORMAT_DEFAULTS['title'])
    ncol = kwargs.get('ncol', PLOT_FORMAT_DEFAULTS['ncol'])

    if logx is None:
        logx = inferAxScale(ax, 'x')
    if logy is None:
        logy = inferAxScale(ax, 'y')
    if loglog or logx:
        ax.set_xscale('log')
    if loglog or logy:
        ax.set_yscale('log')
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if legend:
        ax = placeLegend(ax, legend, ncol)
    if title:
        ax.set_title(title)

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
    data: :class:`numpy.ndarray`
        Data to be plotted and normalized
    norm: None or callable or :class:`matplotlib.colors.Normalize`
        If a ``Normalize`` object, then use this as the normalizer.
        If callable, set the normalizer with
        ``norm(data, xticks, yticks)``. If not None, set the
        normalizer to be based on the min and max of the data
    logScale: bool
        If this evaluates to true, construct a
        :class:`matplotlib.colors.LogNorm` with the minimum
        set to be the minimum of the positive values.
    xticks: :class:`numpy.ndarray`
    yticks: :class:`numpy.ndarray`
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
        if issubclass(norm.__class__, Normalize):
            return norm
        if callable(norm):
            return norm(data, xticks, yticks)
    if logScale:
        if (data < 0).any():
            warning("Negative values will be excluded from logarithmic "
                    "colormap.")
        posData = data[data > 0]
        return LogNorm(posData.min(), posData.max())
    return Normalize(data.min(), data.max())


@magicPlotDocDecorator
def placeLegend(ax, legend, ncol=1):
    """
    Add a legend to the figure outside the plot.

    Parameters
    ----------
    {ax}
    {legend}
    {ncol}

    Returns
    -------
    {rax}

    Raises
    ------
    KeyError
        If ``key`` is not in :py:attr:`~serpentTools.plot.LEGEND_KWARGS`
    """
    handles, labels = ax.get_legend_handles_labels()
    if not (handles and labels):
        return ax
    ncol = max(1, int(ncol)) if ncol else 1
    if not isinstance(legend, str):
        ax.legend(ncol=ncol)
        return ax
    kwargs = LEGEND_KWARGS[legend]
    ax.legend(borderaxespad=0., ncol=ncol, **kwargs)

    return ax


def setAx_xlims(ax, xmin, xmax, pad=10):
    return _set_ax_lims(ax, xmin, xmax, True, pad)


def setAx_ylims(ax, ymin, ymax, pad=10):
    return _set_ax_lims(ax, ymin, ymax, False, pad)


_set_lim_doc = """
Set the {v} limits on an Axes object

Parameters
----------
ax: :class:`matplotlib.axes.Axes`
    Ax to be updated
{v}min: float
    Current minimum extent of {v} axis
{v}max: float
    Current maximum extent of {v} axis
pad: float
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


def addColorbar(ax, mappable, norm, cbarLabel=None):
    """
    Quick utility to add a colorbar to an axes object

    Parameters
    ----------
    mappable: iterable
        Collection of meshes, patches, or values that are used to construct
        the colorbar.
    norm: None or :class:`matplotlib.colors.Normalize` subclass
        Normalizer for this plot
    cbarLabel: None or str
        If given, place this as the y-label for the colorbar

    Returns
    -------
    :class:`matplotlib.colorbar.Colorbar`
        The colorbar that was added
    """
    cbar = ax.figure.colorbar(mappable, norm=norm)
    if cbarLabel is not None:
        cbar.ax.set_ylabel(cbarLabel)
    return cbar
