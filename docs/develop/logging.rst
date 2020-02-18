.. _logging:

.. currentmodule:: serpentTools.messages

Logging and Reporting
=====================

The primary internal logging is performed with a logger named
``serpentTools``, that can be obtained using::

    >>> import logging
    >>> logging.getLogger("serpentTools")

If you want to see the messages produced by this logger, you have a 
few options. First, the Python logging system must be configured. This
can be done simply with::

    >>> import logging
    >>> logging.basicConfig(format="%(levelname)-s: %(message)-s")
    # Display a basic warning
    >>> logging.warning("This is a warning")
    WARNING: This is a warning

To show the internal messages, one can modify the verbosity through the
:ref:`settings` interface with::

    >>> serpentTools.settings.rc["verbosity"] = "debug"

where ``"debug"`` can be one of ``"debug"``, ``"info"``, ``"warning"``,
``"error"`` or ``"critical"``.

Alternatively, the level can be adjusting using the python 
:module:`logging` module::

    >>> logging.getLogger("serpentTools").setLevel(logging.DEBUG)

.. _dev-logging:

Developer Reference
-------------------

.. note::

    The use of built-in python warning support through the
    :mod:`warnings` module should be preferred. These
    functions will be phased out in future versions

This chapter describes the various functions used to convey progress updates
or issues to the user. Functions in this module should be used over a general
``print`` statement, as this module can be be extended to log messages to
a file in the future. In order of increasing severity:

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myfunction.rst

    debug
    info
    warning
    error
    critical

Decorators
----------

Two decorators are provided in the ``messages`` module that are used
to indicate functions or methods who's behavior will be changing
or removed in the future.

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myfunction.rst

    deprecated
    willChange

Custom Handlers
---------------

.. autoclass:: DictHandler
    :show-inheritance:
    :no-inherited-members:
