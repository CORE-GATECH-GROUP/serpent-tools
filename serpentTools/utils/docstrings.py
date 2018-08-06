"""
Utilities for modifying docstrings
"""
from functools import wraps
from textwrap import dedent

__all__ = [
    'magicPlotDocDecorator',
]

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

LEGEND = """legend: bool or str
    Automatically label the plot. Pass one of the following values
    to place the legend outside the plot: {}""".format(
    "above, right")

NCOL = """ncol: int\n    Integer number of columns to apply to the legend."""

PLOT_MAGIC_STRINGS = {
    'loglog': LOG_LOG, 'logy': LOGY, 'logx': LOGX,
    'xlabel': XLABEL, 'ylabel': YLABEL, 'sigma': SIGMA,
    'ax': AX, 'rax': RETURNS_AX, 'labels': LABELS, 'xlabel': XLABEL,
    'ylabel': YLABEL, 'kwargs': KWARGS, 'cmap': CMAP, 'title': TITLE,
    'matLabelFmt': MAT_FMT_DOC, 'legend': LEGEND, 'ncol': NCOL,
    'univLabelFmt': UNIV_FMT_DOC,
}
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
