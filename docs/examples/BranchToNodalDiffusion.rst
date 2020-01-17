.. |BranchCol-tables| replace:: :attr:`~serpentTools.BranchCollector.xsTables`
.. |BranchCol-states| replace:: :attr:`~serpentTools.BranchCollector.states`
.. |BranchCol-perturbations| replace:: :attr:`~serpentTools.BranchCollector.perturbations`
.. |BranchCol-burnups| replace:: :attr:`~serpentTools.BranchCollector.burnups`
.. |BranchCol-axis| replace:: :attr:`~serpentTools.BranchCollector.axis`
.. |BranchCol-universes| replace:: :attr:`~serpentTools.BranchCollector.universes`
.. |BranchCol-univIndex| replace:: :attr:`~serpentTools.BranchCollector.univIndex`
.. |BranchedUniv| replace:: :class:`~serpentTools.xs.BranchedUniv`
.. |BranchedUniv-tables| replace:: :attr:`~serpentTools.xs.BranchedUniv.xsTables`
.. |BranchedUniv-states| replace:: :attr:`~serpentTools.xs.BranchedUniv.states`
.. |BranchedUniv-perturbations| replace:: :attr:`~serpentTools.xs.BranchedUniv.perturbations`

.. _branch-col-example:

.. note::

    Data files, like the one used in this example, are not included with the
    python distribution. They can be downloaded from the GitHub repository,
    and accessed after setting the ``SERPENT_TOOLS_DATA`` environment
    variable

.. code::

    >>> import os
    >>> branchFile = os.path.join(
    ...     os.environ["SERPENT_TOOLS_DATA"],
    ...     "demo.coe")

Coefficient file to nodal diffusion cross sections
==================================================

A recent feature of SERPENT is the ability to performing branching
calculations using the `automated burnup
sequence <http://serpent.vtt.fi/mediawiki/index.php/Automated_burnup_sequence>`__.
``serpentTools`` can read these coefficient files using the |BranchingReader|
This automated burnup sequence is ideal for generating group constant
data for nodal diffusion codes, that often include some multi-physics
features, criticality searches, or other control mechanisms. A
criticality search could be performed by tweaking the boron
concentration in the coolant or adjusting control rod insertions.
Similarly, some codes may include coupled TH analysis to convert power
profiles to temperature profiles and adjust cross sections accordingly.
Each code has a unique flavor for utilizing a set of group constants
across these perturbations, and this notebook will demonstrate using the
|BranchCollector| to gather and write a simple set of cross sections.

.. code:: 
    
    >>> import numpy
    >>> import serpentTools
    >>> from serpentTools.xs import BranchCollector
    >>> coe = serpentTools.read(branchFile)

This specific input file contained two perturbations: boron
concentration and fuel temperature. Boron concentration had three
branches: ``nom`` with no boron, then ``B1000`` and ``B750``, with 1000
and 750 ppm boron in coolant. Fuel temperature had a nominal branch at
900 K, with 1200 and 600 K perturbations as well. These can be confirmed
by observing the
:attr:`~serpentTools.BranchingReader.branches`
dictionary on the |BranchingReader|.

.. code:: 
    
    >>> list(coe.branches.keys())
    [('nom', 'nom'),
     ('B750', 'nom'),
     ('B1000', 'nom'),
     ('nom', 'FT1200'),
    ('B750', 'FT1200'),
     ('B1000', 'FT1200'),
     ('nom', 'FT600'),
     ('B750',
    'FT600'),
     ('B1000', 'FT600')]

Cross sections are spread out through this |BranchingReader| across
branches, burnup, and universes. The job of the |BranchCollector| is
to place that data into mutli-dimensional matrices that represent the
perturbations chosen by the user. A single group constant, say total
cross section, has unique values for each universe, at each burnup
point, for each perturbed state, and each energy group. Such a matrix
would then contain five dimensions for this case.

First, we create the |BranchCollector| from the |BranchingReader|
and instruct the reader what perturbations are present in the file. The
ordering is not important at this point, as it can be changed later.

.. code:: 
    
    >>> collector = BranchCollector(coe)
    >>> collector.collect(('BOR', 'TFU'))

Now we can inspect the perturbation states, |BranchCol-states| found by the
collector.

.. code:: 
    
    >>> collector.states
    (('B1000', 'B750', 'nom'), ('FT1200', 'FT600', 'nom'))

The group constants are stored in the |BranchCol-tables| dictionary. Here we
select the total cross section, ``infTot`` for further exploration.

