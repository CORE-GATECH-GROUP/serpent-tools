.. |nfy| replace:: :attr:`~serpentTools.MicroXSReader.nfy`
.. |fluxRatio| replace:: :attr:`~serpentTools.MicroXSReader.fluxRatio`
.. |fluxUnc| replace:: :attr:`~serpentTools.MicroXSReader.fluxUnc`
.. |xsVal| replace:: :attr:`~serpentTools.MicroXSReader.xsVal`
.. |xsUnc| replace:: :attr:`~serpentTools.MicroXSReader.xsVal`
.. |getFY| replace::  :meth:`~serpentTools.MicroXSReader.getFY`
.. |getXS| replace::  :meth:`~serpentTools.MicroXSReader.getXS`

.. _ex-microXS:

.. note::

    Data files, like the one used in this example, are not included with the
    python distribution. They can be downloaded from the GitHub repository,
    and accessed after setting the ``SERPENT_TOOLS_DATA`` environment
    variable

.. code::

    >>> import os
    >>> mdxFile = os.path.join(
    ...     os.environ["SERPENT_TOOLS_DATA"],
    ...     "ref_mdx0.m")

==========================
Micro cross section reader
==========================

Basic Operation
---------------

This notebook demonstrates the capabilities of the
`serpentTools <https://github.com/CORE-GATECH-GROUP/serpent-tools>`__
in regards to reading group micro cross-section files. SERPENT [1]
produces a `micro depletion
file <http://serpent.vtt.fi/mediawiki/index.php/Description_of_output_files#Micro_depletion_output>`__,
containing independent and cumulative fission yields as well as group
cross-sections for the isotopes and reactions defined by the user. The
|MicroXSReader| is capable of reading this file, and storing the data
directly on the reader. The |MicroXSReader| has two methods to retrieve the data
and ease the analysis. Note: in order to obtain the micro depletion
files, the user must set the ``mdep`` card in the input
`file <http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual#set_mdep>`__.

.. code:: 
    
    >>> import serpentTools
    >>> mdx = serpentTools.read(mdxFile)

The fission yields read in from the file are stored in the |nfy|
dictionary, where the keys represent a specific (parent, energy) pair
and the corresponding values is a dictionary with fission products ids
and corresponding fission yield values.

.. code:: 
    
    >>> # All the (parent, energy) pairs can be obtained by using '.keys()'
    >>> pairs = mdx.nfy.keys()
    >>> list(pairs)[0:5] # list only the first five pairs
    [(902270, 2.53e-08),
     (902280, 2.53e-08),
     (902280, 0.5),
     (902280, 14.0),
     (902290, 2.53e-08)]

Each pair represents the isotope undergoing fission and the impending
neutron energy in MeV.

.. code:: 
    
    >>> pair = list(pairs)[0] # obtain the first (isotope, energy) pair
    >>> print('Isotope= {: 1.0f}'.format(pair[0]))
    Isotope=  902270
    >>> print('Energy= {} MeV'.format(pair[1]))
    Energy= 2.53e-08 MeV

The results for each pair are dictionaries that contain three fields:

1. ``fissProd`` list of fission products ids
2. ``indYield`` corresponding list of independent fission yields
3. ``cumYield`` corresponding list of cumulative fission yields

.. code:: 
    
    >>> # Obtain the keys in the nfy dictionary
    >>> mdx.nfy[pair].keys()
    dict_keys(['fissProd', 'indYield', 'cumYield'])
    >>> # Print only the five first fission products
    >>> print(mdx.nfy[pair]['fissProd'][0:5])
    [ 250660.  250670.  250680.  260660.  260670.]
    >>> # Print only the five first fission independent yields
    >>> print(mdx.nfy[pair]['indYield'][0:5])
    [  6.97001000e-13   1.35000000e-13   1.01000000e-14   2.57000000e-10
    1.13000000e-10]
    >>> # Print only the five first fission cumulative yields
    >>> print(mdx.nfy[pair]['cumYield'][0:5])
    [  6.97001000e-13   1.35000000e-13   1.01000000e-14   2.58000000e-10
    1.13000000e-10]

