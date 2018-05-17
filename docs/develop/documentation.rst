.. |jconvert| replace:: ``jupyter nbconvert --to=rst <file>``

.. |rst| replace:: ``.rst``

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


.. note::

    For multi-line docstrings, like the longer ``depmtx`` above,
    Leave a full blank line between the first line of the docstring,
    the summary, and the rest of the documentation

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

.. _docs-deprecate:

Deprecation
-----------

If an object is deprecated or will be modified in future versions, then the
:py:func:`~serpentTools.messages.deprecated` and
:py:func:`~serpentTools.messages.willChange` decorators should be applied to
the object, and a note should be added to the docstring indicating as much.

.. _jupyterExamples:

Examples
========

When possible, features should be demonstrated, either through
Jupyter notebooks in the ``examples/`` directory, or with an
``Examples`` section in the docstring.
Specifically, all readers should be demonstrated as Jupyter notebooks
that detail the typical usage, user control settings, and examples
of how the data is stored and accessed.

.. _docs-convert:

Converting
----------

These Jupyter notebooks can be converted to |rst| files for inclusion
in the manual with the command |jconvert| .
However, there are some tweaks that should be made so that the documentation
renders properly and has helpful links to objects in the project.

The ``nbconvert`` command will place the following blocks around python code::

    .. code:: ipython3

        print('hello world!')

    .. parsed-literal::

        hello world!

When building this documentation on `readthedocs <serpent-tools.readthedocs.io/latest>`_,
the ``ipython3`` statement can cause the code not to be rendered. 
This is summarized 
`here <https://github.com/CORE-GATECH-GROUP/serpent-tools/issues/123#issuecomment-387788909>`_
, but it appears that the ``ipython3`` lexer 
`is not trivially installed <https://github.com/jupyter/nbconvert/issues/528>`_
and is not found on readthedocs.
For now, all these instances of ``ipython3`` should be removed from the |rst| version of the notebook so that
the wonderful code examples are proudly displayed in our documentation.
The above code block should be replaced with::

    .. code:: 

        print('hello world!')

    .. parsed-literal::

        hello world!

Upon conversion, move the file into the ``docs/examples`` directory and include the 
file name in ``docs/examples/index.rst``.

.. _docs-images:

Images
------

Executing |jconvert| will create a directory containing the images
contained in the notebook.
When moving the |rst| version of the notebook into the ``docs/examples`` folder, make sure
that all links to images are correct.

.. _docs-API-link:

Linking to the API
------------------

When referring to python classes, attributes, functions, or methods, it is 
strongly recommended to utilize 
`python object references <http://www.sphinx-doc.org/en/stable/domains.html#python-roles>`_.
This creates direct links from your text to the object declaration in our
`api section <http://serpent-tools.readthedocs.io/en/latest/api/index.html>`_ that allows
people to get more detail on whatever you are referencing, powered by the 
``docstrings`` on that object. Two such examples are given below:

* ``:py:class:`serpentTools.parsers.depletion.DepletionReader```
  becomes :py:class:`serpentTools.parsers.depletion.DepletionReader`
* ``:py:meth:`~serpentTools.objects.materials.DepletedMaterial.plot``` is shortened to
  :py:meth:`~serpentTools.objects.materials.DepletedMaterial.plot`

.. _docs-verify:

Verifying
=========

You worked hard on this documentation, and we want your great work to be properly displayed 
once completed.
In order to reduce the chances of some errors, try running the following from inside the
``docs`` directory::

    $ make clean html

Navigate to the files created in ``_build/html`` to ensure that images are loaded properly,
code is rendered properly, and the converted notebook looks exactly how you expect it to
look. 

.. warning::

    If there is an issue with rendering your example, we will likely call upon you to fix these
    issues.


.. note::

    Building the documentation locally requires ``sphinx`` and a handful of other
    packages. Installing these is outside the scope of this guide, partially because
    `the sphinx team has a great guide already <http://www.sphinx-doc.org/en/master/usage/installation.html>`_.
    Check this out if you are having issues running the ``make clean install`` commands from the 
    docs directory.

.. _docs-add-API:

Adding Objects to API
=====================

New reader or container objects should be included in the 
`api section of the documentation <http://serpent-tools.readthedocs.io/en/latest/api/index.html>`_, 
as with any function that the end user may utilize.
For documenting these, we utilize the 
`sphinx autodoc <http://www.sphinx-doc.org/en/master/ext/autodoc.html>`_ features to use the 
docstrings to automatically document new features.
This is most simply done by calling ``.. autoclass::`` or ``..autofunction::`` like::

    .. autofunction:: serpentTools.plot.plot
    .. autoclass:: serpentTools.parsers.results.ResultsReader

For new readers, those should be included in their own file, such as ``docs/api/myNewReader.rst``, 
which can be as bare as::

    My New Reader
    =============

    .. autoclass:: serpentTools.parsers.new.MyNewReader

Be sure to include your new file in ``docs/api/index.rst``, or else your file will be 
left out of the documentation.
Proper documentation of the class or function requires thorough and concise
documentation of all attributes, class methods, and construction arguments.
Follow the above guides, such as :ref:`docstrings`, and this process *should*
go smoothly.

