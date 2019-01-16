.. _install:

============
Installation
============

In order to properly install this package, you need a version of
python that plays well with libraries like :term:`numpy` and :term:`matplotlib`.
This is easy or less easy depending on your operating system, but we have
a brief walk through at :ref:`install-python-dist`.

.. note::

    Commands below that begin with ``$`` must be run from the
    terminal containing your preferred python distribution.
    Depending on operating system, this could be the normal
    terminal, or a modified prompt. See :ref:`install-python-dist`
    for more information if you are not sure.

.. _install-pip:

Installing from pip
===================

:term:`pip` is the easiest way to install the latest version of 
``serpentTools``. This can be done with::

   $ python -m pip install --user --upgrade pip serpentTools

This installs the latest ``serpentTools`` release and upgrades your version of ``pip``
along the way. When a new release is issued, run the command again to install
the updated version.
If you have issues installing :term:`numpy` on Windows, please consult 
:ref:`install-python-dist`

.. _install-release:

Installing from a Release
=========================

1. Download the source code for the latest release from
   `GitHub releases <https://github.com/CORE-GATECH-GROUP/serpent-tools/releases/latest>`_
   as a ``.zip`` or ``.tar.gz`` compressed file.
2. Extract/decompress the contents somewhere convenient and memorable
3. Open your terminal and navigate to this directory::

    $ cd path/to/release

4. Install using our `setup script <https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/master/setup.py>`_::

    $ python setup.py install

5. Verify the install by running our test suite::

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

2. Install using our `setup script <https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/setup.py>`_::

    $ python setup.py install

3. Verify the install by running our test suite::

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
    
    Installing :term:`numpy` this way may require super user privileges, or passing
    ``--user`` as a flag

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
Should you choose this route, then you need to launch this prompt and install
with::

    $ conda install setuptools numpy matplotlib

This prompt is what you should use when following the instructions in
in :ref:`install`.
