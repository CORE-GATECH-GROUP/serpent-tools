.. |toMatlab-short| replace:: :func:`~serpentTools.io.toMatlab`
.. |toMatlab-full| replace:: :func:`serpentTools.io.toMatlab`
.. _changelog:

=========
Changelog
=========

.. _v0.10.1:

:release-tag:`0.10.1`
=====================

This is a bug fix release to fix installing the package.
Users should experience no changes. Developer should note
that the package has moved from a "flat-layout" to a "src-layout",
where the code the the package has moved from ``serpentTools``
to ``src/serpentTools``

* Move from "flat-layout" to "src-layout" - :pull:`506`

.. _v0.10.0:

:release-tag:`0.10.0`
=====================

.. warning::

    This release has been pulled from :term:`PyPI` and should
    be replaced with :ref:`v0.10.1`

* Drop support for Python 3.5, 3.6, and 3.7 - :pull:`478`
* Support and test against Python 3.9, 3.10, and 3.11 - :pull:`492`
* Support Serpent 2.2.1 - :pull:`481`

.. _v0.9.5:

:release-tag:`0.9.5`
====================

.. note::

    Following the `0.9.5` release, the default branch for development
    will be the ``main`` branch on GitHub.

*  Allow microxs reader to handle files w/o nfy data :pull:`468`
*  ResultsReader supports Serpent 2.2.0 :pull:`472`
*  SensitivityReader.plot applies the title to the plot :pull:`471`
*  SensitivityReader.plot uses absolute value for yerr :pull:`470`
*  Allow pathlib.Path arguments to readers :pull:`463`

.. _v0.9.4:

:release-tag:`0.9.4`
====================

* Normalize spectrum by maximum value or not at all - :pull:`457`
* Support for reading ``pspec`` fields in xsplot files - :pull:`456`

* Support for Serpent 2.1.32 via :ref:`settings`. 2.1.31 is still
  default - :pull:`447`
* Support for installing under python 3.9 - :pull:`444`
* Various ``plot`` methods now support passing keyword arguments to underlying
  matplotlib plot routines

  * :meth:`serpentTools.objects.HomogUniv.plot` - :pull:`432`
  * :meth:`serpentTools.SensitivityReader.plot` - :pull:`434`
  * :meth:`serpentTools.ResultsReader.plot` - :pull:`446`

Supported by releases :release-tag:`0.9.4rc0` and :release-tag:`0.9.4rc1`

.. _v0.9.3:

:release-tag:`0.9.3`
====================

* Depletion data now exposed through attributes like
  :attr:`~serpentTools.objects.DepletedMaterial.adens` - :pull:`390`
* Generate a :class:`pandas.DataFrame` with depletion data using
  :meth:`~serpentTools.objects.DepletedMaterial.toDataFrame`
  - :pull:`391`
* Dictionary-like item access and iteration for branching, detector,
  history, depletion, and xsplot readers - :pull:`392`, :pull:`395`, :pull:`402`
* Obtain data from :attr:`~serpentTools.ResultsReader.resdata` with
  :meth:`~serpentTools.ResultsReader.__getitem__` and 
  :meth:`~serpentTools.ResultsReader.get` - :pull:`392`
* Modify plot legends for :meth:`serpentTools.objects.XSData.plot` for all
  or some plotted MTs - :pull:`402`
* Options for plotting sensitivity profiles against energies in MeV - :pull:`405`

.. _v0.9.3-bug:

Bug Fixes
---------

* Support ``xsplot`` files with branching fractions - :issue:`387`, :pull:`388`

.. _v0.9.3-dep:

Pending Deprecations
--------------------

* :attr:`serpentTools.DepletionReader.metadata`. Prefer attributes
  like :attr:`~serpentTools.DepletionReader.zais`
* :attr:`serpentTools.samplers.DepletionSampler.metadata`. Prefer
  attributes like :attr:`~serpentTools.samplers.DepletionSampler.zais`
* :meth:`serpentTools.BranchingReader.iterBranches`. Prefer
  :meth:`~serpentTools.BranchingReader.items`
* :attr:`serpentTools.XSPlotReader.metadata` and
  :attr:`serpentTools.objects.XSData.metadata`. Prefer attributes like
  :attr:`~serpentTools.XSPlotReader.majorant` or 
  :attr:`~serpentTools.objects.XSData.energies` - :pull:`402`

.. _v0.9.2:

:release-tag:`0.9.2`
====================

* Officially support installing under Python 3.8
* Support for passing threshold values to hexagonal detector plots
  - :issue:`351`

.. _v0.9.2-bugs:

