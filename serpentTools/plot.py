"""Plot routines"""
from functools import wraps
from textwrap import dedent

from six import iteritems

import numpy
from numpy import meshgrid, where
from matplotlib import pyplot
from matplotlib.axes import Axes
from matplotlib.colors import LogNorm, Normalize

#
# DOCSTRING EXTRAS
#
_MPL_AX = ':py:class:`matplotlib.axes.Axes`'
_LOG_BASE = """log{}: bool\n    Apply a log scale to {}."""
LOG_LOG = _LOG_BASE.format('log', 'both axes')
LOGX = _LOG_BASE.format('x', 'x axis')
LOGY = _LOG_BASE.format('y', 'y axis')
TITLE = """title: str\n    Title to apply to the figure."""
LABELS = """labels: None or iterable
    Labels to apply to each line drawn. This can be used to identify
    which bin is plotted as what line."""

XLABEL = """xlabel: str or None\n    Label for x-axis."""
YLABEL = """yabel: str or None\n    Label for y-axis."""
SIGMA = """sigma: int
    Confidence interval to apply to errors. If not given or ``0``, 
    no errors will be drawn."""
AX = """ax: {} or None
    Ax on which to plot the data.""".format(_MPL_AX)
RETURNS_AX = """{}
    Ax on which the data was plotted.""".format(_MPL_AX)
CMAP = """cmap: str or None
    Valid Matplotlib colormap to apply to the plot."""
KWARGS = """kwargs:\n    Addition keyword arguments to pass to"""
MAT_FMT_DOC = """labelFmt: str or None
    Formattable string for labeling the individual plots. If not 
    given, just label as isotope name, e.g. ``'U235'``.
    Will make the following substitutions on the ``labelFmt`` string, 
    if given:

    +---------------+-------------------------+
    |Keyword        | Replacement             |
    +===============+=========================+
    |``'mat'``      | name of this material   |
    +---------------+-------------------------+
    |``'iso'``      | specific isotope name   |
    +---------------+-------------------------+
    |``'zai'``      | specific isotope ZZAAAI |
    +---------------+-------------------------+
"""

UNIV_FMT_DOC = """labelFmt: str or None
    formattable string for labeling the individual plots. 
    
    +---------+----------------------------+
    | String  | Replaced value             |
    +=========+============================+
    | ``{k}`` | Name of variable plotted   |
    +---------+----------------------------+
    | ``{u}`` | Name of this universe      |
    +---------+----------------------------+
    | ``{b}`` | Value of burnup in MWd/kgU |
    +---------+----------------------------+
    | ``{d}`` | Value of burnup in days    |
    +---------+----------------------------+
    | ``{i}`` | Burnup index               |
    +---------+----------------------------+
"""

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


LEGEND = """legend: bool or str
    Automatically label the plot. Pass one of the following values
    to place the legend outside the plot: {}""".format(
        ', '.join(LEGEND_KWARGS.keys()))

NCOL = """ncol: int\n    Integer number of columns to apply to the legend."""

PLOT_MAGIC_STRINGS = {'loglog': LOG_LOG, 'logy': LOGY, 'logx': LOGX,
        'xlabel': XLABEL, 'ylabel': YLABEL, 'sigma': SIGMA,
        'ax': AX, 'rax': RETURNS_AX, 'labels': LABELS, 'xlabel': XLABEL,
        'ylabel': YLABEL, 'kwargs': KWARGS, 'cmap': CMAP, 'title': TITLE,
        'matLabelFmt': MAT_FMT_DOC, 'legend': LEGEND, 'ncol': NCOL,
        'univLabelFmt': UNIV_FMT_DOC,}
"""Magic strings that, if found as {x}, will be replaced by the key of x"""


def magicPlotDocDecorator(f):
    """
    Decorator that replaces a lot magic strings used in plot functions.
    
    Allows docstrings to contain keyword that will be replaced with
    a valid and proper explanation of the keyword.
    Keywords must be wrapped in single brackets, i.e. ``{x}``
    """
    
    
    @wraps(f)
    def decorated(*args, **kwargs):
        return f(*args, **kwargs)
    doc = dedent(f.__doc__)
    for magic, replace in PLOT_MAGIC_STRINGS.items():
        lookF = '{' + magic + '}'
        if lookF in doc:
            doc = doc.replace(lookF, replace)
    decorated.__doc__ = doc
    return decorated

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

