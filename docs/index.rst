.. serpentTools documentation master file, created by
   sphinx-quickstart on Tue Oct 10 20:03:11 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to serpentTools's documentation!
========================================

.. only:: html

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
:term:`SERPENT` [serpent]_ output files simple and flawless.

The :term:`SERPENT` Monte Carlo code
is developed by VTT Technical Research Centre of Finland, Ltd.
More information, including distribution and licensing of :term:`SERPENT` can be
found at `<http://montecarlo.vtt.fi>`_

The Nuclear Science and Engineering article should be cited for all work
using :term:`SERPENT`.

.. admonition:: Preferred citation for attribution
    :class: tip

    Andrew Johnson, Dan Kotlyar, Stefano Terlizzi, and Gavin Ridley,
    "`serpentTools: A Python Package for Expediting Analysis with
    Serpent <https://doi.org/10.1080/00295639.2020.1723992>`_,"
    *Nuc. Sci. Eng*, **194** (11), pp. 1016-1024 (2020).

Also, let us know if you publish work using this package! We try and
keep an up-to-date list of `works using serpentTools`_, and would be
happy to include more.

If you want to refer to a specific version, follow the `Zenodo DOI
<https://doi.org/10.5281/zenodo.1301035>`_. This will resolve to the latest
version, with links to earlier releases.

 .. _works using serpentTools: https://github.com/CORE-GATECH-GROUP/serpent-tools/wiki/Publications-using-serpentTools

Support
=======

The development of ``serpentTools`` is supported by the following organizations:

* `USNC-Tech <https://usnc.com/space>`_

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   overview
   install
   changelog
   examples/index
   readers.rst
   containers.rst
   samplers.rst
   settings.rst
   misc.rst
   variableGroups
   command-line
   develop/index
   license
   contributors
   publications
   glossary

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. [serpent] Leppanen, J. et al. (2015) "The Serpent Monte Carlo code: Status,
    development and applications in 2013." Ann. Nucl. Energy, `82 (2015) 142-150
    <http://www.sciencedirect.com/science/article/pii/S0306454914004095>`_
