"""
Commonly used functions and utilities
"""

from textwrap import dedent
from functools import wraps

from six import iteritems
from numpy import array, ndarray, fabs, where, zeros_like, dtype

from serpentTools.messages import (
    error,
    identical,
    notIdentical,
    acceptableLow,
    acceptableHigh,
    outsideTols,
    differentTypes,
    logMissingKeys,
    logBadTypes,
    logBadShapes,
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
    vals = iterable[..., 0::2]
    uncs = iterable[..., 1::2]
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
COMPARE_DOC_MAPPING = {
    'herald': COMPARE_DOC_HERALD,
    'desc': COMPARE_DOC_DESC,
    'compLimits': COMPARE_DOC_LIMITS,
    'sigma': COMPARE_DOC_SIGMA,
    'compTypeErr': COMPARE_DOC_TYPE_ERR,
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


@compareDocDecorator
def getCommonKeys(d0, d1, quantity, desc0='first', desc1='second',
                  herald=error):
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
    quantity: str
        Indicator as to what is being compared, e.g. ``'metadta'``
    {desc}
    {herald}
    Returns
    -------
    set:
        Keys found in both ``d{{0, 1}}``
    """
    k0 = d0.keys() if isinstance(d0, dict) else d0
    k1 = d1.keys() if isinstance(d1, dict) else d1
    s0 = set(k0)
    s1 = set(k1)

    common = s0.intersection(s1)
    missing = s0.symmetric_difference(s1)
    if missing:
        in0 = s0.difference(s1)
        in1 = s1.difference(s0)
        logMissingKeys(quantity, desc0, desc1, in0, in1, herald)
    return common


COMPARE_NUMERICS = float, int


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
    if ((type0 not in COMPARE_NUMERICS or type1 not in COMPARE_NUMERICS)
            and type0 != type0):
        differentTypes(type0, type1, quantity)
        return False
    if type0 is str:
        if obj0 != obj1:
            notIdentical(*noticeTuple)
            return False
        identical(*noticeTuple)
        return True

    if type0 is bool:
        return obj0 == obj1

    if type0 in (float, int, ndarray) or hasattr(obj0, 'dtype'):
        diff = fabs(obj0 - obj1) * 100
        if type0 is ndarray:
            nonZI = where(obj0 > LOWER_LIM_DIVISION)
            diff[nonZI] /= obj0[nonZI]
        elif obj0 > LOWER_LIM_DIVISION:
            diff /= obj0
        maxDiff = diff.max() if isinstance(diff, ndarray) else diff
        if maxDiff < LOWER_LIM_DIVISION:
            identical(*noticeTuple)
            return True
        if maxDiff <= lower:
            acceptableLow(*noticeTuple)
            return True
        if maxDiff >= upper:
            outsideTols(*noticeTuple)
            return False
        acceptableHigh(*noticeTuple)
        return True
    raise TypeError(
          "directCompare is not configured to make tests on objects of type "
          "{tp}\n\tQuantity: {k}\n\tUsers: Create a issue on GitHub to alert developers."
          "\n\tDevelopers: Update this function or create a compare function "
          "for {tp} objects.".format(k=quantity, tp=type0))


def splitDictByKeys(map0, map1, keySet=None):
    """
    Return various sub-sets and dictionaries from two maps.

    Used to test the internal workings on :func:`getKeyMatchingShapes`

    Parameters
    ----------
    map0: dict
    map1: dict
        Dictionaries to compare
    keySet: set or None
        Iterable collection of keys found in ``map0`` and ``map1``.
        Missing keys will be returned from this function under
        the ``missing0`` and ``missing1`` sets. If ``None``, take
        to be the set of keys that exist in both maps

    Returns
    -------
    missing0: set
        Keys that exist in ``keySet`` but not in ``map0``
    missing1: set
        Keys that exist in ``keySet`` but not in ``map1``
    badTypes: dict
        Dictionary with tuples ``{key: (t0, t1)}`` indicating the values
        ``map0[key]`` and ``map1[key]`` are of different types
    badShapes: dict
        Dictionary with tuples ``{key: (t0, t1)}`` indicating the values
        ``map0[key]`` and ``map1[key]`` are arrays of different shapes
    goodKeys: set
        Keys found in both ``map0`` and ``map1`` that are of the same type
        or point to arrays of the same shape
    """
    if keySet is None:
        k1 = set(map1.keys())
        keySet = k1.intersection(set(map0.keys()))
    missing = {0: set(), 1: set()}
    badTypes = {}
    badShapes = {}
    goodKeys = set()
    for key in keySet:
        if key not in map0 or key not in map1:
            for mapD, misK in zip((map0, map1), (0, 1)):
                if key not in mapD:
                    missing[misK].add(key)
            continue
        v0 = map0[key]
        v1 = map1[key]
        t0 = type(v0)
        t1 = type(v1)
        if t0 != t1:
            badTypes[key] = (t0, t1)
            continue
        if t0 is ndarray:
            if v0.shape != v1.shape:
                badShapes[key] = (v0.shape, v1.shape)
                continue
        goodKeys.add(key)

    return missing[0], missing[1], badTypes, badShapes, goodKeys


def getKeyMatchingShapes(map0, map1, quantity, keySet=None, desc0='first',
                         desc1='second'):
    """
    Return a set of keys in map0/1 that point to arrays with identical shapes.

    Parameters
    ----------
    keySet: set or list or tuple or iterable or None
        Iterable container with keys that exist in map0 and map1. The contents
        of ``map0/1`` under these keys will be compared. If ``None``, 
        will be determined by :func:`splitDictByKeys`
    map0: dict
    map1: dict
        Two dictionaries containing at least all the keys in ``keySet``.
        Objects under keys in ``keySet`` will have their sizes compared if
        they are :class:`numpy.ndarray`. Non-arrays will be included only
        if their types are identical
    quantity: str
        Indicator as to what is being compared, e.g. ``'metadata'``
    desc0: str
    decs1: str
        Descriptions of the two dictionaries being compared. Used to alert the
        user to the shortcomings of the two dictionaries

    Returns
    -------
    set:
        Set of all keys that exist in both dictionaries and are either
        identical types, or are arrays of identical shapes

    See Also
    --------
    * :func:`splitDictByKeys`
    """
    missing0, missing1, badTypes, badShapes, goodKeys = (
            splitDictByKeys(map0, map1, keySet))

    # raise some messages
    if any(missing0) or any(missing1):
        logMissingKeys(quantity, desc0, desc1, missing0, missing1)
    if badTypes:
        logBadTypes(quantity, desc0, desc1, badTypes)
    if badShapes:
        logBadShapes(quantity, desc0, desc1, badShapes)
    return goodKeys


@compareDocDecorator
def getOverlaps(arr0, arr1, unc0, unc1, sigma, relative=True):
    r"""
    Return the indicies of overlapping confidence intervals

    Parameters
    ----------
    arr0: :class:`numpy.ndarray`
    arr1: :class:`numpy.ndarray`
        Arrays containing the expected values to be compared
    unc0: :class:`numpy.ndarray`
    unc1: :class:`numpy.ndarray`
        Associated absolute uncertainties, :math:`1\sigma`,
        corresponding to the values in ``arr0`` and ``arr1``
    {sigma}
    relative: bool
        True if uncertainties are relative and should be multiplied
        by their respective values. Otherwise, assume values are 
        absolute

    Returns
    -------
    :class:`numpy.ndarray`
        Boolean array of equal shape to incoming arrays.
        Every index with ``True`` as the value indicates that
        the confidence intervals for the arrays overlap
        at those indices.

    Examples
    --------
    Using absolute uncertainties::

        >>> from numpy import ones, zeros, array
        >>> a0 = ones(4)
        >>> a1 = ones(4) * 0.5
        >>> u0 = array([0, 0.2, 0.1, 0.2])
        >>> u1 = array([1, 0.55, 0.25, 0.4])

    Here, the first point in the confidence interval for
    ``a0`` is completely contained within that of ``a1``.
    The upper limit of ``a1[1]`` is contained within the confidence
    interval for ``a0``.
    The confidence intervals for the third point do not overlap,
    while the lower bound of ``a0[3]`` is within the confidence interval
    of ``a1[3]``.
    ::

        >>> getOverlaps(a0, a1, u0, u1, 1, relative=False)
        array([True, True, False, True])

    This function also works for multi-dimensional arrays as well.
    ::

        >>> a2 = a0.reshape(2, 2)
        >>> a3 = a1.reshape(2, 2)
        >>> u2 = u0.reshape(2, 2)
        >>> u3 = u1.reshape(2, 2)
        >>> getOverlaps(a2, a3, u2, u3 1, relative=False)
        array([[ True,  True],
               [False, False])

    Raises
    ------
    IndexError
        If the shapes of incoming arrays do not agree
    """
    shapes = {arg.shape for arg in (arr0, arr1, unc1, unc0)}
    if len(shapes) != 1:
        shapes = [str(a.shape) for a in [arr0, arr1, unc1, unc0]]
        raise IndexError("Array shapes do not agree:\n{}"
                         .format(', '.join(shapes)))
    err0 = fabs(unc0 * sigma)
    err1 = fabs(unc1 * sigma)

    if relative:
        err0 *= arr0
        err1 *= arr1

    min0 = arr0 - err0
    max0 = arr0 + err0
    min1 = arr1 - err1
    max1 = arr1 + err1

    overlap = zeros_like(arr0, dtype=bool)

    # Where values are identical to numerical precision
    overlap[arr0 == arr1] = True

    min0le1 = min0 <= min1
    max0ge1 = max0 >= max1
    min1le0 = min1 <= min0
    max1ge0 = max1 >= max0

    # locations where condidence intervals are completely contained
    # in the other set
    cont0In1 = min0le1 * (min0le1 == max0ge1)
    overlap[cont0In1] = True
    cont1In0 = min1le0 * (min1le0 == max1ge0)
    overlap[cont1In0] = True

    # locations where min of 0 is less than 1, but max 0 > min 1
    # and the opposite
    overlap[min0le1 * (max0 >= min1)] = True
    overlap[min1le0 * (max1 >= min0)] = True

    # locations where max 0 > max 1, but min 0 < max 1
    # and the opposite
    overlap[max0ge1 * (min0 <= max1)] = True
    overlap[max1ge0 * (min1 <= max0)] = True

    return overlap
