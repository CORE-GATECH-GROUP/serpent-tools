import pytest
from serpentTools.settings import rc
from serpentTools.data import readDataFile

from . import compare_or_update_plot


@pytest.fixture
def innerAssem():
    with rc:
        rc["serpentVersion"] = "2.1.30"
        reader = readDataFile("InnerAssembly_res.m")
    return reader


@compare_or_update_plot
def testResultWithRight(innerAssem):
    innerAssem.plot(
        {"absKeff": "keff"},
        right="conversionRatio",
        drawstyle="steps-post",
    )


@compare_or_update_plot
def testResultMulti(innerAssem):
    innerAssem.plot(
        "burnup",
        ["avgVirtCol", "avgRealCol"],
        ylabel="Collision information",
        sigma=0,
        marker=">",
    )
