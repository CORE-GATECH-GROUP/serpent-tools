.. _documentation:

=============
Documentation
=============

All public functions, methods, and classes should have adequate documentation
through docstrings, examples, or inclusion in the appropriate
file in the ``docs`` directory.
Good forethought into documenting the code helps resolve issues and,
in the case of docstrings, helps produce a full manual.

.. _docstrings:

Docstrings
==========

Docstrings are defined in :pep:`257` and are characterized by
``"""triple double quotes"""``.
These can be used to reduce the effort in creating a full manual,
and can be viewed through python consoles to give the user insight
into what is done, what is required, and what is returned from a
particular object. This project uses
`numpy style docstrings <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#docstring-standard>`_,
examples of which are given below

Functions and Methods
---------------------

Below is the :py:func:`~serpentTools.parsers.depmtx` function annotated using
short and longer docstrings::

    def depmtx(filePath):
        """Return t, no, zai, a, and n1 values from the depmtx file."""

or::

    def depmtx(filePath):
        """
        Read the contents of the ``depmtx`` file and return contents

        .. note::

            If ``scipy`` is not installed, matrix ``A`` will be full.
            This can cause some warnings or errors if sparse or
            non-sparse solvers are used.

        Parameters
        ----------
        fileP: str
            Path to depletion matrix file

        Returns
        -------
        t: float
            Length of time
        n0: numpy.ndarray
            Initial isotopic vector
        zai: numpy.array
            String identifiers for each isotope in ``n0`` and ``n1``
        a: numpy.array or scipy.sparse.csc_matrix
            Decay matrix. Will be sparse if scipy is installed
        n1: numpy.array
            Final isotopic vector
        """

Both docstrings indicate what the function does, and what is returned.
The latter, while more verbose, is preferred in most cases, for the following
reasons. First, far more information is yielded to the reader. Second,
the types of the inputs and outputs are given and clear. Some IDEs can obtain
the expected types from the docstrings and inform the user if they are using
an incorrect type.

More content can be added to the docstring, including

* Raises - Errors/warnings raised by this object
* See Also - follow up information that may be useful
* Yields - If this object is a generator. Similar to Returns

Classes
-------

Classes can have a more lengthy docstring, as they often include
attributes to which the class has access. Below is an example of the
docstring for the :py:class:`~serpentTools.parsers.DepletionReader`::

    """
    Parser responsible for reading and working with depletion files.

    Parameters
    ----------
    filePath: str
        path to the depletion file

    Attributes
    ----------
    materials: dict
        Dictionary with material names as keys and the corresponding
        :py:class:`~serpentTools.objects.DepletedMaterial` class
        for that material as values
    metadata: dict
        Dictionary with file-wide data names as keys and the
        corresponding dataas values, e.g. 'zai': [list of zai numbers]
    settings: dict
        names and values of the settings used to control operations
        of this reader

    """

Class docstrings can be added to the class signature, or to the ``__init__``
method, as::

    class Demo(object):
        """
        Demonstration class

        Parameters
        ----------
        x: str
            Just a string

        Attributes
        ----------
        capX: str
            Capitalized x
        """

or::

    def __init__(self, x):
        """
        Demonstration class

        Parameters
        ----------
        x: str
            Just a string

        Attributes
        ----------
        capX: str
            Capitalized x
        """

Deprecation
-----------

If an object is deprecated or will be modified in future versions, then the
:py:func:`~serpentTools.messages.deprecated` and
:py:func:`~serpentTools.messages.willChange` decorators should be applied to
the object, and a note should be added to the docstring indicating as much.

.. _examples:

Examples
========

When possible, features should be demonstrated, either through
Jupyter notebooks in the ``examples/`` directory, or with an
``Examples`` section in the docstring.
Specifically, all readers should be demonstrated as Jupyter notebooks
that detail the typical usage, user control settings, and examples
of how the data is stored and accessed.

These Jupyer notebooks can be converted to ``.rst`` files for inclusion
in the manual with the command ``jupyter nbconvert --to=rst``.
