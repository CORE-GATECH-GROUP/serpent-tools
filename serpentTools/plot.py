"""Plot routines"""

import numpy
from numpy import meshgrid, where
from matplotlib import pyplot
from matplotlib.colors import LogNorm, Normalize

def cartMeshPlot(data, xticks, yticks, ax=None, cmap=None, logScale=False,
                 normalizer=None, **kwargs):
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
    ax: matplotlib.pyplot.Axes
        Existing figure on which to draw the plot
    cmap: None or str
        colormap to apply to the figure. Must be a valid matplotlib
        colormap
    logScale: bool
        If true, apply a logarithmic coloring 
    normalizer: callable or Normalize
        Custom normalizer for this plot.
        If an instance of ``Normalize``, use directly.
        Otherwise, assume a callable object and call as 
        ``norm = normalizer(data, xticks, yticks)``
    kwargs:
        Additional keyword arguments to pass to
        :py:func:`matplotlib.colors.pcolormesh`

    Returns
    -------
    matplotlib.pyplot.Axes
        plot on which the figure was drawn

    Raises
    ------
    ValueError:
        If ``logScale`` and data contains negative quantities

    See Also
    --------
    :py:func:`matplotlib.colors.pcolormesh`
    :py:class:`matplotlib.colors.Normalize`
    """
    assert len(data.shape) == 2, 'Mesh plot requires 2D data, ' \
                                 'not {}'.format(data.shape)
    assert data.size == len(xticks) * len(yticks), (
        'Cannot properly for a mesh with the presented data. \n# points: {}, '
        '# x mesh points: {}, # y mesh points: {}'.format(
            data.shape, len(xticks), len(yticks)))
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
    ax.figure.colorbar(quadmesh, norm=norm)

    return ax
