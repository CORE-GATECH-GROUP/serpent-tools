"""
System-wide methods for producing status update and errors.

See Also
--------
* https://docs.python.org/2/library/logging.html
* https://www.python.org/dev/peps/pep-0391/
"""


import logging
from logging.config import dictConfig


class SerpentToolsException(Exception):
    """Base-class for all exceptions in this project"""
    pass


LOG_OPTS = ['critical', 'error', 'warning', 'info', 'debug']


loggingConfig = {
    'version': 1,
    'formatters': {
        'brief': {'format': '%(levelname)-8s: %(name)-15s: %(message)s'},
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
    'root': {
        'handlers': ['console'],
        'level': logging.INFO
    }
}

dictConfig(loggingConfig)

__logger__ = logging.getLogger('serpentTools')


def debug(message):
    """Log a debug message."""
    __logger__.debug('%s', message)


def info(message):
    """Log an info message, e.g. status update."""
    __logger__.info('%s', message)


def warning(message):
    """Log a warning that something that could go wrong or be avoided."""
    __logger__.warning('%s', message)


def error(message, fatal=True):
    """Log that something went wrong."""
    if fatal:
        __logger__.critical('%s', message, exc_info=True)
        raise SerpentToolsException('%s', message)
    __logger__.error('%s', message)


def updateLevel(level):
    """Set the level of the logger."""
    if level.lower() not in LOG_OPTS:
        __logger__.setLevel('INFO')
        warning('Logger option {} not in options. Set to warning.')
        return 'warning'
    else:
        __logger__.setLevel(level.upper())
        return level
