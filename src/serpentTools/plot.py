"""Plot routines"""

from numpy import meshgrid
from numpy.ma import masked_less_equal
from matplotlib import pyplot

from serpentTools.messages import warning
from serpentTools.utils import (
    magicPlotDocDecorator,
    addColorbar,
    normalizerFactory,
)

__all__ = [
    'cartMeshPlot',
]


@magicPlotDocDecorator
def cartMeshPlot(data, xticks=None, yticks=None, ax=None, cmap=None,
                 logColor=False, normalizer=None, cbarLabel=None,
                 thresh=None, **kwargs):
    """
    Create a cartesian mesh plot of the data

    Parameters
    ----------
    data: numpy.array
        2D array of data to be plotted
    xticks: iterable or None
    yticks: iterable or None
        Values corresponding to lower x/y boundary of meshes.
        If not given, treat this as a matrix plot like
        :func:`matplotlib.pyplot.imshow`.
        If given, they should contain one more item than
        number of elements in their dimension to give dimensions
        for all meshes.
    {ax}
    {cmap}
    logColor: bool
        If true, apply a logarithmic coloring
    normalizer: callable or :py:class:`matplotlib.colors.Normalize`
        Custom normalizer for this plot.
        If an instance of :py:class:`matplotlib.colors.Normalize`,
    normalizer: callable or :py:class:`matplotlib.colors.Normalize`
        Custom normalizer for this plot.
        If an instance of :py:class:`matplotlib.colors.Normalize`,
        use directly.  Otherwise, assume a callable object and call as
        ``norm = normalizer(data, xticks, yticks)``
    cbarLabel: None or str
        Label to apply to colorbar
    {thresh}
    {kwargs} :py:func:`matplotlib.pyplot.pcolormesh` or
        :func:`matplotlib.pyplot.imshow` if ``xticks`` and ``yticks``
        are ``None``

    Returns
    -------
    {rax}

    Raises
    ------
    ValueError
        If ``logColor`` and data contains negative quantities
    TypeError
        If only one of ``xticks`` or ``yticks`` is ``None``.

    Examples
    --------
    .. plot::
        :include-source:

        >>> from serpentTools.plot import cartMeshPlot
        >>> from numpy import arange
        >>> data = arange(100).reshape(10, 10)
        >>> x = y = arange(11)
        >>> cartMeshPlot(data, x, y, cbarLabel='Demo')

    .. plot::
        :include-source:

        >>> from serpentTools.plot import cartMeshPlot
        >>> from numpy import  eye
        >>> data = eye(10)
        >>> for indx in range(10):
        ...     data[indx] *= indx
        >>> cartMeshPlot(data, logColor=True)

    All values less than or equal to zero are excluded from the
    color normalization. The ``logColor`` argument works well for
    plotting sparse matrices, as the zero-valued indices can be
    identified without obscuring the trends presented in the
    non-zero data.

    Alternatively, one can use the ``thresh`` argument to
    set a threshold for plotted data. Any value less
    than or equal to ``thresh`` will not be colored,
    and the colorbar will be updated to reflect this.

    .. plot::
        :include-source:

        >>> from serpentTools.plot import cartMeshPlot
        >>> from numpy import arange
        >>> data = arange(100).reshape(10, 10)
        >>> cartMeshPlot(data, thresh=50)

    See Also
    --------
    * :func:`matplotlib.pyplot.pcolormesh`
    * :func:`matplotlib.pyplot.imshow`
    * :class:`matplotlib.colors.Normalize`

    """
    assert len(data.shape) == 2, 'Mesh plot requires 2D data, ' \
                                 'not {}'.format(data.shape)
    if ((xticks is None and yticks is not None)
            or (xticks is None and yticks is not None)):
        raise TypeError("Both X and Y must be None, or not None.")

    if kwargs.get('logScale', None) is not None:
        warning("Passing logScale is no longer supported. "
                "Use logColor instead.")
        logColor = bool(logColor or kwargs['logScale'])

    if thresh is not None:
        data = masked_less_equal(data, thresh)

    if logColor and data.min() < 0:
        raise ValueError("Will not apply log normalization to data with "
                         "negative elements")
    norm = normalizerFactory(data, normalizer, logColor, xticks, yticks)

    # make the plot

    ax = ax or pyplot.gca()
    if xticks is None:
        mappable = ax.imshow(data, cmap=cmap, norm=norm)
    else:
        X, Y = meshgrid(xticks, yticks)
        mappable = ax.pcolormesh(X, Y, data, cmap=cmap, norm=norm, **kwargs)
    addColorbar(ax, mappable, cbarLabel)

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
    ax = ax or pyplot.gca()

    if yerr is not None:
        if not yerr.shape == plotData.shape:
            raise IndexError(
                "Y error data has shape {}, while plotData has shape {}"
                .format(yerr.shape, plotData.shape))
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
            ax.errorbar(xdata, plotData[:, col], label=label,
                        yerr=yerr[:, col], **kwargs)
        else:
            ax.plot(xdata, plotData[:, col], label=label, **kwargs)

    if any(labels):
        ax.legend()

    return ax
