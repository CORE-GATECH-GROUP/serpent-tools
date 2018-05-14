.. |Results| replace:: :py:class:`~serpentTools.parsers.results.ResultsReader`

.. |Branching| replace:: :py:class:`~serpentTools.parsers.branching.BranchingReader`

.. |Depletion| replace:: :py:class:`~serpentTools.parsers.depletion.DepletionReader`

.. _defaultSettings:

================
Default Settings
================

Presented here are the various settings used by the
readers to control what data is stored and how the 
data is stored. There are specific settings for each reader, 
and those are of the form ``<leader>.<setting>``,
so :ref:`depletion-materials` is used only by the
:py:class:`~serpentTools.parsers.depletion.DepletionReader`.
Without modifying any settings, each reader defaults to storing all of the
data present in the output file.
Many of the settings instruct the readers to store specific data, such as
only materials present in :ref:`depletion-materials`.

---------------
Shared Settings
---------------

There are some settings that are shared between some or all readers.
Any setting that does not have a ``.`` applies to all readers,
such as :ref:`verbosity`.
Below are a list of setting leaders and the readers impacted
by this setting:

====== =========================
Leader
====== =========================
``xs`` |Results| and |Branching|
====== =========================

--------
Examples
--------

Here are links to locations in the :ref:`examples` that display
how the settings can be used on the various readers.

=========== =========================
Reader      Link to example
=========== =========================
|Branching| :ref:`branching-settings`
|Depletion| :ref:`depletion-settings`
=========== =========================

.. include:: ./defaultSettings.rst

