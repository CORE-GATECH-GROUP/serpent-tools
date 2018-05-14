.. |magicPlotDec| replace:: :py:func:`~serpentTools.plot.magicPlotDocDecorator`

.. _dev-plotting:

========
Plotting
========

Many of the readers and containers in this project have plot routines
to quickly visualize relevant data.
The goal for these plots is to quickly provide presentation-worthy
plots by default, with options for formatting via additional arguments.
This document serves as a guide for writing plot functions that
have a cohesive syntax across the project and require little to no
knowledge of `matplotlib` to make a fantastic plot.

This cohesion is accomplished by decorating plot routines with
the |magicPlotDec| and by supporting a collection of additional arguments 
used for formatting the plot. 
These magic strings are detailed in :ref:`dev-plot-magicStrings` and
can be included in any function decorated by |magicPlotDec| as
``{legend}``.

When appropriate, plot functions should accept a
:py:class:`matplotlib.axes.Axes` argument on which to plot
the data.
This is useful for subplotting, or for creating a plot and then
continuing the plotting inside this function.
If not given, the function should create a new 
:py:class:`matplotlib.axes.Axes` object.
All formatting should be done on this axes object, such as::

    def plot(ax=None):
        ax = ax or pyplot.axes.Axes()
        ax.plot([1,2,3])
        ax.set_xlabel('X')
        return ax

By returning the axes object, users can further apply labels, place the 
plot into subplots, or more.

Axes for all plots should be labeled without user intervention, but
should support user-defined labels. 

.. _dev-plot-magicStrings:

Magic Plot Decorator Options
----------------------------

.. note::

    These keyword arguments should only be used when they are 
    appropriate for the specific plot method. Colormaps
    don't really make sense for line plots, but can be very
    useful for 2D contour and mesh plots. ``cmap`` should be a 
    supported argument for most of these plot types, but not
    for line plots, unless it makes sense to do such.

.. include:: ./magicPlotOpts.rst


