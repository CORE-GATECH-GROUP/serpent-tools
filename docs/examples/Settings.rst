.. |rc| replace:: :py:class:`~serpentTools.settings.rc`

.. _settings-ex:

============
User Control
============

The ``serpentTools`` package is designed to, without intervention, be able to store all the
data contained in each of the various output files. However, the
:py:mod:`serpentTools.settings` module grants great flexibility to the user
over what data is obtained through the
`rc <https://unix.stackexchange.com/questions/3467/what-does-rc-in-bashrc-stand-for>`_
class. 

All the settings are given in :ref:`default-settings` 
showing their default values and possible options.

Basic Usage
-----------

.. code:: 
    
    >>> import serpentTools
    >>> from serpentTools.settings import rc

The |rc| object can be used like a dictionary, polling all possible settings
with the ``.keys`` method.
.. code:: 
    
    >>> rc.keys()


.. parsed-literal::
 

    dict_keys(['depletion.processTotal', 'verbosity', 'xs.getInfXS',
    'branching.intVariables', 'branching.areUncsPresent', 'serpentVersion',
    'sampler.raiseErrors', 'xs.getB1XS', 'xs.variableGroups', 'xs.variableExtras',
    'depletion.materialVariables', 'depletion.metadataKeys', 'sampler.freeAll',
    'sampler.allExist', 'depletion.materials', 'sampler.skipPrecheck',
    'xs.reshapeScatter', 'branching.floatVariables', 'detector.names'])

Settings such as :ref:`depletion-materials` are specific for the
:py:class:`~serpentTools.parsers.depletion.DepletionReader`, 
while settings that are led with ``xs`` are sent to
the :py:class:`~serpentTools.parsers.results.ResultsReader` and 
:py:class:`~serpentTools.parsers.branching.BranchingReader` as well as their specific
settings.
Updating a setting is similar to setting a value in a dictionary

.. code:: 
    
    >>> rc['verbosity'] = 'debug'


.. parsed-literal::
 

    DEBUG   : serpentTools: Updated setting verbosity to debug


The ``rc`` object automatically checks to make sure the value is of the
correct type, and is an allowable option, if given.

.. code:: 
    
    >>> try:
    ...     rc['depletion.metadataKeys'] = False
    >>> except TypeError as te:
    ...     print(te)


.. parsed-literal::
 

    Setting depletion.metadataKeys should be of type <class 'list'>, not <class
    'bool'>


.. code:: 
    
    >>> try:
    ...     rc['serpentVersion'] = '1.2.3'
    >>> except KeyError as ke:
    ...     print(ke)


.. parsed-literal::
 

    'Setting serpentVersion is 1.2.3 and not one of the allowed options: 2.1.29,
    2.1.30'


The ``rc`` module can also be used inside a context manager to revert
changes.

.. code:: 
    
    >>> with rc:
    ...     rc['depletion.metadataKeys'] = ['ZAI', 'BU']
    ...     
    >>> rc['depletion.metadataKeys']
    >>> rc['verbosity'] = 'info'


.. parsed-literal::
 

    DEBUG   : serpentTools: Updated setting depletion.metadataKeys to ['ZAI', 'BU']
    DEBUG   : serpentTools: Updated setting depletion.metadataKeys to ['ZAI',
    'NAMES', 'DAYS', 'BU']

.. _group-const-variables:

Group Constant Variables
========================

Two settings control what group constant data and what variables are
extracted from the results and coefficient files.

1. :ref:`xs-variableExtras`: Full ``SERPENT_STYLE`` variable names, i.e.
   ``INF_TOT``, ``FISSION_PRODUCT_DECAY_HEAT``
2. :ref:`xs-variableGroups`: Select keywords that represent blocks of
   common variables

These variable groups are described in :ref:`varialble-groups` 
and rely upon the ``SERPENT`` version to properly expand the groups.


.. code:: 
    
    >>> rc['serpentVersion']

.. parsed-literal::
 

    '2.1.29'

.. code:: 
    
    >>> rc['xs.variableGroups'] = ['kinetics', 'xs', 'diffusion']
    >>> rc['xs.variableExtras'] = ['XS_DATA_FILE_PATH']
    >>> varSet = rc.expandVariables()
    >>> print(sorted(varSet))


