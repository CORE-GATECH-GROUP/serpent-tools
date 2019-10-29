.. _api-misc:

Miscellaneous
=============

Data Module
-----------

The ``data`` module exists to assist with reproducing example problems and the
test interface. It should be used sparsely unless following along with an
example as it is subject to change.

.. currentmodule:: serpentTools.data

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myfunction.rst

    readDataFile
    getFile

Exceptions
----------

``serpentTools`` relies on a few custom exceptions, documented below for convenience.

.. note::

    Developers should rely on built-in exceptions whenever possible. These
    will be fading out over coming versions.

.. currentmodule:: serpentTools.messages

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myexception.rst

    SerpentToolsException
    SamplerError
    MismatchedContainersError

Random Seed Module
------------------

Exposed through the ``serpentTools.seed`` module are functions to assist in
generating repeated input files with unique random seeds. These are used to
support the command line sub-command :ref:`cli-seed`.

.. currentmodule:: serpentTools.seed

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myfunctions.rst

    seedFiles
    generateSeed
