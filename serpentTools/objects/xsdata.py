"""Holds cross section data pertaining to Serpent xsplot output."""
import numpy as np
from matplotlib import pyplot

from serpentTools.messages import error
from serpentTools.objects.base import NamedObject
from serpentTools.utils.plot import magicPlotDocDecorator, formatPlot


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
    isIso: bool
        Whether this describes individual isotope XS, or whole-material XS
    MT: list
        Macroscopic cross section integers
    MTdescip: list
        Descriptions of reactions in ``MT``
    xsdata: :py:class:`numpy.ndarray`
    hasNuData: bool
        True if nu data is present
    metadata: dict
        file-wide metadata from the reader
    """.format(params=docParams)

    MTdescriptions = {
        -1: "Macro total",
        -2: "Macro total capture",
        -3: "Macro total elastic scatter",
        -4: "Macro total heating",
        -5: "Macro total photon production",
        -6: "Macro total fission",
        -7: "Macro total fission neutron production",
        -8: "Total fission energy production",
        -9: "Majorant macro",
        -10: "Macro scattering recoil heating",
        -11: "Source rate",
        -15: "neutron density",
        -16: "Macro total scattering neutron production",
        -53: "Macro proton production",
        -54: "Macro deutron production",
        -55: "Macro triton production",
        -56: "Macro He-3 production",
        -57: "Macro He-4 production",
        -100: "User response function",
    }

    def __init__(self, name, metadata, isIso=False):
        NamedObject.__init__(self, name)

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
        return XSData.MTdescriptions[mt]

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
            self.xsdata[i, :] = np.array(line.split(), dtype=np.float64)

    def setNuData(self, chunk):
        """ Add fission neutrons per fission data """
        self.hasNuData = True
        self.nuData = np.zeros([len(self.metadata['egrid']), 2],
                               dtype=np.float64)
        for i, cc in enumerate(chunk[1:]):
            self.nuData[i, :] = np.array(cc.split(), dtype=np.float64)

    def hasExpectedData(self):
        """ Check that the expected data (MT numbers, an energy grid, etc)
        were collected. """

        if not isinstance(self.xsdata, np.ndarray):
            return False
        if not self.MT:
            return False

        return True

    def tabulate(self, mts='all', colnames=None):
        """ Returns a pandas table, for pretty tabulation in Jupyter
        notebooks.

        Parameters
        ----------
        mts: int, string, or list of ints
            If it's a string, it should be 'all', which is default.
            A single int indicates one MT reaction number.
            A list should be a list of MT numbers to plot.
        colnames: any type with string representation
            Column names for each MT number, if you'd like to change them.

        Returns
        -------
        Pandas Dataframe version of the XS data.

        Raises
        ------
        ModuleNotFoundError:
            if you don't have pandas.
        TypeError:
            if MT numbers that don't make sense come up
        """
        import pandas as pd

        if len(self.metadata['egrid']) > 99:
            y = input('This is about to be a big table. Still want it? (y/n)')
            if not (y == 'y' or y == 'Y'):
                pass
            else:
                return None

        if mts == 'all':
            mts = self.MT
        elif isinstance(mts, int):
            # convert to list if it's just one MT
            mts = [mts]
        elif isinstance(mts, list) and all(
                [isinstance(ii, int) for ii in mts]):
            pass
        else:
            msg = ("mts argument must be a string saying 'all',"
                   "a list of integer MTs, or a single interger"
                   "instead, {} of type {} was passed."
                   .format(mts, type(mts)))
            raise TypeError(msg)

        for mt in mts:
            if mt not in self.MT:
                error("{} not in collected MT numbers, {}".format(mt, self.MT))

        cols2use = []
        mtnums = []
        for mt in mts:
            for i, MT in enumerate(self.MT):
                if mt == MT:
                    cols2use.append(i)
                    mtnums.append(mt)

        frame = pd.DataFrame(self.xsdata[:, cols2use])
        unit = ' b' if self.isIso else ' cm$^{-1}$'
        frame.columns = colnames or ['MT ' + str(mt) + unit for mt in mtnums]
        frame.insert(0, 'Energy (MeV)', self.metadata['egrid'])

        return frame

    @magicPlotDocDecorator
    def plot(self, mts='all', ax=None, loglog=False, xlabel=None, ylabel=None,
             logx=True, logy=False, title=None, legend=True, ncol=1,
             **kwargs):
        """
        Return a matplotlib figure for plotting XS.

        mts should be a list of the desired MT numbers to plot for this
        XS. Units should automatically be fixed between micro and macro XS.

        Parameters
        ----------
        mts: int, string, or list of ints
            If it's a string, it should be 'all'.
            A single int indicates one MT reaction number.
            A list should be a list of MT numbers to plot.
        {ax}
        {loglog}
        {logx}
        {logy}
        {xlabel}
        {ylabel}
        {title}
        {legend}
        {ncol}
        {kwargs} :py:func:`matplotlib.pyplot.plot`

        Returns
        -------
        {rax}

        Raises
        ------
        TypeError:
            if MT numbers that don't make sense come up
        """

        if mts == 'all':
            mts = self.MT
        elif isinstance(mts, int):
            # convert to list if it's just one MT
            mts = [mts]
        elif isinstance(mts, list) and all(
                [isinstance(ii, int) for ii in mts]):
            pass
        else:
            msg = ("mts argument must be a string saying 'all',"
                   "a list of integer MTs, or a single interger"
                   "instead, {} of type {} was passed."
                   .format(mts, type(mts)))
            raise TypeError(msg)

        for mt in mts:
            if mt not in self.MT:
                error("{} not in collected MT numbers, {}".format(mt, self.MT))

        ax = ax or pyplot.axes()

        x = self.metadata['egrid']
        for mt in mts:
            for i, MT in enumerate(self.MT):
                if mt == MT:
                    y = self.xsdata[:, i]
                    ax.plot(x, y, drawstyle='steps', label=self.MTdescrip[i])

        title = title or '{} cross section{}'.format(
            self.name, 's' if len(mts) > 1 else '')
        xlabel = xlabel or "Energy [MeV]"

        ylabel = ylabel or ('Cross Section ({})'.format('b' if self.isIso
                            else 'cm$^{-1}$'))
        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy, ncol=ncol,
                        legend=legend, title=title, xlabel=xlabel,
                        ylabel=ylabel)

        return ax

    def showMT(self, retstring=False):
        """ Pretty prints MT values available for this XS and
        descriptions.

        Parameters
        ----------
        retstring: bool
            return a string if true. Otherwise, print it
        """
        outstr = ""
        outstr += "MT numbers available for {}:\n".format(self.name)
        outstr += "--------------------------" + len(self.name) * '-' + '\n'
        for i, mt in enumerate(self.MT):
            if self.isIso:
                descr = self.MTdescrip[i]
            else:
                descr = XSData.negativeMTDescription(mt)
            spaces = (4 - len(str(mt))) * ' '
            outstr += str(mt) + spaces + descr + '\n'
        if retstring:
            return outstr
        else:
            print(outstr)
