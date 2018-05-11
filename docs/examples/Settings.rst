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
The full list of default settings can be found in :ref:`defaultSettings`.

Basic Usage
===========

The |rc| class acts as a dictionary, and updating a value is
as simple as

.. code:: 

    >> rc['verbosity'] = 'debug'
    DEBUG   : serpentTools: Updated setting verbosity to debug
    

The |rc| object automatically checks to make sure the value is of the
correct type, and is an allowable option, if given.

.. code:: 

    >>> try:
    ...     rc['depletion.metadataKeys'] = False
    ... except TypeError as te:
    ...     print(te)
    Setting depletion.metadataKeys should be of type 
    <class 'list'>, not <class 'bool'>
    >>> try:
    ...     rc['serpentVersion'] = '1.2.3'
    ... except KeyError as ke:
    ...     print(ke)
    "Setting serpentVersion is
    1.2.3
    and not one of the allowed options:
    ['2.1.29']"

The |rc| object can also be used inside a context manager to revert
changes.

.. code:: 

    >>> with rc:
    ...     rc['depletion.metadataKeys'] = ['ZAI', 'BU']
    >>>
    >>> rc['depletion.metadataKeys']
    >>> rc['verbosity'] = 'info'
    DEBUG   : serpentTools: Updated setting depletion.metadataKeys to ['ZAI', 'BU']
    DEBUG   : serpentTools: Updated setting depletion.metadataKeys to ['ZAI', 'NAMES', 'DAYS', 'BU']
    ['ZAI', 'NAMES', 'DAYS', 'BU']

.. _group-const-variables:

Group Constant Variables
========================

Two settings control what group constant data and what variables are
extracted from the results and coefficient files.

1. :ref:`xs-variableExtras`: Full ``SERPENT_STYLE`` variable names, i.e.
   ``INF_TOT``, ``FISSION_PRODUCT_DECAY_HEAT``
2. :ref:`xs-variableGroups`: Select keywords that represent blocks of
   common variables

These variable groups are stored in 
`variables.yaml <https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/develop/serpentTools/variables.yaml>`_
and rely upon the ``SERPENT`` version to properly expand the groups.

.. code:: 

    >>> rc['serpentVersion']
    '2.1.29'
    >>> rc['xs.variableGroups'] = ['kinetics', 'xs', 'diffusion']
    >>> rc['xs.variableExtras'] = ['XS_DATA_FILE_PATH']
    >>> varSet = rc.expandVariables()
    >>> print(sorted(varSet))
    ['ABS', 'ADJ_IFP_ANA_BETA_EFF', 'ADJ_IFP_ANA_LAMBDA', 'ADJ_IFP_GEN_TIME',
     'ADJ_IFP_IMP_BETA_EFF', 'ADJ_IFP_IMP_LAMBDA', 'ADJ_IFP_LIFETIME',
     'ADJ_IFP_ROSSI_ALPHA', 'ADJ_INV_SPD', 'ADJ_MEULEKAMP_BETA_EFF',
     'ADJ_MEULEKAMP_LAMBDA', 'ADJ_NAUCHI_BETA_EFF', 'ADJ_NAUCHI_GEN_TIME',
     'ADJ_NAUCHI_LAMBDA', 'ADJ_NAUCHI_LIFETIME', 'ADJ_PERT_BETA_EFF',
     'ADJ_PERT_GEN_TIME', 'ADJ_PERT_LIFETIME', 'ADJ_PERT_ROSSI_ALPHA', 'CAPT',
     'CHID', 'CHIP', 'CHIT', 'CMM_DIFFCOEF', 'CMM_DIFFCOEF_X', 'CMM_DIFFCOEF_Y',
     'CMM_DIFFCOEF_Z', 'CMM_TRANSPXS', 'CMM_TRANSPXS_X', 'CMM_TRANSPXS_Y',
     'CMM_TRANSPXS_Z', 'DIFFCOEF', 'FISS', 'FWD_ANA_BETA_ZERO',
     'FWD_ANA_LAMBDA', 'INVV', 'KAPPA', 'NSF', 'NUBAR', 'RABSXS', 'REMXS',
     'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'SCATT0', 'SCATT1',
     'SCATT2', 'SCATT3', 'SCATT4', 'SCATT5', 'SCATT6', 'SCATT7', 'TOT',
     'TRANSPXS', 'XS_DATA_FILE_PATH']


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
:py:meth:`~serpentTools.settings.UserSettingsLoader.loadYaml` method.
The file is structured with the names of settings as keys and the
desired setting value as the values.
The loader also attempts to expand nested settings, like reader-specific
settings, that may be lumped in a second level.

.. code:: yaml

    verbosity: warning
    xs.getInfXS: False
    branching:
        areUncsPresent: False
        floatVariables: [Fhi, Blo]
    depletion:
        materials: [fuel*]
        materialVariables:
            [ADENS, MDENS, VOLUME]

