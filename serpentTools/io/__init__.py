"""
.. versionadded:: 0.6.2

Module for converting/creating ``serpentTools`` objects to/from other sources

High-level functions implemented here, such as :func:`toMatlab`, help the
:ref:`cli` in quickly converting files without launching a Python interpreter.
For example,

.. code::

    $ python -m serpentTools -v to-matlab my/depletion_dep.m
    INFO  : serpentTools: Wrote contents of my/depletion_dep.m to my/depletion_dep.mat

"""

from serpentTools.io.base import *  # noqa


def toMatlab(obj, fileP, reconvert=True, append=True,
             format='5', longNames=True, compress=True,
             oned='row'):
        """
        Write a binary MATLAB file from the contents of this object

        Parameters
        ----------
        obj: ``serpentTools`` container
            Parser or container to be written to file
        fileP: str or file-like object
            Name of the file to write
        reconvert: bool
            If this evaluates to true, convert values back into their
            original form as they appear in the output file.
        append: bool
            If true and a file exists under ``output``, append to that file.
            Otherwise the file will be overwritten
        format: {'5', '4'}
            Format of file to write. ``'5'`` for MATLAB 5 to 7.2, ``'4'`` for
            MATLAB 4
        longNames: bool
            If true, allow variable names to reach 63 characters,
            which works with MATLAB 7.6+. Otherwise, maximum length is
            31 characters
        compress: bool
            If true, compress matrices on write
        oned: {'row', 'col'}:
            Write one-dimensional arrays as row vectors if
            ``oned=='row'`` (default), or column vectors

        Raises
        ------
        ImportError:
            If :term:`scipy` is not installed
        NotImplementedError
            If the passed object does not support exporting to MATLAB

        See Also
        --------
        * :func:`scipy.io.savemat`
        * :class:`serpentTools.io.base.MatlabConverter`

        Example
        -------

        >>> import serpentTools
        >>> from serpentTools.io import toMatlab
        >>> det = serpentTools.read('my_det0.m')
        # Write all detectors and grids from file
        # with their original names
        >>> toMatlab(det, 'output.mat',
                     reconvert=True)
        # Write a single detector to the same file
        # but under shorter names
        >>> toMatlab(det['demo'], 'output.mat',
                     reconvert=False, append=True)
        """
        converter = MatlabConverter(obj, fileP)
        return converter.convert(
            reconvert, append, format, longNames, compress, oned)

