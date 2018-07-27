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
    """Log an info message, e.g. status update."""
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
