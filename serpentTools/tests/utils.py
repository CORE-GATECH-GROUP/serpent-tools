"""
Utilities to make testing easier
"""

from logging import NOTSET

from serpentTools.messages import (
    DictHandler, __logger__, removeHandler, addHandler,
)


class LoggerMixin(object):
    """
    Mixin class captures log messages

    Attributes
    ----------
    handler: :class:`serpentTools.messages.DictHandler
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
