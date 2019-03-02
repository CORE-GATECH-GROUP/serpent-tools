.. |homogUniv| replace:: class:`~serpentTools.objects.containers.HomogUniv`
.. |resultReader| replace:: :class:`~serpentTools.ResultsReader` 
.. |detector| replace:: :class:`~serpentTools.objects.Detector`
.. |detectorReader| replace:: :class:`~serpentTools.DetectorReader`
.. |depletionReader| replace:: :class:`~serpentTools.DepletionReader`
.. |depmtxReader| replace:: :class:`~serpentTools.DepmtxReader`
.. |toMatlab-short| replace:: :func:`~serpentTools.io.toMatlab`
.. |toMatlab-full| replace:: :func:`serpentTools.io.toMatlab`
.. |branchCollector| replace:: :class:`~serpentTools.BranchCollector` 
.. _changelog:

=========
Changelog
=========

Next
====

* Easier construction of |branchCollector| objects with
  :class:`~serpentTools.xs.BranchCollector.fromFile`.
* Don't require passing branch information to |branchCollector|. Will be infered
  from file and set with ``(p1, p2, ...)``. State data can be used to 
  determine which index is a given perturbation type.
* Direct ``toMatlab`` methods for ``SensitivityReader``, |depmtxReader|
  |depletionReader|, |detectorReader|, ``HistoryReader``, and |detector| objects.

.. _v0.6.2:

:release-tag:`0.6.2`
====================

* Data files are bundled in source distribution
* CLI interface for converting some output files to matlab files - 
  :ref:`cli-to-matlab`
* Add :mod:`serpentTools.io` module for converting objects to
  other data types. Currently a general function for converting
  |toMatlab-short|
* |detectorReader| and |detector| objects can be writen to 
  MATLAB files using |toMatlab-full|
* |resultReader| can plot data using
  :meth:`~serpentTools.ResultsReader.plot`
* Experimental |branchCollector| for
  collecting group constants from coefficient files. Collects
  group constants in in multi-dimensional matrices according
  to perturbations, universes, and burnup.
* Plotting routines now use attach to the active plot or generate
  a new plot figure if ``ax`` argument not given - :issue:`267`
* :class:`~serpentTools.BranchingReader` can
  read coefficient files with uncertainties - :issue:`270`

.. warning::

   The API for the |branchCollector| may be subject to change
   through revisions until ``0.7.0``

Incompatible API Changes
------------------------

* |homogUniv| objects are now stored on |resultReader| with 
  zero-based indexing for burnup. The previous first value of 
  burnup step was one. All burnup indices are now decreased by
  one. Similarly, if no burnup was present in the file, the
  values of burnup and days for all universes is zero.
* When reading detectors with a single tally, the value of ``tallies``,
  ``errors``, and ``scores`` are stored as floats, rather than 
  :term:`numpy` arrays.

Pending Deprecations
--------------------

* :meth:`~serpentTools.DepletionReader.saveAsMatlab` 
  in favor of |toMatlab-full| with::

      >>> from serpentTools.io import toMatlab
      >>> toMatlab(depR)

* Depletion plot routines will no longer accept ``timePoints`` arguments,
  instead plotting against all points in time
 
.. _v0.6.1:

:release-tag:`0.6.1`
====================

* :pull:`256` :meth:`serpentTools.settings.rc.loadYaml` uses ``safe_load``
* :pull:`257` |depletionReader| now can utilize 
  :meth:`~serpentTools.DepletionReader.saveAsMatlab` for
  exporting data to a binary ``.mat`` file
* :pull:`259` Little more clarity into supported readers through documentation
  and ``serpentTools.read`` function

.. _v0.6.0:

:release-tag:`0.6.0`
====================

* :pull:`174` - Added parent object ``BaseObject`` with basic comparison
  method from which all objects inherit. Comparison method contains
  upper and lower bounds for values w/o uncertainties, :pull:`191`
* :pull:`196` - Add comparison methods for |resultReader| and 
  |homogUniv| objects
* :pull:`228` - Add comparison methods for |detectorReader| and
  |detector| objects
* :pull:`236` - Add comparison methods for |depletionReader| and
  :class:`~serpentTools.objects.DepletedMaterial` objects
* :pull:`241` - Fix a bug in the CLI that rendered the ability to generate files with
  unique random seeds. ``python -m serpentTools seed <input> <N>`` can now be properly
  used.  
* :pull:`249` - Better sparse support for depletion matrix, ``depmtx`` files with a
  |depmtxReader|
* :pull:`252` - Better axis and colorbar labeling for |detector| mesh plots
* :pull:`254` - Better plotting of single concentrations with |depmtxReader|
* :pull:`255` - |depletionReader| can capture material with underscores now!

Deprecations
------------

* :func:`~serpentTools.parsers.depmtx` is deprecated in favor of either
  :func:`~serpentTools.parsers.readDepmtx` or the class-based
  |depmtxReader|


.. _v0.5.4:

:release-tag:`0.5.4`
====================

* :pull:`239` - Update python dependencies to continue use of python 2

.. _v0.5.3:

:release-tag:`0.5.3`
====================

* :pull:`221` - Expanded ``utils`` module to better assist developers
* :pull:`227` - Better documentation of our :ref:`cli`.
  Better documentation and testing of functions for generating input
  files with unique random seeds - :mod:`serpentTools.seed`