Bug Fixes
---------

* Detector reader can handle sequential detectors with very similar
  names - :issue:`374`.
* ``serpentTools`` doesn't make any modifications to the logging state,
  other than introducing package-wide logger - :pull:`380`
* Colorbars for mesh plots are placed next to their corresponding
  plot, rather than near the last drawn plot - :issue:`372`

.. _v0.9.1:

:release-tag:`0.9.1`
====================

.. _v0.9.1-bugs:

Bug Fixes
---------

* Sensitivity arrays generated with ``sens opt history 1`` will no longer
  overwrite the primary result arrays - :pull:`366`. These arrays are not 
  currently stored - :issue:`367`

.. _v0.9.0:

:release-tag:`0.9.0`
====================

* Python 2 support has been dropped.
* Add support for installing and testing against Python 3.7

.. _v0.8.1:

:release-tag:`0.8.1`
====================

* Use ``six>=1.13.0``
* Use ``yaml>=5.1.1``

.. _v0.8.1-bug:

Bug Fixes
---------

* Fix :ref:`detector-names` setting

.. _v0.8.0:

:release-tag:`0.8.0`
====================


.. warning::

    Serpent 1 detectors are no longer supported - :issue:`327`.
    Version 0.9.0 will remove support for python 2 - :issue:`328`

* Better handling of discontinuity factors - :pull:`329`
* |HomogUniv| objects no longer automatically convert data to arrays
* Serpent 2.1.31 is the default version for :ref:`serpentVersion` setting
* Detectors and related subclasses are now standalone classes that can be
  imported as ``serpentTools.Detector`` - :pull:`341`
* :class:`~serpentTools.objects.BranchContainer` now inherits from
  :class:`dict` - :pull:`344`
* Keys for universes in ``ResultsReader.universes`` are
  :class:`~serpentTools.objects.UnivTuple`
* Keys for microscopic cross sections in ``MicroXSReader.xsVal`` and
  ``MicroXSReader.xsUnc`` are :class:`~serpentTools.MicroXSTuple`
