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


.. _dev-ci

Unit Tests and CI Testing
=========================

We utilize `Travis <https://travis-ci.org/>`_ to perform our
continuous integration, or :term:`CI`. 
Unit tests should cover all public methods and a sufficient
set of use cases to reduce the amount of bugs that make it
into releases.

Our test suite can be run from the main directory of the
project with

.. code::

    $ python setup.py test

Individual test files can also be run with

..code::

    $ python my_test_scipt.py

We also utilize a :term:`linter` to analyze the project for
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
