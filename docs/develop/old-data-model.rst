.. _data-model-v0:

==========
Data Model
==========

This project has two key offerings to the ``SERPENT`` community.

1. Scripting tools that are capable of interpreting the output files
2. Purpose-built containers for storing, accessing, and utilizing the data in the output files

Readers
-------

The readers are the core of this package, and should have a
logical and consistent method for structuring data.
Each reader contained in this project should:

#. Be capable of reading the intended output file
#. Yield to the user the data in a logical manner
#. Default to storing all the data without user input
#. Receive input from the user regarding what data to restrict/include
#. Report activity at varying levels, including failure, to the user

The third and fourth points refer to use of the
:py:mod:`serpentTools.settings` module to receive user input.
The final point refers to use of the logging and messaging functions
included in :py:mod:`serpentTools.messages`.

For example,
the :py:class:`~serpentTools.parsers.DepletionReader` stores
data in the following manner::

    Reader
    | - filePath
    | - fileMetadata
        | - isotope names
        | - isotope ZAIs
        | - depletion schedule in days and burnup
    | - materials
    # for each material:
        | - DepletedMaterial-n
            | - name
            | - atomic density
            | - mass density
            | - volume
            | etc

Here, the reader primarily creates and stores material objects, and
the useful data is stored on these objects. Some files, like the fission
matrix and depletion matrix files may not have a structure that naturally
favors this object-oriented approach.

Containers
----------

The readers are primarily responsible for creating and populating
containers, that are responsible for storing and retrieving data.
Just like the
:py:class:`~serpentTools.objects.materials.DepletedMaterial` has
shortcuts for analysis like
:py:meth:`~serpentTools.objects.materials.DepletedMaterial.getValues` and
:py:meth:`~serpentTools.objects.materials.DepletedMaterial.plot`,
each such container should easily and naturally provide access
to the data, and also perform some common analysis on the data.
