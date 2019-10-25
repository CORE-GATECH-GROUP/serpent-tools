.. currentmodule:: serpentTools

.. _api-readers:

File-parsing API
================

This page contains links to the full documentation for the readers used
by ``serpentTools``.

.. _api-read-funcs:

Functions
---------

The core of ``serpentTools`` is the :func:`read` function. This function
attempts to determine the file type based on the extension and use the correct
reader to parse the file. Below are links to primary reader functions that
accept a file path argument and will process the file accordingly.

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myfunction.rst

    read
    readDepmtx


.. _api-read-classes:

Classes
-------

The :func:`read` function relies heavily on the following parsers which can be
created and used outside of the function. These classes are also the returned
types for :func:`read`.

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myclass.rst

    BumatReader
    BranchingReader
    DepletionReader
    DepmtxReader
    DetectorReader
    HistoryReader
    MicroXSReader
    ResultsReader
    SensitivityReader
    XSPlotReader
