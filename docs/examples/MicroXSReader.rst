.. |reader| replace:: :py:class:`~serpentTools.parsers.microxs.MicroXSReader`

.. |nfy| replace:: :py:attr:`~serpentTools.parsers.microxs.MicroXSReader.nfy`

.. |fluxRatio| replace:: :py:attr:`~serpentTools.parsers.microxs.MicroXSReader.fluxRatio`

.. |fluxUnc| replace:: :py:attr:`~serpentTools.parsers.microxs.MicroXSReader.fluxUnc`

.. |xsVal| replace:: :py:attr:`~serpentTools.parsers.microxs.MicroXSReader.xsVal`

.. |xsUnc| replace:: :py:attr:`~serpentTools.parsers.microxs.MicroXSReader.xsVal`

.. |getFY| replace::  :py:meth:`~serpentTools.parsers.microxs.MicroXSReader.getFY`

.. |getXS| replace::  :py:meth:`~serpentTools.parsers.microxs.MicroXSReader.getXS`

.. |settings| replace::  :py:class:`~serpentTools.settings.rc`

=============
MicroXSReader
=============

Basic Operation
---------------

This notebook demonstrates the capabilities of the 
`serpentTools <https://github.com/CORE-GATECH-GROUP/serpent-tools>`__
in regards to reading group micro cross-section files. SERPENT [1]
produces a `micro depletion
file <http://serpent.vtt.fi/mediawiki/index.php/Description_of_output_files#Micro_depletion_output>`__,
containing independent and cumulative fission yields as well as group
cross-sections for the isotopes and reactions defined by the user. The
`MicroXSReader` is capable of reading this file, and storing the data
directly on the |reader|. The reader has two methods to retrieve the data
and ease the analysis. Note: in order to obtain the micro depletion
files, the user must set the ``mdep`` card in the input
`file <http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual#set_mdep>`__.

.. code:: 

    import serpentTools
    from serpentTools.settings import rc

.. code:: 

    %time
    mdxFile = 'ref_mdx0.m'
    mdx = serpentTools.read(mdxFile)


.. parsed-literal::

    Wall time: 0 ns
    

The fission yields read in from the file are stored in |nfy|
dictionary, where the keys represent a specific (parent, energy) pair
and the corresponding values is a dictionary with fission products ids
and corresponding fission yield values.

.. code:: 

    # All the (parent, energy) pairs can be obtained by using '.keys()'
    pairs = mdx.nfy.keys()
    list(pairs)[0:5] # list only the first five pairs




.. parsed-literal::

    [(902270.0, 2.53e-08),
     (902280.0, 2.53e-08),
     (902280.0, 0.5),
     (902280.0, 14.0),
     (902290.0, 2.53e-08)]



Each pair represents the isotope undergoing fission and the impending
neutron energy in MeV.

.. code:: 

    pair = list(pairs)[0] # obtain the first (isotope, energy) pair
    print('Isotope= {: 1.0f}'.format(pair[0]))
    print('Energy= {} MeV'.format(pair[1]))


.. parsed-literal::

    Isotope=  902270
    Energy= 2.53e-08 MeV
    

The results for each pair are dictionaries that contain three fields:

``fissProd`` list of fission products ids

``indYield`` corresponding list of independent fission yields

``cumYield`` corresponding list of cumulative fission yields

.. code:: 

    # Obtain the keys in the nfy dictionary
    mdx.nfy[pair].keys()




.. parsed-literal::

    dict_keys(['fissProd', 'indYield', 'cumYield'])



.. code:: 

    # Print only the five first fission products
    print(mdx.nfy[pair]['fissProd'][0:5])


.. parsed-literal::

    [ 250660.  250670.  250680.  260660.  260670.]
    

.. code:: 

    # Print only the five first fission independent yields
    print(mdx.nfy[pair]['indYield'][0:5])


.. parsed-literal::

    [  6.97001000e-13   1.35000000e-13   1.01000000e-14   2.57000000e-10
       1.13000000e-10]
    

.. code:: 

    # Print only the five first fission cumulative yields
    print(mdx.nfy[pair]['cumYield'][0:5])


