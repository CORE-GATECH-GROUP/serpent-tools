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
`numpydoc style docstrings <https://numpydoc.readthedocs.io/en/latest/format.html>`_::

    def foo(a, b=None):
        """Simple one line docstring

        Parameters
        ----------
        a : float
            Some value
        b : bool, optional
            A flag

        Returns
        -------
        returnType
            Description of the return type

        """

Deprecation
-----------

If an object is deprecated or will be modified in future versions, then the
:func:`~serpentTools.messages.deprecated` and
:func:`~serpentTools.messages.willChange` decorators should be applied to
the object, and a note should be added to the docstring indicating as much.
This can be done with the sphinx `deprecated 
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/
directives.html#directive-deprecated>`_ directive.

.. _docs-jupyter-examples:

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
in the manual with the command |jconvert|, with::

    $ jupyter nbconvert --to=rst Notebook.ipynb

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

It is recommended to use the template in ``examples/rstTemplate.tpl`` to ease this conversion process.
This can be passed to with ::

    
    $ jupyter nbconvert --to=rst --template=rstTemplate.tpl Notebook.ipynb

Upon conversion, move the file into the ``docs/examples`` directory and include the 
file name in ``docs/examples/index.rst``.

.. _docs-images:

Images
------

Executing ``nbconvert`` will create a directory containing the images
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

* ``:class:`serpentTools.DepletionReader```
  becomes :class:`serpentTools.DepletionReader`
* ``:meth:`~serpentTools.objects.DepletedMaterial.plot``` is shortened to
  :py:meth:`~serpentTools.objects.DepletedMaterial.plot`

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

    .. autoclass:: serpentTools.ResultsReader

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
