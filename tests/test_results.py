import re
import os
from os.path import join as pjoin
from tempfile import TemporaryDirectory

import numpy
import pytest
import serpentTools


@pytest.fixture
def multipleGcuNoBu():
    origFile = serpentTools.data.getFile("InnerAssembly_res.m")
    newFile = "MultipleGcuNoBu_res.m"
    nGcu = 3
    counter = re.compile("Increase counter")
    burnKey = re.compile("BURN")
    counts = 0

    with open(origFile, "r") as orig, open(newFile, "w") as new:
        for line in orig:
            if burnKey.match(line):
                continue
            if counter.search(line):
                counts += 1
            if counts > nGcu:
                break
            new.write(line)

    with serpentTools.settings.rc as temprc:
        temprc["serpentVersion"] = "2.1.30"
        yield newFile

    os.remove(newFile)


def test_multipleGcuNoBu(multipleGcuNoBu):
    r = serpentTools.read(multipleGcuNoBu)
    assert len(r.universes) == 3
    for key in r.universes:
        assert key.step == 0
        assert key.burnup == 0
        assert key.days == 0


@pytest.fixture(scope="module")
def tdir():
    with TemporaryDirectory() as temp:
        yield temp


@pytest.fixture(scope="module")
def fake2132File(tdir):
    basefile = serpentTools.data.getFile("InnerAssembly_res.m")
    newfile = pjoin(tdir, "InnerAssembly_2132_res.m")
    with open(newfile, "w") as ostream, open(basefile, "r") as istream:
        for line in istream:
            if "2.1.31" in line:
                ostream.write(line.replace("2.1.31", "2.1.32"))
            else:
                ostream.write(line)
            if line.startswith("BURN_STEP"):
                ostream.write(
                    "BURN_RANDOMIZE_DATA       (idx, [1:  3])  = [ 0 0 0 ];\n"
                )
            elif line.startswith("BURN_DAYS"):
                ostream.write(
                    "FIMA                      (idx, [1:  3])  = [  0.00000E+00  0.00000E+00  1.00000E+25 ];\n"
                )
    yield newfile
    os.remove(newfile)


def test_2132_nofilter(fake2132File):
    with serpentTools.settings.rc as rc:
        rc["serpentVersion"] = "2.1.32"
        reader = serpentTools.read(fake2132File)
    singleFima = numpy.array([0, 0, 1e25])
    assert "fima" in reader.resdata
    assert (reader.resdata["fima"] == singleFima).all(), reader.resdata["fima"]
    assert not reader.resdata["burnRandomizeData"].any()


def test_2132_filterburnup(fake2132File):
    with serpentTools.settings.rc as rc:
        rc["serpentVersion"] = "2.1.32"
        rc["xs.variableGroups"] = ["burnup-coeff", "eig"]
        reader = serpentTools.read(fake2132File)
    assert "fima" in reader.resdata
    assert "burnDays" in reader.resdata
    assert "absKeff" in reader.resdata
    assert "pop" not in reader.metadata
