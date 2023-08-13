.. _git:

===============
Version Control
===============

``serpentTools`` uses :term:`git` for version control. All the source
code can be found at https://github.com/CORE-GATECH-GROUP/serpent-tools.

``serpentTools`` follows the `semantic versioning <https://semver.org/>`_
system, where the released versions have the following form
``{major}.{minor}.{patch}``, where

1. Changes that are not backwards compatible should be denoted by
   incrementing the major number.
2. Changes that are backwards compatible and introduce sufficient new features
   to the API should be denoted by incrementing the minor number.
3. Changes that are largely internal and not recognizable by end-users should
   be denoted by incrementing the patch number

Prior to a release, there may be pre-releases made signified with a "release candidate"
label. These can be identified with a trailing ``.rc.{N}`` e.g., ``0.10.0.rc.5`` would be
the fifth release candidate for version ``0.10.0``.

For developers and users who are using the "bleeding edge" version straight from source
between releases, the version string may be more complex. As this is being written,
the version string is ``0.9.6.dev14+g0d7b6d6.d20230811``. The most recent release
from the time of this writing was ``0.9.5``, so the first part ``0.9.6.dev`` means
we are ahead of version ``0.9.5``, and does not mean the next version **must** be
``0.9.6``.

The ``.dev14+g0d7b6b6`` indicates we are currently ``14`` commits ahead of the last
tag, and the content following the ``+g`` is the SHA-1 hash of the most recent
commit.

Finally, if we have any uncommitted changes, the version string will conclude with
an indicator of the installed date. Which in this case is August 11th, 2023.

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

Package version is pulled using ``setuptools-scm`` based on git tags. Therefore nothing
is needed to be changed in order to change the version. Only the creation of new tags.

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