.. parsed-literal::

    [  6.97001000e-13   1.35000000e-13   1.01000000e-14   2.58000000e-10
       1.13000000e-10]
    

Fluxes ratios and uncertainties are stored in the |fluxRatio| and
|fluxUnc| dictionaries, where the keys represent a specific universe
and the corresponding values are group fluxes values.

.. code:: 

    # obtain the universes
    print(mdx.fluxRatio.keys())


.. parsed-literal::

    dict_keys(['0'])
    

Cross sections and their uncertainties are stored in the |xsVal| and
|xsUnc| dictionaries, where the keys represent a specific universe and
the corresponding values are dictionaries.

.. code:: 

    # The keys within the nested dictionary describe the isotope, reaction and special flag
    print(mdx.xsVal['0'].keys())


.. parsed-literal::

    dict_keys([(10010.0, 102.0, 0.0), (982490.0, 18.0, 0.0), (982510.0, 102.0, 0.0), (982510.0, 16.0, 0.0), (982510.0, 17.0, 0.0), (982510.0, 18.0, 0.0), (40090.0, 107.0, 0.0)])
    

Each key has three entries (isotope, reaction, flag)

``isotope`` ID of the isotope (ZZAAA0/1), int or float

``reaction`` MT
`reaction <http://serpent.vtt.fi/mediawiki/index.php/ENDF_reaction_MT%27s_and_macroscopic_reaction_numbers>`__,
e.g., 102 (n,gamma)

``flag`` special flag to describe isomeric state or fission yield
distribution number

For each such key (isotope, reaction, flag) the ``xsVal`` and ``xsVal``
store the group-wise flux values and uncertainties respectively.

.. code:: 

    val = mdx.xsVal['0']
    unc = mdx.xsUnc['0']

.. code:: 

    # Print flux values
    print(val[(10010, 102, 0)])


.. parsed-literal::

    [3.09753e-05, 3.33901e-05, 3.57054e-05, 3.70926e-05, 3.61049e-05, 3.39464e-05, 3.39767e-05, 3.98315e-05, 5.38962e-05, 7.96923e-05, 0.000118509, 0.000173915, 0.000254571, 0.00033854, 0.000452415, 0.00059819, 0.000769483, 0.00104855, 0.00131149, 0.0016779, 0.00215195, 0.00270125, 0.00344635, 0.00504611]
    

.. code:: 

    # Print flux uncertainties
    print(unc[(10010, 102, 0)])


.. parsed-literal::

    [0.00011, 2e-05, 1e-05, 0.0, 0.0, 0.0, 0.0, 1e-05, 1e-05, 2e-05, 2e-05, 2e-05, 2e-05, 1e-05, 1e-05, 2e-05, 2e-05, 3e-05, 2e-05, 3e-05, 4e-05, 5e-05, 0.00017, 0.00069]
    

Data Retrieval
--------------

The |reader| object has two ``get`` methods.

|getFY| method obtains the independent and cumulative fission yields
for a specific parent (ZZAAA0/1), daughter (ZZAAA0/1), neutron energy
(MeV). If no parent is found, the method raises an exception. However,
if no fission product is found, the method returns empty variables. The
method also has a special flag that indicates whether the user wants to
obtain the value corresponding to the nearest energy.

|getXS| method to obtain the group-wise cross-sections for a specific
universe, isotope and reaction.

.. code:: 

    indYield, cumYield = mdx.getFY(parent=922350, energy=2.53e-08, daughter=541350 )
    print('Independent yield = {}'.format(indYield))
    print('Cumulative yield = {}'.format(cumYield))


.. parsed-literal::

    Independent yield = [ 0.00078513]
    Cumulative yield = [ 0.065385]
    

By default, the method includes a flag that allows to obtain the values
for the closest energy defined by the user.

.. code:: 

    indYield, cumYield = mdx.getFY(parent=922350, energy=1e-06, daughter=541350 )
    print('Independent yield = {}'.format(indYield))
    print('Cumulative yield = {}'.format(cumYield))


