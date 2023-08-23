"""
Hooks for creating adding direct methods for conversion

These functions should be added to classes in the following
manner::

    class HookedObj(object):

        def demo(self):
            print("Hello")


    def demoHook(obj, [args], [**kwargs]):
        # operate as if object is a class instance
        print("Inside demoHook")
        obj.demo()

    HookedObj.hooked = demoHook

This allows the following implementation::

    >>> h = HookedObj()
    >>> h.demo()
    "Hello"
    >>> h.hooked()
    "Inside demoHook"
    "Hello"

"""
from serpentTools.io import MatlabConverter


def matlabHook(obj, fileP, reconvert=True, append=True,
               format='5', longNames=True, compress=True, oned='row'):
    """
    Write a binary MATLAB file from the contents of this object

    Parameters
    ----------
    fileP : str or file-like object
        Name of the file to write. ``.mat`` extension is not needed
        if ``append==True``
    reconvert : bool
        If this evaluates to true, convert values back into their
        original form as they appear in the output file.
    append : bool
        If true and a file exists under ``output``, append to that file.
        Otherwise the file will be overwritten
    format : {'5', '4'}
        Format of file to write. ``'5'`` for MATLAB 5 to 7.2, ``'4'`` for
        MATLAB 4
    longNames : bool
        If true, allow variable names to reach 63 characters,
        which works with MATLAB 7.6+. Otherwise, maximum length is
        31 characters
    compress : bool
        If true, compress matrices on write
    oned : {'row', 'col'}
        Write one-dimensional arrays as row vectors if
        ``oned=='row'`` (default), or column vectors

    Raises
    ------
    ImportError
        If :term:`scipy` is not installed

    See Also
    --------
    * :func:`scipy.io.savemat`
    """
    converter = MatlabConverter(obj, fileP)
    return converter.convert(
        reconvert, append, format, longNames, compress, oned)
