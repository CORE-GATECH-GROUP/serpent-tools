.. |branchReader| replace:: :py:class:`~serpentTools.parsers.branching.BranchingReader`

.. |branchContainer| replace:: :py:class:`~serpentTools.objects.containers.BranchContainer`

.. |homogUniv| replace:: :py:class:`~serpentTools.objects.containers.HomogUniv`

.. _branching-ex:

Branching Reader
================


This notebook demonstrates the capability of the
`serpentTools <https://github.com/CORE-GATECH-GROUP/serpent-tools>`_
package to read branching coefficient files. The format of these files
is structured to iterate over:

1. Branch states, e.g. burnup, material properties
2. Homogenized universes
3. Group constant data

The output files are described in more detail on the 
`SERPENT Wiki <http://serpent.vtt.fi/mediawiki/index.php/Automated_burnup_sequence#Output_format>`_

Basic Operation
---------------

The simplest way to read these files is using the 
:py:func:`serpentTools.parsers.read` function

.. note::

    Without modifying the settings, the
    :py:class:`~serpentTools.parsers.branching.BranchingReader` assumes that all
    group constant data is presented without the associated uncertainties.
    See :ref:`branching-settings` for examples on the various ways to
    control operation

.. code:: 

    >>> import serpentTools
    >>> branchFile = 'demo.coe'
    >>> r0 = serpentTools.read(branchFile)
    INFO    : serpentTools: Inferred reader for demo.coe: BranchingReader
    INFO    : serpentTools: Preparing to read demo.coe
    INFO    : serpentTools: Done reading branching file

The branches are stored in custom |branchContainer| objects in the
:py:attr:`~serpentTools.parsers.branching.BranchingReader.branches`
dictionary