@magicPlotDocDecorator
def cartMeshPlot(data, xticks, yticks, ax=None, cmap=None, logScale=False,
                 normalizer=None, cbarLabel=None, **kwargs):
    """
    Create a cartesian mesh plot of the data

    Parameters
    ----------
    data: numpy.array
        2D array of data to be plotted
    xticks: iterable
        Values corresponding to lower x boundary of meshes
    yticks: iterable
        Values corresponding to lower y boundary of meshes
    {ax}
    {cmap}
    logScale: bool
        If true, apply a logarithmic coloring 
    normalizer: callable or :py:class:`matplotlib.colors.Normalize`
        Custom normalizer for this plot.
        If an instance of :py:class:`matplotlib.colors.Normalize`, 
        use directly.  Otherwise, assume a callable object and call as 
        ``norm = normalizer(data, xticks, yticks)``
    cbarLabel: None or str
        Label to apply to colorbar
    {kwargs} :py:func:`matplotlib.pyplot.pcolormesh`

    Returns
    -------
    {rax}

    Raises
    ------
    ValueError:
        If ``logScale`` and data contains negative quantities

    See Also
    --------
    * :py:func:`matplotlib.pyplot.pcolormesh`
    * :py:class:`matplotlib.colors.Normalize`
    """
    assert len(data.shape) == 2, 'Mesh plot requires 2D data, ' \
                                 'not {}'.format(data.shape)
    if logScale and data.min() < 0:
        raise ValueError("Will not apply log normalization to data with "
                         "negative elements")

    if not logScale and normalizer is None:
        norm = None
    elif normalizer is not None:
        norm =  (normalizer if isinstance(normalizer, Normlize) 
                 else normalizer(data, xticks, yticks))
    else:
        smallestPos = data[where(data > 0)].min()
        norm = LogNorm(smallestPos, data.max())

    # make the plot
    ax = ax or pyplot.axes()
    X, Y = meshgrid(xticks, yticks)
    quadmesh = ax.pcolormesh(X, Y, data, cmap=cmap, norm=norm, **kwargs)
    cbar = ax.figure.colorbar(quadmesh, norm=norm)
    if cbarLabel is not None:
        cbar.ax.set_ylabel(cbarLabel)

    return ax


@magicPlotDocDecorator
def plot(xdata, plotData, ax=None, labels=None, yerr=None, **kwargs):
    """
    Shortcut plot for plotting series of labeled data onto a plot

    If ``plotData`` is an array, it is assumed that each column
    represents one set of data to be plotted against ``xdata``.
    The same assumption is made for ``yerr`` if given.

    Parameters
    ----------
    xdata: numpy.array or iterable
        Points along the x axis to plot
    plotData: numpy.array or iterable
        Data to be plotted
    {ax}
    {labels}
    yerr: None or numpy.array or iterable
        Absolute error for each data point in ``plotData``
    {kwargs} :py:func:`matplotlib.pyplot.plot` or 
        :py:func:`matplotlib.pyplot.errorbar`

    Returns
    -------
    {rax}

    Raises
    ------
    IndexError
        If ``yerr`` is not ``None`` and does not match the shape
        of ``plotData``
        
    """
    ax = ax or pyplot.axes()

    if yerr is not None:
        if not yerr.shape == plotData.shape:
            raise IndexError(
                "Y error data has shape {}, while plotData has shape {}".format(
                yerr.shape, plotData.shape))
        errBar = True
    else:
        errBar = False

    if len(plotData.shape) == 1:
        plotData = plotData.reshape(plotData.size, 1)
    dShape = plotData.shape
    if labels is None:
        labels = [None] * (dShape[1] if len(dShape) > 1 else 1)
    if 'label' in kwargs:
        labels[0] = kwargs.pop('label')
    if errBar and yerr.shape != plotData.shape:
        yerr = yerr.reshape(plotData.shape)
    
    for col, label in enumerate(labels):
        if errBar:
            ax.errorbar(xdata, plotData[:, col], label=label, yerr=yerr[:, col],
                    **kwargs)
        else:
           ax.plot(xdata, plotData[:, col], label=label, **kwargs)

    if any(labels):
        ax.legend()

    return ax


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

