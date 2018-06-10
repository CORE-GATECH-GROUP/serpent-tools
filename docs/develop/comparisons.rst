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
``lower`` less than or equal to ``upper``. These should be be used
when comparing the relative differences between quantities from ``self``
and ``other`` with something like::

   # selfV is the "reference" value from self
   # otherV is the value from ``other``
   >>> relDiff = abs(otherV - selfV)
   >>> if selfV > 1E-6:
   ...     relDiff /= selfV
   >>> if relDiff < lower:
   ...     # close enough, move along
   >>> elif relDiff >= upper:
   ...     # consider test a failure; print an error
   >>> else:
   ...     # close but not close enough; print a warning
   ...     # but don't treat as a failure

It is likely that the ``BaseObject`` or :mod:`serpentTools.utils` module
will have some methods/functions for expediting this process, but the 
procedure for all cases should follow this behavior.

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

    * less than ``lower`` - |info|
    * greater than or equal to ``upper`` - |error|
    * otherwise - |warn|

* Two items are in good agreement - |info|
* Two arrays are not of similar size - |error|
