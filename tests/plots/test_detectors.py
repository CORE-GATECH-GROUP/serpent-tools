from . import compare_or_update_plot
from serpentTools.data import readDataFile


@compare_or_update_plot
def testSpectrumPlot():
    reader = readDataFile("bwr_det0.m")
    reader["spectrum"].spectrumPlot()
