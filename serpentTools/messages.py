"""
System-wide methods for producing status update and errors.

See Also
--------
* https://docs.python.org/2/library/logging.html
* https://www.python.org/dev/peps/pep-0391/
"""

import functools
import warnings
import logging
from logging import Handler
from logging.config import dictConfig
from collections.abc import Callable

from numpy import ndarray

__all__ = [
    'SerpentToolsException',
    'SamplerError',
    'MismatchedContainersError',
]


class SerpentToolsException(Exception):
    """Base-class for all exceptions in this project"""
    pass


class SamplerError(SerpentToolsException):
    """Base-class for errors in sampling process"""
    pass


class MismatchedContainersError(SamplerError):
    """Attempting to sample from dissimilar containers"""
    pass

#
# Logger options
#


LOG_OPTS = ['critical', 'error', 'warning', 'info', 'debug']

loggingConfig = {
    'version': 1,
    'formatters': {
        'brief': {'format': '%(levelname)-8s: %(name)-12s: %(message)s'},
        'precise': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'brief',
            'level': logging.DEBUG,
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'serpentTools': {
            'handlers': ['console'],
            'level': logging.WARNING,
            'propagate': False,
        },
    }
}

dictConfig(loggingConfig)

__logger__ = logging.getLogger('serpentTools')


def addHandler(handler):
    """
    Add a handler to the logger

    Parameters
    ----------
    handler: :class:`python.logging.Handler`
        Subclass to handle the formatting and emitting
        of log messages
    """
    if not issubclass(handler.__class__, Handler):
        raise TypeError("Handler {} is of class {} and does not appear "
                        "to be a subclass of {}"
                        .format(handler, handler.__class__, Handler))
    return __logger__.addHandler(handler)


def removeHandler(handler):
    """
    Remove a handler from the internal logger

    Parameters
    ----------
    handler: :class:`python.logging.Handler`
        Handler to be removed
    """
    return __logger__.removeHandler(handler)


def debug(message):
    """Log a debug message."""
    __logger__.debug('%s', message)


def info(message):
    """Log an info message"""
    __logger__.info('%s', message)


def warning(message):
    """Log a warning that something could go wrong or should be avoided."""
    __logger__.warning('%s', message)


def error(message):
    """Log that something caused an exception but was suppressed."""
    __logger__.error('%s', message)


def critical(message):
    """Log that something has gone horribly wrong."""
    __logger__.critical('%s', message, exc_info=True)


def updateLevel(level):
    """Set the level of the logger."""
    if level.lower() not in LOG_OPTS:
        __logger__.setLevel('INFO')
        warning('Logger option {} not in options. Set to info.'.format(level))
        return 'info'
    __logger__.setLevel(level.upper())
    return level


