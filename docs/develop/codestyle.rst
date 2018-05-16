.. _code-style:

============
Coding Style
============

For the most part, this project follows the
:pep:`8` standard with a few differences. Some points are included here

* 79 characters per line
* Four spaces per indentation level
* Avoiding extraneous whitespace::

    Yes: spam(ham[1], {eggs: 2})
    No:  spam( ham[ 1 ], { eggs: 2 } )

Some of the specific style points for this project are included below

* ``mixedCase`` for variables, methods, and functions
* ``CamelCase`` for classes::

    class DemoClass(object):

        def doSomething(self, arg0, longerArgumentName):
            pass

* Directly call the ``__init__`` method from a parent class, e.g.::

    class MyQueue(list):

        def __init__(self, items):
            list.__init__(self)
            self.extend(items)

* Arrange imports in the following order:

  #. imports from the standard library: os, sys, etc.
  #. imports from third party code: numpy, matplotlib, etc.
  #. imports from the serpentTools package

* Longer import paths are preferred to shorter::

    # yes
    from really.long.path.to.a import function
    function()
    # not preferred
    import really
    really.long.path.to.a.function()


