"""Holds cross section data pertaining to Serpent xsplot output."""

import numpy
from matplotlib import pyplot

from serpentTools import messages
from serpentTools.objects import NamedObject, convertVariableName


class XSData(NamedObject):
    docParams = """name: str
        Name of this material
    metadata: dict
        Dictionary with file metadata"""
    docAttrs = """data: dict
        dictionary that stores all variable data
    zai: list
        Isotopic ZZAAA identifiers, e.g. 93325
    names: list
        Names of isotopes, e.g. U235
    days: numpy.ndarray
        Vector of total, cumulative days of burnup for the run that
        created this material
    burnup: numpy.ndarray
        Vector of total, cumulative burnup [MWd/kgU] for this specific
        material
    adens: numpy.ndarray
        2D array of atomic {densStruct:s}
    mdens: numpy.ndarray
        2D array of mass {densStruct:s}""".format(
    __doc__ = """
    Base class for storing cross section data an xsplot file

    Parameters
    ----------
    {params:s}

    Attributes
    ----------
    {attrs:s}

    """.format(equiv=docEquiv, params=docParams, attrs=docAttrs)

    def __init__(self, name, metadata):
        NamedObject.__init__(self, name)
        self.data = {}
        # Whether this describes individual isotope XS, or whole-material XS
        self.isIso = True

        # serpent starts their names with an "m" if it's a whole-material XS
        if name[0] == 'm':
            self.isIso = False

        # a reference to the energy grid the XS are defined on:
        self.egrid = bleh

        # Possible reactions on this material / nuclide
        # Maps MT integer number to a description
        self.mts = {}

    @staticmethod
    def negativeMTDescription(mt):
        """ Gives descriptions for negative MT numbers used by Serpent
        for whole materials, for neutrons only. """
        if mt > 0:
            error("Uh, that's not a negative MT.")
        descriptions= {
            -1  : "Macro total",
            -2  : "Macro total capture",
            -3  : "Macro total elastic scatter",
            -4  : "Macro total heating",
            -5  : "Macro total photon production",
            -6  : "Macro total fission",
            -7  : "Macro total fission neutron production",
            -8  : "Total fission energy production",
            -9  : "Majorant macro",
            -10 : "Macro scattering recoil heating",
            -11 : "Source rate",
            -15 : "neutron density",
            -16 : "Macro total scattering neutron production",
            -53 : "Macro proton production",
            -54 : "Macro deutron production",
            -55 : "Macro triton production",
            -56 : "Macro He-3 production",
            -57 : "Macro He-4 production",
            -100: "User response function" }
        try:
            return descriptions[mt]
        except KeyError:
            error("Cannot find description for MT {}.".format(mt))
            return None
