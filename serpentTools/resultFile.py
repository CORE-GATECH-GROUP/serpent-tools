from collections import OrderedDict
from collections.abc import Mapping

from cycler import cycler
from matplotlib.pyplot import gca
from matplotlib import rcParams

from .base import getStream, SerpentFile
from serpentTools.objects.containers import UnivTuple
from serpentTools.utils import (
    magicPlotDocDecorator, RESULTS_PLOT_XLABELS, formatPlot, placeLegend,
)
from serpentTools.messages import SerpentToolsException

__all__ = ["ResultFile"]


class ResultFile(SerpentFile):
    """File containing the primary simulation results

    When inspecting keys of :attr:`universes`, it is preferable to use
    an attribute based approach rather than positional. For example::

        >>> for key in res.universes:
        ...     break
        >>> key.universe
        # rather than
        >>> key[0]

    Parameters
    ----------
    resdata : Mapping, optional
        Dictionary with time-dependent variables as keys and the
        corresponding values. The data is unique for each burnup step.
    universes: Mapping, optional
        Dictionary of universe identifiers
        :class:`~serpentTools.objects.UnivTuple` and their corresponding
        :class:`~serpentTools.objects.HomogUniv` objects.
    metadata: Mapping, optional
        Dictionary with descriptive variables as keys and the
        corresponding description.

    Attributes
    ------------
    metadata: Mapping
        Dictionary with descriptive variables as keys and the
        corresponding description. Within the _res.m file this data is
        printed multiple times, but contains the same description
        and thus is stored only once. e.g., 'version': 'Serpent 2.1.29'
    resdata: Mapping
        Dictionary with time-dependent variables as keys and the
        corresponding values. The data is unique for each burnup step.
        Some variables also contain uncertainties.
        e.g., 'absKeff': [[9.91938E-01, 0.00145],[1.81729E-01, 0.00240]]
    universes: Mapping
        Dictionary of universe identifiers
        :class:`~serpentTools.objects.UnivTuple` and their corresponding
        :class:`~serpentTools.objects.HomogUniv` objects. The keys
        describe a unique state: 'universe', burnup (MWd/kg), burnup
        index, time (days) ('0', 0.0, 0, 0.0).  Burnup indexes are
        zero-indexed, meaning the first step is index 0.

    See Also
    --------
    :meth:`fromSerpent` - A convenience method for loading data
    directly from a result file

    """

    def __init__(self, resdata=None, universes=None, metadata=None):
        if resdata is None:
            self.resdata = {}
        elif not isinstance(resdata, Mapping):
            raise TypeError(
                "Expect resdata to be Mapping, not {}".format(type(resdata)))
        else:
            self.resdata = resdata

        if universes is None:
            self.universes = {}
        elif not isinstance(universes, Mapping):
            raise TypeError(
                "Expect universes to be Mapping, not {}".format(type(resdata)))
        else:
            self.universes = universes

        if metadata is None:
            self.metadata = {}
        elif not isinstance(metadata, Mapping):
            raise TypeError(
                "Expect metadata to be Mapping, not {}".format(type(resdata)))
        else:
            self.metadata = metadata

    def getUniv(self, univ, burnup=None, index=None, timeDays=None):
        """
        Return a specific universe given the ID and time of interest

        Parameters
        ----------
        univ: str
            Unique str for the desired universe
        burnup: float or int, optional
            Burnup [MWd/kgU] of the desired universe
        timeDays: float or int, optional
            Time [days] of the desired universe
        index: int, optinal
            Point of interest in the burnup/days index

        Returns
        -------
        :class:`~serpentTools.objects.HomogUniv`
            Requested universe

        Raises
        ------
        KeyError:
            If the requested universe could not be found
        :class:`~serpentTools.SerpentToolsException`
            If burnup, days and index are not given
        """
        if index is None and burnup is None and timeDays is None:
            raise SerpentToolsException(
                'Burnup, time or index are required inputs')

        searchKey = UnivTuple(univ, burnup, index, timeDays)

        # check if key is exactly present

        universe = self.universes.get(searchKey)
        if universe is not None:
            return universe

        for key, universe in self.universes.items():
            for uItem, sItem in zip(key, searchKey):
                if sItem is None:
                    continue
                elif uItem != sItem:
                    break
            else:
                return universe
        raise KeyError(
            "Could not find a universe that matches {}".format(searchKey))

    @magicPlotDocDecorator
    def plot(self, x, y=None, right=None, sigma=3, ax=None, legend=None,
             ncol=None, xlabel=True, ylabel=None, logx=False, logy=False,
             loglog=False, rightlabel=None):
        """
        Plot quantities over time

        Parameters
        ----------
        x: str or iterable of strings
            ``y`` is not given, then plot these quantites against
            burnup in days. Otherwise, plot this quantity as the x
            axis with same rules as if called by ``plot('burndays', x)``.
            Burnup options are ``{'burnup', 'days', 'burnDays', 'burnStep'}``
        y: str or iterable of strings
            Quantity or quantities to plot. For all entries, only
            the first column, with respect to time, will be plotted.
            If the second column exists, and sigma is > 0, that column
            will be treated as the relative uncertainty for an
            errorbar plot. If a dictionary is passed, then plots will
            be labeled by the values of that dictionary, e.g.
            ``{'anaKeff': $k_{eff}$}`` would plot the first column of
            ``anaKeff`` with a ``LaTeX``-ready :math:`k_{eff}`
        right: str or iterable of strings
            Quantites to plot on the same plot, but with a different
            y axis and common x axis. Same rules apply as for arguments
            to ``y``. Each label will modified to have a unique identifier
            indicating the plot uses the right y-axis
        {ax}
        {sigma}
        {legend}
        {ncol}
        {xlabel}
        {ylabel}
        {logx}
        logy: bool or list or tuple
            Apply a log scale to the y-axis. If passing values to
            ``right``, this can be a two item list or tuple,
            corresponding to log-scaling the left and right axis,
            respectively.
        {loglog}
        rlabel: str or None
            If given and passing values to ``right``, use this to label
            the y-axis.

        Returns
        -------
        :class:`matplotlib.axes.Axes` or tuple of axes
            If right is not given, then only the primary axes object
            is returned. Otherwise, the primary and the "right"
            axes object are returned

        """

        # cleanup some inputs
        if y is None:
            y = x
            x = "burnDays"

        sigma = max(int(sigma), 0)

        y = self._expandPlotIterables(y)

        if right is not None:
            right = self._expandPlotIterables(right, ' [right]')

        if xlabel is True:
            xlabel = RESULTS_PLOT_XLABELS[x]

        if len(y) == 1 and ylabel is None:
            for ylabel in y.values():
                break  # just need the first one
            if sigma:
                ylabel += r'$ \pm {}\sigma$'.format(sigma)

        ax = ax or gca()

        self._plot(x, y, ax, sigma)

        if right is None:
            formatPlot(ax, logx=logx, logy=logy, loglog=loglog,
                       xlabel=xlabel, ylabel=ylabel, legend=legend,
                       ncol=ncol)
            return ax

        # plot some other quantity on the same x axis
        other = ax.twinx()

        # update color cycle to not repeat
        colors = rcParams['axes.prop_cycle'].by_key()['color']
        colors = colors[len(y):] + colors[:len(y)]
        other.set_prop_cycle(cycler('color', colors))

        self._plot(x, right, other, sigma)

        # formatting
        if logy is None or isinstance(logy, bool):
            logy = [logy, ] * 2

        if loglog is None or isinstance(loglog, bool):
            loglog = [loglog, None]

        if legend or legend is None:
            leftHandles, leftLabels = ax.get_legend_handles_labels()
            rightHandles, rightLabels = other.get_legend_handles_labels()

            placeLegend(ax, legend, ncol,
                        (leftHandles + rightHandles,
                         leftLabels + rightLabels))

        if len(right) == 1 and rightlabel is None:
            for rightlabel in right.values():
                break  # just need the first one
            if sigma:
                rightlabel += r'$ \pm {}\sigma$'.format(sigma)

        formatPlot(ax, logx=logx, logy=logy[0], loglog=loglog[0],
                   legend=False, xlabel=xlabel, ylabel=ylabel)
        formatPlot(other, logx=False, loglog=False, logy=logy[1],
                   legend=False, ylabel=rightlabel.replace(' [right]', ''))

        return ax, other

    def _plot(self, x, y, ax, sigma):
        """Simple, unformatted plot with dictionary of keys"""
        # get plot data
        xvals = self.resdata[x][:, 0]
        for resKey, label in y.items():
            ydata = self.resdata[resKey]
            if ydata.shape[0] != xvals.size and ydata.size != xvals.size:
                raise ValueError(
                    "Quantity for {} has {} time points, not {} like {}"
                    .format(resKey, ydata.shape[0], xvals.size, x))

            # grab second column for uncertainty
            if sigma and ydata.shape[1] > 1:
                ax.errorbar(xvals, ydata[:, 0], label=label,
                            yerr=ydata[:, 0] * sigma * ydata[:, 1])
            else:
                ax.errorbar(xvals, ydata[:, 0], label=label)

    @staticmethod
    def _expandPlotIterables(y, tail=''):
        if isinstance(y, str):
            return {y: "{}{}".format(y, tail)}
        elif not isinstance(y, (dict, OrderedDict)):
            return OrderedDict([[item, '{}{}'.format(item, tail)]
                                for item in y])
        return y

    def toMatlab(self, fileP, reconvert=True, append=True, format='5',
                 longNames=True, compress=True, oned='row'):
        """
        Write a binary MATLAB file from the contents of this reader

        The group constant data will be presented as a multi-dimensional
        array, rather than a stacked 2D matrix. The axis are ordered
        ``burnup, universeIndex, group, value/uncertainty``

        The ordering of the universes can be found in the ``'UNIVERSES'``
        vector if ``reconvert==True``, otherwise ``'universes'``. Each
        universe ID is present in this vector, ordered to their
        position along the second axis in the matrix.

        Parameters
        ----------
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

        Examples
        --------

        >>> import serpentTools
        >>> from scipy.io import loadmat
        >>> r = serpentTools.readDataFile('pwr_res.m')
        # convert to original variable names
        >>> r.toMatlab('pwr_res.mat', True)
        >>> loaded = loadmat('pwr_res.mat')
        >>> loaded['ABS_KEFF']
        array([[0.991938, 0.00145 ],
               [0.181729, 0.0024  ]])
        >>> kinf = loaded['INF_KINF']
        >>> kinf.shape
        (2, 1, 1, 2)
        >>> kinf[:, 0, 0, 0]
        array([0.993385, 0.181451])
        >>> tot = loaded['INF_TOT']
        >>> tot.shape
        (2, 1, 2, 2)
        >>> tot[:, 0, :, 0]
        array([[0.496553, 1.21388 ],
               [0.481875, 1.30993 ]])
        # use the universes key to identify ordering of universes
        >>> loaded['UNIVERSES']
        array([0])

        Raises
        ------
        ImportError
            If :term:`scipy` is not installed

        """
        converter = MatlabConverter(self, fileP)
        return converter.convert(reconvert, append, format, longNames,
                                 compress, oned)

    def _gather_matlab(self, reconvert):
        if reconvert:
            varFunc = getSerpentCaseName
            out = {
                varFunc(key): value for key, value in self.metadata.items()
            }
            out.update({
                varFunc(key): value for key, value in self.resdata.items()
            })
        else:
            out = {}
            varFunc = getMixedCaseName
            out.update(self.metadata)
            out.update(self.resdata)
        out.update(self._gather_univdata(varFunc))
        return out

    def _gather_univdata(self, func):
        numAppearances = {}

        for key in self.universes:
            if key.universe not in numAppearances:
                numAppearances[key.universe] = 1
                continue
            numAppearances[key.universe] += 1
        # check to make sure all universes appear an identical
        # number of times
        burnupVals = set(numAppearances.values())
        if len(burnupVals) != 1:
            raise SerpentToolsException(
                "Universes appear a different number of times:\n{}"
                .format(numAppearances))

        shapeStart = burnupVals.pop(), len(numAppearances)
        univOrder = tuple(sorted(numAppearances))

        univData = {func('universes'): univOrder}

        for univKey, univ in self.universes.items():

            # position in matrix
            uIndex = univOrder.index(univKey.universe)
            bIndex = univKey.step

            for expName, uncName in zip(
                    ('infExp', 'b1Exp', 'gc'), ('infUnc', 'b1Unc', 'gcUnc')):
                expD = getattr(univ, expName)
                uncD = getattr(univ, uncName)
                gatherPairedUnivData(univ, uIndex, bIndex, shapeStart, func,
                                     expD, uncD, univData)

        return univData

    @classmethod
    def fromSerpent(
            cls, fileOrStream, version=None, variableGroups=None,
            variables=None, getInfXS=None, getB1XS=None):

        from serpentTools.settings import rc
        from serpentTools.parsers import ResultsReader
        if version is None:
            version = rc["serpentVersion"]
        if variableGroups is None:
            variableGroups = rc["xs.variableGroups"]
        if variables is None:
            variables = rc["xs.variableExtras"]
        if getInfXS is None:
            getInfXS = rc["xs.getInfXS"]
        if getB1XS is None:
            getB1XS = rc["xs.getB1XS"]

        parser = ResultsReader(version, variableGroups, variables,
                               getInfXS, getB1XS)
        with getStream(fileOrStream) as stream:
            resdata, universes, metadata = parser.processStream(stream)

        return cls(resdata, universes, metadata)
