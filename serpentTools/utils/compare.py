"""
Comparison utilities
"""
from collections.abc import Iterable

from numpy.core.defchararray import equal as charEqual
from numpy import (
    fabs, zeros_like, ndarray, array, greater, multiply, subtract,
    equal, asarray,
)

from serpentTools.messages import (
    error,
    logIdentical,
    logNotIdentical,
    logAcceptableLow,
    logAcceptableHigh,
    logOutsideTols,
    logDifferentTypes,
    logMissingKeys,
    logBadTypes,
    logBadShapes,
    logMapOfBadShapes,
    logIdenticalWithUncs,
    logInsideConfInt,
    logOutsideConfInt,
)

from serpentTools.utils.docstrings import compareDocDecorator

LOWER_LIM_DIVISION = 1E-8
"""Lower limit for denominator for division"""

#
# Defaults for comparison
#
DEF_COMP_LOWER = 0
DEF_COMP_UPPER = 10
DEF_COMP_SIGMA = 2


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
        Indicator as to what is being compared, e.g. ``'metadata'``
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


TPL_FLOAT_INT = float, int

# Error codes for direct compare
DC_STAT_GOOD = 0
"""Values are identical to FP precision, or by ``==`` operator."""
DC_STAT_LE_LOWER = 1
"""Values are not identical, but max diff <= lower tolerance."""
DC_STAT_MID = 10
"""Values differ with max difference between lower and upper tolerance."""
DC_STAT_GE_UPPER = 100
"""Values differ with max difference greater than or equal to upper tolerance"""  # noqa
DC_STAT_NOT_IDENTICAL = 200
"""Values should be identical but are not, e.g. strings or bools."""
DC_STAT_DIFF_TYPES = 255
"""Values are of different types"""
DC_STAT_NOT_IMPLEMENTED = -1
"""Direct compare is not implemented for these types"""
DC_STAT_DIFF_SHAPES = 250
"""Values are of different shapes."""

COMPARE_STATUS_CODES = {
    DC_STAT_GOOD: (logIdentical, True),
    DC_STAT_LE_LOWER: (logAcceptableLow, True),
    DC_STAT_MID: (logAcceptableHigh, True),
    DC_STAT_NOT_IDENTICAL: (logNotIdentical, False),
    DC_STAT_GE_UPPER: (logOutsideTols, False),
    DC_STAT_DIFF_TYPES: (logDifferentTypes, False),
    DC_STAT_DIFF_SHAPES: (logBadShapes, False),
}
"""Keys of status codes with ``(caller, return)`` values."""


@compareDocDecorator
def directCompare(obj0, obj1, lower, upper):
    """
    Return True if values are close enough to each other.

    Wrapper around various comparision tests for strings, numeric, and
    arrays.

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
    int:
        Status code of the comparison.

        * {good} - Values are identical to floating point precision or,
          for strings/booleans, are identical with the ``==`` operator
        * {leLower} - Values are not identical, but the max difference
          is less than ``lower``.
        * {mid} - Values differ, with the max difference greater
          than ``lower`` but less than ``upper``
        * {geUpper} - Values differ by greater than or equal to ``upper``
        * {notIdentical} - Values should be identical (strings, booleans),
          but are not
        * {diffShapes} - Numeric data has different shapes
        * {diffTypes} - Values are of different types
        * {notImplemented} - Type comparison is not supported. This means that
          developers should either implement a test for this
          data type, or use a different function

    See Also
    --------
    * :func:`logDirectCompare` - Function that utilizes this and logs
      the results using the :mod:`serpentTools.messages` module
    """
    type0 = type(obj0)
    type1 = type(obj1)

    if type0 != type1:
        # can still compare floats and ints easily
        if type0 not in TPL_FLOAT_INT or type1 not in TPL_FLOAT_INT:
            return DC_STAT_DIFF_TYPES
    if type0 in (str, bool):
        if obj0 != obj1:
            return DC_STAT_NOT_IDENTICAL
        return DC_STAT_GOOD

    # Convert all to numpy arrays
    if not isinstance(obj0, Iterable):
        obj0 = array([obj0])
        obj1 = array([obj1])
    else:
        # convert to array, but return if data-type is object
        # need some indexable structure so dicts and sets won't work
        obj0 = array(obj0)
        obj1 = array(obj1)
        if obj0.dtype.name == 'object':
            return DC_STAT_NOT_IMPLEMENTED
    if obj0.shape != obj1.shape:
        return DC_STAT_DIFF_SHAPES

    if not upper:
        return _directCompareIdentical(obj0, obj1)
    return _directCompareWithTols(obj0, obj1, lower, upper)


