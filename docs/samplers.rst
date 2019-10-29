.. _samplers:

Samplers
========

The ``samplers`` module contains classes for reading multiple files of the same type,
and averaging quantities across all files. This is often used to remove or reduce
the stochastic noise associated with a Monte Carlo program.
When generating input files for such runs, it is key that each have a unique random seed.
This can be facilitated with the :func:`~serpentTools.seed.seedFiles` function, or through
the command line with :ref:`cli-seed`.

.. currentmodule:: serpentTools.samplers

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myclass.rst

    DetectorSampler
    SampledDetector
    DepletionSampler
    SampledDepletedMaterial

