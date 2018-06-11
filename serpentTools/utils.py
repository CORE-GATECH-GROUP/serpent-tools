"""
Commonly used functions and utilities
"""

from collections import Callable
from numpy import array, ndarray

from serpentTools.messages import error, critical


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


def getCommonKeys(d0, d1, desc0=None, desc1=None, quiet=False, herald=error):
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
    d{{0, 1}}: dict or iterable
        Dictionary of keys or iterable of keys to be compared
    desc{{0, 1}}: str or None
        Description of the origin of each set of keys. Only
        needed if ``quiet`` evalutes to ``True``
    quiet: bool
        If true, then print warnings for items found in only
        one collection.
    herald: :class:`collections.Callable`
        Function that accepts a single string argument used to
        notify that the collections have missing keys. If
        the function is not a callable object, a
        :func:`serpentTools.messages.critical` message
        will be printed and :func:`serpentTools.messages.error`
        will be used.

    Returns
    -------
    set:
        Keys found in both ``d{{0, 1}}``
    """
    if not isinstance(herald, Callable):
        critical("Heralding object {} is not callable. Falling back to error."
                 .format(herald))
        herald = error
    k0 = d0.keys() if isinstance(d0, dict) else d0
    k1 = d1.keys() if isinstance(d1, dict) else d1
    s0 = set(k0)
    s1 = set(k1)

    common = s0.intersection(s1)
    missing = s0.symmetric_difference(s1)
    if missing and not quiet:
        desc0 = desc0 or "first"
        desc1 = desc1 or "second"
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
