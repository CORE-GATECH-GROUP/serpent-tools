import re
import os

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
