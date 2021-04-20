=============
serpent-tools
=============

.. image:: https://github.com/CORE-GATECH-GROUP/serpent-tools/actions/workflows/testing.yaml/badge.svg?branch=develop
    :target: https://github.com/CORE-GATECH-GROUP/serpent-tools/actions/workflows/testing.yaml
    :alt: Build status - develop

.. image:: https://readthedocs.org/projects/serpent-tools/badge/?version=latest
    :target: http://serpent-tools.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://badge.fury.io/py/serpentTools.svg
   :target: https://badge.fury.io/py/serpentTools
   :alt: PyPi badge

.. image:: https://zenodo.org/badge/DOI/10.1080/00295639.2020.1723992.svg
   :target: https://doi.org/10.1080/00295639.2020.1723992
   :alt: Nuclear Science and Engineering 10.1080/00295639.2020.1723992

A suite of parsers designed to make interacting with
``SERPENT`` [1]_ output files simple and flawless.

The ``SERPENT`` Monte Carlo code
is developed by VTT Technical Research Centre of Finland, Ltd.
More information, including distribution and licensing of ``SERPENT`` can be
found at `<http://montecarlo.vtt.fi>`_

Installation
============

``serpentTools`` can be installed with ``pip`` using::

   $ python -m pip install --user --upgrade pip serpentTools

For more detailed instructions, including operating-system specific
instructions and building from source, see
`Installation Guide <http://serpent-tools.readthedocs.io/en/latest/install.html>`_.

Issues
======

If you have issues installing the project, find a bug, or want to add a feature,
the `GitHub issue page <https://github.com/CORE-GATECH-GROUP/serpent-tools/issues>`_
is the best place to do that.

Support
=======

The development of ``serpentTools`` is supported by the following organizations:

* `USNC-Tech <https://usnc.com/space>`_

References
==========

The Annals of Nuclear Energy article should be cited for all work
using ``SERPENT``. If you are using this project, please considering
citing with

* Andrew Johnson, Dan Kotlyar, Stefano Terlizzi, and Gavin Ridley,
  "`serpentTools: A Python Package for Expediting Analysis with
  Serpent <https://doi.org/10.1080/00295639.2020.1723992>`_,"
  *Nuc. Sci. Eng*, (2020).

Also, let us know if you publish work using this package! We try and
keep an up-to-date list of works using serpentTools [2]_, and would be
happy to include more.

.. [1] Leppanen, J. et al. (2015) "The Serpent Monte Carlo code: Status,
    development and applications in 2013." Ann. Nucl. Energy, `82 (2015) 142-150
    <http://www.sciencedirect.com/science/article/pii/S0306454914004095>`_

.. [2] https://serpent-tools.readthedocs.io/en/latest/publications.html
