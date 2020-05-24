"""Holds cross section data pertaining to Serpent xsplot output."""
from collections.abc import Mapping

import numpy as np
from matplotlib import pyplot

from serpentTools.messages import error
from serpentTools.objects.base import NamedObject
from serpentTools.utils.plot import magicPlotDocDecorator, formatPlot

__all__ = [
    'XSData',
]


class XSData(NamedObject):
    """Base class for storing cross section data an xsplot file

    Parameters
    ----------
    name : str
        Name of this material
    metadata : dict
        Dictionary with file metadata. Expects ``egrid`` as a key
        at least
    isIso : bool, optional
        Flag indicating if this data section is for a single
        isotope or for a material

    Attributes
    ----------
    isIso : bool
        Whether this describes individual isotope XS, or whole-material XS
    MT : list
        Macroscopic cross section integers
    MTdescip : list
        Descriptions of reactions in ``MT``
    xsdata : numpy.ndarray
        Array of xs data. Rows correspond to items in :attr:`MT`
    hasNuData : bool
        True if nu data is present
    energies : numpy.ndarray
        Energy grid [MeV]
    metadata : dict
        File-wide metadata from the reader. Alias for accessing
        :attr:`energies`. Will be removed in the future

    """

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
        super().__init__(name)

        self.isIso = isIso

        # metadata reference
        self.energies = metadata["egrid"]
        self.metadata = metadata

        # Possible reactions on this material / nuclide
        # Maps MT integer number to a description
        self.MT = []
        self.MTdescrip = []

        # Holds XS numeric data
        self.xsdata = None

        # whether nu data present for fissionables
        self.hasNuData = False

    def __len__(self):
        """Number of reactions stored"""
        return len(self.MT)

    def __getitem__(self, mt):
        """Return data corresponding to a given mt

        Parameters
        ----------
        mt : int
            Integer MT reaction number

        Returns
        -------
        numpy.ndarray
            Cross section data for this mt

        Raises
        ------
        AttributeError
            If :attr:`xsdata` is empty
        KeyError
            If ``mt`` not found in :attr:`MT`

        """
        if self.xsdata is None:
            raise AttributeError("xsdata not populated")
        try:
            index = self.MT.index(mt)
        except ValueError as ve:
            raise KeyError(mt) from ve
        return self.xsdata[:, index]

    def get(self, mt, default=None):
        """Return data corresponding to a given mt or a default

        Parameters
        ----------
        mt : int
            Integer MT reaction number
        default : object
            Object to be returned in ``mt`` is not found

        Returns
        -------
        object
            :class:`numpy.ndarray` if ``mt`` is found. Otherwise
            ``default``

        Raises
        ------
        AttributeError
            If :attr:`xsdata` is empty

        """
        try:
            return self[mt]
        except KeyError:
            return default

    @staticmethod
    def negativeMTDescription(mt):
        """Descriptions for Serpent negative MT numbers

        These correspond to macroscopic properties, like
        fission energy production, and for neutrons only.
        From Serpent Wiki

        Parameters
        ----------
        mt : int
            Macroscopic reaction MT. Must be negative

        Returns
        -------
        str
            Description

        """
        if mt > 0:
            raise ValueError("{} is not negative".format(mt))
        return XSData.MTdescriptions[mt]

    def describe(self, mt):
        """Return the description for any reaction MT

        Parameters
        ----------
        mt : int
            Integer reaction number, e.g. 102 or -8. Assumes
            neutrons only

        Returns
        -------
        str
            Description for this reaction

        """
        if mt < 0:
            return XSData.MTdescriptions[mt]
        index = self.MT.index(mt)
        return self.MTdescrip[index]

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
            self.MTdescrip = [c.split('%')[1].strip() for c in chunk[1:]]

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
        pandas.DataFrame
            Tabulated representation of the cross section data

        Raises
        ------
        ImportError
            If ``pandas`` is not installed
        TypeError
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
             logx=True, logy=False, title=None, legend=None, ncol=1,
             labels=None, **kwargs):
        """
        Plot XS corresponding to their MTs.

        Parameters
        ----------
        mts : int, string, or list of ints
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
        labels : str or list of str or dict {int: str}
            Labels to apply to the plot. Defaults to labeling by MT
            description.  If a string, then ``mts`` must be a single
            integer. If a list of strings, each label will be applied
            to each entry in ``mts``. If a dictionary, keys must be
            mts and their labels as values. The number of keys do
            not have to align with the number of MTs
        {kwargs} :func:`matplotlib.pyplot.plot`

        Returns
        -------
        {rax}

        Raises
        ------
        TypeError
            If MT numbers that don't make sense come up

        """

        mts = self._processPlotMts(mts)

        userlabel = kwargs.pop("label", None)
        if userlabel is not None:
            # Allow label to be passed for single MT plots
            # Little easier to remember and it makes more sense.
            # Don't allow mixed label / labels arguments
            if labels is not None:
                raise ValueError(
                    "Passing label and labels is not allowed. Prefer labels")
            if len(mts) == 1:
                labels = [userlabel]
            else:
                raise ValueError("Use labels when plotting multiple MTs")
        else:
            labels = self._processPlotLabels(mts, labels)

        ax = ax or pyplot.gca()

        kwargs.setdefault("drawstyle", "steps")
        for mt, label in zip(mts, labels):
            y = self[mt]
            ax.plot(self.energies, y, label=label, **kwargs)

        title = title or '{} cross section{}'.format(
            self.name, 's' if len(mts) > 1 else '')
        xlabel = xlabel or "Energy [MeV]"

        ylabel = ylabel or ('Cross Section ({})'.format('b' if self.isIso
                            else 'cm$^{-1}$'))
        ax = formatPlot(
            ax, loglog=loglog, logx=logx, logy=logy, legendcols=ncol,
            legend=legend, title=title, xlabel=xlabel, ylabel=ylabel)

        return ax

    def _processPlotMts(self, mts):
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
                raise ValueError(
                    "{} not in collected MT numbers, {}".format(mt, self.MT))
        return mts

    def _processPlotLabels(self, mts, labels):
        if isinstance(labels, str):
            if len(mts) != 1:
                raise ValueError(
                    "Labels and mts do not align: {} mts, 1 label".format(
                        len(mts)))
            return [labels]
        if labels is None:
            return [self.describe(mt) for mt in mts]
        if isinstance(labels, Mapping):
            out = []
            for i, mt in enumerate(mts):
                out.append(labels.get(mt, self.MTdescrip[i]))
            return out
        if len(mts) != len(labels):
            raise ValueError(
                "Labels and mts do not align: {} mts, {} labels".format(
                    len(mts), len(labels)))
        return labels

    def showMT(self, retstring=False):
        """Create a pretty-print style string of the MT values avaialable


        Parameters
        ----------
        retstring : bool
            Return a string if true. Otherwise, print it

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
