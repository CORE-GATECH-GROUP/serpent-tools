.. _api-containers:

Containers
==========

.. currentmodule:: serpentTools

Many of the readers provided in this project and by :func:`read` rely on
custom classes for storing physically-similar data. This includes detector
data, where tallies can be stored next to underlying spatial and/or energy grids,
or depleted material data with isotopes and burnup data. Below are links to
reference documentation for all of the helper classes used in ``serpentTools``

.. note::

    With the exception of the detectors, these classes
    are not well suited to be created and populated
    outside of the readers. Much of the data accessing
    methods are stable, but providing data may change
    in future versions

.. _api-detectors:

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
    :template: myclass.rst

    Detector
    CartesianDetector
    HexagonalDetector
    CylindricalDetector
    SphericalDetector


.. _api-objects:

Supporting Classes
------------------

.. currentmodule:: serpentTools.objects

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myclass.rst

    BranchContainer
    DepletedMaterial
    HomogUniv
    XSData

.. _api-xs:

Branching Collector
-------------------

The ``xs`` module provides classes that condense :class:`HomogUniv`
data read in the :class:`serpentTools.BranchingReader`. The goal of
of these is to arrange the data in a structure that is more beneficial
for nodal diffusion codes.

.. currentmodule:: serpentTools.xs

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myclass.rst

    BranchCollector
    BranchedUniv
