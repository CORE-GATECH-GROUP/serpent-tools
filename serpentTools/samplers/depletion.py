"""
Class responsible for reading multiple depletion files
and obtaining true uncertainties
"""
from math import fabs
from six import iteritems
from numpy import zeros, zeros_like

from matplotlib import pyplot

from serpentTools.parsers.depletion import DepletionReader
from serpentTools.samplers import Sampler, SampledContainer
from serpentTools.objects.materials import DepletedMaterialBase

CONSTANT_MDATA = ('names', 'zai')
"""metadata that should be invariant throughout repeated runs"""
VARIED_MDATA = ('days', 'burnup')
"""metadata that could be varied throughout repeated runs"""


class DepletionSampler(Sampler):

    def __init__(self, files):
        self.materials = {}
        self.metadata = {}
        self.metadataUncs = {}
        self.allMdata = {}
        Sampler.__init__(self, files, DepletionReader)

    def _precheck(self):
        self._checkParserDictKeys('materials')
        self._checkParserDictKeys('metadata')
        self._checkMetadata()

    def _checkMetadata(self):
        misMatch = {}
        for parser in self:
            for key, value in iteritems(parser.metadata):
                valCheck = (tuple(value) if key in CONSTANT_MDATA
                            else value.size)
                if key not in misMatch:
                    misMatch[key] = {}
                if valCheck not in misMatch[key]:
                    misMatch[key][valCheck] = {parser.filePath}
                else:
                    misMatch[key][valCheck].add(parser.filePath)
        for mKey, matches in iteritems(misMatch):
            if len(matches) > 1:
                self._raiseErrorMsgFromDict(matches, 'values',
                                            '{} metadata'.format(mKey))

    def _process(self):
        for N, parser in enumerate(self.parsers):
            if not self.metadata:
                self.__allocateMetadata(parser.metadata)
            self._copyMetadata(parser.metadata, N)
            for matName, material in iteritems(parser.materials):
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
        for _matName, material in iteritems(self.materials):
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
        for _mName, material in iteritems(self.materials):
            material.free()

    def iterMaterials(self):
        for name, material in iteritems(self.materials):
            yield name, material


class SampledDepletedMaterial(SampledContainer, DepletedMaterialBase):

    def __init__(self, N, name, metadata):
        SampledContainer.__init__(self, N, DepletedMaterialBase)
        DepletedMaterialBase.__init__(self, name, metadata)
        self.uncertainties = {}
        self.allData = {}

    def _loadFromContainer(self, container):
        for varName, varData in iteritems(container.data):
            if not self.allData:
                self.__allocateLike(container)
            self.allData[varName][self._index] = varData

    def __allocateLike(self, container):
        for varName, varData in iteritems(container.data):
            shape = tuple([self.N] + list(varData.shape))
            self.allData[varName] = zeros(shape)

    def _finalize(self):
        for varName, varData in iteritems(self.allData):
            self.data[varName] = varData.mean(axis=0)
            self.uncertainties[varName] = varData.std(axis=0)

    def free(self):
        self.allData = {}

    def plot(self, xUnits, yUnits, timePoints=None, names=None, ax=None,
             sigma=3, legend=True, label=True, xlabel=None, ylabel=None):
        """
        Plot the average of some data vs. time for some or all isotopes.

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
        ax: None or matplotlib.pyplot.axes
            If given, add the data to this plot.
            Otherwise, create a new plot
        sigma: int
            Confidence interval for uncertainties
        legend: bool
            Automatically add the legend
        label: bool
            Automatically label the axis
        xlabel: None or str
            If given, use this as the label for the x-axis.
            Otherwise, use xUnits
        ylabel: None or str
            If given, use this as the label for the y-axis.
            Otherwise, use yUnits

        Returns
        -------
        matplotlib.pyplot.axes
            Axes corresponding to the figure that was plotted

        See Also
        --------
        :py:func:`~serpentTools.objects.materials.DepletedMaterial.getValues`

        """
        if sigma and yUnits not in self.uncertainties:
            raise KeyError("Uncertainties for {} not stored"
                           .format(yUnits))
        sigma = int(fabs(sigma))
        xVals = timePoints or self.days
        colIndices = self._getColIndices(xUnits, timePoints)
        rowIndices = self._getRowIndices(names)
        yVals = self._slice(self.data[yUnits], rowIndices, colIndices)
        yUncs = self._slice(self.uncertainties[yUnits], rowIndices, colIndices)
        if xUnits in self.uncertainties and sigma:
            xUncs = (sigma * self._slice(self.uncertainties[xUnits], None,
                                         colIndices))
        else:
            xUncs = zeros_like(xVals)
        ax = ax or pyplot.axes()
        labels = names or self.names
        yVals = yVals.copy(order='F')
        yUncs = yUncs.copy(order='F') * sigma
        for row in range(yVals.shape[0]):
            ax.errorbar(xVals, yVals[row], yerr=yUncs[row], xerr=xUncs,
                        label=labels[row])

        # format the plot
        if legend:
            ax.legend()
        if label:
            confStr = r'$\pm{} \sigma$'.format(sigma) if sigma else ''
            xlabel = (xlabel or xUnits) + confStr
            ylabel = (ylabel or yUnits) + confStr
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
        return ax
