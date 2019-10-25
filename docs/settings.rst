.. _settings:

Settings
========

Presented here are the various settings used by the
readers to control what data is stored and how the 
data is stored. There are specific settings for each reader, 
and those are of the form ``<leader>.<setting>``,
so :ref:`depletion-materials` is used only by the
:class:`~serpentTools.DepletionReader`.
Without modifying any settings, each reader defaults to storing all of the
data present in the output file.
Many of the settings instruct the readers to store specific data, such as
only materials present in :ref:`depletion-materials`.

Setting Control
---------------

.. currentmodule:: serpentTools.settings

Setting control is done using the :class:`rc` global. It acts largely
like a dictionary with some validation. 

.. class:: rc

    .. automethod:: rc.__getitem__

    .. automethod:: rc.__setitem__

    .. automethod:: rc.__enter__

The settings are explained below and are used by the readers to control
what data are stored when reading from files.

Shared Settings
---------------

There are some settings that are shared between some or all readers.
Any setting that does not have a ``.`` applies to all readers,
such as :ref:`verbosity`.
Below are a list of setting leaders and the readers impacted
by this setting:

====== =====================================
Leader
====== =====================================
``xs`` |ResultsReader| and |BranchingReader|
====== =====================================

Here are links to locations in the :ref:`examples` that display
how the settings can be used on the various readers.

================= =========================
Reader            Link to example
================= =========================
|BranchingReader| :ref:`branching-settings`
|DepletionReader| :ref:`depletion-settings`
================= =========================

.. _default-settings:

Default Settings
----------------

.. _branching-floatVariables:

``branching.floatVariables``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Names of state data variables to convert to floats for each branch::

  Default: []
  Type: list
  

.. _branching-intVariables:

``branching.intVariables``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Name of state data variables to convert to integers for each branch::

  Default: []
  Type: list
  

.. _depletion-materialVariables:

``depletion.materialVariables``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Names of variables to store. Empty list -> all variables::

  Default: []
  Type: list
  

.. _depletion-materials:

``depletion.materials``
~~~~~~~~~~~~~~~~~~~~~~~

Names of materials to store. Empty list -> all materials::

  Default: []
  Type: list
  

.. _depletion-metadataKeys:

``depletion.metadataKeys``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Non-material data to store, i.e. zai, isotope names, burnup schedule, etc::

  Default: ['ZAI', 'NAMES', 'DAYS', 'BU']
  Type: list
  Options: [ZAI, NAMES, DAYS, BU]

.. _depletion-processTotal:

``depletion.processTotal``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Option to store the depletion data from the TOT block::

  Default: True
  Type: bool
  

.. _detector-names:

``detector.names``
~~~~~~~~~~~~~~~~~~

List of detectors to store. Empty list -> store all detectors::

  Default: []
  Type: list
  

.. _microxs-getFY:

``microxs.getFY``
~~~~~~~~~~~~~~~~~

If true, store the fission yields::

  Default: True
  Type: bool
  

.. _microxs-getFlx:

``microxs.getFlx``
~~~~~~~~~~~~~~~~~~

If true, store the group flux ratios::

  Default: True
  Type: bool
  

.. _microxs-getXS:

``microxs.getXS``
~~~~~~~~~~~~~~~~~

If true, store the micro-group cross sections::

  Default: True
  Type: bool
  

.. _sampler-allExist:

``sampler.allExist``
~~~~~~~~~~~~~~~~~~~~

True if all the files should exist. Suppresses errors if a file does not exist::

  Default: True
  Type: bool
  

.. _sampler-freeAll:

``sampler.freeAll``
~~~~~~~~~~~~~~~~~~~

If true, do not retain data from parsers after reading. Limits memory usage after reading::

  Default: False
  Type: bool
  

.. _sampler-raiseErrors:

``sampler.raiseErrors``
~~~~~~~~~~~~~~~~~~~~~~~

If True, stop at the first error. Otherwise, continue reading but make a note about the error::

  Default: True
  Type: bool
  

.. _sampler-skipPrecheck:

``sampler.skipPrecheck``
~~~~~~~~~~~~~~~~~~~~~~~~

If True, no checks are performed prior to preparing data.
Set this to be True only if you know all files contain the same data as errors may arise::

  Default: False
  Type: bool
  

.. _serpentVersion:

``serpentVersion``
~~~~~~~~~~~~~~~~~~

Version of Serpent::

  Default: 2.1.31
  Type: str
  Options: [2.1.29, 2.1.30, 2.1.31]

.. _verbosity:

``verbosity``
~~~~~~~~~~~~~

Set the level of errors to be shown::

  Default: warning
  Type: str
  Options: [critical, error, warning, info, debug]

.. _xs-getB1XS:

``xs.getB1XS``
~~~~~~~~~~~~~~

If true, store the critical leakage cross sections::

  Default: True
  Type: bool
  

.. _xs-getInfXS:

``xs.getInfXS``
~~~~~~~~~~~~~~~

If true, store the infinite medium cross sections::

  Default: True
  Type: bool
  

.. _xs-reshapeScatter:

``xs.reshapeScatter``
~~~~~~~~~~~~~~~~~~~~~

If true, reshape the scattering matrices to square matrices. By default,
these matrices are stored as vectors::

  Default: False
  Type: bool
  

.. _xs-variableExtras:

``xs.variableExtras``
~~~~~~~~~~~~~~~~~~~~~

Full SERPENT name of variables to be read::

  Default: []
  Type: list
  

.. _xs-variableGroups:

``xs.variableGroups``
~~~~~~~~~~~~~~~~~~~~~

Name of variable groups from variables.yaml to be expanded into SERPENT
variable to be store::

  Default: []
  Type: list
