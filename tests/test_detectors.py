"""
Test various aspects of the detectors classes
"""

import numpy
import pytest
from serpentTools import detectors


def testDetectorProperties():
    bins = numpy.ones((25, 12))
    tallies = numpy.ones((5, 5))
    errors = numpy.ones_like(tallies)
    detector = detectors.Detector(
        "test", bins=bins, tallies=tallies, errors=errors)

    # Modify the tally data
    detector.tallies *= 2
    assert (detector.tallies == 2).all()
    detector.tallies = detector.tallies / 2
    assert (detector.tallies == 1).all()

    detector.errors *= 2
    assert (detector.errors == 2).all()
    detector.errors = detector.errors / 2
    assert (detector.errors == 1).all()

    energies = numpy.arange(bins.shape[0] * 3).reshape(bins.shape[0], 3)
    energyDet = detectors.Detector(
        "energy", bins=bins, grids={"E": energies})

    assert (energyDet.energy == energies).all()


def testCartesianDetector():
    xgrid = numpy.empty((4, 3))
    xgrid[:, 0] = range(-2, 2)
    xgrid[:, 1] = xgrid[:, 0] + 1
    xgrid[:, 2] = xgrid[:, 0] + 0.5
    ygrid = xgrid.copy()
    zgrid = numpy.array([[-1, 1, 0]])

    bins = numpy.ones((16, 12))
    tallies = numpy.ones((4, 4))
    errors = numpy.ones_like(tallies)

    detector = detectors.CartesianDetector(
        "xy", bins=bins, tallies=tallies, errors=errors,
        grids={"X": xgrid, "Y": ygrid, "Z": zgrid})

    # Modify the tally data
    detector.tallies *= 2
    assert (detector.tallies == 2).all()
    detector.tallies = detector.tallies / 2
    assert (detector.tallies == 1).all()

    detector.errors *= 2
    assert (detector.errors == 2).all()
    detector.errors = detector.errors / 2
    assert (detector.errors == 1).all()

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
