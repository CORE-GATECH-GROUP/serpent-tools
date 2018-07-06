.. _dev-plot-utilities:

==================
Plotting Utilities
==================

Plot Functions
==============

The `serpentTools.plot` module contains some functions to assist in plotting
and for describing plot functions. These are not required for use, but
their behavior, and the advice given in :ref:`dev-plotting`, should be
followed. This will yield a consistent and flexible plotting environment
to the user without having to dive deep into the :mod:`matplotlib`
framework.

.. autofunction:: serpentTools.plot.cartMeshPlot

.. autofunction:: serpentTools.plot.plot


.. _dev-plot-formatters:

Plot Formatters
===============

The following functions can be used to tidy up a plot given our wide-range
of supported arguments.

.. autofunction:: serpentTools.plot.formatPlot

.. autoattribute:: serpentTools.plot.PLOT_FORMAT_DEFAULTS

.. autoattribute:: serpentTools.plot.LEGEND_KWARGS

.. autofunction:: serpentTools.plot.placeLegend

.. autofunction:: serpentTools.plot.setAx_xlims

.. autofunction:: serpentTools.plot.setAx_ylims

.. autofunction:: serpentTools.plot.addColorbar

.. autofunction:: serpentTools.plot.normalizerFactory

.. _dev-plot-docformatters:

Docstring Formatters for Plots
==============================

Many of the plot routines accept common parameters, such as ``logx``
for applying a log scale to the x-axis. To reduce the amount of
repeated code, the following formatting functions operate
on the docstrings of a plot function/method and save a lot of
extra code.

See :ref:`dev-plot-magicStrings` for a listing of what is replaced
by what when calling :func:`serpentTools.plot.magicPlotDocDecorator`.

.. autofunction:: serpentTools.plot.magicPlotDocDecorator

.. autoattribute:: serpentTools.plot.PLOT_MAGIC_STRINGS
    :annotation: Magic strings that, if found as {x}, will be replaced
                 by PLOT_MAGIC_STRINGS[x]