def _directCompareIdentical(obj0, obj1):
    """Compare arrays that should be identical"""
    # special case for strings
    if obj0.dtype.name[:3] == 'str':
        compArray = charEqual(obj0, obj1)
    else:
        compArray = equal(obj0, obj1)
    if compArray.all():
        return DC_STAT_GOOD
    return DC_STAT_NOT_IDENTICAL


def _directCompareWithTols(obj0, obj1, lower, upper):
    """Compare arrays that have some allowable tolerances"""
    diff = multiply(
        fabs(subtract(obj0, obj1)), 100
    )
    nonZI = greater(fabs(obj0), LOWER_LIM_DIVISION)
    diff[nonZI] /= obj0[nonZI]
    maxDiff = diff.max()
    if maxDiff < LOWER_LIM_DIVISION:
        return DC_STAT_GOOD
    if maxDiff <= lower:
        return DC_STAT_LE_LOWER
    if maxDiff >= upper:
        return DC_STAT_GE_UPPER
    return DC_STAT_MID


directCompare.__doc__ = directCompare.__doc__.format(
    good=DC_STAT_GOOD,
    leLower=DC_STAT_LE_LOWER,
    mid=DC_STAT_MID,
    geUpper=DC_STAT_GE_UPPER,
    notIdentical=DC_STAT_NOT_IDENTICAL,
    diffTypes=DC_STAT_DIFF_TYPES,
    notImplemented=DC_STAT_NOT_IMPLEMENTED,
    diffShapes=DC_STAT_DIFF_SHAPES,
)


@compareDocDecorator
def logDirectCompare(obj0, obj1, lower, upper, quantity):
    """
    Compare objects using :func:`directCompare` and log the result

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
        ``True`` if the objects agree according to tolerances, or numerics
        differ less than ``upper``. ``False`` otherwise

    Raises
    ------
    TypeError:
        If the objects being compared are not supported by
        :func:`directCompare`.  Developers should either extend the
        function or utilize a different comparison function

    See Also
    --------
    * :func:`directCompare` - function that does the comparison
    * :func:`getOverlaps` - function for evaluating values with uncertainties
    * :func:`getLogOverlaps` - function that logs the result of stastistical
      comparisions
    """
    result = directCompare(obj0, obj1, lower, upper)
    if result < 0:  # failures
        if result == DC_STAT_NOT_IMPLEMENTED:
            raise TypeError(
                "directCompare is not configured to make tests on objects "
                "of type {tp}\n\tQuantity: {k}\n\tUsers: Create a issue on "
                "GitHub to alert developers.\n\tDevelopers: Update this "
                "function or create a compare function "
                "for {tp} objects.".format(k=quantity, tp=type(obj0)))
    noticeTuple = [obj0, obj1, quantity]
    if result in COMPARE_STATUS_CODES:
        func, returnV = COMPARE_STATUS_CODES[result]
        func(*noticeTuple)
        return returnV
    raise ValueError("Received value of {} from directCompare. Not sure "
                     "what this means.")


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
    differentTypes: dict
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
        keySet = set(map1.keys())
        keySet.update(set(map0.keys()))
    missing = {0: set(), 1: set()}
    differentTypes = {}
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
            differentTypes[key] = (t0, t1)
            continue
        if t0 is ndarray:
            if v0.shape != v1.shape:
                badShapes[key] = (v0.shape, v1.shape)
                continue
        goodKeys.add(key)

    return missing[0], missing[1], differentTypes, badShapes, goodKeys


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
    missing0, missing1, differentTypes, badShapes, goodKeys = (
        splitDictByKeys(map0, map1, keySet))

    # raise some messages
    if any(missing0) or any(missing1):
        logMissingKeys(quantity, desc0, desc1, missing0, missing1)
    if differentTypes:
        logBadTypes(quantity, desc0, desc1, differentTypes)
    if badShapes:
        logMapOfBadShapes(quantity, desc0, desc1, badShapes)
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

    See Also
    --------
    * :func:`getLogOverlaps` - High-level function that
      uses this to report if two values have overlapping
      confidence intervals
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


