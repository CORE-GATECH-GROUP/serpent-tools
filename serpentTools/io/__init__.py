"""
.. versionadded:: 0.6.2

Module for converting/creating ``serpentTools`` objects to/from other sources

High-level functions implemented here, such as :func:`toMatlab`, help the
:ref:`cli` in quickly converting files without launching a Python interpreter.
For example,

.. code::

    $ python -m serpentTools -v to-matlab my/depletion_dep.m
    INFO  : serpentTools: Wrote contents of my/depletion_dep.m to
    my/depletion_dep.mat

"""

from serpentTools.io.base import *  # noqa
