"""
Core utilities
"""

from re import compile

from numpy import array, ndarray, fromiter


# Regular expressions

STR_REGEX = compile(r'\'.+\'')  # string
VEC_REGEX = compile(r'(?<==.)\[.+?\]')  # vector
SCALAR_REGEX = compile(r'=.+;')  # scalar
FIRST_WORD_REGEX = compile(r'^\w+')  # first word in the line


def str2vec(iterable, dtype=float, out=array):
    """
    Convert a string or other iterable to vector.

    Parameters
    ----------
    iterable: str or iterable
        If a string containing spaces, will be split using
        ```iterable.split()``. If no spaces are found, the
        outgoing type is filled with a single string, e.g.
        a list with a single string as the first and only
        entry. This is returned directly, avoiding conversion
        with ``dtype``.
        Every item in this split list, or original
        iterable, will be iterated over and converted accoring
        to the other arguments.
    dtype: type
        Convert each value in ``iterable`` to this data type.
    out: type
        Return data type. Will be passed the iterable of
        converted items of data dtype ``dtype``.

    Returns
    -------
    vector
        Iterable of all values of ``iterable``, or split variant,
        converted to type ``dtype``.

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

        >>> str2vec("ADF")
        array(['ADF', dtype='<U3')

    """
    if isinstance(iterable, str):
        if ' ' in iterable:
            iterable = iterable.split()
        else:
            return out([iterable])
    cmap = map(dtype, iterable)
    if out is array:
        return fromiter(cmap, dtype)
    return out(cmap)


def splitValsUncs(iterable, copy=False):
    """
    Return even and odd indexed values from iterable

    Designed to extract expected values and uncertainties from
    SERPENT vectors/matrices of the form
    ``[x1, u1, x2, u2, ...]``

    Slices along the last axis present on ``iterable``, e.g.
    columns in 2D matrix.

    Parameters
    ----------
    iterable: :class:`numpy.ndarray`or iterable
        Initial arguments to be processed. If not
        :class:`numpy.ndarray`, then strings will be converted
        by calling :func:`str2vec`. Lists and tuples
        will be sent directly to arrays with
        :func:`numpy.array`.
    copy: bool
        If true, return a unique instance of the values
        and uncertainties. Otherwise, returns a view
        per numpy slicing methods

    Returns
    -------
    :class:`numpy.ndarray`
        Even indexed values from ``iterable``
    :class:`numpy.ndarray`
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

        >>> v = [[1, 2], [3, 4]]
        >>> splitValsUncs(v)
        array([[1], [3]]), array([[2], [4]])

    """

    if not isinstance(iterable, ndarray):
        iterable = (str2vec(iterable) if isinstance(iterable, str)
                    else array(iterable))
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


def deconvertVariableName(variable):
    """Convert ``mixedCase`` to ``SERPENT_CASE``"""
    out = ""
    for char in variable:
        if char.isupper():
            out += '_' + char
            continue
        out += char.upper()
    return out


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
