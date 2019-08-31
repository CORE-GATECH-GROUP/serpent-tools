"""
Test the logging and messaging functions
"""

from unittest import TestCase
from warnings import catch_warnings

from serpentTools.messages import (
    deprecated, willChange,
    addHandler, removeHandler,
    __logger__,
    debug, info, warning, error, critical,
)
from serpentTools.settings import rc
from serpentTools.tests.utils import TestCaseWithLogCapture, LoggerMixin


LOGGER_FUNCTIONS = [debug, info, warning, error, critical]


class DecoratorTester(TestCase):
    """Class to test the decorators for warnings."""

    def test_futureDecorator(self):
        """Verify that the future decorator doesn't break"""

        @willChange('This function will be updated in the future, '
                    'but will still exist')
        def demoFuture(x, val=5):
            return x + val

        with catch_warnings(record=True) as record:
            self.assertEqual(7, demoFuture(2))
            self.assertEqual(7, demoFuture(2, 5))
            self.assertEquals(len(record), 2,
                              'Did not catch two warnings::willChange')

    def test_deprecatedDecorator(self):
        """Verify that the deprecated decorator doesn't break things"""

        @deprecated('this nonexistent function')
        def demoFunction(x, val=5):
            return x + val

        with catch_warnings(record=True) as record:
            self.assertEqual(7, demoFunction(2))
            self.assertEqual(7, demoFunction(2, 5))
            self.assertEquals(len(record), 2,
                              'Did not catch two warnings::deprecation')


class LoggingTester(TestCaseWithLogCapture):
    """
    Class for testing various logging capabilities
    """

    def test_logger(self):
        """Test the basic logging functions."""
        searchMessage = "test_logger"
        with rc:
            rc['verbosity'] = 'debug'
            for logFunc in LOGGER_FUNCTIONS:
                funcLevel = logFunc.__name__.upper()
                logFunc(searchMessage)
                self.msgInLogs(funcLevel, searchMessage)

    def test_addRemoveHandlers(self):
        """Test that the add/remove handler functions work."""
        with self.assertRaises(TypeError):
            addHandler(1)
        addHandler(self.handler)
        self.assertIn(self.handler, __logger__.handlers,
                      msg="addHandler did not add the handler")
        removeHandler(self.handler)
        self.assertNotIn(self.handler, __logger__.handlers,
                         msg="removeHandler did not remove the handler")

    def test_keyInLogs(self):
        """Verify the behavrior of LoggerMixin.msgInLogs"""
        message = "look for me"
        warning(message)
        self.assertMsgInLogs("WARNING", message)
        self.assertMsgInLogs("WARNING", message[:5], partial=True)
        self.assertMsgNotInLogs("WARNING", "<none>")
        self.assertMsgNotInLogs("WARNING", "<none>", partial=True)
        with self.assertRaises(KeyError):
            self.msgInLogs("DEBUG", message)
        with self.assertRaises(AttributeError):
            newM = LoggerMixin()
            newM.msgInLogs("WARNING", message)


if __name__ == '__main__':
    from unittest import main
    main()
