.. _pr-checklist:

======================
Pull Request Checklist
======================

Below is the criteria that will be used in the process of
reviewing pull requests (PR):

#. The content of the PR fits within the scope of the project - :ref:`project-scope`
#. The code included in the PR is written in good
   `pythonic  <https://stackoverflow.com/a/25011492>`_
   fashion, and follows the style of the project - :ref:`code-style`
#. The code directly resolves a previously raised issue - :ref:`issues`
#. PR does not cause unit tests and builds to fail
#. Changes are reflected in documentation - :ref:`documentation`

.. _dev-ci:

CI Testing
==========

We utilize `Travis <https://travis-ci.org/>`_ to perform our
continuous integration, or :term:`CI`. 
Two types of tests are run: unit tests and tests on the example
notebooks. The former are used to perform more granular testing
over the project, while the latter ensure our example notebooks
are runnable.

.. _dev-unittests:

Unit Tests
----------

Unit tests should cover all public methods and a sufficient
set of use cases to reduce the amount of bugs that make it into releases.
Unit tests are run using :term:`pytest` from the project directory::

    $ ls
    examples/ LICENSE serpentTools/ tests/ ...
    $ pytest

Unit tests rely on data files that are shipped with the repository. These
files are found using the environment variable ``SERPENT_TOOLS_DATA``, which
should point to a directory containing the data files. For a temporary fix,
this variable can be included in the command line, with::

    $ SERPENT_TOOLS_DATA=/path/to/data/files pytest

Alternatively, one can make the fix permanent by including the line
``export SERPENT_TOOLS_DATA=/path/to/data/files`` into a shell startup
file, e.g. ``~/.bashrc``.

.. note::

    The notebook test script uses a temporary directory, which may not
    find files if ``SERPENT_TOOLS_DATA`` is a relative path. Using the
    absolute path is recommended.

If the ``pytest-cov`` package is installed, you can view the coverage, or
how much of the project is touched by tests, with::

    $ pytest --cov=serpentTools

It is always preferable to increase coverage to decreasing coverage, but minor
deviations are acceptable. The coverage is not a factor in passing or failing
CI, but substantial changes to the test suite should serve a valid purpose if
the coverage does decrease.

.. _dev-notebooks:

Notebook Tests
--------------

We try to provide a :term:`Jupyter notebook` for each of the main readers
in the package. These are converted to be used in our main documentation, and serve
as a handy way for new users to discover the features provided with ``serpentTools``.
In order to ensure that these are valid notebooks as changes are introduced, our :term:`CI`
converts these to python scripts and runs them using 
`the test notebooks script <https://github.com/CORE-GATECH-GROUP/serpent-tools/blob/develop/scripts/travis/testNotebooks.sh>`_. 
It is beneficial to run this script during major changes to the API, as well as correcting any
errors or deprecated/removed features.

.. _dev-lint:

Lint
====

We also recommend using a :term:`linter` to analyze the project for
code that might induce errors and does not conform to our
style guide - :ref:`code-style`. This is applied on proposed
changes using `flake8 <http://flake8.pycqa.org/en/latest/index.html>`_.
Code to be merged into this project should not cause any unit tests
to break, nor introduce lint.
If you are working on a feature/bug-fix branch, you can compare
the lint that would be introduced with

.. code::

    $ git diff --unified=0 develop | flake8 --diff

Here, ``develop`` is the intended target branch into which these changes
will be merged.
