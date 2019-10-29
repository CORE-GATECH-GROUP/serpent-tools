.. |magicPlotDec| replace:: :py:func:`~serpentTools.plot.magicPlotDocDecorator`

.. |axes| replace:: :py:class:`matplotlib.axes.Axes` 

.. |formatPlot| replace:: :py:func:`~serpentTools.plot.formatPlot`

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

.. note::

    Plot functions should contain sufficient formatting such that,
    with minimal user input, processional and publishable plots
    are produced.

This cohesion is accomplished by decorating plot routines with
the |magicPlotDec| and by supporting a collection of additional arguments 
used for formatting the plot. 
These magic strings are detailed in :ref:`dev-plot-magicStrings` and
can be included in any function decorated by |magicPlotDec| as
``{legend}``.

When appropriate, plot functions should accept a
|axes| argument on which to plot the data.
This is useful for subplotting, or for creating a plot and then
continuing the plotting inside this function.
If not given, the function should create a new |axes| object.
All plotting should be done on this axes object, such as::

    def plot(ax=None):
        ax = ax or pyplot.axes()
        ax.plot([1,2,3])
        return ax

By returning the axes object, users can further apply labels, place the 
plot into subplots, or more.

Axes for all plots should be labeled without user intervention, but
should support user-defined labels. 
This process can be expedited by utilizing |formatPlot| as 
the last stage of the plotting process. This function accepts
a variety of keyword arguments that are used to set axis labels 
or scaling, even placing the legend outside the plot. Taking
the simple plot method from above, we can modify this method
to accept user arguments for labels, but also have default labels
should the user not provide them::

    def plot(ax=None, xlabel=None, ylabel=None):
        ax = ax or pyplot.axes()
        ax.plot([1, 2, 3])
        xlabel = xlabel or "Default x label"
        ax = formatPlot(ax, xlabel=xlabel,
                        ylabel=ylabel or "Y axis")
        return ax

.. _dev-plot-utilities:

Plotting Utilities
==================

Plot Functions
--------------

The ``serpentTools.plot`` module contains some functions to assist in plotting
and for describing plot functions. These are not required for use, but
their behavior, and the advice given in :ref:`dev-plotting`, should be
followed. This will yield a consistent and flexible plotting environment
to the user without having to dive deep into the :mod:`matplotlib`
framework.

.. currentmodule:: serpentTools.plot

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myfunction.rst

    cartMeshPlot
    plot

.. _dev-plot-formatters:

Plot Formatters
---------------

The following functions can be used to tidy up a plot given our wide-range
of supported arguments.

.. currentmodule:: serpentTools.utils.plot

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myfunction.rst

    formatPlot
    placeLegend
    setAx_xlims
    setAx_ylims
    addColorbar
    normalizerFactory

.. _dev-plot-docformatters:

Docstring Formatters for Plots
------------------------------

Many of the plot routines accept common parameters, such as ``logx``
for applying a log scale to the x-axis. To reduce the amount of
repeated code, the following formatting functions operate
on the docstrings of a plot function/method and save a lot of
extra code.

See :ref:`dev-plot-magicStrings` for a listing of what is replaced
by what when calling :func:`serpentTools.plot.magicPlotDocDecorator`.

.. autofunction:: serpentTools.utils.docstrings.magicPlotDocDecorator

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

