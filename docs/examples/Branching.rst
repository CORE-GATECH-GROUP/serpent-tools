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

.. code:: ipython3

    >>> import serpentTools
    >>> branchFile = 'demo.coe'
    INFO    : serpentTools: Using version 0.1.0
    >>> r0 = serpentTools.read(branchFile)
    INFO    : serpentTools: Inferred reader for demo.coe: BranchingReader
    INFO    : serpentTools: Preparing to read demo.coe
    INFO    : serpentTools: Done reading branching file

The branches are stored in custom
:py:class:`~serpentTools.objects.containers.BranchContainer` objects in the
``branches`` dictionary

.. code:: ipython3

    >>> r0.branches
    {('Fhi', 'Bhi', 'His'):
        <serpentTools.objects.containers.BranchContainer at 0x14d0106c0f0>,
     ('Fhi', 'Blo', 'His'):
        <serpentTools.objects.containers.BranchContainer at 0x14d01063d30>,
     ('Fhi', 'nom', 'His'):
        <serpentTools.objects.containers.BranchContainer at 0x14d0105e908>,
     ('nom', 'Bhi', 'His'):
        <serpentTools.objects.containers.BranchContainer at 0x14d01068748>,
     ('nom', 'Blo', 'His'):
        <serpentTools.objects.containers.BranchContainer at 0x14d01063320>,
     ('nom', 'nom', 'His'):
        <serpentTools.objects.containers.BranchContainer at 0x14d01053ef0>}

Here, the keys are tuples of strings indicating what
perturbations/branch states were applied for each ``SERPENT`` solution.
Examining a particular case

.. code:: ipython3

    >>> b0 = r0.branches['Fhi', 'Bhi', 'His']
    >>> print(b0)
    <BranchContainer for Fhi, Bhi, His from demo.coe>
    

``SERPENT`` allows the user to define variables for each branch through:

::

    var V1_name V1_value

cards. These are stored in the ``stateData`` attribute

.. code:: ipython3

    >>> b0.stateData
    {'BOR': '1000',
     'DATE': '17/10/18',
     'TFU': '1200',
     'TIME': '10:26:48',
     'VERSION': '2.1.29'}

The keys ``'DATE'``, ``'TIME'``, and ``'VERSION'`` are included by
default in the output, while the ``'BOR'`` and ``'TFU'`` have been
defined for this branch. Branch name ``'Fhi'`` :math:`\rightarrow`
higher fuel temperature :math:`\rightarrow` ``'TFU'`` = 1200 K

Group Constant Data
~~~~~~~~~~~~~~~~~~~

.. note::

    Group constants are converted from ``SERPENT_STYLE`` to
    ``mixedCase`` to fit the overall style of the project.

The :py:class:`~serpentTools.objects.containers.BranchContainer` stores group 
constant data in :py:class:`~serpentTools.objects.containers.HomogUniv`
objects in the ``universes`` dictionary

.. code:: ipython3

    >>> b0.universes
    {(0, 0.0, 1): <serpentTools.objects.containers.HomogUniv at 0x14d010689e8>,
     (0, 1.0, 2): <serpentTools.objects.containers.HomogUniv at 0x14d0106c320>,
     (0, 5.0, 3): <serpentTools.objects.containers.HomogUniv at 0x14d0106c4a8>,
     (0, 10.0, 4): <serpentTools.objects.containers.HomogUniv at 0x14d0106c630>,
     (0, 50.0, 5): <serpentTools.objects.containers.HomogUniv at 0x14d0106c668>}

The keys here are vectors indicating the universe ID, burnup [MWd/kgU],
and burnup index corresponding to the point in the burnup schedule.
These universes can be obtained by indexing this dictionary, or by using
the :py:meth:`~serpentTools.objects.containers.BranchContainer.getUniv` method

.. code:: ipython3

    >>> univ0 = b0.universes[0, 1, 2]
    >>> print(univ0)
    >>> print(univ0.name)
    >>> print(univ0.bu)
    >>> print(univ0.step)
    >>> print(univ0.day)
    <HomogUniv from demo.coe>
    0
    1.0
    2
    0
    >>> univ1 = b0.getUniv(0, burnup=1)
    >>> univ2 = b0.getUniv(0, index=2)
    >>> assert univ0 is univ1 is univ2

Since the coefficient files do not store the day value of burnup, all
:py:class:`~serpentTools.objects.containers.HomogUniv` objects created by the
:py:class:`~serpentTools.objects.containers.BranchContainer` default to day
zero.

Group constant data is stored in five dictionaries:

1. ``infExp``: Expected values for infinite medium group constants
2. ``infUnc``: Relative uncertainties for infinite medium group
   constants
3. ``b1Exp``: Expected values for leakge-corrected group constants
4. ``b1Unc``: Relative uncertainties for leakge-corrected group
   constants
5. ``metaData``: items that do not fit the in the above categories

