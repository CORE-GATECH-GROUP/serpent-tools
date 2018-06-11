"""
Commonly used functions and utilities
"""

from collections import Callable
from textwrap import dedent
from functools import wraps

from six import iteritems
from numpy import array, ndarray, fabs, where

from serpentTools.messages import (
    error,
    critical,
    identical,
    notIdentical,
    acceptableLow,
    acceptableHigh,
    outsideTols,
    differentTypes,
    )

LOWER_LIM_DIVISION = 1E-8
"""Lower limit for denominator for division"""


def str2vec(iterable, of=float, out=array):
    """
    Convert a string or other iterable to vector.

    Parameters
    ----------
    iterable: str or iterable
        If string, will be split with ``split(splitAt)``
        to create a list. Every item in this list, or original
        iterable, will be iterated over and converted accoring
        to the other arguments.
    of: type
        Convert each value in ``iterable`` to this data type.
    out: type
        Return data type. Will be passed the iterable of
        converted items of data dtype ``of``.

    Returns
    -------
    vector
        Iterable of all values of ``iterable``, or split variant,
        converted to type ``of``.

    Examples
    --------
    ::

        >>> v = "1 2 3 4"
        >>> str2vec(v)
        array([1., 2., 3., 4.,])

        >>> str2vec(v, int, list)
        [1, 2, 3, 4]

        >>> x = [1, 2, 3, 4]
        >>> str2vec(x)
        array([1., 2., 3., 4.,])

    """
    vec = (iterable.split() if isinstance(iterable, str)
           else iterable)
    return out([of(xx) for xx in vec])


def splitValsUncs(iterable, copy=False):
    """
    Return even and odd indexed values from iterable

    Designed to extract expected values and uncertainties from
    SERPENT vectors of the form
    ``[x1, u1, x2, u2, ...]``

    Parameters
    ----------
    iterable: ndarray or iterable
        Initial arguments to be processed. If not
        :py:class:`numpy.ndarray`, then will be converted
        by calling :py:func:`serpentTools.utils.str2vec`
    copy: bool
        If true, return a unique instance of the values
        and uncertainties. Otherwise, returns a view
        per numpy slicing methods

    Returns
    -------
    numpy.ndarray
        Even indexed values from ``iterable``
    numpy.ndarray
        Odd indexed values from ``iterable``

    Examples
    --------
    ::

        >>> v = [1, 2, 3, 4]
        >>> splitValsUncs(v)
        array([1, 3]), array([2, 4])

        >>> line = "1 2 3 4"
        >>> splitValsUnc(line)
        array([1, 3]), array([2, 4])

    """

    if not isinstance(iterable, ndarray):
        iterable = str2vec(iterable)
    vals = iterable[0::2]
    uncs = iterable[1::2]
    if copy:
        return vals.copy(), uncs.copy()
    return vals, uncs


def convertVariableName(variable):
    """
    Return the mixedCase version of a SERPENT variable.

    Parameters
    ----------
    variable: str
        ``SERPENT_STYLE`` variable name to be converted

    Returns
    -------
    str:
        Variable name that has been split at underscores and
        converted to ``mixedCase``

    Examples
    --------
    ::

        >>> v = "INF_KINF"
        >>> convertVariableName(v)
        infKinf

        >>> v = "VERSION"
        >>> convertVariableName(v)
        version

    """
    lowerSplits = [item.lower() for item in variable.split('_')]
    if len(lowerSplits) == 1:
        return lowerSplits[0]
    return lowerSplits[0] + ''.join([item.capitalize()
                                     for item in lowerSplits[1:]])


LEADER_TO_WIKI = "http://serpent.vtt.fi/mediawiki/index.php/"


def linkToWiki(subLink, text=None):
    """
    Return a string that will render as a hyperlink to the SERPENT wiki.

    Parameters
    ----------
    subLink: str
        Desired path inside the SERPENT wiki - following the
        ``index.php``
    text: None or str
        If given, use this as the shown text for the full link.

    Returns
    -------
    str:
        String that can be used as an rst hyperlink to the
        SERPENT wiki

    Examples
    --------
    >>> linkToWiki('Input_syntax_manual')
    http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual
    >>> linkToWiki('Description_of_output_files#Burnup_calculation_output',
    ...            "Depletion Output")
    `Depletion Output <http://serpent.vtt.fi/mediawiki/index.php/
    Description_of_output_files#Burnup_calculation_output>`_
    """
    fullLink = LEADER_TO_WIKI + subLink
    if not text:
        return fullLink
    return "`{} <{}>`_".format(text, fullLink)


COMPARE_DOC_DESC = """
    desc0: dict or None
    desc1: dict or None
        Description of the origin of each value set. Only needed
        if ``quiet`` evalues to ``True."""
COMPARE_DOC_HERALD = """herald: callable
        Function that accepts a single string argument used to
        notify that differences were found. If
        the function is not a callable object, a
        :func:`serpentTools.messages.critical` message
        will be printed and :func:`serpentTools.messages.error`
        will be used."""
COMPARE_DOC_LIMITS = """
    lower: float or int
        Lower limit for relative tolerances.
        Differences below this will be considered allowable
    upper: float or int
        Upper limit for relative tolerances. Differences
        above this will be considered failure and errors
        messages will be raised"""
