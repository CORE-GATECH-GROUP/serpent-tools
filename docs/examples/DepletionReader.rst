.. |depReader| replace:: :py:class:`~serpentTools.parsers.depletion.DepletionReader`

.. |depMat| replace:: :py:class:`~serpentTools.objects.materials.DepletedMaterial`

.. |materials| replace:: :py:attr:`~serpentTools.parsers.depletion.DepletionReader.materials`

.. |matData| replace:: :py:attr:`~serpentTools.objects.materials.DepletedMaterial.data`

.. |getValues| replace:: :py:meth:`~serpentTools.objects.materials.DepletedMaterialBase.getValues`

.. |depMatPlot| replace:: :py:meth:`~serpentTools.objects.materials.DepletedMaterial.plot` 

.. _depletion-reader-ex:

===============
DepletionReader
===============

Basic Operation
---------------
SERPENT produces a
`burned material file <http://serpent.vtt.fi/mediawiki/index.php/Description_of_output_files#Burnup_calculation_output>`_,
containing the evolution of material properties through burnup for all
burned materials present in the problem. The |depReader| is capable of reading
this file, and storing the data inside |depMat| objects.
Each such object has methods and attributes that should ease analysis.

.. code:: 

    >>> import six
    >>> import serpentTools
    >>> from serpentTools.settings import rc
    >>> depFile = 'demo_dep.m'
    >>> dep = serpentTools.read(depFile)
    INFO    : serpentTools: Inferred reader for demo_dep.m: DepletionReader
    INFO    : serpentTools: Preparing to read demo_dep.m
    INFO    : serpentTools: Done reading depletion file

The materials read in from the file are stored in the |materials| 
dictionary, where the keys represent the name of specific materials, and
the corresponding values are the depleted material.

.. code:: 

    >>> dep.materials
    {'bglass0': <serpentTools.objects.materials.DepletedMaterial at 0x23905154668>,
     'fuel0': <serpentTools.objects.materials.DepletedMaterial at 0x2390578eeb8>,
     'total': <serpentTools.objects.materials.DepletedMaterial at 0x2390579e978>}

Metadata, such as the isotopic vector and depletion schedule are also
present inside the reader

.. code:: 

    >>> dep.metadata.keys()
    dict_keys(['zai', 'burnup', 'names', 'days'])
    >>> dep.metadata['burnup']
    array([ 0.  ,  0.02,  0.04,  ...,  1.36,  1.38,  1.4 ,  1.42])
    >>> dep.metadata['names']
    ['Xe135', 'I135', 'U234', 'U235', 'U236', 'U238', 'Pu238',
     'Pu239',..., 'lost', 'total']

DepletedMaterial
----------------

As mentioned before, all the material data is stored inside these
|depMat| objects.
These objects share access to the metadata of the reader as well.

.. code:: 

    >>> fuel = dep.materials['fuel0']
    >>> fuel.burnup
    array([ 0.  ,  0.02,  0.04,  ...,  1.36,  1.38,  1.4 ,  1.42])
    >>> fuel.days is dep.metadata['days']
    True

All of the variables present in the depletion file for this material are
present, stored in the |matData| dictionary. A few properties commonly
used are accessible as attributes as well.

.. code:: 

    >>> fuel.data.keys()
    dict_keys(['a', 'adens', 'burnup', 'gsrc', ..., 'volume'])
    >>> fuel.adens
    array([[  0.00000000e+00,   2.43591000e-09,   4.03796000e-09, ...,
              4.70133000e-09,   4.70023000e-09,   4.88855000e-09],
           ..., 
           [  6.88332000e-02,   6.88334000e-02,   6.88336000e-02, ...,
              6.88455000e-02,   6.88457000e-02,   6.88459000e-02]])

Similar to the original file, the rows of the matrix correspond to
positions in the isotopic vector, and the columns correspond to
positions in burnup/day vectors.

.. code:: 

    >>> fuel.mdens.shape  # rows, columns
    (34, 72)
    >>> fuel.burnup.shape
    (72,)
    >>> len(fuel.names)
    34

Data Retrieval
--------------

At the heart of the |depMat|  is the |getValues| method.
This method acts as an slicing mechanism that returns data for a
select number of isotopes at select points in time. |getValues| 
requires two arguments for the units of time requested, e.g. ``days`` or
``burnup``, and the name of the data requested. This second value must
be a key in the |matData| dictionary.

Specific days or values of burnup can be passed with the ``timePoints``
keyword. This will instruct the slicing tool to retrieve data that
corresponds to values of ``days`` or ``burnup`` in the ``timePoints``
list. By default the method returns data for every time point on the
material unless ``timePoints`` is given. Similarly, one can pass a
string or list of strings as the ``names`` argument and obtain data for
those specific isotopes. Data for every isotope is given if ``names`` is
not given.

