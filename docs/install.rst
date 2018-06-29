.. _install:

============
Installation
============

In order to properly install this package, you need a version of
python that plays well with libraries like ``numpy`` and ``matplotlib``.
This is easy or less easy depending on your operating system, but we have
a brief walk through at :ref:`install-python-dist`.

.. note::

    Commands below that begin with ``$`` must be run from the
    terminal containing your preferred python distribution.
    Depending on operating system, this could be the normal
    terminal, or a modified prompt. See :ref:`install-python-dist`
    for more information if you are not sure.

Currently, the only way to obtain the package is via Github. If you 
only want a specific instance of the project, you can download
and install a zipped version of the project by following the
instructions in :ref:`install-release`.

If you want the entire history of the project, or want a constant
link to the most up-to-date development version of the project,
you can clone and install the package via ``git`` by following
the instructions in :ref:`install-git`.

For installing via GitHub and our ``setup.py`` script, having
`setuptools <https://pypi.org/project/setuptools/>`_ installed
makes things go a tad more smoothly. This will automatically
install some of the required packages for you when you
run the setup script.

.. _install-release:

Installing from a Release
=========================

1. Download the source code for the latest release from
   `GitHub releases <https://github.com/CORE-GATECH-GROUP/serpent-tools/releases/latest>`_
   as a ``.zip`` or ``.tar.gz`` compressed file.
1. Extract/decompress the contents somewhere convenient and memorable
1. Open your terminal and navigate to this directory::

    $ cd path/to/release

1. Install using our `setup script <https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/master/setup.py>`_::

    $ python setup.py install

1. Verify the install by running our test suite::

    $ python setup.py test


.. _install-git:

Installing via git
==================

The newest features are available on the ``develop`` branch before getting
pushed to the ``master`` branch. We try to give decent notice when features are
going to change via warning messages and our :ref:`changelog`, but changes
to the API and other functionality can occur across the develop branch.

1. Clone the repository and checkout the branch of your choosing. The default
   is ``develop``::

        $ git clone https://github.com/CORE-GATECH-GROUP/serpent-tools.git
        $ cd serpent-tools
        $ git checkout master

1. Install using our `setup script <https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/setup.py>`_::

    $ python setup.py install

1. Verify the install by running our test suite::

    $ python setup.py test

.. _install-python-dist:

Obtaining a Python Distribution
===============================

Obtaining a version of python into which ``serpent-tools`` can be installed
varies by operating system, with Windows requiring the most finesse. 

Linux/Mac/Unix-like Operating Systems
-------------------------------------

You're basically fine.

If you can open you terminal and run the following commands with ease, carry on::

    $ pip install -U pip setuptools numpy
    $ python -c "import numpy"

.. note::
    
    Installing ``numpy`` this way may require super user privileges, or passing
    ``--user`` as a flag

Windows
-------

The easiest and most painless way to obtain packages like ``numpy`` on Windows is with
either the `anaconda <https://www.anaconda.com/download/#windows>`_ or
`miniconda <https://conda.io/miniconda.html>`_ distributions. 
Each of these also includes the ``Anaconda Prompt`` which is a modified
terminal that plays better with Python.
The former comes with a few hundred packages, included most of the ones
needed for this project, bundled for you.
The latter is a very small distribution and requires you to install the packages
you want via the ``Anaconda Prompt``.
Should you choose this route, then you need to launch this prompt and install
with::

    $ conda install setuptools numpy matplotlib

This prompt is what you should use when following the instructions in
in :ref:`install`.
