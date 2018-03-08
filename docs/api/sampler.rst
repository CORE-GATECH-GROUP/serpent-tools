.. |serpentTools| replace:: :ref:`welcome`

.. |depletion| replace:: :ref:`depletion`

.. |detector| replace:: :ref:`detector-reader`

.. |sampler| replace:: :py:class:`~serpentTools.samplers.Sampler`

.. |detector-container| replace:: :py:class:`~serpentTools.objects.containers.Detector`

.. _samplerAPI:

Samplers
========

A common practice in Monte Carlo analysis is repeat a single case
with a variety of new random number seeds.
Averaging the results from these runs reduces the impact of stochastic
uncertainty and can give a better picture of the *true* behavior of a
system. The |serpentTools| package supports reading multiple output
files of a common type and obtaining average values and associated
uncertainties, while retaining data structure and retrieval
methods similar to the single file cases.


Detector Sampler
----------------

This sampler extends the |sampler| class for reading detector files.

.. autoclass:: serpentTools.samplers.detector.DetectorSampler

.. autoclass:: serpentTools.samplers.detector.SampledDetector

DepletionSampler
----------------

This sampler extends the |sampler| class for reading depletion files.

.. autoclass:: serpentTools.samplers.depletion.DepletionSampler

.. autoclass:: serpentTools.samplers.depletion.SampledDepletedMaterial


.. _sampler::

Base Classes
------------

.. autoclass:: serpentTools.samplers.Sampler

.. autoclass:: serpentTools.samplers.SampledContainer
