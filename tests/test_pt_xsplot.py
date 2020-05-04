"""Pytests for the xsplot reader"""


import numpy
import pytest
import serpentTools

from . import getLegendTexts


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


@pytest.mark.parametrize("name", ["i8016_03c", "mfissile"])
def test_mts(plut, name):
    xsd = plut[name]
    for i, (mt, desc) in enumerate(zip(xsd.MT, xsd.MTdescrip)):
        assert numpy.equal(xsd[mt], xsd.xsdata[:, i]).all()
        assert xsd.describe(mt) == desc


@pytest.mark.parametrize("name", ["i8016_03c", "mfissile"])
def test_plotlegends(plut, name):
    from matplotlib import pyplot

    pyplot.close("all")

    ax = pyplot.gca()
    case = plut[name]
    # Plot all MTs
    case.plot(ax=ax)
    assert getLegendTexts(ax) == case.MTdescrip
    pyplot.cla()

    case.plot(case.MT[:2], ax=ax)
    assert getLegendTexts(ax) == case.MTdescrip[:2]
    pyplot.cla()

    case.plot(case.MT[:2], ax=ax, labels=["foo", "bar"])
    assert getLegendTexts(ax) == ["foo", "bar"]
    pyplot.cla()

    # Try a dictionary, but see if the plotter falls back for
    # missing labels

    case.plot(case.MT[:2], ax=ax, labels={case.MT[1]: "baz"})
    assert getLegendTexts(ax) == [case.MTdescrip[0], "baz"]

    with pytest.raises(ValueError):
        case.plot(labels=["hello", "world"], label=["failure", "mode"])
