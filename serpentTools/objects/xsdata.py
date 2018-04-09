"""Holds cross section data pertaining to Serpent xsplot output."""
import numpy as np
from matplotlib import pyplot

from serpentTools import messages
from serpentTools.objects import NamedObject, convertVariableName
from serpentTools.plot import magicPlotDocDecorator # make nice docstring

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

    MTdescriptions= {
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

    def __init__(self, name, metadata, isIso=False):
        NamedObject.__init__(self, name)

        # Whether this describes individual isotope XS, or whole-material XS
        # serpent starts their names with an "m" if it's a whole-material XS
        self.isIso = isIso

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
        try:
            return XSData.MTdescriptions[mt]
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
        if not self.MT:
            return False

        return True

    @magicPlotDocDecorator
    def plot(self, mts, logscale=True, figargs={}, **kwargs):
        """ Return a matplotlib figure for plotting XS.
        mts should be a list of the desired MT numbers to plot for this
        XS. Units should automatically be fixed between micro and macro XS.

        Parameters
        ----------
        mts: int, string, or list of ints
            If it's a string, it should be 'all'.
            A single int indicates one MT reaction number.
            A list should be a list of MT numbers to plot.
        logscale: bool
            whether to use a logscale
        figargs: dict
            kwarguments to pass to plt.figure, like dpi:96 or figsize:(6,6)
            by default, extra kwargs go to plot.
        """
        # don't pass figargs to plotting command
        kwargs.pop('figargs', None)

        if mts == 'all':
            mts = self.MT
        elif isinstance(mts, int):
            # convert to list if it's just one MT
            mts = [mts]
        elif isinstance(mts, list) and all([isinstance(ii, int) for ii in mts]):
            pass
        else:
            msg = ("mts argument must be a string saying 'all',"
                   "a list of integer MTs, or a single interger"
                   "instead, {} of type {} was passed.".format(
                   mts, type(mts)))
            raise Exception(msg)

        for mt in mts:
            if mt not in self.MT:
                error("{} not in collected MT numbers, {}".format(mt, self.MT))
        fig = pyplot.figure(**figargs)

        # could possibly automatically set up subplotting
        ax = fig.add_subplot(111)

        # list of MT number descriptions
        descriplist = []

        for mt in mts:
            for i, MT in enumerate(self.MT):
                if mt == MT:
                    x = self.metadata['egrid']
                    y = self.xsdata[:,i]
                    if logscale:
                        ax.loglog(x, y, drawstyle='steps')
                    else:
                        ax.plot(x, y, drawstyle='steps')
                    descriplist.append(self.MTdescrip[i])

        ax.legend(descriplist)
        ax.set_title('{} cross section{}'.format(self.name,'s' if len(mts)>1 else ''))
        ax.set_xlabel('Energy (MeV)')
        ax.set_ylabel('XS ({})'.format('b' if self.isIso else 'cm$^{-1}$'))

        return fig

    def showMT(self):
        """ Pretty prints MT values available for this XS and
        descriptions.
        """
        print("MT numbers available for {}:".format(self.name))
        print("--------------------------"+len(self.name)*'-')
        for i, mt in enumerate(self.MT):
            if self.isIso:
                descr = self.MTdescrip[i]
            else:
                descr = XSData.negativeMTDescription(mt)
            spaces = (4-len(str(mt)))*' '
            print(str(mt)+spaces, descr)
