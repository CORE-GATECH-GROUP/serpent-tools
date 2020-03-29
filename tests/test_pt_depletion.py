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
    adensFrame = referenceMaterial.toDataFrame(quantity)
    assert numpy.array_equal(
        adensFrame.columns.values, referenceMaterial.names
    )
    assert numpy.array_equal(adensFrame.index.values, referenceMaterial.days)
    assert numpy.array_equal(
        adensFrame.values, referenceMaterial.data[quantity].T
    )

    reference = referenceMaterial.getValues(
        "days", quantity, names=["U235", "Xe135", "Pu239"]
    )
    frame0 = referenceMaterial.toDataFrame(
        quantity, names=["U235", "Xe135", "Pu239"], index="burnup"
    )
    frame1 = referenceMaterial.toDataFrame(
        quantity, zai=[922350, 541350, 942390], index="step"
    )

    assert numpy.array_equal(frame0.values, reference.T)
    assert numpy.array_equal(frame0.values, frame1.values)
    assert numpy.array_equal(frame0.index.values, referenceMaterial.burnup)
    assert numpy.array_equal(frame0.columns.values, ["U235", "Xe135", "Pu239"])
    assert numpy.array_equal(frame1.columns.values, [922350, 541350, 942390])
    assert numpy.array_equal(
        frame1.index.values, range(len(referenceMaterial.days))
    )


@pytest.mark.skipif(sys.version_info < (3, 6), reason="pandas requires 3.6+")
def test_toDataFrameErrors(referenceMaterial):
    with pytest.raises(ValueError, match=".*2D"):
        referenceMaterial.toDataFrame("burnup")

    with pytest.raises(ValueError, match="Cannot pass both"):
        referenceMaterial.toDataFrame("adens", names=["U235"], zai=[922350])

    with pytest.raises(AttributeError, match=".*bad"):
        referenceMaterial.toDataFrame("bad")
