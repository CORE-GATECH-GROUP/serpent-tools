"""
Class responsible for reading multiple depletion files
and obtaining true uncertainties
"""

from six import iteritems
from numpy import zeros

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