* Spread plots for sampled detector and depletion containers allow
  changing how the mean data and sampled data are plotted by passing
  dictionary of matplotlib commands, e.g.
  ``meanKwargs={"c": "r", "marker": x"}`` would plot the mean data in
  red with crosses as markers.

.. _v0.8.0-bug:

Bug Fixes
---------

* Burnup and days are properly set on homogenized universes when reading a
  result file with multiple universes but no burnup - :pull:`346`
* Modifications made to detector tally data will be reflected in later
  plots - :issue:`337`, :pull:`341`
* Variable groups for version 2.1.31 are properly expanded - :pull:`347`

.. _v0.8.0-api:

Incompatible API Changes
------------------------

* Values are stored in array form on |HomogUniv| when it makes sense.
  For example, values like ``infKinf`` are stored as scalars.
* Setting ``expectGcu`` has been removed as :pull:`324` fixed how files without
  group constants are handled.
* Keys to |BranchedUniv| objects stored in
  :attr:`serpentTools.xs.BranchCollector.universes` are stored as strings,
  rather than integers, e.g. ``0`` is replaced with ``"0"`` - :pull:`321`
* Keys to |HomogUniv| instances stored on
  :class:`~serpentTools.objects.BranchContainer` are now
  :class:`~serpentTools.objects.UnivTuple`, or tuples with
  ``universe, burnup, step, days`` - :pull:`344`
* :class:`serpentTools.Detector.indexes` is now a tuple of strings
  describing each dimension of ``tallies`` rather than ``OrderedDict``
  - :pull:`341`

.. _v0.7.1:

:release-tag:`0.7.1`
====================

* Add :meth:`~serpentTools.objects.HomogUniv.__getitem__` and
  :meth:`~serpentTools.objects.HomogUniv.__setitem__` convenience
  methods for accessing expected values on |HomogUniv| objects
* Add ``thresh`` argument to |Detector| ``meshPlot`` where
  only data greater than ``thresh`` is plotted.
* Mitigate pending deprecated imports from ``collections`` - :issue:`313`
* Increase required version of :term:`yaml` to ``5.1.1``
* Include ``SERPENT`` ``2.1.31`` support in :ref:`serpentVersion` setting

.. _v0.7.1-bug:

Bug fixes
---------

* Tally data for detectors with time-bins are properly handled - :issue:`312`
* Support for generic string universe names for |BranchingReader| and
  |BranchCollector| - :issue:`318`

.. _v0.7.1-dep:

Pending Deprecations
--------------------

* Keys to |BranchedUniv| objects stored in
  :attr:`serpentTools.xs.BranchCollector.universes` are stored as strings,
  rather than integers, e.g. ``0`` is replaced with ``"0"``. A workaround
  is in-place, but will be removed in future versions.
* ``SERPENT`` 1 style detectors with additional score column will not be
  supported starting at version ``0.8.0``.

.. _v0.7.0:

:release-tag:`0.7.0`
=======================

* Easier construction of |BranchCollector| objects - :pull:`276`
    * Directly from the class :class:`~serpentTools.xs.BranchCollector.fromFile`
    * Don't require passing branch information to |BranchCollector|. Will be inferred
      from file and set with ``(p0, p1, ...)``. State data can be used to
      determine which index is a given perturbation type.
* Direct ``toMatlab`` methods for |ResultsReader|, |SensitivityReader|,
  |DepmtxReader| |DepletionReader|, |DetectorReader|, |HistoryReader|,
  and |Detector| objects - :pull:`290`, :pull:`291`
* Overhaul, reorganization, and cleanup of documentation

.. _v0.7.0-api:

Incompatible API Changes
------------------------

* |HomogUniv| objects are now stored on |ResultsReader| with
  zero-based indexing for burnup. The previous first value of
  burnup step was one. All burnup indices are now decreased by
  one. Similarly, if no burnup was present in the file, the
  values of burnup and days for all universes is zero - :pull:`288`
* When reading Detectors with a single tally, the value of ``tallies``,
  ``errors``, and ``scores`` are stored as floats, rather than
  :term:`numpy` arrays - :pull:`289`

.. _v0.7.0-dep:

Deprecations
------------

* |DepletionReader| ``saveAsMatlab`` in favor of
  :meth:`~serpentTools.DepletionReader.toMatlab`
* SERPENT ``2.1.30`` is the default version of :ref:`serpentVersion`. Will
  alter some variable groups, like :ref:`optimization-base` and
  :ref:`optimization-2-1-30`, that exist in both versions but are slightly
  different.

.. _v0.7.0-bug:

Bug Fixes
---------

* |BranchingReader| is now capable of reading ``.coe`` files with
  uncertainties - :pull:`272`
* Fixed a bug that caused some plots not to return the axes object of the plot
  - :pull:`297`
* |HomogUniv| plots are plotted against energy group when no group structure
  can be determined, and now labeled as such - :pull:`299`
* Removed a non-zero exit code from a successful use of the :ref:`cli-seed`
  command line command - :pull:`300`
* |ResultsReader| can process files with assembly discontinuity factors (ADFs)
  - :pull:`305`

.. _v0.6.2:

:release-tag:`0.6.2`
====================

* Data files are bundled in source distribution
* CLI interface for converting some output files to matlab files -
  :ref:`cli-to-matlab`
* Add :mod:`serpentTools.io` module for converting objects to
  other data types. Currently a general function for converting
  |toMatlab-short|
* |DetectorReader| and |Detector| objects can be written to
  MATLAB files using |toMatlab-full|
* |ResultsReader| can plot data using
  :meth:`~serpentTools.ResultsReader.plot`
* Experimental |BranchCollector| for
  collecting group constants from coefficient files. Collects
  group constants in in multi-dimensional matrices according
  to perturbations, universes, and burnup.
* Plotting routines now use attach to the active plot or generate
  a new plot figure if ``ax`` argument not given - :issue:`267`
* |BranchingReader| can
  read coefficient files with uncertainties - :issue:`270`

.. warning::

   The API for the |BranchCollector| may be subject to change
   through revisions until ``0.7.0``

.. _v0.6.2-dep:

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
* :pull:`257` |DepletionReader| now can utilize
  :meth:`~serpentTools.DepletionReader.saveAsMatlab` for
  exporting data to a binary ``.mat`` file
* :pull:`259` Little more clarity into supported readers through documentation
  and |read-full| function

.. _v0.6.0:

:release-tag:`0.6.0`
====================

* :pull:`174` - Added parent object ``BaseObject`` with basic comparison
  method from which all objects inherit. Comparison method contains
  upper and lower bounds for values w/o uncertainties, :pull:`191`
* :pull:`196` - Add comparison methods for |ResultsReader| and
  |HomogUniv| objects
* :pull:`228` - Add comparison methods for |DetectorReader| and
  |Detector| objects
* :pull:`236` - Add comparison methods for |DepletionReader| and
  :class:`~serpentTools.objects.DepletedMaterial` objects
* :pull:`241` - Fix a bug in the CLI that rendered the ability to generate files with
  unique random seeds. ``python -m serpentTools seed <input> <N>`` can now be properly
  used.
* :pull:`249` - Better sparse support for depletion matrix, ``depmtx`` files with a
  |DepmtxReader|
* :pull:`252` - Better axis and colorbar labeling for |Detector| mesh plots
* :pull:`254` - Better plotting of single concentrations with |DepmtxReader|
* :pull:`255` - |DepletionReader| can capture material with underscores now!

.. _v0.6.0-dep:

Deprecations
------------

* :func:`~serpentTools.parsers.depmtx` is deprecated in favor of either
  :func:`~serpentTools.parsers.readDepmtx` or the class-based
  |DepmtxReader|

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
* :pull:`231` - |ResultsReader| objects can now read files that do not
  contain group constant data. The setting ``results-expectGcu`` should
  be used to inform the reader that no group constant data is anticipated

    .. note::

        This setting was removed in :ref:`v0.8.0` and in :pull:`324`

.. _v0.5.2:

:release-tag:`0.5.2`
====================

* :pull:`198` - Import test and example files using :mod:`serpentTools.data`.
  Load example readers with :func:`serpentTools.data.readDataFile`
* :pull:`199` - Support for structured or unstructured matrix plotting with
  :func:`serpentTools.plot.cartMeshPlot`
* :pull:`201` - Support for plotting hexagonal meshes with
  :meth:`serpentTools.objects.HexagonalDetector.hexPlot`
* :pull:`204` - Access |Detector|
  objects directly from |DetectorReader|
  with ``reader[detName]``
* :pull:`205` - Access materials from |DepletionReader|
  and :class:`serpentTools.samplers.DepletionSampler` using key-like
  indexing, e.g. ``reader[matName] == reader.material[matName]``
* :pull:`213` - Better default x-axis labels for simple Detector plots

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

* :pull:`189` - Support for reading Detectors with hexagonal, cylindrical, and
  spherical meshes.

.. _v0.5.1-api:

API Changes
-----------

* ``zzaaai`` data is stored on
  :attr:`~serpentTools.objects.DepletedMaterial.zai` as a list
  of integers, not strings

.. _v0.5.0:

:release-tag:`0.5.0`
====================

* :pull:`131` Updated variable groups between ``2.1.29`` and ``2.1.30`` - include
  poison cross section, kinetic parameters, six factor formula (2.1.30 exclusive),
  and minor differences
* :pull:`141` - Setting :ref:`xs-reshapeScatter` can be used to reshape scatter
  matrices on |HomogUniv|
  objects to square matrices
* :pull:`145` - :meth:`~serpentTools.objects.HomogUniv.hasData`
  added to check if |HomogUniv|
  objects have any data stored on them
* :pull:`146` - |HomogUniv| object
  stores group structure on the object. New dictionaries for storing group constant
  data that is not ``INF`` nor ``B1`` -
  :attr:`~serpentTools.objects.HomogUniv.gc` and
  :attr:`~serpentTools.objects.HomogUniv.gcUnc`
* :pull:`130` Added the ability to read results file
* :pull:`149` - Add the ability to read sensitivity files
* :pull:`161` - Add the :mod:`~serpentTools.utils` module
* :pull:`165` - Add the :meth:`serpentTools.objects.HomogUniv.plot`
  method

.. _v0.5.0-api:

API Changes
-----------

* :pull:`146` removed ``metadata`` dictionaries on |HomogUniv| objects.

.. _v0.5.0-dep:

Deprecation
-----------

* Variable group ``xs-yields`` is removed. Use ``poisons`` instead
* Branches of a single name are only be accessible through
  ``branches['nom']``, not ``branches[('nom'), ]`` as per :pull:`114`

.. _v0.4.0:

:release-tag:`0.4.0`
====================

* :pull:`95` Add ``xsplot`` file reader - |XSPlotReader|
* :pull:`121` Samplers will raise more warnings/errors if no files are loaded
  from ``*`` wildcards
* :pull:`122` Better Detector labeling
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
* :pull:`107` - |DepletionReader| can now plot data for some or all materials

.. _v0.2.2:

:release-tag:`0.2.2`
====================

* :pull:`82` - Command line interface and some sub-commands
* :pull:`88` - Pre- and post-check methods for readers
* :pull:`93` - Detector and Depletion Samplers
* :pull:`96` - Better mesh plotting for Detector
* :issue:`99` - Negative universe burnup with branching reader - :pull:`100`
* :attr:`serpentTools.objects.Detector.indexes` are now zero-indexed
* The PDF manual is no longer tracked in this repository
