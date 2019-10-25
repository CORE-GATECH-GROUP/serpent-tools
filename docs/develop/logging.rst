.. _dev-logging:

.. currentmodule:: serpentTools.messages

Logging and Reporting
=====================

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
