"""Holds cross section data pertaining to Serpent xsplot output."""
import numpy as np
from matplotlib import pyplot

from serpentTools import messages
from serpentTools.objects import NamedObject, convertVariableName


class XSData(NamedObject):
    docParams = """name: str
        Name of this material
    metadata: dict
        Dictionary with file metadata"""
    __doc__ = """
    Base class for storing cross section data an xsplot file

    Parameters
    ----------
    {params:s}

    Attributes
    ----------

    """.format(params=docParams)

    def __init__(self, name, metadata, isIso=False):
        NamedObject.__init__(self, name)

        # Whether this describes individual isotope XS, or whole-material XS
        self.isIso = True

        # serpent starts their names with an "m" if it's a whole-material XS
        self.isIso = isIso

        # energy grid for the nuclides
        self.egrid = None

        # metadata reference
        self.metadata = metadata

        # Possible reactions on this material / nuclide
        # Maps MT integer number to a description
        self.MT = []
        self.MTdescrip = []

        # Holds XS numeric data
        self.xsdata = None

        # whether nu data present for fissionables
        self.hasNuData = False

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

    def setMTs(self, chunk):
        """ Parse chunk to MT numbers and descriptions"""
        if not self.isIso:
            self.MT = [int(c) for c in chunk[1:]]
        else:
            self.MT = [int(c.split('%')[0]) for c in chunk[1:]]

        # Make MT descriptions
        if not self.isIso:
            for mt in self.MT:
                self.MTdescrip.append(self.negativeMTDescription(mt))
        else:
            self.MTdescrip = [c.split('%')[1].rstrip() for c in chunk[1:]]

    def setData(self, chunk):
        """ Parse data from chunk to np array."""
        self.xsdata = np.zeros([len(self.metadata['egrid']), len(self.MT)])
        for i, line in enumerate(chunk[1:]):
            self.xsdata[i,:] = np.array(line.split(), dtype=np.float64)

    def setNuData(self, chunk):
        """ Add fission neutrons per fission data """
        self.hasNuData = True
        self.nuData = np.zeros([len(self.metadata['egrid']),2], dtype=np.float64)
        for i, cc in enumerate(chunk[1:]):
            self.nuData[i,:] = np.array(cc.split(), dtype=np.float64)

    def hasExpectedData(self):
        """ Check that the expected data (MT numbers, an energy grid, etc)
        were collected. """

        if not isinstance(self.xsdata, np.ndarray):
            return False
        if self.MT == []:
            return False
        else:
            return True