COMPARE_DOC_SIGMA = """sigma: int
        Size of confidence interval to apply to
        quantities with uncertainties. Quantities that do not
        have overlapping confidence intervals will fail"""

COMPARE_DOC_MAPPING = {
    'herald': COMPARE_DOC_HERALD,
    'desc': COMPARE_DOC_DESC,
    'compLimits': COMPARE_DOC_LIMITS,
    'sigma': COMPARE_DOC_SIGMA,
}

COMPARE_FAIL_MSG = "Values {desc0} and {desc1} are not identical:\n\t"
COMPARE_WARN_MSG = ("Values {desc0} and {desc1} are not identical, but within "
                    "tolerances:\n\t")
COMPARE_PASS_MSG = "Values {desc0} and {desc0} are identical:\n\t"


def compareDocDecorator(f):
    """Decorator that updates doc strings for comparison methods.

    Similar to :func:`serpentTools.plot.magicPlotDocDecorator`
    but for comparison functions
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        return f(*args, **kwargs)
    doc = dedent(f.__doc__)
    for magic, replace in iteritems(COMPARE_DOC_MAPPING):
        lookF = '{' + magic + '}'
        if lookF in doc:
            doc = doc.replace(lookF, dedent(replace))
    decorated.__doc__ = doc
    return decorated


def _getDefDescs(desc0, desc1):
    desc0 = desc0 if desc0 is not None else 'first'
    desc1 = desc1 if desc1 is not None else 'second'
    return desc0, desc1


def _checkHerald(herald):
    if not isinstance(herald, Callable):
        critical("Heralding object {} is not callable. Falling back to error."
                 .format(herald))
        return error
    return herald


@compareDocDecorator
def getCommonKeys(d0, d1, desc0=None, desc1=None, herald=error):
    """
    Return a set of common keys from two dictionaries

    Also supports printing warning messages for keys not
    found on one collection.

    If ``d0`` and ``d1`` are :class:`dict`, then the
    keys will be obtained with ``d1.keys()``. Otherwise,
    assume we have an iterable of keys and convert to
    :class:`set`.

    Parameters
    ----------
    d0: dict or iterable
    d1: dict or iterable
        Dictionary of keys or iterable of keys to be compared
    {desc}
    {herald}
    Returns
    -------
    set:
        Keys found in both ``d{{0, 1}}``
    """
    herald = _checkHerald(herald)
    k0 = d0.keys() if isinstance(d0, dict) else d0
    k1 = d1.keys() if isinstance(d1, dict) else d1
    s0 = set(k0)
    s1 = set(k1)

    common = s0.intersection(s1)
    missing = s0.symmetric_difference(s1)
    if missing:
        desc0, desc1 = _getDefDescs(desc0, desc1)
        msg = ("Objects {} and {} contain different values"
               .format(desc0, desc1))
        missingMsg = "\n\tItems present in {} but not in {}:\n\t\t{}"
        in0 = s0.difference(s1)
        if any(in0):
            msg += missingMsg.format(desc0, desc1, in0)
        in1 = s1.difference(s0)
        if any(in1):
            msg += missingMsg.format(desc1, desc0, in1)
        herald(msg)
    return common


@compareDocDecorator
def directCompare(obj0, obj1, lower, upper, quantity):
    """
    Return True if values are close enough to each other.

    Wrapper around various comparision tests for strings, numeric, and
    arrays.

    The failing values will be appended to the next line of the error message

    Parameters
    ----------
    obj0: str or float or int or :class:`numpy.ndarray`
    obj1: str or float or int or :class:`numpy.ndarray`
        Objects to compare
    {compLimits}
    quantity: str
        Description of the value being compared. Will be
        used to notify the user about any differences

    Returns
    -------
    bool:
        If the values are close enough as determined by the settings.

    Raises
    ------
    TypeError:
        If the object types are not supported. This means the developers
        need to either extend this to meet the type, or use a different
        test function.
    """
    type0 = type(obj0)
    type1 = type(obj1)
    noticeTuple = [obj0, obj1, quantity]
    if type0 != type(obj1):
        differentTypes(type0, type1, quantity)
        return False
    if type0 is str:
        if obj0 != obj1:
            notIdentical(*noticeTuple)
            return False
        identical(*noticeTuple)
        return True

    if type0 in (float, int, ndarray):
        diff = fabs(obj0 - obj1)
        if type0 is ndarray:
            nonZI = where(obj0 > LOWER_LIM_DIVISION)
            diff[nonZI] /= obj0[nonZI]
        elif obj0 > LOWER_LIM_DIVISION:
            diff /= obj0
        if diff < lower:
            acceptableLow(*noticeTuple)
            return True
        if diff >= upper:
            outsideTols(*noticeTuple)
            return False
        acceptableHigh(*noticeTuple)
        return True
    raise TypeError(
          "directCompare is not configured to make tests on objects of type "
          "{tp}\n\tUsers: Create a issue on GitHub to alert developers."
          "\n\tDevelopers: Update this function or create a compare function "
          "for {tp} objects.".format(tp=type0))
