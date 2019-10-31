.. _git:

===============
Version Control
===============

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

Releases should be done with `git tags <https://git-scm.com/docs/git-tag>`_ from the master branch 
and then pushed to GitHub. 
Annotated tags should be used and can be created with::

    git tag -a <version>
    git tag -s <version>
    git tag -m <msg> <version>

Pushing these tags to GitHub creates a new 
`release <https://github.com/CORE-GATECH-GROUP/serpent-tools/releases>`_.
If a message is used, the messages should be a brief message describing the changes on this tag.
On the release page, a more detail list of changes, such as pull requests and issues closed, 
should be listed.

In the future, python installers such as 
`python wheels <https://pythonwheels.com/>`_ can be built by running ``python setup.py bdist_wheel``.
These can be manually uploaded to the release page, or the 
`python package index <https://pypi.python.org/pypi>`_ for users who only want the python
files without examples or documentation.
Before and after a release, the project version number should be updated in the
following places:

1. ``setup.py``
2. ``serpentTools/__init__.py``
3. ``docs/conf.py``


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
