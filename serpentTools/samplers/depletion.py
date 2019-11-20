"""
Class responsible for reading multiple depletion files
and obtaining true uncertainties
"""
from math import fabs

from numpy import zeros, zeros_like
from matplotlib import pyplot

from serpentTools.messages import SamplerError, warning
from serpentTools.utils import (
    magicPlotDocDecorator, formatPlot, DEPLETION_PLOT_LABELS,
)
from serpentTools.objects.materials import DepletedMaterialBase
from serpentTools.parsers.depletion import DepletionReader, DepPlotMixin
from serpentTools.samplers.base import (
    Sampler, SampledContainer,
)

CONSTANT_MDATA = ('names', 'zai')
"""metadata that should be invariant throughout repeated runs"""
VARIED_MDATA = ('days', 'burnup')
"""metadata that could be varied throughout repeated runs"""


class DepletionSampler(DepPlotMixin, Sampler):
    __doc__ = """
    Class that reads and stores data from multiple ``*dep.m`` files

    The following checks are performed in order to ensure that depletion
    files are of similar form:

    1. Keys of ``materials`` dictionary are consistent for all parsers
    2. Metadata keys are consistent for all parsers
    3. Isotope names and ZZAAA metadata are equal for all parsers

    These tests can be skipped by settings ``<sampler.skipPrecheck>`` to be
    ``False``.

    Parameters
    ----------
    files: str or iterable
        Single file or iterable (list) of files from which to read.
        Supports file globs, ``*dep.m`` expands to all files that
        end with ``dep.m``

    Attributes
    ----------
    materials: dict
        Dictionary with material names as keys and the corresponding
        :py:class:`~serpentTools.objects.materials.DepletedMaterial` class
        for that material as values
    metadata: dict
        Dictionary with file-wide data names as keys and the
        corresponding data, e.g. ``'zai'``: [list of zai numbers]
    metadataUncs: dict
        Dictionary containing uncertainties in file-wide metadata,
        such as burnup schedule
    allMdata: dict
        Dictionary where key, value pairs are name of metadata and
        metadata arrays for all runs. Arrays with be of one greater dimension,
        as the first index corresponds to the file index.
    files: set
        Unordered set containing full paths of unique files read
    settings: dict
        Dictionary of sampler-wide settings
    parsers: set
        Unordered set of all parsers that were successful
    map: dict
        Dictionary where key, value pairs are files and their corresponding
        parsers

    """

    def __init__(self, files):
        self.materials = {}
        self.metadata = {}
        self.metadataUncs = {}
        self.allMdata = {}
        Sampler.__init__(self, files, DepletionReader)
        DepPlotMixin.__init__(self)

    def __getitem__(self, name):
        """Retrieve a material from :attr:`materials`."""
        return self.materials[name]

    def _precheck(self):
        self._checkParserDictKeys('materials')
        self._checkParserDictKeys('metadata')
        self._checkMetadata()

    def _checkMetadata(self):
        misMatch = {}
        for parser in self:
            for key, value in parser.metadata.items():
                valCheck = (tuple(value) if key in CONSTANT_MDATA
                            else value.size)
                if key not in misMatch:
                    misMatch[key] = {}
                if valCheck not in misMatch[key]:
                    misMatch[key][valCheck] = {parser.filePath}
                else:
                    misMatch[key][valCheck].add(parser.filePath)
        for mKey, matches in misMatch.items():
            if len(matches) > 1:
                self._raiseErrorMsgFromDict(matches, 'values',
                                            '{} metadata'.format(mKey))

    def _process(self):
        for N, parser in enumerate(self.parsers):
            if not self.metadata:
                self.__allocateMetadata(parser.metadata)
            self._copyMetadata(parser.metadata, N)
            for matName, material in parser.materials.items():
                if matName in self.materials:
                    sampledMaterial = self.materials[matName]
                else:
                    numFiles = len(self.parsers)
                    self.materials[matName] = sampledMaterial = (
                        SampledDepletedMaterial(numFiles, material.name,
                                                parser.metadata))
                sampledMaterial.loadFromContainer(material)
        self._finalize()

    def _finalize(self):
        for _matName, material in self.materials.items():
            material.finalize()
        for key in VARIED_MDATA:
            allData = self.allMdata[key]
            self.metadata[key] = allData.mean(axis=0)
            self.metadataUncs[key] = allData.std(axis=0)

    def __allocateMetadata(self, parserMdata):
        for key in CONSTANT_MDATA:
            self.metadata[key] = parserMdata[key]
        vectorShape = tuple([len(self.files)]
                            + list(parserMdata['days'].shape))
        for key in VARIED_MDATA:
            self.allMdata[key] = zeros(vectorShape)

    def _copyMetadata(self, parserMdata, N):
        for key in VARIED_MDATA:
            self.allMdata[key][N, ...] = parserMdata[key]

    def _free(self):
        self.allMdata = {}
        for _mName, material in self.materials.items():
            material.free()

    def iterMaterials(self):
        """Yields material names and objects"""
        for name, material in self.materials.items():
            yield name, material