.. code:: 

    >>> dayPoints = [0, 5, 10, 30]
    >>> iso = ['Xe135', 'Sm149']
    >>> vals = fuel.getValues('days', 'a', dayPoints, iso)
    >>> print(vals.shape)
    (2, 4)
    >>> print(vals)
    [[  0.00000000e+00   3.28067000e+14   3.24606000e+14   3.27144000e+14]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00]]
    

The |depMat| uses this slicing for the built-in |depMatPlot| method, 
which takes similar slicing arguments to |getValues|.

In addition, the ``labelFmt`` argument can be used to apply a consistent
label to each unique plot. This argument supports `brace-delimited
formatting <https://docs.python.org/3/library/stdtypes.html?#str.format>`__,
and will automatically replace strings like ``{mat}`` with the name of
the material. The table below contains the special strings and their
replacements

+-----------+--------------------------------------+
| String    | Replacement                          |
+===========+======================================+
| ``'mat'`` | Name of the material                 |
+-----------+--------------------------------------+
| ``'iso'`` | Name of the isotope, e.g. ``'U235'`` |
+-----------+--------------------------------------+
| ``'zai'`` | ZZAAAI of the isotope, e.g. 922350   |
+-----------+--------------------------------------+

.. code:: 

    >>> fuel.plot('days', 'ingTox', dayPoints, iso,
                  ylabel='Ingenstion Toxicity')

.. image:: images/DepletionReader_22_0.png

.. code::
    
    >>> fuel.plot('burnup', 'ingTox', names='Xe135', logy=True,
                  labelFmt="{iso}")

.. image:: images/DepletionReader_23_0.png

This type of plotting can also be applied to the |depReader| 
:py:func:`~serpentTools.parsers.depletion.DepletionReader.plot` method
, with similar options for formatting and retrieving data. The
materials to be plotted can be filtered using the ``materials``
argument.

.. code:: 

    dep.plot('days', 'adens', names=iso, 
             materials=['fuel0', 'total'],
             labelFmt="{mat}: {iso}", logy=True);

.. image:: images/DepletionReader_25_0.png

Limitations
-----------

Currently, the |depReader| cannot catch materials with underscore in the name,
due to variables like ``ING_TOX`` also containing an underscore.
Issue `#58 <https://github.com/CORE-GATECH-GROUP/serpent-tools/issues/58>`_

.. _depletion-settings:

Settings
--------

The |depReader| also has a collection of settings to control
what data is stored. If none of these settings are modified, the default
is to store all the data from the output file. The settings that
control the depletion reader are 

  * :ref:`depletion-materials`
  * :ref:`depletion-materialVariables`
  * :ref:`depletion-metadataKeys`
  * :ref:`depletion-processTotal`

Below is an example of configuring a |depReader| that only
stores the burnup days, and atomic density for all materials that begin
with ``bglass`` followed by at least one integer.

.. note::

    Creating the ``DepletionReader`` in this manner is functionally
    equivalent to ``serpentTools.read(depFile)``

.. code:: 

    >>> rc['depletion.processTotal'] = False
    >>> rc['depletion.metadataKeys'] = ['BU']
    >>> rc['depletion.materialVariables'] = ['ADENS']
    >>> rc['depletion.materials'] = [r'bglass\d+']
    >>>
    >>> bgReader = serpentTools.parsers.DepletionReader(depFile)
    >>> bgReader.read()
    INFO    : serpentTools: Preparing to read demo_dep.m
    INFO    : serpentTools: Done reading depletion file
    >>> bgReader.materials
    {'bglass0': <serpentTools.objects.materials.DepletedMaterial at 0x239057dcb00>}
    >>> bglass = bgReader.materials['bglass0']
    >>> bglass.data
    {'adens': array([[ 0.       ,  0.       ,  0.       , ...,  0.       ,  0.       ,
              0.       ],
            [ 0.       ,  0.       ,  0.       , ...,  0.       ,  0.       ,
              0.       ],
            [ 0.       ,  0.       ,  0.       , ...,  0.       ,  0.       ,
              0.       ],
            ..., 
            [ 0.       ,  0.       ,  0.       , ...,  0.       ,  0.       ,
              0.       ],
            [ 0.       ,  0.       ,  0.       , ...,  0.       ,  0.       ,
              0.       ],
            [ 0.0715841,  0.0715843,  0.0715845, ...,  0.0715968,  0.0715969,
              0.0715971]])}
    >>> bglass.data.keys()
    dict_keys(['adens'])

Conclusion
----------

The |depReader| is capable of reading and storing all the data
from the SERPENT burned materials file. Upon reading, the reader creates
custom |depMat| objects that are responsible for storing and
retrieving the data. These objects also have a handy |depMatPlot| method for
quick analysis. Use of the 
:py:class:`~serpentTool.settings.rc` settings control object allows
increased control over the data selected from the output file.

References
----------

1. J. Leppänen, M. Pusa, T. Viitanen, V. Valtavirta, and T.
   Kaltiaisenaho. "The Serpent Monte Carlo code: Status, development and
   applications in 2013." Ann. Nucl. Energy, `82 (2015)
   142-150 <https://www.sciencedirect.com/science/article/pii/S0306454914004095>`_