.. code:: 

    >>> r0.branches
    {('B1000', 'FT1200'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8d8c9b00>,
     ('B1000', 'FT600'):
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8cfecfd0>,
     ('B1000', 'nom'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8d052b00>,
     ('B750', 'FT1200'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8d8cc400>,
     ('B750', 'FT600'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8cfe58d0>,
     ('B750', 'nom'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8d041470>,
     ('nom', 'FT1200'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8cfda208>,
     ('nom', 'FT600'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8cfdf1d0>,
     ('nom', 'nom'): 
        <serpentTools.objects.containers.BranchContainer at 0x7f2c8d03eda0>}

Here, the keys are tuples of strings indicating what
perturbations/branch states were applied for each ``SERPENT`` solution.
Examining a particular case

.. code:: 

    >>> b0 = r0.branches['B1000', 'FT600']
    >>> print(b0)
    <BranchContainer for B1000, FT600 from demo.coe>
    

``SERPENT`` allows the user to define variables for each branch through:

::

    var V1_name V1_value

cards. These are stored in the 
:py:attr:`~serpentTools.objects.containers.BranchContainer.stateData` 
attribute

.. code:: 

    >>> b0.stateData
    {'BOR': '1000',
     'DATE': '17/12/19',
     'TFU': '600',
     'TIME': '09:48:54',
     'VERSION': '2.1.29'}

The keys ``'DATE'``, ``'TIME'``, and ``'VERSION'`` are included by
default in the output, while the ``'BOR'`` and ``'TFU'`` have been
defined for this branch.

Group Constant Data
~~~~~~~~~~~~~~~~~~~

.. note::

    Group constants are converted from ``SERPENT_STYLE`` to
    ``mixedCase`` to fit the overall style of the project.

The |branchContainer| stores group 
constant data in |homogUniv| objects in the 
:py:attr:`~serpentTools.parsers.branching.BranchingReader.branches`
dictionary

.. code:: 

    >>> b0.universes
    {(0, 0.0, 1): <serpentTools.objects.containers.HomogUniv at 0x2220c781ac8>,
     (0, 1.0, 2): <serpentTools.objects.containers.HomogUniv at 0x2220c78b5f8>,
     (0, 10.0, 3): <serpentTools.objects.containers.HomogUniv at 0x2220c791240>,
     (10, 0.0, 1): <serpentTools.objects.containers.HomogUniv at 0x2220c787a58>,
     (10, 1.0, 2): <serpentTools.objects.containers.HomogUniv at 0x2220c78b6a0>,
     (10, 10.0, 3): <serpentTools.objects.containers.HomogUniv at 0x2220c791320>,
     (20, 0.0, 1): <serpentTools.objects.containers.HomogUniv at 0x2220c787cc0>,
     (20, 1.0, 2): <serpentTools.objects.containers.HomogUniv at 0x2220c78b908>,
     (20, 10.0, 3): <serpentTools.objects.containers.HomogUniv at 0x2220c791588>,
     (30, 0.0, 1): <serpentTools.objects.containers.HomogUniv at 0x2220c78b048>,
     (30, 1.0, 2): <serpentTools.objects.containers.HomogUniv at 0x2220c78bb70>,
     (30, 10.0, 3): <serpentTools.objects.containers.HomogUniv at 0x2220c7917f0>,
     (40, 0.0, 1): <serpentTools.objects.containers.HomogUniv at 0x2220c78b1d0>,
     (40, 1.0, 2): <serpentTools.objects.containers.HomogUniv at 0x2220c78bdd8>,
     (40, 10.0, 3): <serpentTools.objects.containers.HomogUniv at 0x2220c791a58>}

The keys here are vectors indicating the universe ID, burnup, and burnup
index corresponding to the point in the burnup schedule. ``SERPENT``
prints negative values of burnup to indicate units of days, which is
reflected in the 
:py:attr:`~serpentTools.objects.containers.BranchContainer.hasDays`
attribute. ``hasDays-> True`` indicates
that the values of burnup, second item in the above tuple, are in terms
of days, not MWd/kgU.
These universes can be obtained by indexing this dictionary, or by using
the :py:meth:`~serpentTools.objects.containers.BranchContainer.getUniv` method

.. code:: 

    >>> univ0 = b0.universes[0, 1, 1]
    >>> print(univ0)
    <HomogUniv 0: burnup: 1.000 MWd/kgu, step: 1>
    >>> print(univ0.name)
    0
    >>> print(univ0.bu)
    1.0
    >>> print(univ0.step)
    1
    >>> print(univ0.day)
    None
    >>> print(b0.hasDays)
    False
    >>> univ1 = b0.getUniv(0, burnup=1)
    >>> univ2 = b0.getUniv(0, index=1)
    >>> assert univ0 is univ1 is univ2

Group constant data is stored in five dictionaries:

1. :py:attr:`~serpentTools.objects.containers.HomogUniv.infExp`: Expected values for infinite medium group constants
2. :py:attr:`~serpentTools.objects.containers.HomogUniv.infUnc`: Relative uncertainties for infinite medium group constants
3. :py:attr:`~serpentTools.objects.containers.HomogUniv.b1Exp`: Expected values for leakge-corrected group constants
4. :py:attr:`~serpentTools.objects.containers.HomogUniv.b1Unc`: Relative uncertainties for leakge-corrected group constants
5. :py:attr:`~serpentTools.objects.containers.HomogUniv.metaData`: items that do not fit the in the above categories

.. code:: 

    >>> univ0.infExp
    {'infDiffcoef': array([ 1.83961 ,  0.682022]),
     'infFiss': array([ 0.00271604,  0.059773  ]),
     'infRem': array([], dtype=float64),
     'infS0': array([ 0.298689  ,  0.00197521,  0.00284247,  0.470054  ]),
     'infS1': array([ 0.0847372 ,  0.00047366,  0.00062865,  0.106232  ]),
     'infTot': array([ 0.310842,  0.618286])}
    >>> univ0.infUnc
    {}
    >>> univ0.b1Exp
    {'b1Diffcoef': array([ 1.79892 ,  0.765665]),
     'b1Fiss': array([ 0.00278366,  0.0597712 ]),
     'b1Rem': array([], dtype=float64),
     'b1S0': array([ 0.301766  ,  0.0021261 ,  0.00283866,  0.470114  ]),
     'b1S1': array([ 0.0856397 ,  0.00051071,  0.00062781,  0.106232  ]),
     'b1Tot': array([ 0.314521,  0.618361])}
    >>> univ0.metaData
    {}

Group constants and their associated uncertainties can be obtained using
the :py:meth:`~serpentTools.objects.containers.HomogUniv.get` method.

.. code:: 

    >>> univ0.get('infFiss')
    array([ 0.00286484,  0.0577559 ])
    >>> try:
    >>>     univ0.get('infS0', uncertainty=True)
    >>> except KeyError as ke:  # no uncertainties here
    >>>     print(str(ke))
    'Variable infS0 absent from uncertainty dictionary'

Iteration
---------

The branching reader has a
:py:meth:`~serpentTools.parsers.branching.BranchingReader.iterBranches`
method that works to yield branch names and their associated
|branchContainer| objects. This can
be used to efficiently iterate over all the branches presented in the file.

.. code:: 

    >>> for names, branch in r0.iterBranches():
    >>>    print(names, branch)
    ('nom', 'nom') <BranchContainer for nom, nom from demo.coe>
    ('B750', 'nom') <BranchContainer for B750, nom from demo.coe>
    ('B1000', 'nom') <BranchContainer for B1000, nom from demo.coe>
    ('nom', 'FT1200') <BranchContainer for nom, FT1200 from demo.coe>
    ('B750', 'FT1200') <BranchContainer for B750, FT1200 from demo.coe>
    ('B1000', 'FT1200') <BranchContainer for B1000, FT1200 from demo.coe>
    ('nom', 'FT600') <BranchContainer for nom, FT600 from demo.coe>
    ('B750', 'FT600') <BranchContainer for B750, FT600 from demo.coe>
    ('B1000', 'FT600') <BranchContainer for B1000, FT600 from demo.coe>

.. _branching-settings:

User Control
------------

The ``SERPENT``
`set coefpara <http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual#set_coefpara>`_
card already restricts the data present in the coeffient file to user
control, and the |branchReader|  includes similar control. 
Below are the various settings that the |branchReader| uses to read and
process coefficient files.

.. code:: 

    >>> import six
    >>> from serpentTools.settings import rc
    >>> from serpentTools.settings import rc, defaultSettings
    >>> for setting in defaultSettings:
    >>>     if 'xs' in setting or 'branching' in setting:
    >>>         print(setting)
    >>>         for k, v in six.iteritems(defaultSettings[setting]):
    >>>             print('\t', k+':', v)
    branching.areUncsPresent
         default: False
         type: <class 'bool'>
         description: True if the values in the .coe file contain uncertainties
    branching.intVariables
         default: []
         description: Name of state data variables to convert to integers for
         each branch
         type: <class 'list'>
    branching.floatVariables
         default: []
         description: Names of state data variables to convert to floats for
         each branch
         type: <class 'list'>
    xs.getInfXS
         default: True
         description: If true, store the infinite medium cross sections.
         type: <class 'bool'>
    xs.getB1XS
         default: True
         description: If true, store the critical leakage cross sections.
         type: <class 'bool'>
    xs.variableGroups
         default: []
         description: Name of variable groups from variables.yaml to be expanded
          into SERPENT variable to be stored
         type: <class 'list'>
    xs.variableExtras
         default: []
         description: Full SERPENT name of variables to be read
         type: <class 'list'>

In our example above, the ``BOR`` and ``TFU`` variables represented
boron concentration and fuel temperature, and can easily be cast into
numeric values using the ``branching.intVariables`` and
``brancing.floatVariables`` settings. From the previous example, we see
that the default action is to store all state data variables as strings.

.. code:: 

    >>> assert isinstance(b0.stateData['BOR'], str)

As demonstrated in the :ref:`group-const-variables` example, use of
``xs.variableGroups`` and ``xs.variableExtras`` controls what data is
stored on the |homogUniv| 
objects. By default, all variables present in the coefficient file are stored.

.. code:: 

    >>> rc['branching.floatVariables'] = ['BOR']
    >>> rc['branching.intVariables'] = ['TFU']
    >>> rc['xs.getB1XS'] = False
    >>> rc['xs.variableExtras'] = ['INF_TOT', 'INF_SCATT0']
    >>> r1 = serpentTools.read(branchFile)
    INFO    : serpentTools: Inferred reader for demo.coe: BranchingReader
    INFO    : serpentTools: Preparing to read demo.coe
    INFO    : serpentTools: Done reading branching file
    >>> b1 = r1.branches['B1000', 'FT600']
    >>> b1.stateData
    {'BOR': 1000.0,
     'DATE': '17/10/18',
     'TFU': 600,
     'TIME': '10:26:48',
     'VERSION': '2.1.29'}
    >>> assert isinstance(b1.stateData['BOR'], float)
    >>> assert isinstance(b1.stateData['TFU'], int)

Inspecting the data stored on the homogenized universes reveals only the
variables explicitly requested are present

.. code:: 

    >>> univ4 = b1.getUniv(0, 0)
    >>> univ4.infExp
    {'infTot': array([ 0.313338,  0.54515 ])}
    >>> univ4.b1Exp
    {}

Conclusion
----------

The |branchReader| is capable of reading coefficient files created
by the ``SERPENT`` automated branching process. The data is stored
according to the branch parameters, universe information, and burnup.
This reader also supports user control of the processing by selecting
what state parameters should be converted from strings to numeric types,
and further down-selection of data.
