import pytest
from serpentTools.data import readDataFile

from . import compare_or_update_plot


LOWER_XLIM = 1e3
"""Lower xlimit for plots: energy in eV"""


@pytest.fixture
def flattop():
    return readDataFile("flattop_sens.m")


@compare_or_update_plot
def test_sensitivity_filter(flattop):
    ax = flattop.plot(
        "keff", zai=922380, pert="total xs", labelFmt="{r}: {z} {p}",
    )
    ax.set_xlim(LOWER_XLIM)



@compare_or_update_plot
def test_sensitivity_kwargs(flattop):
    flattop.plot(
        "keff",
        zai=["total", 922380],
        pert=["total xs", "fission xs"],
        mat=["total"],
        logx=False,
        logy=False,
        normalize=False,
        legend="above",
        ncol=2,
        mevscale=True,
        drawstyle=None,
        linestyle="--",
    )
