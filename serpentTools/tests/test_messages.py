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
from serpentTools.tests.utils import LoggerMixin


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


class LoggingTester(TestCase, LoggerMixin):
    """
    Class for testing various logging capabilities
    """

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        LoggerMixin.__init__(self)

    def setUp(self):
        self.attach()

    def tearDown(self):
        self.detach()

    def _assertLogInLevel(self, level, msg):
        """Assert that the specified message is in the handler"""
        messages = self.handler.logMessages
        self.assertIn(level, messages,
                      msg="Level {} missing from logs".format(level))
        self.assertIn(msg, messages[level],
                      msg="Message missing from log level")

    def test_logger(self):
        """Test the basic logging functions."""
        searchMessage = "test_logger"
        with rc:
            rc['verbosity'] = 'debug'
            for logFunc in LOGGER_FUNCTIONS:
                funcLevel = logFunc.__name__.upper()
                logFunc(searchMessage)
                self._assertLogInLevel(funcLevel, searchMessage)

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


if __name__ == '__main__':
    from unittest import main
    main()
