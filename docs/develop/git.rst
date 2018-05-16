.. _git:

===============
Version Control
===============

This project utilizes `versioneer <https://github.com/warner/python-versioneer>`_
to update the project version based on release and commit history.
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
``[+/-]N`` indicates that this version is ``N`` commits ahead of or behind the latest
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


.. _dev-commitMessages:

Commit Messages
---------------

Helpful and detailed commit messages can make searching for changes easier and 
accelerate the review process.
Here is the sections `straight from the git documentation <https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project>`_ on commit messages:

.. highlights::

    The last thing to keep in mind is the commit message. 
    Getting in the habit of creating quality commit messages makes using 
    and collaborating with Git a lot easier. As a general rule, your
    messages should start with a single line that’s no more than about 
    50 characters and that describes the changeset concisely, followed 
    by a blank line, followed by a more detailed explanation.
    The Git project requires that the more detailed explanation include 
    your motivation for the change and contrast its implementation with 
    previous behavior — this is a good guideline to follow.
    It’s also a good idea to use the imperative present tense in these 
    messages. In other words, use commands.
    Instead of “I added tests for” or “Adding tests for,” use “Add tests for.” 

Here is a useful template for a good commit message via 
`Tim Pope <https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_

.. code-block:: none

    Capitalized, short (50 chars or less) summary

    More detailed explanatory text, if necessary.  Wrap it to about 72
    characters or so.  In some contexts, the first line is treated as the
    subject of an email and the rest of the text as the body.  The blank
    line separating the summary from the body is critical (unless you omit
    the body entirely); tools like rebase can get confused if you run the
    two together.

    Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
    or "Fixes bug."  This convention matches up with commit messages generated
    by commands like git merge and git revert.

    Further paragraphs come after blank lines.

    - Bullet points are okay, too

    - Typically a hyphen or asterisk is used for the bullet, followed by a
        single space, with blank lines in between, but conventions vary here

      - Use a hanging indent
