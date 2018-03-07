.. _git:

===============
Version Control
===============

This project utilizes `versioneer <https://github.com/warner/python-versioneer>`_
to update the project verion based on release and commit history.
Using this tool allows the project version to match :pep:`440` style versions, with
minor exceptions for developer (non-public release) versions.
For public releases, where sufficient changes have been made through added features,
bug fixes, or wholesale changes, the version will be of the form ``major.release.patch``.
Changes in ``major`` indicate vast user-facing changes to
the core functionality and/or API, while changes to ``release`` indicate a 
new feature added or substantial improvement that does not alter the user-facing API.
In the event of bug fixes or minor tweaks, the ``patch`` number should be incremented.

For non-public releases, e.g. the develop branch, ``versioneer`` includes some additional
information in the project version. Here, the version is of the form
``major.minor.patch[+/-]N.commit[.dirty]``.
``[+/-]N`` indicates that this version is ``N`` commits ahead of or behing the latest
public release, and ``commit`` is the short version of the latest commit on the branch for this 
version. ``dirty`` will be present if the current version has uncommitted changes.
This level of precision with respect to versioning allows for easy identification if
people are working on multiple branches and/or having issues.

Releases
========

Releases should be done with `git tags <https://git-scm.com/docs/git-tag>`_ from the master branch 
and then pushed to GitHub. 
``versioneer`` works by locating these tags in the git history, and works best with annotated tags,
which can be created with::

    git tag -a <version>
    git tag -s <version>
    git tag -m <msg> <version>

Pushing these tags to GitHub creates a new 
`release <https://github.com/CORE-GATECH-GROUP/serpent-tools/releases>`_, and
shares the tag with all who have cloned the repository.
If a message is used, the messages should be a brief message describing the changes on this tag.
On the release page, a more detail list of changes, such as pull requests and issues closed, 
should be listed.

In the future, python installers such as 
`python wheels <https://pythonwheels.com/>`_ can be built by running ``python setup.py bdist_wheel``.
These can be manually uploaded to the release page, or the 
`python package index <https://pypi.python.org/pypi>`_ for users who only want the python
files without examples or documentation.