* :pull:`229` - :meth:`serpentTools.SensitivityReader.plot`
  now respects the option to not set x nor y labels.
* :pull:`231` - |resultReader| objects
  can now read files that do not contain group constant data. The setting
  :ref:`results-expectGcu` should be used to inform the reader that no
  group constant data is anticipated
  

.. _v0.5.2:

:release-tag:`0.5.2`
====================

* :pull:`198` - Import test and example files using :mod:`serpentTools.data`. 
  Load example readers with :func:`serpentTools.data.readDataFile`
* :pull:`199` - Support for structured or unstructured matrix plotting with
  :func:`serpentTools.plot.cartMeshPlot`
* :pull:`201` - Support for plotting hexagonal meshes with
  :meth:`serpentTools.objects.HexagonalDetector.hexPlot`
* :pull:`204` - Access |detector|
  objects directly from |detectorReader|
  with ``reader[detName]``
* :pull:`205` - Access materials from |depletionReader|
  and :class:`serpentTools.samplers.DepletionSampler` using key-like
  indexing, e.g. ``reader[matName] == reader.material[matName]``
* :pull:`213` - Better default x-axis labels for simple detector plots

.. _v0.5.2-api:

API Changes
-----------
* :pull:`194` - Some settings in :attr:`serpentTools.ResultsReader.metadata`
  are now stored as :class:`int` or :class:`float`, depending upon their nature.
  Many of these settings refer to flags of settings used by ``SERPENT``

.. _v0.5.1:

:release-tag:`0.5.1`
====================

* :pull:`180` - Add capability to pass isotope ``zzaaai`` for 
  :meth:`~serpentTools.objects.materials.DepletedMaterial.getValues` 
  and associated plot routines
* :pull:`187` - Import all readers and samplers from the main package::

    >>> from serpentTools import ResultsReader
    >>> from serpentTools import DetectorSampler

* :pull:`189` - Support for reading detectors with hexagonal, cylindrical, and 
  spherical meshes.

.. _v0.5.1-api:

API Changes
-----------

* ``zzaaai`` data is stored on 
  :attr:`~serpentTools.objects.materials.DepletedMaterial.zai` as a list
  of integers, not strings

.. _v0.5.0:

:release-tag:`0.5.0`
====================

* :pull:`131` Updated variable groups between ``2.1.29`` and ``2.1.30`` - include
  poison cross section, kinetic parameters, six factor formula (2.1.30 exclusive),
  and minor differences
* :pull:`141` - Setting :ref:`xs-reshapeScatter` can be used to reshape scatter
  matrices on |homogUniv|
  objects to square matrices
* :pull:`145` - :meth:`~serpentTools.objects.containers.HomogUniv.hasData` 
  added to check if |homogUniv| 
  objects have any data stored on them
* :pull:`146` - |homogUniv| object
  stores group structure on the object. New dictionaries for storing group constant
  data that is not ``INF`` nor ``B1`` - 
  :attr:`~serpentTools.objects.containers.HomogUniv.gc` and 
  :attr:`~serpentTools.objects.containers.HomogUniv.gcUnc` 
* :pull:`130` Added the ability to read results file
* :pull:`149` - Add the ability to read sensitivity files
* :pull:`161` - Add the :mod:`~serpentTools.utils` module
* :pull:`165` - Add the :meth:`serpentTools.objects.containers.HomogUniv.plot` 
  method
   
.. _v0.5.0API-changes:

API Changes
-----------

* :pull:`146` removed ``metadata`` dictionaries on |homogUniv| objects.

.. _v0.5.0Deprecated:

Deprecation
-----------

* Variable group ``xs-yields`` is removed. Use ``poisons`` instead
* Branches of a single name are only be accessible through 
  ``branches['nom']``, not ``branches[('nom'), ]`` as per :pull:`114`

.. _v0.4.0:

:release-tag:`0.4.0`
====================

* :pull:`95` Add ``xsplot`` file reader
* :pull:`121` Samplers will raise more warnings/errors if no files are loaded
  from ``*`` wildcards
* :pull:`122` Better detector labeling
* :pull:`135` Added instructions for better converting Jupyter notebooks to 
  ``.rst`` files. Plotting guidelines

.. _v0.3.1:

:release-tag:`0.3.1`
====================

* :pull:`118` - Support for ``SERPENT`` 2.1.30
* :issue:`119` - SampledDepletedMaterial now respects the value of `xUnits` 
  - :pull:`120`
* :pull:`114` - Standalone branches in the coefficient files are stored
  and accessed using a single string, rather than a single-entry tuple
  ``branches['myBranch']`` vs. ``branches[('myBranch', )]``

    
.. _v0.3.0:

:release-tag:`0.3.0`
====================

* :pull:`109` - Capability to read history files
* :pull:`107` - DepletionReader can now plot data for some or all materials

.. _v0.2.2:

:release-tag:`0.2.2`
====================

* :pull:`82` - Command line interface and some sub-commands
* :pull:`88` - Pre- and post-check methods for readers
* :pull:`93` - Detector and Depletion Samplers
* :pull:`96` - Better mesh plotting for detector
* :issue:`99` - Negative universe burnup with branching reader - :pull:`100`
* :attr:`serpentTools.objects.containers.Detector.indexes` are now zero-indexed
* The PDF manual is no longer tracked in this repository

