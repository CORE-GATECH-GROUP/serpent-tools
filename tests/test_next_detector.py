"""Test for the new detector file"""
import pathlib
import zipfile
import io

import pytest
import serpentTools
from serpentTools.data import getFile
import serpentTools.next

BWR_FILE = getFile("bwr_det0.m")
HEX_FILE = getFile("hexplot_det0.m")


@pytest.fixture(scope="module")
def previousBWR():
    return serpentTools.read(BWR_FILE)


@pytest.fixture
def zippedStream(tmp_path):
    d = tmp_path / "next_detector"
    d.mkdir()
    filename = d / "bwr.zip"
    zipname = "bwr_det0.m"

    # Create the file in a zipped archive
    with zipfile.ZipFile(filename, mode="w") as z:
        with z.open(zipname, mode="w") as zfile, open(
            BWR_FILE, mode="rb"
        ) as sfile:
            zfile.write(sfile.read())

    # Yield the stream of binary zip data to be reader
    with zipfile.ZipFile(filename, mode="r") as z:
        with z.open(zipname, mode="r") as zstream:
            yield zstream

    # Clean up after the test
    filename.unlink()
    d.rmdir()


def compareDetector(actual, expected):
    assert type(actual) is type(expected)
    assert actual.indexes == expected.indexes
    assert actual.bins == pytest.approx(expected.bins)
    assert actual.tallies == pytest.approx(expected.tallies)
    assert actual.errors == pytest.approx(expected.errors)

    assert set(actual.grids) == set(expected.grids)

    for gridK, grid in expected.grids.items():
        assert actual.grids[gridK] == pytest.approx(grid)


def compareDetReader(actual, expected):
    assert set(actual) == set(expected)

    for key, detector in expected.items():
        compareDetector(actual[key], detector)


def test_new_det(previousBWR):
    fromstr = serpentTools.next.DetectorFile.fromSerpent(BWR_FILE)
    compareDetReader(fromstr, previousBWR)

    frompath = serpentTools.next.DetectorFile.fromSerpent(
        pathlib.Path(BWR_FILE)
    )
    compareDetReader(frompath, previousBWR)

    with open(BWR_FILE, mode="r") as stream:
        fromstream = serpentTools.next.DetectorFile.fromSerpent(stream)
    compareDetReader(fromstream, previousBWR)


def test_from_zip(previousBWR, zippedStream):
    newfile = serpentTools.next.DetectorFile.fromSerpent(zippedStream)
    compareDetReader(previousBWR, newfile)


@pytest.fixture(scope="module")
def previousHex():
    return serpentTools.read(HEX_FILE)


def test_filtered(previousHex):
    reader = serpentTools.next.DetectorReader()
    full = reader.read(HEX_FILE)
    compareDetReader(full, previousHex)

    for name, detector in previousHex.items():
        reader.names.clear()
        reader.names.add(name)
        single = reader.read(HEX_FILE)
        assert len(single) == 1
        found, fromFilter = single.popitem()
        assert found == name
        compareDetector(fromFilter, detector)


def test_postcheck():
    fakestream = io.StringIO()
    reader = serpentTools.next.DetectorReader()

    with pytest.raises(serpentTools.SerpentToolsException):
        reader.read(fakestream, postcheck=True, strict=True)

    reader.read(fakestream, postcheck=False)

    with pytest.warns(UserWarning):
        reader.read(fakestream, postcheck=True, strict=False)
