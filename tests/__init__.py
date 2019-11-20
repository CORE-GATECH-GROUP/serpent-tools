"""
Module for testing the ``serpentTools`` package
"""
from unittest import TestCase
from functools import wraps
from unittest import TestCase, SkipTest
from logging import NOTSET

from numpy import stack
from numpy.testing import assert_allclose
from serpentTools.messages import (
    DictHandler, __logger__, removeHandler, addHandler,
)
from serpentTools.utils import checkScipy


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
    for key, value in expected.items():
        actualValue = actual[key]
        assert_allclose(value, actualValue, rtol=rtol, atol=atol,
                        err_msg=fmtMsg.format(key=key))


class LoggerMixin(object):
    """
    Mixin class captures log messages

    Attributes
    ----------
    handler: :class:`serpentTools.messages.DictHandler`
        Logging handler that stores messages in a
        :attr:`serpentTools.messages.DictHandler.logMessages`
        dictionary according to level.
    """
    def __init__(self):
        self.__old = []
        self.handler = None

    def attach(self, level=NOTSET):
        """
        Attach the :class:`serpentTools.messages.DictHandler`

        Removes all :class:`logging.Handler` objects from the
        old logger, and puts them back when :class:`detach` is
        called

        Parameters
        ----------
        level: int
            Initial level to apply to handler
        """
        self.handler = DictHandler(level)
        self.__old = __logger__.handlers
        for handler in self.__old:
            removeHandler(handler)
        addHandler(self.handler)

    def detach(self):
        """Restore the original handers to the main logger"""
        if self.handler is None:
            raise AttributeError("Handler not set. Possibly not attached.")
        removeHandler(self.handler)
        for handler in self.__old:
            addHandler(handler)
        self.handler = None
        self.__old = []

    def msgInLogs(self, level, msg, partial=False):
        """
        Determine if the message is contained in the logs

        Parameters
        ----------
        level: str
            Level under which this message was posted.
            Must be a key in the
            :attr:`~serpentTools.messages.DictHandler.logMessages`
            on the :attr:`handler` for this class
        msg: str
            Message to be found in the logs.
        partial: bool
            If this evaluates to true, then search through each
            ``message`` in `logMessages` and return ``True`` if
            ``msg in message``. Otherwise, look for exact matches

        Returns
        -------
        bool:
            If the message was found in the logs

        Raises
        ------
        KeyError:
            If the level was not found in the logs
        AttributeError:
            If the :attr:`handler` has not been created with :meth:`attach`
        """
        if self.handler is None:
            raise AttributeError("Handler has not been attached. Must run "
                                 "<attach> first")
        logs = self.handler.logMessages
        if level not in logs:
            raise KeyError("Level {} not found in logs. Existing levels:\n{}"
                           .format(level, list(sorted(logs.keys()))))
        if not partial:
            return msg in logs[level]
        for message in logs[level]:
            if msg in message:
                return True
        return False


class TestCaseWithLogCapture(TestCase, LoggerMixin):
    """
    Lightly overwritten :class:`unittest.TestCase` that captures logs

    Mix in the :class:`LoggerMixin` to automatically
    :meth:`~LoggerMixin.attach` during
    :meth:`~unittest.TestCase.setUp` and :meth:`~LoggerMixin.detach`
    during :meth:`~unittest.TestCase.tearDown`

    Intended to be subclassed for actual test methods
    """

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        LoggerMixin.__init__(self)

    def setUp(self):
        """
        Method to be called before every individual test.

        Call ``attach`` to capture any log messages that would
        be presented during testing.
        Should be called during any subclassing.
        """
        LoggerMixin.attach(self)

    def tearDown(self):
        """
        Method to be called immediately after calling and recording test

        Call ``detach`` to reset the module logger to its original state.
        Should be called during any subclassing.
        """
        LoggerMixin.detach(self)

    def _concatLogs(self, level):
        logs = self.handler.logMessages.get(level, [])
        return "\n- ".join([str(item) for item in logs])

    def assertMsgInLogs(self, level, msg, partial=False):
        """
        Assert that the message was stored under a given level

        Combines :meth:`LoggerMixin.msgInLogs` with
        :meth:`unittest.TestCase.assertTrue`
        """
        matchType = "a partial" if partial else "an exact"
        failMsg = "Could not find {} match for {} under {}\n{}".format(
            matchType, msg, level, self._concatLogs(level))
        self.assertTrue(self.msgInLogs(level, msg, partial),
                        msg=failMsg)

    def assertMsgNotInLogs(self, level, msg, partial=False):
        """
        Assert that the message was not stored under a given level

        Combines :meth:`LoggerMixin.msgInLogs` with
        :meth:`unittest.TestCase.assertFalse`
        """
        matchType = "a partial" if partial else "an exact"
        failMsg = "Found {} match for {} under {} but should not have"
        self.assertFalse(self.msgInLogs(level, msg, partial),
                         msg=failMsg.format(matchType, msg, level))


HAS_SCIPY = checkScipy('1.0')


class MatlabTesterHelper(TestCase):
    """Helper class for matlab conversion"""

    def setUp(self):
        """Call this from subclasses to skip if scipy is unavailable"""
        # skip tests if scipy not installed
        if not HAS_SCIPY:
            raise SkipTest("scipy needed to test matlab conversion")


def plotTest(f):
    """Decorator that clears up existing plots prior to test."""
    from matplotlib.pyplot import close, figure

    @wraps(f)
    def wrappedTest(*args, **kwargs):
        close('all')
        figure()
        return f(*args, **kwargs)
    return wrappedTest


def getLegendTexts(ax):
    """
    Return all texts for items in legend.

    An empty list signifies no legend or no labeled
    objects.
    """
    lgd = ax.get_legend()

    if lgd is None:
        return []

    return [item.get_text() for item in lgd.get_texts()]


def plotAttrTest(testobj, ax=None, xlabel=None, ylabel=None,
                  xscale=None, yscale=None, legendLabels=None,
                  title=None):
    """Compare properties of a generated axes object"""
    if ax is None:
        from matplotlib.pyplot import gca
        ax = gca()

    if xlabel is not None:
        testobj.assertEqual(xlabel, ax.get_xlabel(), msg='xlabel')

    if ylabel is not None:
        testobj.assertEqual(ylabel, ax.get_ylabel(), msg='ylabel')

    if xscale is not None:
        testobj.assertEqual(xscale, ax.get_xscale(), msg='xscale')

    if yscale is not None:
        testobj.assertEqual(yscale, ax.get_yscale(), msg='yscale')

    if legendLabels is not None:
        if isinstance(legendLabels, str):
            legendLabels = [legendLabels, ]
        testobj.assertEqual(legendLabels, getLegendTexts(ax),
                            msg='legend text')
    if title is not None:
        testobj.assertEqual(title, ax.get_title(), msg='title')
