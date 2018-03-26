.. _welcome:

=============
serpent-tools
=============

    A suite of parsers designed to make interacting with
    ``SERPENT`` [1]_ output files simple and flawless.

The ``SERPENT`` Monte Carlo code
is developed by VTT Technical Research Centre of Finland, Ltd.
More information, including distribution and licensing of ``SERPENT`` can be
found at `<montecarlo.vtt.fi>`_

Installation
------------

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

Issues
------

If you have issues installing the project, find a bug, or want to add a feature,
the `GitHub issue page <https://github.com/CORE-GATECH-GROUP/serpent-tools/issues>`_
is the best place to do that.

Contributors
------------

Here are all the wonderful people that helped make this project happen

* `Andrew Johnson <https://github.com/drewejohnson>`_
* `Dr. Dan Kotlyar <https://github.com/CORE-GATECH>`_
* `Stefano Terlizzi <https://github.com/sallustius>`_
* `Gavin Ridley <https://github.com/gridley>`_

References
----------

The Annals of Nuclear Energy article should be cited for all work
using ``SERPENT``. If you wish to cite this project, please cite as::

    url{@serpentTools
        author = {Andrew Johnson and Dan Kotlyar and Stefano Terlizzi and Gavin Ridley},
        title = {serpentTools: A suite of parsers designed to make
        interacting with SERPENT outputs simple and flawless},
        url = {https://github.com/CORE-GATECH-GROUP/serpent-tools},
        year = {2017}
    }

.. [1] Leppanen, J. et al. (2015) "The Serpent Monte Carlo code: Status,
    development and applications in 2013." Ann. Nucl. Energy, `82 (2015) 142-150
    <http://www.sciencedirect.com/science/article/pii/S0306454914004095>`_
