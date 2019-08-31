"""Test the basic aspect of the comparison system."""

from unittest import TestCase

from serpentTools.objects.base import BaseObject
from serpentTools.parsers.results import ResultsReader


class SafeCompare(BaseObject):
    """Object that can use the comparison method."""

    def _compare(self, *args, **kwargs):
        return True


class SafeSubclass(SafeCompare):
    pass


class BaseCompareTester(TestCase):
    """Class responsible for testing the basic compare system."""

    def setUp(self):
        self.obj = SafeCompare()

    def test_badCompType(self):
        """Verify that comparisons against bad-types raise errors."""
        with self.assertRaises(TypeError):
            self.obj.compare(ResultsReader(None))
        with self.assertRaises(TypeError):
            self.obj.compare(list())

    def test_safeCompare(self):
        """
        Verify that the compare method doesn't fail when
        comparing against similar objects or subclasses
        """
        self.obj.compare(SafeCompare())
        self.obj.compare(SafeSubclass())

    def test_badArgs(self):
        """Verify that the compare method fails for bad arguments."""
        other = SafeCompare()
        with self.assertRaises(ValueError):
            self.obj.compare(other, lower=-1)
        with self.assertRaises(ValueError):
            self.obj.compare(other, upper=-1)
        with self.assertRaises(ValueError):
            self.obj.compare(other, sigma=-1)
        with self.assertRaises(ValueError):
            self.obj.compare(other, lower=100, upper=1)


if __name__ == '__main__':
    from unittest import main
    main()