def deprecated(useInstead):
    """Decorator that warns that different function should be used instead."""

    def decorate(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            msg = ('Function {} has been deprecated. Use {} instead'
                   .format(f.__name__, useInstead))
            _updateFilterAlert(msg, DeprecationWarning)
            return f(*args, **kwargs)

        return decorated

    return decorate


def willChange(changeMsg):
    """Decorator that warns that some functionality may change."""

    def decorate(f):
        @functools.wraps(f)
        def decoratedFunc(*args, **kwargs):
            _updateFilterAlert(changeMsg, FutureWarning)
            return f(*args, **kwargs)

        return decoratedFunc

    return decorate


def _updateFilterAlert(msg, category):
    warnings.simplefilter('always', category)
    warnings.warn(msg, category=category, stacklevel=3)
    warnings.simplefilter('default', category)

# =========================================================
# Functions for notifying the user about comparison results
# =========================================================


def _prefaceNotice(obj, leader):
    msg = '\n\t{} '.format(leader) + ''.join(str(obj).split('\n'))
    return msg


def _notify(func, quantity, header, obj0, obj1):
    msg = header.format(quantity)
    msg += _prefaceNotice(obj0, '>')
    if obj1 is not None:
        msg += _prefaceNotice(obj1, '<')
    func(msg)


def logIdentical(obj0, obj1, quantity):
    """Two objects are identical."""
    _notify(debug, quantity, 'Values for {} are identical', obj0, None)


def logNotIdentical(obj0, obj1, quantity):
    """Values should be identical but aren't."""
    _notify(error, quantity, "Values for {} are not identical",
            obj0, obj1)


def logAcceptableLow(obj0, obj1, quantity):
    """Two values differ, but inside nominal and acceptable ranges."""
    _notify(info, quantity, "Values for {} are not identical, but close",
            obj0, obj1)


def logAcceptableHigh(obj0, obj1, quantity):
    """Two values differ, enough to merit a warning but not an error."""
    _notify(warning, quantity,
            "Values for {} are different, but within tolerances", obj0, obj1)


def logOutsideTols(obj0, obj1, quantity):
    """Two values differ outside acceptable tolerances."""
    _notify(error, quantity,
            "Values for {} are outside acceptable tolerances.", obj0, obj1)


def _notifyWithUncs(func, quantity, msg, value0, unc0, value1, unc1):
    logMsg = msg.format(quantity)
    logMsg += _prefaceNotice(value0, '>V')
    logMsg += _prefaceNotice(unc0, '>U')
    if value1 is not None:
        logMsg += _prefaceNotice(value1, '<V')
    logMsg += _prefaceNotice(unc0, '<U')
    func(logMsg)


def logIdenticalWithUncs(value, unc0, unc1, quantity):
    """Notify that two values have identical expected values."""
    _notifyWithUncs(debug, quantity,
                    'Expected values for {} are identical',
                    value, unc0, None, unc1)


def logInsideConfInt(value0, unc0, value1, unc1, quantity):
    """Two values are within acceptable statistical limits."""
    _notifyWithUncs(debug, quantity, 'Confidence intervals for {} overlap',
                    value0, unc0, value1, unc1)


def logOutsideConfInt(value0, unc0, value1, unc1, quantity):
    """Two values are outside acceptable statistical limits."""
    _notifyWithUncs(error, quantity,
                    "Values for {} are outside acceptable statistical limits",
                    value0, unc0, value1, unc1)


def logDifferentTypes(type0, type1, quantity):
    """Two values are of different types."""
    _notify(error, quantity, "Types for {} are different.",
            type0, type1)


def logBadShapes(obj0, obj1, quantity):
    """
    Log an error message that two arrays are of different shapes.

    Parameters
    ----------
    obj0: :class:`numpy.ndarray`
    obj1: :class:`numpy.ndarray`
        Arrays that have been compared and found to have different shapes
    quantity: str
        Descriptor of the quantity being compared, e.g. what these objects
        represent
    """
    shapes = [obj.shape if isinstance(obj, ndarray)
              else len(obj) for obj in (obj0, obj1)]
    _notify(error, quantity, "Shapes for {} are different.",
            shapes[0], shapes[1])


MISSING_MSG_HEADER = "{} from {} and {} contain different items"
MISSING_MSG_SUBJ = "\n\tItems present in {} but not in {}:\n\t\t{}"


def _checkHerald(herald):
    if not isinstance(herald, Callable):
        critical("Heralding object {} is not callable. Falling back to error."
                 .format(herald))
        return error
    return herald


def logMissingKeys(quantity, desc0, desc1, in0, in1, herald=error):
    """
    Log a warning message that two objects contain different items

    Parameters
    ----------
    quantity: str
        Indicator as to what is being compared, e.g. ``'metadata'``
    desc0: str
    desc1: str
        Descriptions of the two originators
    in0: set or iterable
    in1: set or iterable
        Items that are unique to originators ``0`` and ``1``, respectively
    herald: callable
        Callable function that accepts a single string. This will be called
        with the error message. If not given, defaults to :func:`error`
    """
    if not any(in0) and not any(in1):
        return
    herald = _checkHerald(herald)
    msg = MISSING_MSG_HEADER.format(quantity, desc0, desc1)
    if any(in0):
        msg += MISSING_MSG_SUBJ.format(desc0, desc1,
                                       ', '.join([str(xx) for xx in in0]))
    if any(in1):
        msg += MISSING_MSG_SUBJ.format(desc1, desc0,
                                       ', '.join([str(xx) for xx in in1]))
    herald(msg)


BAD_TYPES_HEADER = "Items from {d0} and {d1} {q} have different types"
BAD_SHAPES_HEADER = "Items from {d0} and {d1} {q} have different shapes"
BAD_OBJ_SUBJ = "\n\t{key}: {t0} - {t1}"


def logBadTypes(quantity, desc0, desc1, types):
    """
    Log an error message for containers with mismatched types

    Parameters
    ----------
    quantity: str
        Indicator as to what is being compared, e.g. ``'metadata'``
    desc0: str
    desc1: str
        Descriptions of the two originators
    types: dict
        Dictionary where the keys represent the locations of
        items with mismatched types. Corresponding keys should
        be a list or tuple of the types for objects from
        ``desc0`` and ``desc1`` stored under ``key``
    """
    msg = BAD_TYPES_HEADER.format(q=quantity, d0=desc0, d1=desc1)
    for key in sorted(list(types.keys())):
        t0, t1 = types[key]
        msg += BAD_OBJ_SUBJ.format(key=key, t0=t0, t1=t1)
    error(msg)


def logMapOfBadShapes(quantity, desc0, desc1, shapes):
    """
    Log an error message for containers with mismatched shapes

    Parameters
    ----------
    quantity: str
        Indicator as to what is being compared, e.g. ``'metadata'``
    desc0: str
    desc1: str
        Descriptions of the two originators
    shapes: dict
        Dictionary where the keys represent the locations of
        items with mismatched shapes. Corresponding keys should
        be a list or tuple of the shapes for objects from
        ``desc0`` and ``desc1`` stored under ``key``
    """
    msg = BAD_SHAPES_HEADER.format(q=quantity, d0=desc0, d1=desc1)
    for key in sorted(list(shapes.keys())):
        t0, t1 = shapes[key]
        msg += BAD_OBJ_SUBJ.format(key=key, t0=t0, t1=t1)
    error(msg)


class DictHandler(Handler):
    """
    Handler that stores log messages in a dictionary

    Attributes
    ----------
    logMessages: dict
        Dictionary of lists where each key is a log level such
        as ``'DEBUG'`` or ``'WARNING'``. The list associated
        with each key contains all messages called under that
        logging level
    """
    def __init__(self, level=logging.NOTSET):
        Handler.__init__(self, level)
        self.logMessages = {}

    def flush(self):
        """Clear the log messages dictionary"""
        self.logMessages = {}

    def close(self):
        """Tidy up before removing from list of handlers"""
        self.logMessages = {}
        Handler.close(self)

    def emit(self, record):
        """
        Store the message in the log messages by level.

        Does no formatting to the record, simply stores
        the message in :attr:`logMessages` dictionary
        according to the records ``levelname``

        Anticipates a :class:`logging.LogRecord` object
        """
        level = record.levelname
        if level not in self.logMessages:
            self.logMessages[level] = []
        self.logMessages[level].append(record.getMessage())
