.. |matlabConv| replace:: :class:`~serpentTools.io.base.MatlabConverter`

.. _dev-convert:

===================
Converter Utilities
===================

One goal for this project is to allow users to use ``serpentTools`` as a
pipeline for taking :term:`SERPENT` data to other programs.
The first demonstration of this is creating binary ``.mat`` files that can
be read into MATLAB, when a large text file would cause issues, done with
the |matlabConv|.

Classes intending do first look for specific methods for gathering data 
on each object. These are obscured from the public API as they don't serve
a direct purpose besides a simple method by which to translate data
from one place to the next.
This collection is called inside the primary ``convert`` method,
which is responsible for gathering and writing the data into the new
form.

Keeping with the |matlabConv| as an example, it looks for
``_gather_matlab`` method. This method simply places data into
a dictionary, but do to the layout of each object, must be reimplemented
as a unique method.
Due to the simplicity of :func:`scipy.io.savemat`, the main writing function,
:meth:`serpentTools.io.base.MatlabConverter.convert`, is rather light.
However, some data forms may require more depth to ensure fidelity in the 
converted data.

There may be some cases where a conversion does not make sense
for all data types. Detector objects are the few pieces of data that
can have a spatial grid attached, yet this grid varies across detectors.
It may be advantageous to implement converters directly as instance methods.
The decision will be up to the developer and the review process in that case.

Converters should also make sure, prior to potentially expensive collection
steps are taken, that the user is in the best position to execute this
operation. As of this writing and :release-tag:`0.6.1`, :term:`scipy`
is not a requirement for this package, yet it is required for MATLAB
conversion. Therefore, the |matlabConv| implements a check for :term:`scipy`
in :meth:`~serpentTools.io.base.MatlabConverter.checkImports`. The other 
check method, :meth:`~serpentTools.io.base.MatlabConverter.checkContainerReq`,
is responsible for checking the container has the required data gathering
routines, e.g. ``_gather_matlab``.
These checks are called at creation of the converter object.

.. autoclass:: serpentTools.io.base.MatlabConverter