class SampledDepletedMaterial(SampledContainer, DepletedMaterialBase):
    __doc__ = """
    Class that stores data from a variety of depleted materials

    {equiv:s}

    .. note ::

        :py:func:`~serpentTools.samplers.depletion.SampledDepletedMaterial.free`
        sets ``allData`` to an empty dictionary {free:s}

    Parameters
    ----------
    N: int
        Number of containers to expect
    name: str
        Name of this material
    metadata: dict
        File-wide metadata for this run. Should contain ZAI and names for all
        isotopes, days, and burnup schedule

    Attributes
    ----------
    {depAttrs:s}
    uncertainties: dict
        Absolute uncertainties for all variables stored in ``data``
    allData: dict
        Dictionary where key, value pairs correspond to names of
        variables stored on this object and arrays of data from all files.
        The dimensionality will be increased by one, as the first index
        corresponds to the order in which files were loaded

    """.format(free=SampledContainer.docFree,
               equiv=DepletedMaterialBase.docEquiv,
               depAttrs=DepletedMaterialBase.docAttrs)

    def __init__(self, N, name, metadata):
        SampledContainer.__init__(self, N, DepletedMaterialBase)
        DepletedMaterialBase.__init__(self, name, metadata)
        self.uncertainties = {}
        self.allData = {}

    def _loadFromContainer(self, container):
        if container.name != self.name:
            warning("Attempting to store data from material {} onto "
                    "sampled material {}".format(self.name, container.name))
        for varName, varData in container.data.items():
            if not self.allData:
                self.__allocateLike(container)
            self.allData[varName][self._index] = varData

    def __allocateLike(self, container):
        for varName, varData in container.data.items():
            shape = tuple([self.N] + list(varData.shape))
            self.allData[varName] = zeros(shape)

    def _finalize(self):
        for varName, varData in self.allData.items():
            self.data[varName] = varData.mean(axis=0)
            self.uncertainties[varName] = varData.std(axis=0)

    def free(self):
        """Clear up data from all sampled parsers"""
        self.allData = {}

    @magicPlotDocDecorator
    def plot(self, xUnits, yUnits, timePoints=None, names=None, ax=None,
             sigma=3, xlabel=None, ylabel=None, logx=False,
             logy=False, loglog=False, legend=None, ncol=1, labelFmt=None,
             **kwargs):
        """
        Plot the average of some data vs. time for some or all isotopes.

        .. note::

            ``kwargs`` will be passed to the errorbar plot for all
            isotopes. If ``c='r'`` is passed, to make a plot red, then
            data for all isotopes plotted will be red and potentially
            very confusing.

        Parameters
        ----------
        xUnits: str
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'burnup'``
        timePoints: list or None
            If given, select the time points according to those
            specified here. Otherwise, select all points
        names: list or None
            If given, return y values corresponding to these isotope
            names. Otherwise, return values for all isotopes.
        {ax}
        {sigma}
        {xlabel}
        {ylabel}
        {logx}
        {logy}
        {loglog}
        {legend}
        {ncol}
        {matLabelFmt}
        {kwargs} :py:func:`matplotlib.pyplot.errorbar`

        Returns
        -------
        {rax}

        See Also
        --------
        * :meth:`~serpentTools.objects.materials.
          DepletedMaterialBase.getValues`
        * :func:`matplotlib.pyplot.errorbar`

        """
        if sigma and yUnits not in self.uncertainties:
            raise KeyError("Uncertainties for {} not stored"
                           .format(yUnits))
        if xUnits not in ('days', 'burnup'):
            raise KeyError("Plot method only uses x-axis data from <days> "
                           "and <burnup>, not {}".format(xUnits))
        xVals = timePoints if timePoints is not None else (
            self.days if xUnits == 'days' else self.burnup)
        sigma = int(fabs(sigma))
        colIndices = self._getColIndices(xUnits, timePoints)
        rowIndices = self._getRowIndices(names)
        yVals = self._slice(self.data[yUnits], rowIndices, colIndices)
        yUncs = self._slice(self.uncertainties[yUnits], rowIndices, colIndices)
        if xUnits in self.uncertainties and sigma:
            xUncs = (sigma * self._slice(self.uncertainties[xUnits], None,
                                         colIndices))
        else:
            xUncs = zeros_like(xVals)
        ax = ax or pyplot.gca()
        labels = self._formatLabel(labelFmt, names)
        yVals = yVals.copy(order='F')
        yUncs = yUncs.copy(order='F') * sigma

        for row in range(yVals.shape[0]):
            ax.errorbar(xVals, yVals[row], yerr=yUncs[row], xerr=xUncs,
                        label=labels[row], **kwargs)

        ax = sigmaLabel(ax, xlabel or DEPLETION_PLOT_LABELS[xUnits],
                        ylabel or DEPLETION_PLOT_LABELS[yUnits], sigma)
        formatPlot(ax, legend=legend, ncol=ncol, loglog=loglog, logx=logx,
                   logy=logy)
        return ax

    @magicPlotDocDecorator
    def spreadPlot(self, xUnits, yUnits, isotope=None, zai=None,
                   sampleKwargs=None, meanKwargs=None,
                   timePoints=None, ax=None,
                   xlabel=None, ylabel=None, logx=False, logy=False,
                   loglog=False, legend=True):
        """
        Plot the mean quantity and data from all sampled files.

        Parameters
        ----------
        xUnits : str
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits : str
            name of y value to return, e.g. ``'adens'``, ``'burnup'``
        isotope : str, optional
            Plot data for this isotope
        zai : int, optional
            Plot data for this isotope. Not allowed if ``isotope`` given.
        sampleKwargs : dict, optional
            Additional matplotlib-acceptable arguments to be passed into the
            plot when plotting data from unique runs, e.g.
            ``{"c": k, "alpha": 0.5}``.
        meanKwargs : dict, optional
            Additional matplotlib-acceptable argumentst to be used when
            plotting the mean value, e.g. ``{"c": "b", "marker": "o"}``
        timePoints : list or None
            If given, select the time points according to those
            specified here. Otherwise, select all points
        {ax}
        {xlabel}
        {ylabel}
        {logx}
        {logy}
        {loglog}
        {legend}

        Returns
        -------
        {rax}

        """
        if not self.allData:
            raise SamplerError("Data from all sampled files has been freed "
                               "and cannot be used in this plot method")
        if isotope is not None and zai is not None:
            raise ValueError("Please specify isotope name or zai, not both")
        elif isotope is None and zai is None:
            raise ValueError("Isotope name or zai needed")

        if sampleKwargs is None:
            sampleKwargs = {"c": "k", "alpha": 0.5, "marker": ""}
        if meanKwargs is None:
            meanKwargs = {"c": "#0173b2", "marker": "o"}

        ax = ax or pyplot.gca()
        if xUnits not in ('days', 'burnup'):
            raise KeyError("Plot method only uses x-axis data from <days> "
                           "and <burnup>, not {}".format(xUnits))
        xVals = timePoints if timePoints is not None else (
            self.days if xUnits == 'days' else self.burnup)
        if isotope is not None:
            rows = self._getRowIndices("names", [isotope])
        else:
            rows = self._getRowIndices("zai", [zai])
        cols = self._getColIndices(xUnits, timePoints)
        primaryData = self._slice(self.data[yUnits], rows, cols)[0]

        for data in self.allData[yUnits][:self._index]:
            plotData = self._slice(data, rows, cols)[0]
            ax.plot(xVals, plotData, **sampleKwargs)

        ax.plot(xVals, primaryData, label='Mean value', **meanKwargs)

        ax = sigmaLabel(ax, xlabel or DEPLETION_PLOT_LABELS[xUnits],
                        ylabel or DEPLETION_PLOT_LABELS[yUnits])

        formatPlot(ax, legend=legend, logx=logx, logy=logy, loglog=loglog)
        return ax


def sigmaLabel(ax, xlabel, ylabel, sigma=None):
    """Label the axes on a figure with some uncertainty."""
    confStr = r'$\pm{} \sigma$'.format(sigma) if sigma is not None else ''
    ax.set_xlabel(xlabel + confStr)
    ax.set_ylabel(ylabel + confStr)
    return ax
