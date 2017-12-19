"""Plot routines"""

import numpy
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection


def cartMeshPlot(data, xticks, yticks, widths=1, heights=1, ax=None, cmap=None,
                 addcbar=True):
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
    widths: float or iterable
        Width of each mesh
    heights: float or iterable
        Height of each mesh
    ax: None or matplotlib.pyplot.axes.Axe
        Figure on which to draw the plot
    cmap: None or str
        colormap to apply to the figure. Must be a valid matplotlib
        colormap
    addcbar: bool
        If true, attach a colorbar to the plot

    Returns
    -------
    ax: matplotlib.pyplot.Axes
        Object containing the patches
    """
    assert len(data.shape) == 2, 'Mesh plot requires 2D data, ' \
                                 'not {}'.format(data.shape)
    assert data.size == len(xticks) * len(yticks), (
        'Cannot properly for a mesh with the presented data. \n# points: {}, '
        '# x mesh points: {}, # y mesh points: {}'.format(
            data.shape, len(xticks), len(yticks)))
    if isinstance(widths, (float, int)):
        widths = numpy.ones_like(xticks) * widths
    else:
        assert len(widths) == len(xticks)
    if isinstance(heights, (float, int)):
        heights = numpy.ones_like(yticks) * heights
    else:
        assert len(heights) == len(yticks)

    # make the patches

    patches = []
    for xindx, xbound in enumerate(xticks):
        for yindx, ybound in enumerate(yticks):
            patches.append(Rectangle(
                (xbound, ybound), width=widths[xindx], height=heights[yindx]
            ))
    patches = PatchCollection(patches, cmap=cmap)
    patches.set_array(data.flatten())

    # make the plot
    ax = ax or pyplot.axes()

    ax.add_collection(patches)
    if addcbar:
        fig = pyplot.gcf()
        fig.colorbar(patches, ax=ax)

    ax.set_xlim((xticks.min(), xticks.max() + widths[-1]))
    ax.set_ylim((yticks.min(), yticks.max() + heights[-1]))

    return ax
