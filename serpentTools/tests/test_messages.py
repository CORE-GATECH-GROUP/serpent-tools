"""
Test the logging and messaging functions
"""

from unittest import TestCase
from warnings import catch_warnings

from serpentTools.messages import (
    deprecated, willChange,
)


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


if __name__ == '__main__':
    from unittest import main
    main()
