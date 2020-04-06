.. _data-model:

==================
Updated Data Model
==================

The goal of this document is to describe developer-specific changes
that should drive the next phase of development. The contents
reflect changes that will be introduced between release
:ref:`v0.9.3` and the next major release of ``0.10.0``.

Goals and non-goals
===================

The new data model and developer guide is provided to help the
next release of ``serpentTools`` have:

1. Little to no high-level API breaks
2. Less superfluous code like the settings interface
3. Generic, library-like readers and containers
4. Inherited methods only when they make sense and are implemented
5. Standard base classes like :class:`collections.abc.Mapping` when
   appropriate

These items should be accomplished without:

1. Breaking the ease of :func:`serpentTools.read`
2. Removing plotting capabilities
3. Removing filtering capabilities

Data Model
==========

Separation of readers and containers
------------------------------------

Objects that store information from Serpent files should be separated from
objects that read Serpent files. Much of this is inspired by :issue:`335`,
and will help 1) reduce left-over code and methods related to reading files, and
2) support integration with other file formats. Classes that store the file data
will be designated as ``<X>File`` like ``ResultFile``, while classes that read
file data will be designated as ``<X>Reader``, e.g. ``ResultReader``.

These file classes will emululate the previous behavior of creating a reader
and then reading the file through :func:`classmethod`, like below::

    class DemoFile:

        @classmethod
        def fromSerpent(cls, fp, *args, **kwargs):
            # process
            # return an instance of DemoFile or cls()

Here, a user or a new read function can call ``DemoFile.fromSerpent`` to
parse the file and store it's contents. This helps reduce the likelihood of
partially instantiated readers running around, like creating a ``ResultsReader``
and trying to plot before calling ``read``.

This has an additional benefit of allowing additional class methods for creating
files from alternative data types. A ``fromHdf`` method would be extra wonderful.
But, new file formats are not the intended goal of version ``0.10.0``.

Reusable readers
----------------

Readers should be reusable and configurable. Users should be able to pass settings
either through the ``__init__`` method and/or as attributes to control what
data is read. This is how the settings module will be deprecated and removed.
Settings can be controlled through :class:`property` decorators.

The primary task of a reader will be to read a file, or incoming stream of data,
and produced a corresponding ``<X>File`` instance. Readers should also be capable
of reading multiple files or streams, clearing caches or temporary variables as
necessary. The implementation should support the following::

    >>> r = DemoReader()
    >>> f0 = r.read(examplefile0)
    >>> f1 = r.read(examplefile1)

This should save time when reading multiple files of the same type, especially
if filtering is used in all cases.

Generic Containers
------------------

Containers like detectors and homogeneous universes should be introduced into the
main API, with a sufficiently generic interface. Some of this work has already
been implemented on the :class:`serpentTools.Detector` and its related subclasses.
The main change to the current implementations would be things like

1. Making :meth:`serpenTools.objects.HomogUniv.addData` accept arrays rather than
   string data to be converted and split
2. Making :class:`serpentTools.objects.DepletedMaterial` accept name, day, zai, and/or
   burnup vectors directly, rather than a ``metadata`` argument.
3. Providing adequate setters, like ``__setitem__`` when applicable, that allow data
   to be provided from a generic source. 

These routines will also help the file objects create these auxiliary containers
when reading additional file formats.

Math methods
------------

Some classes may benefit from implementing methods like ``__add__`` or ``__mul__``
to scale and modify stored data. Converting a power profile stored on a detector
from W to MW with::

    >>> det /= 1E6

or compute the difference between two detectors with::

    >>> diff = det0 - det1

Sufficient checks should be made that the ``other`` object has a compatible
data layout (two detectors have similar indexes, grids etc). 

Additional information on methods like this can be found in the
`Python data model <https://docs.python.org/3/reference/datamodel.html
#emulating-numeric-types>`_ documentation.

Proposed integration 
=====================

This is not going to be easy, as there will undoubtedly be some backwards 
incompatible changes introduced. However, the end product with be a python
package that will be more friendly to users and developers, and, hopefully,
easier to extend and maintain.

The following changes are proposed:

1. A new module be introduced under the name ``serpentTools.next``
   (name up for discussion). This should reside inside the main source
   directly in ``serpentTools/next/``
2. This new module will remain detached from the main API, meaning that all
   features must be utilized with::

       >>> import serpentTools.next
       >>> r0 = serpentTools.next.read(filep)

3. Parsers, file-objects, and containers should be implemented inside this new
   module. These need not inherit from the current ``BaseObject``. When
   it makes sense, the use of the :mod:`collections.abc` should be used to
   provide maximum features for minimal work
4. Tests should be written using ``pytest`` that ensure the new
   parsers store identical data as the previous parsers. These will become the
   foundation for the next round of regression tests.
5. A dedicated changelog will be added to track features that are removed,
   modified, or deprecated in this process. Keeping this up to date is
   of tantamount importance to alert developers and users on the
   eventual release.

Release Targets
===============

The following release targets are proposed. No dates are enforced.

Except for critical bug fixes, all work should pause on the master
branch.  This will hopefully reduce the amount of features to be
back-ported into the new library.

When the ``next`` module is complete and ready for release, a beta
release of the form ``0.10.0b0`` should be made and pushed to the
Python package index.  Users should be alerted through appropriate
channels.

After this point, a new main release on the ``0.9.x`` 
tree should be made. Users should be alerted to changes, primarily in
:func:`serpentTools.read` and the settings interface. These are likely
to have the largest changes to non-developer end-users.

The beta version should be live and un-touched for a sufficient
amount of time. How long is difficult to say, but two weeks seems
like a good low end target. 

If/when sufficient bugs are found and fixed, a new beta release should
be made and pushed.

Once the beta period is complete, a release candidate, ``0.10.0rc0``
or similar, should be made and pushed. Users should be alerted through
appropriate channels. This release candidate should be live for a
reasonable amount of time.

If/when sufficient bugs are found and fixed, a new release candidate
should be made and pushed.

Work should be done to merge the ``next`` module as the main parsing and
analysis library. This is the primary goal of the following major release
``0.11.0``, following a similar beta and release candidate period.
