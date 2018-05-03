.. _history:

.. |arrays| replace:: :py:attr:`~serpentTools.parsers.history.HistoryReader.arrays`

==============
History Reader
==============

This class reads the history file, ``_his<n>.m``, and stores the arrays
in the |arrays| dictionary.

A more thorough description of the arrays present in the history file can be found
`on the SERPENT wiki <http://serpent.vtt.fi/mediawiki/index.php/Description_of_output_files#History_output>`_.
From this wiki

    The output consists of tables corresponding to different parameters.
    The first column lists the cycle index, which is then followed by the
    results grouped in three columns that provide the cycle-wise value,
    the cumulative mean and the corresponding relative statistical error.
    If the parameter has two values, the number of columns is 7 (cycle
    index + two groups of three columns of results), and so on. 

.. note::

    The variables in |arrays| will be converted from ``SERPENT_STYLE`` to
    ``camelCase``, with the initial ``HIS_`` string dropped. For example, the 
    variable ``HIS_IMP_KEFF`` would be stored under ``impKeff``. 

.. note:: 

    The first column listed above, the index column, is not present in the arrays.
    If only the active cycles are desired, utilze the 
    :py:attr:`~serpentTools.parsers.history.HistoryReader.numInactive`
    to determine the starting index for array indexing::

        >>> his = serpentTools.read('bwr_his0.m')
        >>> nSkip = his.numInactive
        >>> timeR = his.arrays['time']
        >>> activeTime = timeR[nSkip:]

.. autoclass:: serpentTools.parsers.history.HistoryReader

