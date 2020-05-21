import sys
import numpy
import pytest
import serpentTools


@pytest.fixture(scope="module")
def referenceDepReader():
    return serpentTools.readDataFile("ref_dep.m")


@pytest.fixture(scope="module")
def referenceMaterial(referenceDepReader):
    return referenceDepReader.materials["fuel"]


@pytest.mark.skipif(sys.version_info < (3, 6), reason="pandas requires 3.6+")
@pytest.mark.parametrize("quantity", ["adens", "ingTox", "inhTox"])
def test_toDataFrame(referenceMaterial, quantity):
    fullFrame = referenceMaterial.toDataFrame(quantity)

    assert numpy.array_equal(
        fullFrame.columns.values, referenceMaterial.names
    )
    assert numpy.array_equal(fullFrame.index.values, referenceMaterial.days)
    assert numpy.array_equal(
        fullFrame.values, referenceMaterial.data[quantity].T
    )
    assert fullFrame.index.name == "Time [d]"
    assert fullFrame.columns.name == "Isotope"

    reference = referenceMaterial.getValues(
        "days", quantity, names=["U235", "Xe135", "Pu239"]
    )
    namedBurnup = referenceMaterial.toDataFrame(
        quantity, names=["U235", "Xe135", "Pu239"], time="burnup"
    )
    zaiSteps = referenceMaterial.toDataFrame(
        quantity, zai=[922350, 541350, 942390], time="step"
    )

    assert numpy.array_equal(namedBurnup.values, reference.T)
    assert numpy.array_equal(namedBurnup.values, zaiSteps.values)
    assert numpy.array_equal(namedBurnup.index.values, referenceMaterial.burnup)
    assert numpy.array_equal(namedBurnup.columns.values, ["U235", "Xe135", "Pu239"])
    assert numpy.array_equal(zaiSteps.columns.values, [922350, 541350, 942390])
    assert numpy.array_equal(
        zaiSteps.index.values, range(len(referenceMaterial.days))
    )
    # Don't check the formatting of units, nor start of ZAI to prevent against
    # future changes
    assert namedBurnup.index.name.startswith("Burnup")
    assert zaiSteps.columns.name.endswith("ZAI")
    assert zaiSteps.index.name.endswith("Step")


@pytest.mark.skipif(sys.version_info < (3, 6), reason="pandas requires 3.6+")
def test_toDataFrameErrors(referenceMaterial):
    with pytest.raises(ValueError, match=".*2D"):
        referenceMaterial.toDataFrame("burnup")

    with pytest.raises(ValueError, match="Cannot pass both"):
        referenceMaterial.toDataFrame("adens", names=["U235"], zai=[922350])

    with pytest.raises(AttributeError, match=".*bad"):
        referenceMaterial.toDataFrame("bad")
