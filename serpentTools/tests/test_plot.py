"""
Test the plotting module

"""
import unittest

from matplotlib.pyplot import subplots

from serpentTools.plot import formatPlot


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


if __name__ == '__main__':
    unittest.main()

