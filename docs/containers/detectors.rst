.. _api-detectors:

.. currentmodule:: serpentTools


Detectors
---------

.. warning::

    Serpent 1 detectors are not supported as of 0.8.0


.. note::

    Energy grids are stored in order of increasing
    energy, exactly as they appear in the output file. The three
    columns of this array correspond to lower bound, upper bound,
    and mid-point of that energy group


.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: mydetector.rst

    Detector
    CartesianDetector
    HexagonalDetector
    CylindricalDetector
    SphericalDetector
