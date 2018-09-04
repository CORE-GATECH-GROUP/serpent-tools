.. |baseObj| replace:: ``BaseObject``

.. |error| replace:: :func:`~serpentTools.messages.error`

.. |warn| replace:: :func:`~serpentTools.messages.warning`

.. |info| replace:: :func:`~serpentTools.messages.info`

.. |debug| replace:: :func:`~serpentTools.messages.debug`

.. _dev-comparisons:

==================
Comparison Methods
==================

We are currently developing methods for our readers and containers to be able
for comparing between like objects. This could be used to compare the effect 
of changing fuel enrichment on pin powers or criticality, or used to compare
the effect of different ``SERPENT`` settings. The ``BaseObject`` that 
every object **should** inherit from contains the bulk of the input checking,
so each reader and object needs to implement a private ``_compare`` method with
the following structure::

    def _compare(self, other, lower, upper, sigma):
        return <boolean output of comparison>

.. note::

    While these methods will iterate over many quantities, and some quantities
    may fail early on in the test, the comparison method should continue
    until all quantities have been tested.

The value ``sigma`` should be used to compare quantities with uncertainties
by constructing intervals bounded by :math:`x\pm S\sigma`, where
``sigma``:math:`=S`. Quantities that do not have overlapping confidence
windows will be considered too different and should result in a ``False`` 
value being returned from the method.

The ``lower`` and ``upper`` arguments should be used to compare values
that do not have uncertainties. Both will be ``float`` values, with 
``lower`` less than or equal to ``upper``.  This functionality is
implemented with the :func:`serpentTools.utils.directCompare` function,
while the result is reported with :func:`serpentTools.utils.logDirectCompare`.

.. _dev-comp-message:

Use of messaging module
=======================

Below is a non-definitive nor comprehensive list of possible comparison cases
and the corresponding message that should be printed. Using a range of message
types allows the user to be able to easily focus on things that are really bad by
using our :ref:`verbosity` setting.

* Two objects contain different data sets, e.g. different dictionary values
  - |warn| displaying the missing items, and then apply test to items in both objects
* Two items are identically zero, or arrays of zeros - |debug|
* Two items are outside of the ``sigma`` confidence intervals - |error|
* Two items without uncertainties have relative difference

    * less than ``lower`` - |debug|
    * greater than or equal to ``upper`` - |error|
    * otherwise - |warn|

* Two items are identical - |debug|
* Two arrays are not of similar size - |error|


.. _dev-comp-utils:

High-level Logging and Comparison Utilities
===========================================

The :mod:`~serpentTools.utils` module contains a collection of functions
that can be used to compare quantities and automatically log results.
When possible, these routines should be favored over hand-writing 
comparison routines. If the situation calls for custom comparison 
functions, utilize or extend logging routines from :ref:`dev-comp-log`
appropriately.

.. autofunction:: serpentTools.utils.compare.compareDictOfArrays

.. autofunction:: serpentTools.utils.compare.getCommonKeys

.. autofunction:: serpentTools.utils.compare.directCompare

.. autofunction:: serpentTools.utils.compare.logDirectCompare

.. autofunction:: serpentTools.utils.compare.splitdictByKeys

.. autofunction:: serpentTools.utils.compare.getKeyMatchingShapes

.. autofunction:: serpentTools.utils.compare.getOverlaps

.. autofunction:: serpentTools.utils.compare.getLogOverlaps

.. autofunction:: serpentTools.utils.docstrings.compareDocDecorator

.. _dev-comp-log:

Low-level Logging Utilities
===========================

The :mod:`~serpentTools.messages` module contains a collection of functions
that can be used to notify the user about the results of a comparison
routine. 

.. autofunction:: serpentTools.messages.logIdentical

.. autofunction:: serpentTools.messages.logNotIdentical

.. autofunction:: serpentTools.messages.logAcceptableLow

.. autofunction:: serpentTools.messages.logAcceptableHigh

.. autofunction:: serpentTools.messages.logOutsideTols

.. autofunction:: serpentTools.messages.logIdenticalWithUncs

.. autofunction:: serpentTools.messages.logInsideConfInt

.. autofunction:: serpentTools.messages.logOutsideConfInt

.. autofunction:: serpentTools.messages.logDifferentTypes

.. autofunction:: serpentTools.messages.logMissingKeys

.. autofunction:: serpentTools.messages.logBadTypes

.. autofunction:: serpentTools.messages.logBadShapes

