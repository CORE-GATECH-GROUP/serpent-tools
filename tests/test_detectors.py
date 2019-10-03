"""
Test various aspects of the detectors classes
"""

import numpy
import pytest
from serpentTools import detectors

@pytest.fixture(scope="module")
def meshedBinData():
    bins = numpy.ones((25, 12), order="f")
    bins[:, -1] = range(25)
    bins[:, -2] = range(25)
    bins[:, -3] = numpy.tile(range(1, 6), 5)
    bins[:, -4] = numpy.repeat(range(1, 6), 5)

    tallies = numpy.arange(25).reshape(5, 5)
    errors = tallies.copy()

    return bins, tallies, errors


def testDetectorProperties(meshedBinData):
    bins, tallies, errors = meshedBinData

    detector = detectors.Detector(
        "test", bins=bins, tallies=tallies, errors=errors)

    # Modify the tally data
    detector.tallies = detector.tallies * 2
    assert (detector.tallies == tallies * 2).all()

    detector.errors = detector.errors * 2
    assert (detector.errors == errors * 2).all()

    energies = numpy.arange(bins.shape[0] * 3).reshape(bins.shape[0], 3)
    energyDet = detectors.Detector(
        "energy", bins=bins, grids={"E": energies})

    assert (energyDet.energy == energies).all()

    # Test setting indexes

    detector.indexes = tuple(range(len(tallies.shape)))

    with pytest.raises(ValueError, match="indexes"):
        detector.indexes = detector.indexes[:1]

@pytest.mark.parametrize("how", ["bins", "grids", "bare", "init"])
def testCartesianDetector(meshedBinData, how):

    xgrid = numpy.empty((5, 3))
    xgrid[:, 0] = range(5)
    xgrid[:, 1] = xgrid[:, 0] + 1
    xgrid[:, 2] = xgrid[:, 0] + 0.5

    ygrid = xgrid.copy()

    zgrid = numpy.array([[-1, 1, 0]])

    bins, tallies, errors = meshedBinData

    grids = {"X": xgrid.copy(), "Y": ygrid.copy(), "Z": zgrid.copy()}

    if how == "bare":
        detector = detectors.CartesianDetector("xy_bare")
        detector.bins = bins
        detector.tallies = tallies
        detector.errors = errors
        detector.x = grids["X"]
        detector.y = grids["Y"]
        detector.z = grids["Z"]
    elif how == "grids":
        detector = detectors.CartesianDetector(
            "xy_full", bins=bins, tallies=tallies, errors=errors,
            grids=grids)
    elif how == "init":
        detector = detectors.CartesianDetector(
            "xy_full", bins=bins, tallies=tallies, errors=errors,
            x=grids["X"], y=grids["Y"], z=grids["Z"])
    elif how == "bins":
        detector = detectors.CartesianDetector.fromTallyBins(
            "xyBins", bins=bins, grids=grids)

    # Modify the tally data
    detector.tallies = tallies * 2
    assert (detector.tallies == tallies * 2).all()

    detector.errors = errors * 2
    assert (detector.errors == errors * 2).all()

    assert (detector.x == xgrid).all()
    assert (detector.y == ygrid).all()
    assert (detector.z == zgrid).all()

    # Emulate scaling by some conversion factor
    detector.x *= 100
    assert (detector.x == xgrid * 100).all()
    detector.y *= 100
    assert (detector.y == ygrid * 100).all()
    detector.z *= 100
    assert (detector.z == zgrid * 100).all()

    # Test failure modes

    for gridk in ["x", "y", "z"]:
        msg = ".*shape of {} grid".format(gridk)
        with pytest.raises(ValueError, match=msg):
            setattr(detector, gridk, [1, 2, 3])

    # Test setting indexes

    detector.indexes = tuple(range(len(tallies.shape)))

    with pytest.raises(ValueError, match="indexes"):
        detector.indexes = detector.indexes[:1]

