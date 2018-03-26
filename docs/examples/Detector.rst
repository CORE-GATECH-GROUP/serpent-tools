.. _detector-example:

.. |detector| replace:: :py:class:`~serpentTools.objects.containers.Detector`

.. |detectorReader| replace:: :py:class:`~serpentTools.parsers.detector.DetectorReader`

.. |detBins| replace:: :py:attr:`~serpentTools.objects.containersBase.Detector.bins`

.. |detIndx| replace:: :py:attr:`~serpentTools.objects.containers.Detector.indexes`

.. |detTallies| replace:: :py:attr:`~serpentTools.objects.containers.Detector.tallies`

.. |detErrors| replace:: :py:attr:`~serpentTools.objects.containers.Detector.errors`

.. |detGrids| replace:: :py:attr:`~serpentTools.objects.containers.Detector.grids`

.. |detSlice| replace:: :py:meth:`~serpentTools.objects.containers.DetectorBase.slice`

.. |plot| replace:: :py:meth:`~serpentTools.objects.containers.DetectorBase.plot`

.. |mesh| replace:: :py:meth:`~serpentTools.objects.containers.DetectorBase.meshPlot`

.. |spectrum| replace:: :py:meth:`~serpentTools.objects.containers.Detector.spectrumPlot`

==============
DetectorReader
==============

Basic Operation
---------------

The |detectorReader|
is capable of reading SERPENT detector files.
These detectors can be defined with many binning parameters,
listed
`on the SERPENT
Wiki <http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual#det_.28detector_definition.29>`_.
One could define a detector that has a spatial mesh, ``dx/dy/dz/``, but
also includes reaction and material bins, ``dr, dm``. Detectors are
stored on the reader object in the 
:py:attr:`~serpentTools.parsers.detector.DetectorReader.detectors`
dictionary as custom |detector| objects. 
Here, all energy and spatial grid data are stored,
including other binning information such as reaction, universe, and
lattice bins.

.. code::

    >>> from matplotlib import pyplot
    >>> import serpentTools
    INFO    : serpentTools: Using version 0.2.1
    >>> pinFile = 'fuelPin_det0.m'
    >>> bwrFile = 'bwr_det0.m'
    >>> pin = serpentTools.read(pinFile)
    INFO    : serpentTools: Inferred reader for fuelPin_det0.m: DetectorReader
    INFO    : serpentTools: Preparing to read fuelPin_det0.m
    INFO    : serpentTools: Done
    >>> bwr = serpentTools.read(bwrFile)
    INFO    : serpentTools: Inferred reader for bwr_det0.m: DetectorReader
    INFO    : serpentTools: Preparing to read bwr_det0.m
    INFO    : serpentTools: Done
    >>> print(pin.detectors)
    {'nodeFlx': 
        <serpentTools.objects.containers.Detector object at 0x7fb3ae1db978>}
    >>> print(bwr.detectors)
    {'spectrum':
        <serpentTools.objects.containers.Detector object at 0x7fb3ae1db9e8>,
     'xymesh':
         <serpentTools.objects.containers.Detector object at 0x7fb3ae1dba20>}

These detectors were defined for a single fuel pin with 16 axial layers
and a separate BWR assembly, with a description of the detectors provided in
below:

+--------------+---------------+
| Name         | Description   |
+==============+===============+
| ``nodeFlx``  | One-group     |
|              | flux tallied  |
|              | in each axial |
|              | layer         |
+--------------+---------------+
| ``spectrum`` | CSEWG 239     |
|              | group         |
|              | stucture for  |
|              | flux and      |
|              | U-235 fission |
|              | cross section |
+--------------+---------------+
| ``xymesh``   | Two-group     |
|              | flux for a    |
|              | 20x20 xy grid |
+--------------+---------------+

For each |detector| object,
the full tally matrix is stored in the
|detBins| array.

