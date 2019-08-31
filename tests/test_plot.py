"""
Test the plotting module

"""
import unittest

from numpy import arange
from matplotlib.colors import Normalize, LogNorm
from matplotlib.pyplot import subplots

from serpentTools.utils import (
    formatPlot, normalizerFactory, setAx_xlims, setAx_ylims,
)


class PlotFormatTester(unittest.TestCase):
    """Class for testing the formatPlot function."""

    def setUp(self):
        _fig, self.ax = subplots(1, 1)
        self.compareScales('linear', 'linear')
        self.compareLabels('', '')
        self.compareTitle('')

    def plot(self, **kwargs):
        """Emulate plotting."""
        self.ax = formatPlot(self.ax, **kwargs)

    def test_logx_logy(self):
        """Verify the format method can be used to set each axis scale."""
        self.plot(logx=True, logy=True)
        self.compareScales('log', 'log')

    def compareScales(self, xscale, yscale):
        self.assertEqual(self.ax.get_xscale(), xscale)
        self.assertEqual(self.ax.get_yscale(), yscale)

    def compareLabels(self, xlabel, ylabel):
        self.assertEqual(self.ax.get_xlabel(), xlabel)
        self.assertEqual(self.ax.get_ylabel(), ylabel)

    def compareTitle(self, title):
        self.assertEqual(self.ax.get_title(), title)

    def test_loglog(self):
        """Verify the format function can be used to set both axes at once."""
        self.plot(loglog=True)
        self.compareScales('log', 'log')

    def test_logx(self):
        self.plot(logx=True)
        self.compareScales('log', 'linear')

    def test_logy(self):
        self.plot(logy=True)
        self.compareScales('linear', 'log')

    def test_xlabel(self):
        self.plot(xlabel='xlabel')
        self.compareLabels('xlabel', '')

    def test_ylabel(self):
        self.plot(ylabel='ylabel')
        self.compareLabels('', 'ylabel')

    def test_xlabel_ylabel(self):
        self.plot(xlabel='xlabel', ylabel='ylabel')
        self.compareLabels('xlabel', 'ylabel')

    def test_title(self):
        self.plot(title='title')
        self.compareTitle('title')


class NormalizerTester(unittest.TestCase):
    """Class for testing the normalizerFactory function."""

    def setUp(self):
        self.data = arange(-4, 5)

    def _testType(self, norm):
        """Ensure the return type is an instance/sublass of Normalize."""
        typeFlag = (isinstance(norm, Normalize)
                    or issubclass(norm.__class__, Normalize))
        self.assertTrue(typeFlag, msg=(
            "Output should be Normalize or a subclass, not {}"
            .format(norm.__class__)))

    def _testNormalizer(self, norm):
        """Internal for comparing min and max of normalizer"""
        self._testType(norm)
        self.assertEqual(self.data.min(), norm.vmin)
        self.assertEqual(self.data.max(), norm.vmax)

    def test_simpleNormalizer(self):
        """Verify that the factory sets min and max from a dataset."""
        out = normalizerFactory(self.data, None, False, None, None)
        self._testNormalizer(out)

    def test_positiveLogNorm(self):
        """Verify the logScaling for a positive dataset."""
        self.data[self.data <= 0] = 1
        out = normalizerFactory(self.data, None, True, None, None)
        self._testNormalizer(out)

    def test_passNormaliser(self):
        """Verify that passing an instance of Normalize is allowed."""
        emin, emax = 5, 100
        norm = Normalize(vmin=emin, vmax=emax)
        out = normalizerFactory(self.data, norm, False, None, None)
        self.assertIs(norm, out)

    def test_normSubclass(self):
        """Verify that passing a subclass of Normalize is allowed."""
        emin, emax = 5, 100
        norm = LogNorm(vmin=emin, vmax=emax)
        out = normalizerFactory(self.data, norm, False, None, None)
        self.assertIs(norm, out)


class _AxLimitSetterHelper(unittest.TestCase):
    """Class for testing the setAx_{x/y}lims functions."""

    def setUp(self):
        _fig, self.ax = subplots(1, 1)
        self.limSetter = setAx_xlims if self.dim == 'x' else setAx_ylims
        self.limGetter = getattr(self.ax, "get_{}lim".format(self.dim))

    def _testLims(self, expected):
        actual = self.limGetter()
        self.assertTupleEqual(expected, actual)

    @property
    def dim(self):
        raise NotImplementedError

    def test_tightLims(self):
        """Verify the axis limits are exactly set with no padding."""
        expected = vmin, vmax = 0.5, 1.5
        self.limSetter(self.ax, vmin, vmax, pad=0)
        self._testLims(expected)

    def test_noNegPadding(self):
        """Verify that assertion errors are raised for negative padding."""
        with self.assertRaises(AssertionError):
            self.limSetter(self.ax, 0, 1, -1)

    def test_setWithPadding(self):
        """Verify that padding is correctly handled."""
        minV = 0
        maxV = 100
        pad = 10  # percent of difference between values
        expected = minV - pad, maxV + pad
        self.limSetter(self.ax, minV, maxV, pad)
        self._testLims(expected)


class XAxisLimitSetterTester(_AxLimitSetterHelper):
    """Class for testing the ability to set x-axis limits"""
    dim = 'x'


class YAxisLimitSetterTester(_AxLimitSetterHelper):
    """Class for testing the ability to set y-axis limits"""
    dim = 'y'


del _AxLimitSetterHelper

if __name__ == '__main__':
    unittest.main()