Fluxes ratios and uncertainties are stored in the |fluxRatio| and
|fluxUnc| dictionaries, where the keys represent a specific universe
and the corresponding values are group fluxes values.

.. code:: 
    
    >>> # obtain the universes
    >>> print(mdx.fluxRatio.keys())
    dict_keys(['0'])

Cross sections and their uncertainties are stored in the |xsVal| and
|xsUnc| dictionaries, where the keys represent a specific universe and
the corresponding values are dictionaries.
The keys within the nested dictionary describe the isotope, reaction and special flag::

    >>> print(mdx.xsVal['0'].keys())
    dict_keys([(10010, 102, 0), (982490, 18, 0), (982510, 102, 0), (982510, 16, 0),
    (982510, 17, 0), (982510, 18, 0), (40090, 107, 0)])

Each key has three entries (isotope, reaction, flag)

1. ``isotope`` ID of the isotope (ZZAAA0/1), int or float
2. ``reaction`` MT
`reaction <http://serpent.vtt.fi/mediawiki/index.php/ENDF_reaction_MT%27s_and_macroscopic_reaction_numbers>`__,
e.g., 102 (n,gamma)
3. ``flag`` special flag to describe isomeric state or fission yield distribution number

For each such key (isotope, reaction, flag) the ``xsVal`` and ``xsVal``
store the group-wise flux values and uncertainties respectively.

.. code:: 
    
    >>> val = mdx.xsVal['0']
    >>> unc = mdx.xsUnc['0']
    >>> # Print flux values
    >>> print(val[(10010, 102, 0)])
    [  3.09753000e-05   3.33901000e-05   3.57054000e-05   3.70926000e-05
    3.61049000e-05   3.39464000e-05   3.39767000e-05   3.98315000e-05
    5.38962000e-05   7.96923000e-05   1.18509000e-04   1.73915000e-04
    2.54571000e-04   3.38540000e-04   4.52415000e-04   5.98190000e-04
    7.69483000e-04   1.04855000e-03   1.31149000e-03   1.67790000e-03
    2.15195000e-03   2.70125000e-03   3.44635000e-03   5.04611000e-03]
    >>> # Print flux uncertainties
    >>> print(unc[(10010, 102, 0)])
    [  1.10000000e-04   2.00000000e-05   1.00000000e-05   0.00000000e+00
    0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e-05
    1.00000000e-05   2.00000000e-05   2.00000000e-05   2.00000000e-05
    2.00000000e-05   1.00000000e-05   1.00000000e-05   2.00000000e-05
    2.00000000e-05   3.00000000e-05   2.00000000e-05   3.00000000e-05
    4.00000000e-05   5.00000000e-05   1.70000000e-04   6.90000000e-04]

Data Retrieval
--------------

The |MicroXSReader| object has two ``get`` methods:
1. |getFY| method obtains the independent and cumulative fission yields
for a specific parent (ZZAAA0/1), daughter (ZZAAA0/1), neutron energy
(MeV). If no parent or daaughter is found, the method raises an
exception. The method also has a special flag that indicates whether the
user wants to obtain the value corresponding to the nearest energy.
2. |getXS| method to obtain the group-wise cross-sections for a specific
universe, isotope and reaction.

.. code:: 
    
    >>> indYield, cumYield = mdx.getFY(parent=922350, energy=2.53e-08, daughter=541350 )
    >>> print('Independent yield = {}'.format(indYield))
    Independent yield = 0.000785125
    >>> print('Cumulative yield = {}'.format(cumYield))
    Cumulative yield = 0.065385

By default, the method includes a flag that allows to obtain the values
for the closest energy defined by the user.

