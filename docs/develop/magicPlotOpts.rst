#. ``ax``: ax: :py:class:`matplotlib.axes.Axes` or None
    Ax on which to plot the data.
#. ``cmap``: cmap: str or None
    Valid Matplotlib colormap to apply to the plot.
#. ``kwargs``: kwargs:
    Addition keyword arguments to pass to
#. ``labels``: labels: None or iterable
    Labels to apply to each line drawn. This can be used to identify
    which bin is plotted as what line.
#. ``legend``: legend: bool or str
    Automatically label the plot. Pass one of the following values
    to place the legend outside the plot: above, right
#. ``loglog``: loglog: bool
    Apply a log scale to both axes.
#. ``logx``: logx: bool
    Apply a log scale to x axis.
#. ``logy``: logy: bool
    Apply a log scale to y axis.
#. ``matLabelFmt``: labelFmt: str or None
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

#. ``ncol``: ncol: int
    Integer number of columns to apply to the legend.
#. ``rax``: :py:class:`matplotlib.axes.Axes`
    Ax on which the data was plotted.
#. ``sigma``: sigma: int
    Confidence interval to apply to errors. If not given or ``0``, 
    no errors will be drawn.
#. ``title``: title: str
    Title to apply to the figure.
#. ``xlabel``: xlabel: str or None
    Label for x-axis.
#. ``ylabel``: yabel: str or None
    Label for y-axis.