.. code:: ipython3

    >>> univ0.infExp
    {'infFiss': array([ 0.00286484,  0.0577559 ]),
     'infS0': array([ 0.501168  ,  0.0180394 ,  0.00155388,  1.2875    ]),
     'infS1': array([ 0.247105  ,  0.00535317,  0.00073696,  0.352806  ]),
     'infScatt0': array([ 0.519208,  1.28905 ]),
     'infScatt1': array([ 0.252459,  0.353543]),
     'infTot': array([ 0.529552,  1.38805 ])}
    >>> univ0.infUnc
    {}
    >>> univ0.b1Exp
    {}
    >>> univ0.metaData
    {'macroE': array([], dtype=float64), 'macroNg': array([], dtype=float64)}



Group constants and their associated uncertainties can be obtained using
the :py:meth:`~serpentTools.objects.containers.HomogUniv.get` method.

.. code:: ipython3

    >>> univ0.get('infFiss')
    array([ 0.00286484,  0.0577559 ])
    >>> try:
    >>>     univ0.get('infS0', uncertainty=True)
    >>> except KeyError as ke:  # no uncertainties here
    >>>     print(str(ke))
    'Variable infS0 absent from uncertainty dictionary'
    >>> univ0.get('macroE')
    array([], dtype=float64)

Iteration
---------

The branching reader has a
:py:meth:`~serpentTools.parsers.branching.BranchingReader.iterBranches`
method that works to yield branch names and their associated
:py:class:`~serpentTools.objects.containers.BranchContainer` objects. This can
be used to efficiently iterate over all the branches presented in the file.

.. code:: ipython3

    >>> for names, branch in r0.iterBranches():
    >>>    print(names, branch)
    ('nom', 'nom', 'His') <BranchContainer for nom, nom, His from demo.coe>
    ('Fhi', 'nom', 'His') <BranchContainer for Fhi, nom, His from demo.coe>
    ('nom', 'Blo', 'His') <BranchContainer for nom, Blo, His from demo.coe>
    ('Fhi', 'Blo', 'His') <BranchContainer for Fhi, Blo, His from demo.coe>
    ('nom', 'Bhi', 'His') <BranchContainer for nom, Bhi, His from demo.coe>
    ('Fhi', 'Bhi', 'His') <BranchContainer for Fhi, Bhi, His from demo.coe>

.. _branching-settings:

User Control
------------

The ``SERPENT``
`set coefpara <http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual#set_coefpara>`_
card already restricts the data present in the coeffient file to user
control, and the :py:class:`~serpentTools.parsers.branching.BranchingReader`
includes similar control. Below are the various settings that the
:py:class:`~serpentTools.parsers.branching.BranchingReader` uses to read and
process coefficient files.

.. code:: ipython3

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

.. code:: ipython3

    >>> assert isinstance(b0.stateData['BOR'], str)

As demonstrated in the :ref:`group-const-variables` example, use of
``xs.variableGroups`` and ``xs.variableExtras`` controls what data is
stored on the :py:class:`~serpentTools.objects.containers.HomogUniv`
objects. By default, all variables present in the coefficient file are stored.

.. code:: ipython3

    >>> rc['branching.floatVariables'] = ['BOR']
    >>> rc['branching.intVariables'] = ['TFU']
    >>> with rc:
    >>>     rc['xs.variableExtras'] = ['INF_TOT', 'INF_SCATT0']
    >>>     r1 = serpentTools.read(branchFile)
    INFO    : serpentTools: Inferred reader for demo.coe: BranchingReader
    INFO    : serpentTools: Preparing to read demo.coe
    INFO    : serpentTools: Done reading branching file
    >>> b1 = r1.branches['Fhi', 'Bhi', 'His']
    >>> b1.stateData
    {'BOR': 1000.0,
     'DATE': '17/10/18',
     'TFU': 1200,
     'TIME': '10:26:48',
     'VERSION': '2.1.29'}
    >>> assert isinstance(b1.stateData['BOR'], float)
    >>> assert isinstance(b1.stateData['TFU'], int)

Inspecting the data stored on the homogenized universes reveals only the
variables explicitly requested are present

.. code:: ipython3

    >>> univ4 = b1.getUniv(0, 0)
    >>> univ4.infExp
    {'infScatt0': array([ 0.519337,  1.28894 ]),
     'infTot': array([ 0.529682,  1.38649 ])}

Conclusion
----------

The :py:class:`~serpentTools.parsers.branching.BranchingReader` is capable of
reading coefficient files created
by the ``SERPENT`` automated branching process. The data is stored
according to the branch parameters, universe information, and burnup.
This reader also supports user control of the processing by selecting
what state parameters should be converted from strings to numeric types,
and further down-selection of data.

A more complicated coefficient file, with multiple universes and more
varied coefficients, will be coming shortly - Issue
`#64 <https://github.com/CORE-GATECH-GROUP/serpent-tools/issues/64>`_

