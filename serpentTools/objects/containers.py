import numpy
from serpentTools.Objects import _SupportingObject


class container(_SupportingObject):
    """Class for storing material data from ``_dep.m`` files.

    Parameters
    ----------
    parser: :py:class:`~serpentTools.parsers.depletion.DepletionReader`
        Parser that found this material.
        Used to obtain file metadata like isotope names and burnup
    name: str
        Name of this material

    Attributes
    ----------
    zai: numpy.array
        Isotope id's
    names: numpy.array
        Names of isotopes
    days: numpy.array
        Days overwhich the material was depleted
    adens: numpy.array
        Atomic density over time for each nuclide

    :note:

        These attributes only exist if the pasers was instructed to
        read in this data. I.e. if ``readers.depletion.metadataKeys``
        does not contain ``ZAI``, then this object will not have
        the ``zai`` data.

    """