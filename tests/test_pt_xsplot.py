"""Pytests for the xsplot reader"""


import pytest
import serpentTools


@pytest.fixture(scope="module")
def plut():
    return serpentTools.readDataFile("plut_xs0.m")


def test_dictaccess(plut):
    xsections = plut.xsections

    assert len(plut) == len(xsections)

    for key, value in plut.items():
        assert key in plut
        assert key in xsections
        assert value is xsections[key]
        assert plut[key] is value
        assert plut.get(key) is value

    assert plut.keys() == xsections.keys()

    # Check ids from values
    actual = {id(v) for v in plut.values()}
    expected = {id(v) for v in xsections.values()}

    assert actual == expected

    assert plut.get("this should not exist") is None
