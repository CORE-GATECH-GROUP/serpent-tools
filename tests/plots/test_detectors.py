import pytest
from serpentTools.data import readDataFile

from . import compare_or_update_plot


@compare_or_update_plot
def testSpectrumPlot():
    reader = readDataFile("bwr_det0.m")
    reader["spectrum"].spectrumPlot()


@compare_or_update_plot
def testBwrMeshPlot():
    reader = readDataFile("bwr_det0.m")
    # Ensure that fix for #414 in in: matplotlib colorbar norm
    with pytest.warns(None) as record:
        reader["xymesh"].meshPlot(fixed={"energy": 0})
    assert len(record) == 0
