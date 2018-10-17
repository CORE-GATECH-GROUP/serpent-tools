=============
serpent-tools
=============

.. image:: https://travis-ci.org/CORE-GATECH-GROUP/serpent-tools.svg?branch=develop
    :target: https://travis-ci.org/CORE-GATECH-GROUP/serpent-tools
    :alt: Build status - develop

.. image:: https://readthedocs.org/projects/serpent-tools/badge/?version=latest
    :target: http://serpent-tools.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://zenodo.org/badge/102786755.svg
   :target: https://zenodo.org/badge/latestdoi/102786755
   :alt: Zenodo DOI 10.5281/zenodo.1301036

A suite of parsers designed to make interacting with
``SERPENT`` [1]_ output files simple and flawless.

The ``SERPENT`` Monte Carlo code
is developed by VTT Technical Research Centre of Finland, Ltd.
More information, including distribution and licensing of ``SERPENT`` can be
found at `<http://montecarlo.vtt.fi>`_

Installation
============

The ``serpentTools`` package can be downloaded either as a git repository or
as a zipped file. Both can be obtained through the ``Clone or download`` option
at the
`serpent-tools GitHub <https://github.com/CORE-GATECH-GROUP/serpent-tools>`_.

For more detailed instructions, including operating-system specific
instructions, see
`Installation Guide <http://serpent-tools.readthedocs.io/en/latest/install.html>`_.

Once the repository has been downloaded or extracted from zip, the package
can be installed with::

    cd serpentTools
    python setup.py install
    python setup.py test

Installing with `setuptools <https://pypi.python.org/pypi/setuptools/38.2.4>`_
is preferred over the standard ``distutils`` module. ``setuptools`` can be
installed with ``pip`` as::

    pip install -U setuptools

Installing in this manner ensures that the supporting packages,
like ``numpy`` are installed and up to date.

Issues
======

If you have issues installing the project, find a bug, or want to add a feature,
the `GitHub issue page <https://github.com/CORE-GATECH-GROUP/serpent-tools/issues>`_
is the best place to do that.

References
==========

The Annals of Nuclear Energy article should be cited for all work
using ``SERPENT``. If you wish to cite this project, please cite as::

    Andrew Johnson, Dan Kotlyar, Gavin Ridley, Stefano Terlizzi, & Paul Romano.
    (2018, June 29). "`serpent-tools: A collection of parsing tools and
    data containers to make interacting with SERPENT outputs easy, intuitive, and flawless.
    <https://doi.org/10.5281/zenodo.1301036>`_,".

.. [1] Leppanen, J. et al. (2015) "The Serpent Monte Carlo code: Status,
    development and applications in 2013." Ann. Nucl. Energy, `82 (2015) 142-150
    <http://www.sciencedirect.com/science/article/pii/S0306454914004095>`_
