.. _settings-ex:

============
User Control
============

The ``serpentTools`` package is designed to, without intervention, be able to store all the
data contained in each of the various output files. However, the
:py:mod:`serpentTools.settings` module grants great flexibility to the user
over what data is obtained through the
```rc`` <https://unix.stackexchange.com/questions/3467/what-does-rc-in-bashrc-stand-for>`_
class. This notebook will provide as an intro into using this class.

Basic Usage
===========

.. code:: ipython3

    >>> import serpentTools
    >>> from serpentTools.settings import rc, defaultSettings
    INFO    : serpentTools: Using version 1.0b0+24.g23e6eac.dirty

Below are the default values for each setting available

.. code:: ipython3

    >>> for setting in sorted(defaultSettings.keys()):
    >>>     print(setting)
    >>>     for key in defaultSettings[setting]:
    >>>         print('\t', key, '-', defaultSettings[setting][key])
    depletion.materialVariables
         default - []
         description - Names of variables to store. Empty list -> all variables.
         type - <class 'list'>
    depletion.materials
         default - []
         description - Names of materials to store. Empty list -> all materials.
         type - <class 'list'>
    depletion.metadataKeys
         default - ['ZAI', 'NAMES', 'DAYS', 'BU']
         description - Non-material data to store, i.e. zai, isotope names, burnup schedule, etc.
         type - <class 'list'>
         options - default
    depletion.processTotal
         default - True
         description - Option to store the depletion data from the TOT block
         type - <class 'bool'>
    serpentVersion
         default - 2.1.29
         description - Version of SERPENT
         type - <class 'str'>
         options - ['2.1.29']
    verbosity
         default - warning
         type - <class 'str'>
         description - Set the level of errors to be shown.
         updater - <function updateLevel at 0x000001B7F3DD6598>
         options - ['critical', 'error', 'warning', 'info', 'debug']
    xs.variableExtras
         default - []
         description - Full SERPENT name of variables to be read
         type - <class 'list'>
    xs.variableGroups
         default - []
         description - Name of variable groups from variables.yaml to be expanded into SERPENT variable to be stored
         type - <class 'list'>

Settings such as ``depletion.materialVariables`` are specific for the
``DepletionReader``, while settings that are led with ``xs`` are sent to
the ``ResultsReader`` and ``BranchingReader``, as well as their specific
settings. The ``rc`` class acts as a dictionary, and updating a value is
as simple as

.. code:: ipython3

    >> rc['verbosity'] = 'debug'
    DEBUG   : serpentTools: Updated setting verbosity to debug
    

The ``rc`` object automatically checks to make sure the value is of the
correct type, and is an allowable option, if given.

.. code:: ipython3

    >>> try:
    >>>     rc['depletion.metadataKeys'] = False
    >>> except TypeError as te:
    >>>     print(te)
    Setting depletion.metadataKeys should be of type <class 'list'>, not <class 'bool'>
    >>> try:
    >>>     rc['serpentVersion'] = '1.2.3'
    >>> except KeyError as ke:
    >>>     print(ke)
    "Setting serpentVersion is
    1.2.3
    and not one of the allowed options:
    ['2.1.29']"

The ``rc`` object can also be used inside a context manager to revert
changes.

.. code:: ipython3

    >>> with rc:
    >>>     rc['depletion.metadataKeys'] = ['ZAI', 'BU']
    >>>
    >>> rc['depletion.metadataKeys']
    DEBUG   : serpentTools: Updated setting depletion.metadataKeys to ['ZAI', 'BU']
    DEBUG   : serpentTools: Updated setting depletion.metadataKeys to ['ZAI', 'NAMES', 'DAYS', 'BU']
    ['ZAI', 'NAMES', 'DAYS', 'BU']
