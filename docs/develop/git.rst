.. _git:

===============
Version Control
===============

``serpentTools`` uses :term:`git` for version control. All the source
code can be found at https://github.com/CORE-GATECH-GROUP/serpent-tools.

``serpentTools`` follows the `semantic versioning <https://semver.org/>`_
system, where the version number as found in ``setup.py``,
``serpentTools/__init__.py``, and ``docs/conf.py`` has the following form:
``major.minor.patch``, e.g. ``0.8.0`` or ``1.1.20``. Each of the numbers
should be incremented prior to new releases with the following designation:

1. Changes that are not backwards compatible should be denoted by
   incrementing the major number.
2. Changes that are backwards compatible and introduce sufficient new features
   to the API should be denoted by incrementing the minor number.
3. Changes that are largely internal and not recognizable by end-users should
   be denoted by incrementing the patch number

.. note::

    Until a stable 1.0.0 release, the positions are essentially shifted,
    e.g. the version is ``0.major.minor``

.. _dev-release:

Releases
========

Following a release, the following actions should be performed:

1. Archived and installable python files should be created
2. Archived and installable python files should be uploaded to the
   python package index, :term:`PyPI`
3. The tag should be pushed to GitHub and marked as a release, including information
   on the changes introduced in this release

This section details changes and procedures that, if followed, will increase chances
of a painless release.

Updating the package version
----------------------------

Before and after a release, the project version number should be updated in the
following places:

1. ``setup.py``
2. ``serpentTools/__init__.py``
3. ``docs/conf.py``

The new version should be indicative of the changes introduced between this release
and the previous release.

Generating distributions
------------------------

The new distribution, that can be uploaded to :term:`PyPI`, can be
generated with

.. code:: sh

   python setup.py sdist bdist_wheel

This will produce a source distribution and binary python wheel in the ``dist``
directory, each of the form ``dist/serpentTools-<version>.<extension>``.
Before tagging and pushing releases to :term:`PyPI`, the distribution should be
checked with

.. code:: sh

   twine check dist/serpentTools-<version>*

:term:`twine` will check that the package is compatible with the standards set
by :term:`PyPI` prior to uploading. Following a successful check, the distribution
can be pushed to the package index using

..code:: sh

    twine upload dist/serpentTools-<version>*

Tagging
-------

Releases should be done with `git tags <https://git-scm.com/docs/git-tag>`_ from the master branch 
and then pushed to GitHub. 
Annotated tags should be used and can be created with

.. code:: sh

    git tag -s <version>

Pushing these tags to GitHub creates a new 
`release <https://github.com/CORE-GATECH-GROUP/serpent-tools/releases>`_.
If a message is used, the messages should be a brief message describing the changes on this tag.
On the release page, a more detail list of changes, such as pull requests and issues closed, 
should be listed.

.. _dev-commitMessages:

Commit Messages
===============

When possible, please provide commit messages that:

* have a initial single summary line (~<50 characters),
* followed by a blank line,
* followed by as detailed of a description as possible wrapped
  to ~70 characters wide

Helpful and detailed commit messages can make searching for
changes easier and accelerate the review process.
As an added benefit, if your pull request is a single commit,
GitHub will automatically populate the request summary with your
commit message!

Other references:

* `git documentation on commit messages
  <https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project>`_
* `Good example commit message - Tim Pope
  <https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_
