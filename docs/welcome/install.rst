.. _install:

============
Installation
============

The ``serpentTools`` package can be downloaded either as a git repository or
as a zipped file. Both can be obtained through the ``Clone or download`` option
at the
`serpent-tools GitHub <https://github.com/CORE-GATECH-GROUP/serpent-tools>`_.

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