.. parsed-literal::

    Independent yield = [ 0.00078513]
    Cumulative yield = [ 0.065385]
    

The user can set this boolean flag to False if only the values at
existing energies are of interest.

.. code:: 

    indYield, cumYield = mdx.getFY(parent=922350, energy=2.53e-08, daughter=541350, flagEnergy=False )

If the fission product does not exist then empty values are returned

.. code:: 

    indYield, cumYield = mdx.getFY(parent=922350, energy=1e-06, daughter=50000, flagEnergy=True)
    print('Independent yield = {}'.format(indYield))
    print('Cumulative yield = {}'.format(cumYield))


.. parsed-literal::

    Independent yield = []
    Cumulative yield = []
    

|getXS| method is used to obtain the group cross-sections for a
specific universe, isotope and reaction. The method returns the values
and uncertainties.

.. code:: 

    # Obtain the group cross-sections
    vals, unc = mdx.getXS(universe='0', isotope=10010, reaction=102)

.. code:: 

    # Print group flux values
    print(vals)


.. parsed-literal::

    [3.09753e-05, 3.33901e-05, 3.57054e-05, 3.70926e-05, 3.61049e-05, 3.39464e-05, 3.39767e-05, 3.98315e-05, 5.38962e-05, 7.96923e-05, 0.000118509, 0.000173915, 0.000254571, 0.00033854, 0.000452415, 0.00059819, 0.000769483, 0.00104855, 0.00131149, 0.0016779, 0.00215195, 0.00270125, 0.00344635, 0.00504611]
    

.. code:: 

    # Print group flux uncertainties values
    print(unc)


.. parsed-literal::

    [0.00011, 2e-05, 1e-05, 0.0, 0.0, 0.0, 0.0, 1e-05, 1e-05, 2e-05, 2e-05, 2e-05, 2e-05, 1e-05, 1e-05, 2e-05, 2e-05, 3e-05, 2e-05, 3e-05, 4e-05, 5e-05, 0.00017, 0.00069]
    

The method includes a special flag ``isomeric``, which is set to zero by
default. The special flag either describes the isomeric state or fission
yield distribution number.

.. code:: 

    # Example of how to use the isomeric flag
    vals, unc = mdx.getXS(universe='0', isotope=10010, reaction=102, isomeric=0)

If the universe exist, but the isotope or reaction do not exist, the
method returns empty values.

.. code:: 

    # Example of how to use the isomeric flag
    vals, unc = mdx.getXS(universe='0', isotope=922350, reaction=102, isomeric=0)
    print(vals)
    print(unc)


.. parsed-literal::

    []
    []
    

Settings
--------

The |reader| also has a collection of |settings| to control what
data is stored. If none of these settings are modified, the default is
to store all the data from the output file.

.. code:: 

    rc['microxs.getFY'] = False # True/False only
    rc['microxs.getXS'] = True # True/False only
    rc['microxs.getFlx'] = True # True/False only

:ref:`microxs-getFY`: True or False, store fission yields

:ref:`microxs-getXS`: True or False, store group cross-sections and
uncertainties

:ref:`microxs-getFlx`: True or False, store flux ratios and uncertainties

.. code:: 

    mdxFile = 'ref_mdx0.m'
    mdx = serpentTools.read(mdxFile)

.. code:: 

    # fission yields are not stored on the reader
    mdx.nfy.keys()




.. parsed-literal::

    dict_keys([])



Conclusion
----------

The |reader| is capable of reading and storing all the data
from the SERPENT micro depletion file. Yields, cross-sections and flux
ratios are stored on the reader. The reader also includes two methods
|getFY| and |getXS| to retrieve the data. Use of |settings|
control object allows increased control over the data selected from the
output file.

References
----------

1. J. Leppänen, M. Pusa, T. Viitanen, V. Valtavirta, and T.
   Kaltiaisenaho. "The Serpent Monte Carlo code: Status, development and
   applications in 2013." Ann. Nucl. Energy, `82 (2015)
   142-150 <https://www.sciencedirect.com/science/article/pii/S0306454914004095>`__
