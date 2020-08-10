"""pytest tests for reading the result file"""

import pytest
import serpentTools.data
from serpentTools.settings import rc


@pytest.fixture(scope="module")
def read_2_1_29():
    with rc:
        rc["serpentVersion"] = "2.1.29"
        yield


@pytest.fixture
def fullPwrFile(read_2_1_29):
    return serpentTools.data.readDataFile("pwr_res.m")


def test_scalars(fullPwrFile):
    """Ensure that the full precision of scalars are captured

    Related: GH issue #411
    """
    assert fullPwrFile["miscMemsize"] == pytest.approx([6.59, 6.59], abs=0, rel=0)
    assert fullPwrFile["availMem"] == pytest.approx([15935.20, 15935.20], abs=0, rel=0)
    assert fullPwrFile["totCpuTime"] == pytest.approx([0.282078, 0.494889], abs=0, rel=0)

