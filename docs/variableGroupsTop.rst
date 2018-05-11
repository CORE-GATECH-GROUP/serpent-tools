.. |Branching| replace:: :py:class:`~serpentTools.parsers.branching.BranchingReader`

.. |Results| replace:: :py:class:`~serpentTools.parsers.results.ResultsReader`

.. |Serpent| replace:: ``SERPENT``

.. _variable-groups:

===============
Variable Groups
===============

The |Branching| and |Results| can also be used to store cross sections 
and other group constant data on
:py:class:`~serpentTools.objects.containers.HomogUniv` objects.
The group constants to be stored are controlled by two distinct settings:
:ref:`xs-variableExtras` and :ref:`xs-variableGroups`.
The former includes the names of |Serpent| variables *exactly* how they
appear in the specific output file.
The latter variables that are commonly grouped together, such
as kinetic parameters or general cross sections, without having to exactly
specify the names of each variable.
Without adjusting these settings, the |Branching| and |Results| will store all data
present in the file.

Below are the various variable groups that can be used in the 
:ref:`xs-variableGroups` setting. These groups follow an inheritance-like 
pattern. For example, using |Serpent| 2.1.29, any group not directly placed
in the :ref:`vars-2-1-29` block, such as `eig`, will be replaced by those
variables present in the :ref:`vars-base` block. 

Below are the variable groups that correspond to each version of |Serpent|
supported by this project. Under each block, such as :ref:`diffusion-2-1-29`, 
are the original ``SERPENT_STYLE_VARIABLES`` and their corresponding
variable names converted to ``mixedCaseNames``. This conversion is done
to fit the style of the project and reduce a few keystrokes for accessing
variable names.

.. note::
    
    Variable  group ``xs-yields`` will be deprecated in favor of 
    ``poisons`` at version ``0.5.0`` :ref:`vDeprecated`. Both groups exist now and
    contain identical variables. 

.. include:: ./variableGroups.rst