@compareDocDecorator
def getLogOverlaps(quantity, arr0, arr1, unc0, unc1, sigma, relative=True):
    """
    Wrapper around :func:`getOverlaps` that logs the result

    Parameters
    ----------
    quantity: str
        Name of the value being compared
    arr0: :class:`numpy.ndarray`
    arr1: :class:`numpy.ndarray`
    unc0: :class:`numpy.ndarray`
    unc1: :class:`numpy.ndarray`
        Arrays and their uncertainties to evaluate
    {sigma}
    relative: bool
        If uncertainties are relative. Otherwise, assume absolute
        uncertainties.

    Returns
    -------
    bool:
        ``True`` if all locations ``arr0`` and ``arr1`` are either
        identical or within allowable statistical variations.

    See Also
    --------
    * :func:`getOverlaps` - This function performs all the comparisons
      while this function simply reports the output using
      :mod:`serpentTools.messages`
    """

    arr0 = asarray(arr0)
    unc0 = asarray(unc0)
    arr1 = asarray(arr1)
    unc1 = asarray(unc1)
    if (arr0 == arr1).all():
        logIdenticalWithUncs(arr0, unc0, unc1, quantity)
        return True
    overlaps = getOverlaps(arr0, arr1, unc0, unc1, sigma, relative)
    if overlaps.all():
        logInsideConfInt(arr0, unc0, arr1, unc1, quantity)
        return True
    logOutsideConfInt(arr0, unc0, arr1, unc1, quantity)
    return False


@compareDocDecorator
def compareDictOfArrays(d0, d1, desc, lower=DEF_COMP_LOWER,
                        upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA,
                        u0={}, u1={}, relative=True):
    """
    High-level routine for evaluating the similarities of two dictionaries

    The following tests are performed

        1. Find a set of keys that both exist in ``d0`` and ``d1``
          and point to arrays with identical shapes using
          :meth:`getKeyMatchingShapes`
        2. For each key in this common set, compare the values
          with :meth:`logDirectCompare` or :meth:`getLogOverlaps`.
          The latter is used if the key exists in  ``u0`` and
          ``u1``, provided uncertainty arrays are of identical shapes.

    Parameters
    ----------
    d0: dict
    d1: dict
        Dictionaries to be compared
    desc: str
        Descption of the two dictionaries. What data do they represent?
    {compLimits}
    {sigma}
    u0: dict
    u1: dict
        If uncKeys is not ``None``, then find the uncertainties for data in
        ``d0`` and ``d1`` under the same keys.
    relative: bool
        If this evaluates to ``true``, then uncertainties in ``u0`` and ``u1``
        are relative.

    Returns
    -------
    bool
        ``True`` If all comparisons pass
    """
    similar = len(d0) == len(d1)
    keysMatchingTypes = getKeyMatchingShapes(d0, d1, desc)
    similar &= len(d0) == len(keysMatchingTypes)

    for key in sorted(keysMatchingTypes):
        val0 = d0[key]
        val1 = d1[key]
        if key in u0 and key in u1:
            unc0 = u0[key]
            unc1 = u1[key]
            similar &= getLogOverlaps(key, val0, val1, unc0, unc1,
                                      sigma, relative)
            continue
        similar &= logDirectCompare(val0, val1, lower, upper, key)
    return similar


FINAL_COMPARE_MSG = "Objects {} and {}{} agree within given tolerances"


def finalCompareMsg(obj0, obj1, similar):
    """
    Return the string used to signify the conclusion of a comparison

    Mainly exposed to developers for testing purposes.

    Parameters
    ----------
    obj0:
    obj1: Subclass of :class:`~serpentTools.objects.base.BaseObject`
        Objects that have been compared
    similar: bool
        Result of comparison

    Returns
    -------
    str:
        Concluding remark about the comparison.
    """
    return FINAL_COMPARE_MSG.format(obj0, obj1, "" if similar else "do not")