.. code:: 

    >>> nodeFlx = pin.detectors['nodeFlx']
    >>> print(nodeFlx.bins.shape)
    (16, 12)
    >>> nodeFlx.bins[:3, :].T
    array([[  1.00000000e+00,   2.00000000e+00,   3.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  1.00000000e+00,   2.00000000e+00,   3.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  1.00000000e+00,   1.00000000e+00,   1.00000000e+00],
           [  2.34759000e-02,   5.75300000e-02,   8.47000000e-02],
           [  4.53000000e-03,   3.38000000e-03,   2.95000000e-03]])

Here, only three columns, shown as rows for readability, are changing:

-  column 0: universe column
-  column 10: tally column
-  column 11: errors

.. note::

    For SERPENT-1, there would be an additional column 12 that
    contained the scores for each bin

.. code:: 

    >>> nodeFlx.bins[:, 0]
    array([  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.,  
            11.,  12.,  13.,  14.,  15.,  16.])

Once each detector is given this binned tally data, the
:py:meth:`~serpentTools.objects.containers.Detector.reshape`
method is called to recast the
|detTallies|, |detErrors|, and, if applicable,
the :py:attr:`~serpentTools.objects.containers.Detector.scores` columns into
individual, multidimensional arrays. For this case,
since the only variable bin quantity is that of the universe, these
will all be 1D arrays.

.. code:: 

    >>> assert nodeFlx.tallies.shape == (16, )
    >>> assert nodeFlx.errors.shape == (16, )
    >>> nodeFlx.tallies
    array([ 0.0234759 ,  0.05753   ,  0.0847    ,  0.102034  ,  0.110384  ,
            0.110174  ,  0.102934  ,  0.0928861 ,  0.0810541 ,  0.067961  ,
            0.0550446 ,  0.0422486 ,  0.0310226 ,  0.0211475 ,  0.0125272 ,
            0.00487726])
    >>> nodeFlx.errors
    array([ 0.00453,  0.00338,  0.00295,  0.00263,  0.00231,  0.00222,
            0.00238,  0.00251,  0.00282,  0.00307,  0.00359,  0.00415,
            0.00511,  0.00687,  0.00809,  0.01002])

Bin information is retained through the |detIndx| attribute. This is an 
:py:class:`~collections.OrderedDict` as the keys are placed according to their column
position. These postions can be found in the SERPENT Manual, and are
provided in the ``DET_COLS`` tuple.

.. note:: 
    
    Python and numpy arrays are zero-indexed, meaning the first item
    is accessed with ``array[0]``, rather than ``array[1]``.

.. code:: 

    >>> from serpentTools.objects.containers import DET_COLS
    >>> print(DET_COLS)
    ('value', 'energy', 'universe', 'cell', 'material', 'lattice', 
     'reaction', 'zmesh', 'ymesh', 'xmesh', 'tally', 'error', 'scores')
    >>> print(DET_COLS.index('cell'))
    3
    >>> nodeFlx.indexes
    OrderedDict([('universe',
                  array([  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   
                           9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.]))])


Each item in the |detIndx| ordered dictionary corresponds to the
unique values of that bin in the original |detBins| array. Here,
``universe`` is the first item and contains an equal number of elements
to the size of the first (and only) axis in the ``nodeFlx`` tally matrix

.. code:: 

    >>> assert nodeFlx.indexes['universe'].size == nodeFlx.tallies.size

For detectors that include some grid matrices, such as spatial or energy
meshes ``DET<name>E``, these arrays are stored in the |detGrids| dictionary

.. code:: 

    >>> spectrum = bwr.detectors['spectrum']
    >>> print(spectrum.grids['E'][:5, :])
    [[  1.00002000e-11   4.13994000e-07   2.07002000e-07]
     [  4.13994000e-07   5.31579000e-07   4.72786000e-07]
     [  5.31579000e-07   6.25062000e-07   5.78320000e-07]
     [  6.25062000e-07   6.82560000e-07   6.53811000e-07]
     [  6.82560000e-07   8.33681000e-07   7.58121000e-07]]

