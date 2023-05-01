.. _install:

============
Installation
============

In order to properly install this package, you need a version of
python that plays well with libraries like :term:`numpy` and :term:`matplotlib`.
This is easy or less easy depending on your operating system, but we have
a brief walk through at :ref:`install-python-dist`.

.. _install_terminals:

Terminal terminology
====================

Commands below that begin with ``$`` must be run from the
terminal containing your preferred python distribution, neglecting
the ``$``.
Depending on operating system, this could be the normal
terminal, or a modified prompt. See :ref:`install-python-dist`
for more information if you are not sure.

Commands that begin with ``>>>`` should be run inside of a python
environment.
The following would be a valid set of instructions to pass to your terminal,
printing a very basic python command::

    $ python -m "print('hello world')"
    hello world
    $ python
    >>> print('hello world')
    hello world

.. _install-pip:

Installing from pip
===================

Installing with :term:`pip` will pull from the python package index and is
the simplest way to install::

    $ pip install serpentTools

This will install the latest release from https://pypi.org/project/serpentTools/.

Some additional packages, like ``pandas``, are not needed for core functionality
but do provide nice capabilities. These can be picked up through the "extras"
dependency group with::

    $ pip install "serpentTools[extras]"

.. _install-release:

Installing from a Release
=========================

1. Download the source code for the latest release from
   `GitHub releases <https://github.com/CORE-GATECH-GROUP/serpent-tools/releases/latest>`_
   as a ``.zip`` or ``.tar.gz`` compressed file.
2. Extract/decompress the contents somewhere convenient and memorable
3. Open your terminal and navigate to this directory::

    $ cd path/to/release

4. Install with :term:`pip`

    $ pip install .

.. _install-git:

Installing via git
==================

1. Clone the repository and checkout the branch of your choosing. The default
   is ``main``::

        $ git clone https://github.com/CORE-GATECH-GROUP/serpent-tools.git
        $ cd serpent-tools
        $ git checkout main

2. Install all utilities with using :term:`pip`

    $ pip install -e ".[extras,test]"

3. Verify the install by running our test suite::

    $ pytest tests

.. _install-python-dist:

Obtaining a Python Distribution
===============================

Obtaining a version of python into which ``serpent-tools`` can be installed
varies by operating system, with Windows requiring the most finesse. 

Linux/Mac/Unix-like Operating Systems
-------------------------------------

If you don't have :term:`numpy` installed, you will have to obtain it from
your package manager or from pip::

    # ubuntu
    $ sudo apt-get install python-numpy
    # pip
    $ sudo pip install --upgrade numpy

If you already have :term:`numpy`, then the :term:`pip` installtion
process will take care of our other dependencies.

Windows
-------

The easiest and most painless way to obtain packages like :term:`numpy` on Windows is with
either the :term:`Anaconda` or :term:`Miniconda` distributions. 
Each of these also includes the :term:`Anaconda Prompt` which is a modified
terminal that plays better with Python.
The former comes with a few hundred packages, included most of the ones
needed for this project, bundled for you.
The latter is a very small distribution and requires you to install the packages
you want via :term:`conda`.
Should you choose this route, then you need to launch the :term:`Anaconda Prompt`
and install with::

    $ conda install setuptools numpy matplotlib pyyaml

This prompt is what you should use when following the instructions in
in :ref:`install`.
