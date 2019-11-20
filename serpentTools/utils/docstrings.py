"""
Utilities for modifying docstrings
"""
from textwrap import dedent

__all__ = [
    'magicPlotDocDecorator',
    'compareDocDecorator',
    'compareDocReplacer',
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

LEGEND = """legend: bool or str or None
    Automatically label the plot. No legend will be made if a
    single item is plotted. Pass one of the following values
    to place the legend outside the plot: {}""".format(
    "above, right")

NCOL = """ncol: int\n    Integer number of columns to apply to the legend."""

MESH_THRESH = """thresh: float
    Do not plot data less than or equal to this value."""

PLOT_MAGIC_STRINGS = {
    'loglog': LOG_LOG, 'logy': LOGY, 'logx': LOGX,
    'xlabel': XLABEL, 'ylabel': YLABEL, 'sigma': SIGMA,
    'ax': AX, 'rax': RETURNS_AX, 'labels': LABELS, 'xlabel': XLABEL,
    'ylabel': YLABEL, 'kwargs': KWARGS, 'cmap': CMAP, 'title': TITLE,
    'matLabelFmt': MAT_FMT_DOC, 'legend': LEGEND, 'ncol': NCOL,
    'univLabelFmt': UNIV_FMT_DOC, 'mthresh': MESH_THRESH,
}
"""Magic strings that, if found as {x}, will be replaced by the key of x"""


def magicPlotDocDecorator(f):
    """
    Decorator that replaces a lot magic strings used in plot functions.

    Allows docstrings to contain keyword that will be replaced with
    a valid and proper explanation of the keyword.
    Keywords must be wrapped in single brackets, i.e. ``{x}``
    """

    doc = dedent(f.__doc__)
    for magic, replace in PLOT_MAGIC_STRINGS.items():
        lookF = '{' + magic + '}'
        if lookF in doc:
            doc = doc.replace(lookF, replace)
    f.__doc__ = doc
    return f


COMPARE_DOC_DESC = """
    desc0: dict or None
    desc1: dict or None
        Description of the origin of each value set. Only needed
        if ``quiet`` evalues to ``True``."""
COMPARE_DOC_HERALD = """herald: callable
        Function that accepts a single string argument used to
        notify that differences were found. If
        the function is not a callable object, a
        :func:`serpentTools.messages.critical` message
        will be printed and :func:`serpentTools.messages.error`
        will be used."""
COMPARE_DOC_LIMITS = """
    lower: float or int
        Lower limit for relative tolerances in percent
        Differences below this will be considered allowable
    upper: float or int
        Upper limit for relative tolerances in percent. Differences
        above this will be considered failure and errors
        messages will be raised"""
COMPARE_DOC_SIGMA = """sigma: int
        Size of confidence interval to apply to
        quantities with uncertainties. Quantities that do not
        have overlapping confidence intervals will fail"""
COMPARE_DOC_TYPE_ERR = """TypeError
        If ``other`` is not of the same class as this class
        nor a subclass of this class"""
COMPARE_DOC_HEADER = """header: bool
        Print/log an ``info`` message about this comparison."""
COMPARE_DOC_MAPPING = {
    'herald': COMPARE_DOC_HERALD,
    'desc': COMPARE_DOC_DESC,
    'compLimits': COMPARE_DOC_LIMITS,
    'sigma': COMPARE_DOC_SIGMA,
    'compTypeErr': COMPARE_DOC_TYPE_ERR,
    'header': COMPARE_DOC_HEADER,
}

COMPARE_FAIL_MSG = "Values {desc0} and {desc1} are not identical:\n\t"
COMPARE_WARN_MSG = ("Values {desc0} and {desc1} are not identical, but within "
                    "tolerances:\n\t")
COMPARE_PASS_MSG = "Values {desc0} and {desc0} are identical:\n\t"


def compareDocReplacer(doc):
    """Make replacements for comparison docstrings."""
    if not doc:
        return ""
    doc = dedent(doc)
    for magic, replace in COMPARE_DOC_MAPPING.items():
        lookF = '{' + magic + '}'
        if lookF in doc:
            doc = doc.replace(lookF, dedent(replace))
    return doc


def compareDocDecorator(f):
    """Decorator that updates doc strings for comparison methods.

    Similar to :func:`serpentTools.plot.magicPlotDocDecorator`
    but for comparison functions
    """

    f.__doc__ = compareDocReplacer(f.__doc__)
    return f
