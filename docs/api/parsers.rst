=============
Parser Module
=============

The main module associated with reading ``SERPENT`` files.
For information on each individual reader, please see the dedicated
file listed below

.. _reader-table:

        ============= ====================
        Reader        Hyperlink
        ============= ====================
        Branching     :ref:`branching`
        Bumat         :ref:`bumat`
        Depletion     :ref:`depletion`
        Detector      :ref:`detector`
        FissionMatrix :ref:`fissionMatrix`
        Results       :ref:`results`
        ============= ====================

.. autofunction:: serpentTools.parsers.inferReader

.. autofunction:: serpentTools.parsers.read

.. autofunction:: serpentTools.parsers.depmtx


.. _engines:

Parsing Engines
===============

Included in this file are the two parsing classes that are
part of the ``drewtils`` package. These help with reading
structured text files, by yielding regular expressions matches
and blocks of text separated by keywords. 

.. automodule:: serpentTools.engines