.. code:: 
    
    >>> list(collector.xsTables.keys())
    ['infTot', 'infFiss', 'infS0', 'infS1',
     'infDiffcoef', 'b1Tot', 'b1Fiss', 'b1S0',
     'b1S1', 'b1Diffcoef']
    >>> infT = collector.xsTables['infTot']
    >>> infT.shape
    (5, 3, 3, 3, 2)

Five dimensions as mentioned above. But how are they ordered? Inspecting
the |BranchCol-axis| attribute tells us that the dimensions are universe, boron
concentration, fuel temperature, burnup, and energy group.

.. code:: 
    
    >>> collector.axis
    ('Universe', 'BOR', 'TFU', 'Burnup', 'Group')

The ordering of each of these dimensions is found by examining the
|BranchCol-univIndex|, |BranchCol-states| and |BranchCol-burnups| attributes.

.. code:: 
    
    >>> collector.univIndex
    (0, 10, 20, 30, 40)
    >>> collector.states
    (('B1000', 'B750', 'nom'), ('FT1200', 'FT600', 'nom'))
    >>> collector.burnups
    array([ 0.,  1., 10.])

For example, if we wanted the total cross section for universe 10, at
1000 ppm boron, nominal fuel temperature, and 10 MWd/kgU burnup, we
would request

.. code:: 
    
    >>> infT[1, 0, 2, 2]
    array([0.324746, 0.864346])

For this example, the scattering matrices were not reshaped from vectors
to matrices and we would observe slightly different behavior in the
``'Group'`` dimension.

.. code:: 
    
    >>> collector.xsTables['infS1'].shape
    (5, 3, 3, 3, 4)

Four items in the last axis as the vectorized matrix represents fast to
fast, fast to thermal, thermal to fast, and thermal to thermal
scattering.

.. code:: 
    
    >>> collector.xsTables['infS1'][1, 0, 2, 2]
    array([0.087809  , 0.00023068, 0.00073939, 0.123981  ])

Many nodal diffusion codes request group constants on a per universe
basis, or per assembly type. As we saw above, the first dimension of the
|BranchCol-tables| matrices corresponds to universe. One can view group
constants for specific universes with the |BranchCol-universes| dictionary.

.. code:: 
    
    >>> collector.universes
    {"0": <serpentTools.BranchedUniv at 0x7fb62f749a98>, 10:
    <serpentTools.BranchedUniv at 0x7fb62f731b88>, 20:
    <serpentTools.BranchedUniv at 0x7fb62f749e08>, 30:
    <serpentTools.BranchedUniv at 0x7fb62f749e58>, 40:
    <serpentTools.BranchedUniv at 0x7fb62f749ea8>}
    >>> u0 = collector.universes["0"]

These |BranchedUniv| objects store views into the underlying
collectors |BranchedUniv-tables| data corresponding to a single universe. The
structuring is identical to that of the collector, with the first axis
removed.

.. code:: 
    
    >>> u0.perturbations
    ('BOR', 'TFU')
    >>> u0.axis
    ('BOR', 'TFU', 'Burnup', 'Group')
    >>> u0.states
    (('B1000', 'B750', 'nom'), ('FT1200', 'FT600', 'nom'))

The contents of the |BranchedUniv-tables| dictionary are
:class:`numpy.array` views into the data stored on the 
collector.

.. code:: 
    
    >>> list(u0.xsTables.keys())
    ['infTot', 'infFiss', 'infS0', 'infS1',
     'infDiffcoef', 'b1Tot', 'b1Fiss', 'b1S0',
     'b1S1', 'b1Diffcoef']
    >>> u0Tot = u0.xsTables['infTot']
    >>> u0Tot.shape
    (3, 3, 3, 2)
    >>> u0Tot
    array([[[[0.313696, 0.544846],
             [0.311024, 0.617734],
             [0.313348, 0.614651]],
    
            [[0.313338, 0.54515 ],
             [0.310842, 0.618286],
             [0.31299 , 0.614391]],
    
             ...
    
            [[0.210873, 0.223528],
             [0.208646, 0.      ],
             [0.206532, 0.      ]]]])

.. _branch-col-change:

Changing perturbation values
----------------------------

The values of |BranchCol-states| and |BranchCol-perturbations| can be easily modified,
so long as the structures are preserved. For example, as the current
|BranchCol-states| are string values, and of equal perturbations (three boron
concentrations, three fuel temperatures), we can set the |BranchCol-states| to
be a single 2x3 array

.. code:: 
    
    >>> collector.states = numpy.array([
    ...     [1000, 750, 0], 
    ...     [1200, 600, 900]], 
    ...     dtype=float)
    >>> collector.states
    array([[1000.,  750.,    0.],
           [1200.,  600.,  900.]])

Some error checking is performed to make sure the passed perturbations
match the structure of the underlying data. Here, we attempt to pass the
wrong number of fuel temperature perturbations.