@pytest.mark.parametrize("how", ["grids", "bins", "bare", "init"])
def testHexagonalDetector(meshedBinData, how):
    centers = numpy.array([
        [-3.000000E+00, -1.732051E+00],
        [-2.500000E+00, -8.660254E-01],
        [-2.000000E+00, 0.000000E+00],
        [-1.500000E+00, 8.660254E-01],
        [-1.000000E+00, 1.732051E+00],
        [-2.000000E+00, -1.732051E+00],
        [-1.500000E+00, -8.660254E-01],
        [-1.000000E+00, 0.000000E+00],
        [-5.000000E-01, 8.660254E-01],
        [0.000000E+00, 1.732051E+00],
        [-1.000000E+00, -1.732051E+00],
        [-5.000000E-01, -8.660254E-01],
        [0.000000E+00, 0.000000E+00],
        [5.000000E-01, 8.660254E-01],
        [1.000000E+00, 1.732051E+00],
        [0.000000E+00, -1.732051E+00],
        [5.000000E-01, -8.660254E-01],
        [1.000000E+00, 0.000000E+00],
        [1.500000E+00, 8.660254E-01],
        [2.000000E+00, 1.732051E+00],
        [1.000000E+00, -1.732051E+00],
        [1.500000E+00, -8.660254E-01],
        [2.000000E+00, 0.000000E+00],
        [2.500000E+00, 8.660254E-01],
        [3.000000E+00, 1.732051E+00],
    ])
    z = numpy.array([[0, 0, 0]])

    bins, tallies, errors = meshedBinData

    pitch = 1.0
    hexType = 2

    if how == "init":
        detector = detectors.HexagonalDetector(
            "hexInit", bins=bins, tallies=tallies, errors=errors,
            z=z, centers=centers, pitch=pitch, hexType=hexType)
    elif how == "grids":
        detector = detectors.HexagonalDetector(
            "hexGrids", bins=bins, tallies=tallies, errors=errors,
            grids={"Z": z, "COORD": centers})
    elif how == "bins":
        detector = detectors.HexagonalDetector.fromTallyBins(
            "hexBins", bins, grids={"Z": z, "COORD": centers})
    elif how == "bare":
        detector = detectors.HexagonalDetector("hexBins")
        detector.bins = bins
        detector.tallies = tallies
        detector.errors = errors
        detector.z = z
        detector.centers = centers

    if how != "init":
        detector.pitch = pitch
        detector.hexType = hexType

    assert (detector.bins == bins).all()
    assert (detector.tallies == tallies).all()
    assert (detector.errors == errors).all()
    assert (detector.z == z).all()
    assert (detector.centers == centers).all()
    assert detector.pitch == pitch
    assert detector.hexType == hexType

    detector.tallies = detector.tallies * 2
    detector.errors = detector.errors * 2
    detector.z = detector.z * 2
    detector.centers = detector.centers * 2
    detector.pitch = detector.pitch * 2

    assert (detector.tallies == tallies * 2).all()
    assert (detector.errors == errors * 2).all()
    assert (detector.z == z * 2).all()
    assert (detector.centers == centers * 2).all()
    assert detector.pitch == pitch * 2

    # Test failure modes

    with pytest.raises(ValueError, match="Hex type"):
        detector.hexType = -1

    with pytest.raises(ValueError, match="Pitch must be positive"):
        detector.pitch = 0

    with pytest.raises(ValueError, match="Pitch must be positive"):
        detector.pitch = -1

    with pytest.raises(TypeError, match="Cannot set pitch"):
        detector.pitch = [1, 2]

    with pytest.raises(ValueError, match="Expected centers"):
        detector.centers = detector.centers[:5]

    with pytest.raises(ValueError, match="Expected shape of z"):
        detector.z = [[-1, 0, -0.5], [0, 1, 0.5]]


@pytest.fixture(scope="module")
def binsWithScores():
    bins = numpy.ones((2, 13))
    bins[0, -3] = 1.5
    return bins

def testNoScores(binsWithScores):

    with pytest.raises(ValueError, match=".*scores"):
        detectors.Detector("scored", bins=binsWithScores)

    with pytest.raises(ValueError, match=".*scores"):
        detectors.Detector("scored").bins = binsWithScores

    with pytest.raises(ValueError, match=".*scores"):
        detectors.Detector.fromTallyBins("scored", bins=binsWithScores)
