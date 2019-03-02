.. |depletion| replace:: :ref:`depletion`

.. |detector| replace:: :ref:`detector-reader`

.. |sampler| replace:: :py:class:`~serpentTools.samplers.Sampler`

.. |detector-container| replace:: :py:class:`~serpentTools.Detector`

.. _samplerAPI:

Samplers
========

A common practice in Monte Carlo analysis is repeat a single case
with a variety of new random number seeds.
Averaging the results from these runs reduces the impact of stochastic
uncertainty and can give a better picture of the *true* behavior of a
system. The ``sampler`` package supports reading multiple output
files of a common type and obtaining average values and associated
uncertainties, while retaining data structure and retrieval
methods similar to the single file cases.


Detector Sampler
----------------

This sampler extends the |sampler| class for reading detector files.

.. autoclass:: serpentTools.samplers.DetectorSampler
    :special-members: __getitem__

.. autoclass:: serpentTools.samplers.SampledDetector

DepletionSampler
----------------

This sampler extends the |sampler| class for reading depletion files.

.. autoclass:: serpentTools.samplers.DepletionSampler
    :special-members: __getitem__

.. autoclass:: serpentTools.samplers.SampledDepletedMaterial


.. _sampler-base:

Base Classes
------------

.. autoclass:: serpentTools.samplers.Sampler

.. autoclass:: serpentTools.samplers.SampledContainer