.. parsed-literal::
 

    ['ABS', 'ADJ_IFP_ANA_BETA_EFF', 'ADJ_IFP_ANA_LAMBDA', 'ADJ_IFP_GEN_TIME',
    'ADJ_IFP_IMP_BETA_EFF', 'ADJ_IFP_IMP_LAMBDA', 'ADJ_IFP_LIFETIME',
    'ADJ_IFP_ROSSI_ALPHA', 'ADJ_INV_SPD', 'ADJ_MEULEKAMP_BETA_EFF',
    'ADJ_MEULEKAMP_LAMBDA', 'ADJ_NAUCHI_BETA_EFF', 'ADJ_NAUCHI_GEN_TIME',
    'ADJ_NAUCHI_LAMBDA', 'ADJ_NAUCHI_LIFETIME', 'ADJ_PERT_BETA_EFF',
    'ADJ_PERT_GEN_TIME', 'ADJ_PERT_LIFETIME', 'ADJ_PERT_ROSSI_ALPHA', 'BETA_EFF',
    'CAPT', 'CHID', 'CHIP', 'CHIT', 'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X',
    'CMM_DIFFCOEF_Y', 'CMM_DIFFCOEF_Z', 'CMM_TRANSPXS', 'CMM_TRANSPXS_X',
    'CMM_TRANSPXS_Y', 'CMM_TRANSPXS_Z', 'DIFFCOEF', 'FISS', 'FWD_ANA_BETA_ZERO',
    'FWD_ANA_LAMBDA', 'INVV', 'KAPPA', 'LAMBDA', 'NSF', 'NUBAR', 'RABSXS', 'REMXS',
    'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'SCATT0', 'SCATT1', 'SCATT2',
    'SCATT3', 'SCATT4', 'SCATT5', 'SCATT6', 'SCATT7', 'TOT', 'TRANSPXS',
    'XS_DATA_FILE_PATH']

However, one might see that the full group constant cross sections are
not present in this set

.. code:: 

    >>> assert 'INF_SCATT3' not in varSet

This is because two additional settings instruct the
:py:class:`~serpentTools.parsers.branching.BranchingReader`
and :py:class:`~serpentTools.parsers.results.ResultsReader` to obtain
infinite medium and leakage-corrected
cross sections: :ref:`xs-getInfXS` and :ref:`xs-getB1XS`, respectively. 
By default, :ref:`xs-getInfXS` and :ref:`xs-getB1XS` default to True. This, in
conjunction with leaving the :ref:`xs-variableExtras` and
:ref:`xs-variableGroups` settings to empty lists, instructs these readers
to obtain all the data present in their respective files.

See the :ref:`branching-ex` example for more information on using these
settings to control scraped data.

.. _conf-files:

Configuration Files
===================

The |rc| object allows for settings to be updated
from a yaml configuration file using the
:py:meth:`~serpentTools.settings.rc.loadYaml` method.
The file is structured with the names of settings as keys and the
desired setting value as the values.
The loader also attempts to expand nested settings, like reader-specific
settings, that may be lumped in a second level.

::

    verbosity: warning
    xs.getInfXS: False

However, the loader can also expand a nested dictionary structure, as

::

    branching:
      areUncsPresent: False
      floatVariables: [Fhi, Blo]
    depletion:
      materials: [fuel*]
      materialVariables:
        [ADENS, MDENS, VOLUME]

.. code:: 
    
    >>> %cat myConfig.yaml


.. parsed-literal::
 

    xs.getInfXS: False
    xs.getB1XS: True
    xs.variableGroups: [gc-meta, kinetics,
    xs]
    branching:
      areUncsPresent: False
      floatVariables: [Fhi, Blo]
    depletion:
      materials: [fuel*]
      metadataKeys: [NAMES, BU]
    materialVariables:
        [ADENS, MDENS, VOLUME]
    serpentVersion: 2.1.29


.. code:: 
    
    >>> myConf = 'myConfig.yaml'
    >>> rc.loadYaml(myConf)
    >>> rc['branching.areUncsPresent']

.. parsed-literal::
 

    INFO    : serpentTools: Done

.. parsed-literal::
 

    False

