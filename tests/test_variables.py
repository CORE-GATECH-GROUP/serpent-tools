"""
Some tests for the setting of variable extras and groups
"""

import pytest
import serpentTools.settings

@pytest.fixture
def tempRC():
    """Provide an RC object that is reset after each test"""
    with serpentTools.settings.rc as temp:
        yield temp


@pytest.mark.parametrize("version", ["2.1.30", "2.1.31"])
def test_variableGroups(tempRC, version):
    tempRC["serpentVersion"] = version
    tempRC["xs.variableGroups"] = ["six-ff", "eig"]

    expected = {"SIX_FF_" + s for s in {
        "EPSILON", "ETA", "F", "KEFF", "KINF", "LT", "LF", "P"}}
    expected.update({
        "ANA_KEFF", "IMP_KEFF", "COL_KEFF", "ABS_KEFF", "ABS_KINF",
        "GEOM_ALBEDO"})
    assert expected == tempRC.expandVariables()
