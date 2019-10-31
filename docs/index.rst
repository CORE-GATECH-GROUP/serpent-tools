.. serpentTools documentation master file, created by
   sphinx-quickstart on Tue Oct 10 20:03:11 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to serpentTools's documentation!
========================================

.. only:: html

    .. image:: https://travis-ci.org/CORE-GATECH-GROUP/serpent-tools.svg?branch=develop
        :target: https://travis-ci.org/CORE-GATECH-GROUP/serpent-tools
        :alt: Build status - develop

    .. image:: https://readthedocs.org/projects/serpent-tools/badge/?version=latest
        :target: http://serpent-tools.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

    .. image:: https://badge.fury.io/py/serpentTools.svg
       :target: https://badge.fury.io/py/serpentTools
       :alt: PyPi badge

    .. image:: https://zenodo.org/badge/102786755.svg
       :target: https://zenodo.org/badge/latestdoi/102786755
       :alt: Zenodo DOI 10.5281/zenodo.1301036
  
A suite of parsers designed to make interacting with
:term:`SERPENT` [serpent]_ output files simple and flawless. 

The :term:`SERPENT` Monte Carlo code
is developed by VTT Technical Research Centre of Finland, Ltd.
More information, including distribution and licensing of :term:`SERPENT` can be
found at `<http://montecarlo.vtt.fi>`_

The Annals of Nuclear Energy article should be cited for all work
using :term:`SERPENT`. 

.. admonition:: Preferred citation for attribution
    :class: tip

    Andrew Johnson, Dan Kotlyar, Gavin Ridley, Stefano Terlizzi, & Paul Romano.
    (2018, June 29). "`serpent-tools: A collection of parsing tools and
    data containers to make interacting with SERPENT outputs easy, intuitive, and flawless.
    <https://doi.org/10.5281/zenodo.1301036>`_,".

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
   utilities/index
   variableGroupsTop
   command-line
   develop/index
   license
   contributors
   glossary

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. [serpent] Leppanen, J. et al. (2015) "The Serpent Monte Carlo code: Status,
    development and applications in 2013." Ann. Nucl. Energy, `82 (2015) 142-150
    <http://www.sciencedirect.com/science/article/pii/S0306454914004095>`_
