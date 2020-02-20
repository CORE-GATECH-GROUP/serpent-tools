"""
Test the abstract base class approach upon
which our objects are built.
"""

from unittest import TestCase

from serpentTools.parsers.base import BaseReader


class BadSubclass(BaseReader):
    """Class that does not overwrite abstract methods."""

    def __init__(self):
        BaseReader.__init__(self, None, '')


class ProperSubclass(BaseReader):
    """Class that does overwrite abstract methods."""

    def __init__(self):
        BaseReader.__init__(self, None, '')

    def _read(self):
        pass

    def _postcheck(self):
        pass

    def _precheck(self):
        pass


class MetaTester(TestCase):
    """Class that tests the construction of base classes."""

    def test_badsubclass(self):
        """Verify that one cannot instantiate incomplete base classes."""
        with self.assertRaises(TypeError):
            BadSubclass()

    def test_properSubclass(self):
        """Verify that one can instantiate completed base classes."""
        ProperSubclass()
