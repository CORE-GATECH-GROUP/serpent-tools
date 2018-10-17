.. _dev-logging::

=====================
Logging and Reporting
=====================

This chapter describes the various functions used to convey progress updates
or issues to the user. Functions in this module should be used over a general
``print`` statement, as this module can be/will be extended to log messages to
a file in the future.
In order of increasing severity:

.. autofunction:: serpentTools.messages.debug

.. autofunction:: serpentTools.messages.info

.. autofunction:: serpentTools.messages.warning

.. autofunction:: serpentTools.messages.error

.. autofunction:: serpentTools.messages.critical

Decorators
==========

Two decorators are provided in the ``messages`` module that are used
to indicate functions or methods who's behavior will be changing
or removed in the future.

.. autofunction:: serpentTools.messages.deprecated

.. autofunction:: serpentTools.messages.willChange


Custom Handlers
===============

.. autoclass:: serpentTools.messages.DictHandler
    :show-inheritance:
    :no-inherited-members:
