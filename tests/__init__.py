"""
Module for testing the ``serpentTools`` package
"""
from unittest import TestCase

from numpy import stack
from numpy.testing import assert_allclose
from six import iteritems


def computeMeansErrors(*arrays):
    """
    Return the matrices of element-wise means and standard deviations

    This function assumes that:

    1. Each element in ``arrays`` is a numpy array
    2. Each element in ``arrays`` is of equal dimensionality

    The arrays are all stacked to create a new array with one
    additional axis at index 0. The mean and standard deviation are
    computed along this new axis so that the returned arrays
    are of equal dimensionality to the incoming arrays

    Parameters
    ----------
    arrays: iterable
        Arrays to be stacked

    Returns
    -------
    numpy.ndarray
        Element-wise mean of all incoming arrays
    numpy.ndarray
        Element-wise standard deviation of all incoming arrays
    """
    workMat = stack(arrays)
    return workMat.mean(axis=0), workMat.std(axis=0)


def compareDictOfArrays(expected, actual, fmtMsg=None, rtol=0, atol=0,
                        testCase=None):
    """
    Compare a dictionary of arrays.

    Parameters
    ----------
    expected: dict
        Dictionary of expected data
    actual: dict
        Dictionary of actual data.
    fmtMsg: str
        Message to be passed as the error message. Formatted with
        ``.format(key=key)``, where ``key`` is the specific key
        where the arrays were too different.
    rtol: float
        Relative tolerance for arrays
    atol: float
        Absolute tolerance for arrays
    testCase: None or :class:`unittest.TestCase`
        If given, use the ``testCase.assertSetEqual`` to compare keys

    Raises
    ------
    AssertionError:
        If the keys in both dictionaries differ, or if any
        one array in ``actual`` is too different from it's counterpart
        in ``expected``.
    """
    fmtMsg = fmtMsg or "Key: {key}"
    eKeys = set(expected.keys())
    aKeys = set(actual.keys())
    if isinstance(testCase, TestCase):
        testCase.assertSetEqual(eKeys, aKeys)
    else:
        in1Not2 = eKeys.difference(aKeys)
        in2Not1 = aKeys.difference(eKeys)
        errMsg = ''
        if any(in1Not2):
            errMsg += ('Keys in expected not actual: {}\n'
                       .format(', '.join(in1Not2)))
        if any(in2Not1):
            errMsg += ('Keys in actual not expected: {}\n'
                       .format(', '.join(in2Not1)))
        if errMsg:
            raise AssertionError(errMsg)
    for key, value in iteritems(expected):
        actualValue = actual[key]
        assert_allclose(value, actualValue, rtol=rtol, atol=atol,
                        err_msg=fmtMsg.format(key=key))