.. code:: 
    
    >>> try:
    ...     collector.states = numpy.array([
    ...         [1000, 750, 0],
    ...         [1200, 600],  # wrong
    ...     ])
    >>> except ValueError as ve:
    ...     print(str(ve))

    Current number of perturbations for state TFU is 3, not 2


If the specific perturbations were not known when creating the
collector, the value of |BranchCol-perturbations| can also be changed, with
similar error checking.

.. code:: 
    
    >>> collector.perturbations = ['boron conc', 'fuel temperature']
    >>> collector.perturbations
    ['boron conc', 'fuel temperature']
    >>> try:
    ...     collector.perturbations = ['boron', 'fuel', 'ctrl']  # wrong
    >>> except ValueError as ve:
    ...     print(str(ve))
    Current number of perturbations is 2, not 3

Example nodal diffusion writer
------------------------------

As each nodal diffusion code has it’s own required data structure,
creating a general writer is a difficult task. The intent with the
|BranchCollector| is to provide a framework where the data is readily
available, and such a writer can be created with ease. Here, an example
writer is demonstrated, one that writes each cross section. The writer
first writes a table of the perturbations at the top of the input file,
showing the ordering and values of the perturbations. Options are also
provided for controlling formatting.

The full file is available for download:
`nodal_writer.py <https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/develop/examples/nodal_writer.py>`_

.. code:: 
    
    >>> from nodal_writer import Writer
    >>> print(Writer.__doc__.strip())
    Class for writing an example cross section file.
    
    Parameters
    ----------
    collector: Collector
            Object that read the branching file and stored
    the cross sections
            along the perturbation vector
        xsPerLine: int
    Number of cross sections / group constants to write per line
        floatFmt: str
    Formattable string used when writing floating point values
        strFmt: str
    Formattable string used when writing the names of the perturbations
    xsRemap: None or dict
            Dictionary used to find a replacement name for
    cross sections when
            writing.  Between each cross section block, the
    name of cross
            section and group will be written as ``# {name} group
    {g}``.
            When ``xsRemap`` is ``None``, the names are ``mixedCase`` as
    they appear in ``HomogUniv`` objects, e.g.  ``'infTot'``,
    ``'diffCoeff'``, etc. If ``xsRemap`` is a dictionary, it can
            be used to
    write a different name. Passing ``{'infTot': 'Total
            cross section'}``
    would write ``'Total cross seciton'``
            instead of ``'infTot'``, but all
    other names would be unchanged.

    >>> writer = Writer(collector)
    >>> print(writer.write.__doc__.strip())
    Write the contents of a single universe
    
    Parameters
    ----------
    universe: int or key
                Key of universe that exists in
    ``self.collector``. Typically
                integer values of homogenized
    universes from coefficient file
            stream: None or str or writeable
    If ``None``, return a string containing what would have been
    written to file. If a string, then write to this file. Otherwise,
    ensure that the object has a ``write`` method and write to this
    object
            mode: {'a', 'w'}
                Write or append to file. Only
    needed if stream is a string
    
    >>> # write to a file "in memory"
    >>> out = writer.write(0)
    >>> print(out[:1000])
    # Cross sections for universe 0
    boron conc           1.00000000E+03
    7.50000000E+02 0.00000000E+00
    fuel temperature     1.20000000E+03
    6.00000000E+02 9.00000000E+02
    Burnup [MWd/kgU]     0.00000000E+00
    1.00000000E+00 1.00000000E+01
    # infTot group 1
     3.13696000E-01 3.11024000E-01
    3.13348000E-01 3.13338000E-01
     3.10842000E-01 3.12990000E-01 3.16730000E-01
    3.13987000E-01
     3.16273000E-01 3.13772000E-01 3.11335000E-01 3.13311000E-01
    3.13437000E-01 3.10967000E-01 3.13160000E-01 3.16688000E-01
     3.14245000E-01
    3.16392000E-01 2.08020000E-01 2.05774000E-01
     2.03646000E-01 2.07432000E-01
    2.05326000E-01 2.03533000E-01
     2.10873000E-01 2.08646000E-01 2.06532000E-01
    #
    infTot group 2
     5.44846000E-01 6.17734000E-01 6.14651000E-01 5.45150000E-01
    6.18286000E-01 6.14391000E-01 5.48305000E-01 6.21804000E-01
     6.18120000E-01
    5.41505000E-01 6.09197000E-01 6.08837000E-01
     5.42373000E-01 6.09192000E-01
    6.08756000E-01 5.45294000E-01
     6.12767000E-01 6.12985000E-01 2.28908000E-01
    1.07070000E-01
     0.00000000E+00 3.1
