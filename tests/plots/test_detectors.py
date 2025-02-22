from serpentTools.data import readDataFile

from . import compare_or_update_plot


@compare_or_update_plot
def testSpectrumPlot():
    reader = readDataFile("bwr_det0.m")
    reader["spectrum"].spectrumPlot()


@compare_or_update_plot
def testBwrMeshPlot(recwarn):
    reader = readDataFile("bwr_det0.m")
    # Ensure that fix for #414 in in: matplotlib colorbar norm
    reader["xymesh"].meshPlot(fixed={"energy": 0})
    assert len(recwarn) == 0

@compare_or_update_plot
def testSpectrumJustNormPerLethargy():
    reader = readDataFile("bwr_det0.m")
    reader["spectrum"].spectrumPlot(by=None, fixed={"reaction": 1})


@compare_or_update_plot
def testHexPlot():
    reader = readDataFile("hexplot_det0.m")
    h2 = reader["hex2"]
    h2.pitch = 1
    h2.hexType = 2
    h2.hexPlot()