Multi-dimensional Detectors
---------------------------

The |detector| objects are capable
of reshaping the detector data intoan array where each axis corresponds to a
varying bin. In the above examples, the reshaped data was one-dimensional,
because the detectors only tallied data against one bin, universe and energy.
In the following example, the detector has been configured to tally the
fission and capture rates (two ``dr`` arguments) in an XY mesh.

.. code:: 

    >>> xy = bwr.detectors['xymesh']
    >>> for key in xy.indexes:
    >>>     print(key, xy.indexes[key])
    energy [0 1]
    ymesh [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
    xmesh [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

Traversing the first axis in the |detTallies| array corresponds to
changing the value of the ``reaction``. The second axis corresponds to
changing ``ymesh`` values, and the final axis reflects changes in
``xmesh``.

.. code:: 

    >>> print(xy.bins.shape)
    (800, 12)
    >>> print(xy.tallies.shape)
    (2, 20, 20)
    >>> print(xy.bins[:5, 10])
    [  8.19312000e+17   7.18519000e+17   6.90079000e+17   6.22241000e+17
       5.97257000e+17]
    >>> print(xy.tallies[0, 0, :5])
    [  8.19312000e+17   7.18519000e+17   6.90079000e+17   6.22241000e+17
       5.97257000e+17]

Slicing
~~~~~~~

As the detectors produced by SERPENT can contain multiple bin types, as
seen in ``DET_COLS``, obtaining data from the tally data can become
complicated. This retrieval can be simplified using the |detSlice| method. 
This method takes an argument indicating what bins (keys in |detIndx|)
to fix at what position.

If we want to retrive the tally data for the fission reaction in the
``spectrum`` detector, you would instruct the
|detSlice| method to use column 1 along the axis that corresponds to the reaction bin, 
as the fission reaction corresponded to reaction tally 2 in the original
matrix. Since python and numpy arrays are zero indexed, the second
reaction tally is stored in column 1.

.. code:: 

    >>> print(spectrum.indexes['reaction'])
    [0 1]
    >>> spectrum.slice({'reaction': 1})[:20]
    array([  3.66341000e+22,   6.53587000e+20,   3.01655000e+20,
             1.51335000e+20,   3.14546000e+20,   7.45742000e+19,
             4.73387000e+20,   2.82554000e+20,   9.89379000e+19,
             9.49670000e+19,   8.98272000e+19,   2.04606000e+20,
             3.58272000e+19,   1.44708000e+20,   7.25499000e+19,
             6.31722000e+20,   2.89445000e+20,   2.15484000e+20,
             3.59303000e+20,   3.15000000e+20])

This method also works for slicing the error and score matrices by using
``what='errors'`` or ``'scores'``, respectively.

.. code:: 

    >>> spectrum.slice({'reaction': 1}, 'errors')[:20]
    array([ 0.00692,  0.01136,  0.01679,  0.02262,  0.01537,  0.02915,
            0.01456,  0.01597,  0.01439,  0.01461,  0.01634,  0.01336,
            0.01549,  0.01958,  0.02165,  0.0192 ,  0.02048,  0.01715,
            0.02055,  0.0153 ]) 

Plotting Routines
-----------------

Each |detector| object is capable of
simple 1D and 2D plotting routines. The simplest 1D plot method is simply |plot|, 
however a wide range of plot options are supported.
Below are keyword arguments that can be used to format the plots.

+--------------+------------------------------------------------+
| Option       | Description                                    |
+==============+================================================+
| ``what``     | What data to plot                              |
+--------------+------------------------------------------------+
| ``ax``       | Preprepared figure on which to add this plot   |
+--------------+------------------------------------------------+
| ``xdim``     | Quantity from |detIndx| to use as x-axis       |
+--------------+------------------------------------------------+
| ``sigma``    | Confidence interval to place on errors - 1D    |
+--------------+------------------------------------------------+
| ``steps``    | Draw tally values as constant inside bin - 1D  |
+--------------+------------------------------------------------+
| ``xlabel``   | Label to apply to x-axis                       |
+--------------+------------------------------------------------+
| ``ylabel``   | Label to apply to y-axis                       |
+--------------+------------------------------------------------+
| ``loglog``   | Use a log scalling on both of the axes         |
+--------------+------------------------------------------------+
| ``logx``     | Use a log scaling on the x-axis                |
+--------------+------------------------------------------------+
| ``logy``     | Use a log scaling on the y-axis                |
+--------------+------------------------------------------------+

The plot routine also accepts various options, which can be found in the
`matplotlib.pyplot.plot
documentation <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html>`_

.. code:: 

    >>> nodeFlx.plot()


.. image:: images/Detector_31_0.png


.. code:: 

    >>> ax = nodeFlx.plot(steps=True, label='steps')
    >>> ax = nodeFlx.plot(sigma=100, ax=ax, c='k', alpha=0.6, 
                          marker='x', label='sigma')


.. image:: images/Detector_32_0.png

Passing ``what='errors'`` to the plot method plots the associated
relative errors, rather than the tally data on the y-axis. 
Similarly, passing a key from |detIndx|
as the ``xdim`` argument sets the x-axis to be that specific index.

.. code:: 

    >>> nodeFlx.plot(xdim='universe', what='errors', 
    >>>              ylabel='Relative tally error [%]')


.. image:: images/Detector_34_0.png

Mesh Plots
~~~~~~~~~~

For data with dimensionality greater than one, the |mesh| method
can be used to plot some 2D slice of the data on a Cartesian grid.
Passing a dictionary as the ``fixed`` argument restricts the tally data
down to two dimensions. The X and Y axis can be quantities from
|detGrids| or |detIndx|. If the quantity to be used for an axis is in
the |detGrids| dictionary, then the appropriate spatial or energetic grid
from the detector file will be used. Otherwise, the axis will reflect
changes in a specific bin type. The following keyword arguments can be
used in conjunction with the above options to format the mesh plots.

+------------------+--------------------------------------------------------+
| Option           | Action                                                 |
+==================+========================================================+
| ``cmap``         | Colormap to apply to the figure                        |
+------------------+--------------------------------------------------------+
| ``cbarLabel``    | Label to apply to the colorbar                         |
+------------------+--------------------------------------------------------+
| ``logScale``     | If true, use a logarithmic scale for the colormap      |
+------------------+--------------------------------------------------------+
| ``normalizer``   | Apply a custom non-linear normalizer to the colormap   |
+------------------+--------------------------------------------------------+

The ``cmap`` argument must be something that ``matplotlib`` can
understand as a valid colormap. This can be a string of any of the
colormaps supported by matplotlib.

Since the ``xymesh`` detector is three dimensions, (energy, x, and y),
we must pick an energy group to plot.

.. code:: 

    >>> ax = xy.meshPlot('x', 'y', fixed={'energy': 0}, 
    >>>                  cbarLabel='Mesh-integrated flux $[n/cm^2/s]$');
    >>> ax.set_title("Fast spectrum flux $[>0.625 eV]$");



.. image:: images/Detector_36_0.png


The |mesh| also supports a range of labeling and plot options.
Here, we attempt to plot the flux and U-235 fission reaction rate errors
as a function of energy, with the two reaction rates separated on the
y-axis. Passing ``logColor=True`` applies a logarithmic color scale to
all the positive data. Data that is zero is not shown, and errors will
be raised if the data contain negative quantities.

Here we also apply custom y-tick labels to reflect the reaction that is
being plotted.

.. code:: 

    >>> ax = spectrum.meshPlot('e', 'reaction', what='errors', 
    >>>                        ylabel='Reaction type', cmap='PuBu_r',
    >>>                        cbarLabel="Relative error $[\%]$",
    >>>                        xlabel='Energy [MeV]', logColor=True,
    >>>                        logx=True);
    >>> ax.set_yticks([0.5, 1.5]);
    >>> ax.set_yticklabels([r'$\psi$', r'$U-235 \sigma_f$'], rotation=90,
    >>>                    verticalalignment='center');


.. image:: images/Detector_38_0.png


Using the ``slicing`` arguments allows access to the 1D plot methods
from before

.. code:: 

    >>> xy.plot(fixed={'energy': 1, 'xmesh': 1}, 
    >>>         xlabel='Y position',
    >>>         ylabel='Thermal flux along x={}'
    >>>         .format(xy.grids['X'][1, 0]));

.. image:: images/Detector_40_0.png


Spectrum Plots
~~~~~~~~~~~~~~

The |detector| objects are also capable of energy spectrum plots, if
an associated energy grid is given. The ``normalize`` option will
normalize the data per unit lethargy. This plot takes some additional
assumptions with the scaling and labeling, but all the same controls as
the above line plots.

The |spectrum| method is designed to prepare plots of energy
spectra. Supported arguments for the |spectrum| method include

+-----------------+----------------+----------------------------------------------+
| Option          | Default        | Description                                  |
+=================+================+==============================================+
| ``normalize``   | ``True``       | Normalize tallies per unit lethargy          |
+-----------------+----------------+----------------------------------------------+
| ``fixed``       | ``None``       | Dictionary that controls matrix reduction    |
+-----------------+----------------+----------------------------------------------+
| ``sigma``       | 3              | Level of confidence for statistical errors   |
+-----------------+----------------+----------------------------------------------+
| ``xscale``      | ``'log'``      | Set the x scale to be log or linear          |
+-----------------+----------------+----------------------------------------------+
| ``yscale``      | ``'linear'``   | Set the y scale to be log or linear          |
+-----------------+----------------+----------------------------------------------+

The figure below demonstrates the default options and control in this
|spectrum| routine by

1. Using the less than helpful plot routine with no formatting
2. Using |spectrum| without normalization to show default labels
   and scaling
3. Using |spectrum| with normalization

Since our detector has energy bins and reaction bins, we need to reduce
down to one-dimension with the ``fixed`` command.

.. code:: 

    >>> fig, axes = pyplot.subplots(1, 3, figsize=(16, 4))
    >>> fix = {'reaction': 0}
    >>> spectrum.plot(fixed=fix, ax=axes[0]);
    >>> spectrum.spectrumPlot(fixed=fix, ax=axes[1], normalize=False);
    >>> spectrum.spectrumPlot(fixed=fix, ax=axes[2]);

.. image:: images/Detector_44_0.png


Multiple line plots
~~~~~~~~~~~~~~~~~~~

Plots can be made against multiple bins, such as spectrum in different
materials or reactions, with the |plot| and |spectrum| methods.
Below is the flux spectrum and spectrum of the U-235 fission reaction
rate from the same detector. The ``labels`` argument is what is used to
label each individual plot in the order of the bin index.

.. code:: 

    >>> labels = (
    >>>     'flux',
    >>>     r'$\sigma_f^{U-235}\psi$')  # render as mathtype
    >>> spectrum.plot(labels=labels, loglog=True);

.. image:: images/Detector_46_0.png


.. code:: 

    >>> spectrum.spectrumPlot(labels=labels);

.. image:: images/Detector_47_0.png

Conclusion
----------

The |detectorReader| is capable of reading and storing detector data from SERPENT detector files.
The data is stored on custom |detector|
objects, capable of reshaping tally and error matrices into arrays with
dimensionality reflecting the detector binning.
These |detector| objects have simple methods for retrieving and plotting detector data.

References
----------

1. `matplotlib plot <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html>`_
2. `Custom colormap normalization <https://matplotlib.org/gallery/userdemo/colormap_normalizations_custom.html#sphx-glr-gallery-userdemo-colormap-normalizations-custom-py>`_
3. `matplotlib 2.0 colormaps <https://matplotlib.org/examples/color/colormaps_reference.html>`_
