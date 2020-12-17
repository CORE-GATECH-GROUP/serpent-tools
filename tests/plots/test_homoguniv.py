import pytest
from serpentTools.settings import rc
from serpentTools.data import readDataFile

from . import compare_or_update_plot


@pytest.fixture(scope="module")
def univ():
    with rc:
        rc["serpentVersion"] = "2.1.30"
        reader = readDataFile("InnerAssembly_res.m")
    yield reader.universes["0", 0, 0, 0]


@compare_or_update_plot
def test_homoguniv_single(univ):
    univ.plot("infTot", label="Total", legend=True)


@compare_or_update_plot
def test_homoguniv_multi(univ):
    univ.plot(
        ["infAbs", "infTot"],
        logx=False,
        logy=False,
        labelFmt="{u} @ {b} MWd/kgU // {d} days // step {i}: {k}",
        xlabel="Incident energy (MeV)",
        ylabel="Macroscopic cross section (cm$^{-1})$",
        # Addtional arguments to pass along to the underlying plot
        linestyle="--",
    )


@compare_or_update_plot
def test_homoguniv_multi_named(univ):
    univ.plot(
        ["infAbs", "infFlx"],
        labels=["Absorption", "Flux"],
    )
