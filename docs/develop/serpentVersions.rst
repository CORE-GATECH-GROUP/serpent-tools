.. |sss| replace:: ``SERPENT``  

.. |vars.yaml| replace:: ``serpentTools/variables.yaml``

.. _dev-sss-versions:

===================================
Adding Support for Serpent Versions
===================================

One of the main goals for this project is to include support for
more |sss| versions. The goal of this document is to detail what
steps are required in order to include support for additional
|sss| versions.

.. note::

    Supporting additional versions is an ongoing task. 
    See :issue:`117` and linked issues for updates

.. _dev-sss-versions-checklist:

Checklist
=========

#. Include the version as an option in the `serpentVersion` setting - :ref:`serpentVersion`
#. Update the :ref:`defaultSettings` using the script ``docs/rstDefaultSettings.py``
#. Update |vars.yaml| to include the version and any new variable groups
   present in the results files - :ref:`dev-sss-versions-newVars`
#. If |vars.yaml| is updated, update :ref:`variable-groups` using the script 
   ``docs/rstVariableGroups.py``

.. _dev-sss-versions-newVars:

New Variables
=============

As detailed in :ref:`variable-groups`, ``serpentTools`` utilizes a collection of
variable groups to expedite what data is extracted from results and branching files.
Some versions of |sss| may have different data, as more features are added to the code,
whiles some may have the same data with different names.
Variables and variable groups can be added to |vars.yaml| as sets.
Since the order of the variables present in the file is not important, and we are
simply interested in `if` a variable found in a file is in a group, the :py:class:`set`
provides a good framework for this inspection.

The basic structure of |vars.yaml| is given below for a single version::

    version
        |- group_0
            | - variable_0
            | - variable_1
             ...
        |- group_1
             | - variable_0
             | - variable_1
             ...
        ...

There is also a ``base`` version that serves as a catch-all, as detailed in
:ref:`dev-sss-versions-var-lookup`.

Variables are loaded from |vars.yaml| as nested dictionaries::

    variables = {
        version0: {group_0: {variable_0, variable_1, ...},
                   group_1: {variable_0, variable_1, ...},
                   ...
                  },
        version1: {group_0: {variable_0, variable_1, ...},
                   group_1: {variable_0, variable_1, ...},
                   ...
                  },
        ...
        }


.. _dev-sss-versions-var-lookup:

Variable Lookup Procedure
-------------------------

The lookup procedure for variable groups is as follows. 
For a specific |sss| version ``V`` and variable group ``g``,

* If the variable group is explicitly declared under ``variables[V]``, then take the 
   variables from ``variables[V][g]``
* If the group is declared under ``variables['base']``, then
   take the variables from ``variables['base'][g]``
* Otherwise, raise an error

The ``'base'`` serves to store variables that are invariant across all |sss| versions. 
As the development of |sss| progresses, it is not unlikely that the ``'base'`` group
may dwindle, as each version listed in |vars.yaml| expands.


Shared Variable Groups
----------------------

For variable groups that are similar between two versions but not contained in ``'base'``,
one can take advantage of 
`YAML anchors and aliases <http://yaml.org/spec/1.2/spec.html#id2765878>`_, implemented in
``PyYAML`` as ``&`` and ``*`` characters. An example of sharing a group between two versions
this way is given below::

    parentV:
      parentG: !!set &parentG
        {vx0, vx1, ...}
    childV:
      childG: *parentG

Loading such a file would return a dictionary like::

    {parentV: {parentG: {vx0, vx1, ...}},
     childV: {childV:{vx0, vx1, ...}}}


.. _dev-sss-versions-newFormats

Versions with New File Formats
==============================

In the event that a future version of |sss| causes substantial changes to the
layout of output files, such that present readers will not work, then 
version-specific read methods will have to be written.
If/when this happens, a procedure will be developed and added here.

MapStrVersions
----------------

This is a mapping variable located in the ResultsReader parser. 
The variable is a nested dictionary, where the keys describe the version and the nested
dictionary describes the various data blocks within the results file (_res.m). 

In general the results file is divided into three main blocks:
- metadata: general description of the simulation
- resdata: time-dependent values, e.g. k-eff
- universes: universe dependent values, such as cross-sections
The mapping through the variable `MapStrVersions` should reflect this. 

The basic mapping definition relies on the following structure:
MapStrVersions = {'2.1.29':                        	# serpent version
				   {'meta': 'VERSION',				# The starting keyword of the metadata block
					'rslt': 'MIN_MACROXS',          # The starting keyword of the resdata block
					'univ': 'GC_UNIVERSE_NAME',     # The starting keyword of the universes block
                    'days': 'BURN_DAYS', 			# A keyword used in Serpent to describe time, days
					'burn': 'BURNUP',               # A keyword used in Serpent to describe burnup, MWd/kgU
					'infxs': 'INF_',                # A prefix in Serpent used to describe infinite cross-sections
					'b1xs': 'B1_',					# A prefix in Serpent used to describe b1 cross-sections
                    'varsUnc': ['MICRO_NG', 'MICRO_E', 'MACRO_NG', 'MACRO_E']}} # Only the variables that have no uncertainties in the universe block
					
In order to support different serpent versions, these keywords would need to be updated.
							 


