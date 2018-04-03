"""Plot routines"""
from functools import wraps
from textwrap import dedent

from six import iteritems

import numpy
from numpy import meshgrid, where
from matplotlib import pyplot
from matplotlib.colors import LogNorm, Normalize

#
# DOCSTRING EXTRAS
#
_MPL_AX = ':py:class:`matplotlib.axes.Axes`'
_LOG_BASE = """log{}: bool\n    Apply a log scale to {}."""
LOG_LOG = _LOG_BASE.format('log', 'both axes')
LOGX = _LOG_BASE.format('x', 'x axis')
LOGY = _LOG_BASE.format('y', 'y axis')
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

PLOT_MAGIC_STRINGS = {'loglog': LOG_LOG, 'logy': LOGY, 'logx': LOGX,
        'xlabel': XLABEL, 'ylabel': YLABEL, 'sigma': SIGMA,
        'ax': AX, 'rax': RETURNS_AX, 'labels': LABELS, 'xlabel': XLABEL,
        'ylabel': YLABEL, 'kwargs': KWARGS, 'cmap': CMAP,
        'matLabelFmt': MAT_FMT_DOC}
"""Magic strings that, if found as {x}, will be replaced by the key of x"""


def magicPlotDocDecorator(f):
    """Decorator that replaces a lot magic strings used in plot functions"""
    
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
    normalizer: callable or Normalize
        Custom normalizer for this plot.
        If an instance of ``Normalize``, use directly.
        Otherwise, assume a callable object and call as 
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