.. code:: 
    
    >>> indYield, cumYield = mdx.getFY(parent=922350, energy=1e-06, daughter=541350 )
    >>> print('Independent yield = {}'.format(indYield))
    Independent yield = 0.000785125
    >>> print('Cumulative yield = {}'.format(cumYield))
    Cumulative yield = 0.065385

The user can set this boolean flag to False if only the values at
existing energies are of interest.

.. code:: 
    
    >>> indYield, cumYield = mdx.getFY(parent=922350, energy=2.53e-08, daughter=541350, flagEnergy=False )

|getXS| method is used to obtain the group cross-sections for a
specific universe, isotope and reaction. The method returns the values
and uncertainties.

.. code:: 
    
    >>> # Obtain the group cross-sections
    >>> vals, unc = mdx.getXS(universe='0', isotope=10010, reaction=102)
    >>> # Print group flux values
    >>> print(vals)
    [  3.09753000e-05   3.33901000e-05   3.57054000e-05   3.70926000e-05
    3.61049000e-05   3.39464000e-05   3.39767000e-05   3.98315000e-05
    5.38962000e-05   7.96923000e-05   1.18509000e-04   1.73915000e-04
    2.54571000e-04   3.38540000e-04   4.52415000e-04   5.98190000e-04
    7.69483000e-04   1.04855000e-03   1.31149000e-03   1.67790000e-03
    2.15195000e-03   2.70125000e-03   3.44635000e-03   5.04611000e-03]
    >>> # Print group flux uncertainties values
    >>> print(unc)
    [  1.10000000e-04   2.00000000e-05   1.00000000e-05   0.00000000e+00
    0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e-05
    1.00000000e-05   2.00000000e-05   2.00000000e-05   2.00000000e-05
    2.00000000e-05   1.00000000e-05   1.00000000e-05   2.00000000e-05
    2.00000000e-05   3.00000000e-05   2.00000000e-05   3.00000000e-05
    4.00000000e-05   5.00000000e-05   1.70000000e-04   6.90000000e-04]

The method includes a special flag ``isomeric``, which is set to zero by
default. The special flag either describes the isomeric state or fission
yield distribution number.

.. code:: 
    
    >>> # Example of how to use the isomeric flag
    >>> vals, unc = mdx.getXS(universe='0', isotope=10010, reaction=102, isomeric=0)

If the universe exist, but the isotope or reaction do not exist, the
method raises an error.

Settings
--------

The |MicroXSReader| also has a collection of |rc| to control what
data is stored. If none of these settings are modified, the default is
to store all the data from the output file.

.. code:: 
    
    >>> from serpentTools.settings import rc
    >>> rc['microxs.getFY'] = False # True/False only
    >>> rc['microxs.getXS'] = True # True/False only
    >>> rc['microxs.getFlx'] = True # True/False only

- :ref:`microxs-getFY`: True or False, store fission yields
- :ref:`microxs-getXS`: True or False, store group cross-sections and
  uncertainties
- :ref:`microxs-getFlx`: True or False, store flux ratios and uncertainties

.. code:: 
    
    >>> mdx = serpentTools.read(mdxFile)
    >>> # fission yields are not stored on the reader
    >>> mdx.nfy.keys()
    dict_keys([])

Conclusion
----------

The |MicroXSReader| is capable of reading and storing all the data
from the SERPENT micro depletion file. Fission yields, cross-sections
and flux ratios are stored on the reader. The reader also includes two
methods |getFY| and |getXS| to retrieve the data. Use of |rc|
settings control object allows increased control over the data selected
from the output file.

References
----------

1. J. Leppänen, M. Pusa, T. Viitanen, V. Valtavirta, and T.
   Kaltiaisenaho. "The Serpent Monte Carlo code: Status, development and
   applications in 2013." Ann. Nucl. Energy, `82 (2015)
   142-150 <https://www.sciencedirect.com/science/article/pii/S0306454914004095>`__
