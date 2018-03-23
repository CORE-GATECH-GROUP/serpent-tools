"""
Class to read Sensitivity file
"""
from collections import OrderedDict

import numpy
from numpy import empty, float64
from scipy.sparse import csr_matrix

import serpentTools
from serpentTools.engines import KeywordParser
from serpentTools.messages import warning, SerpentToolsException
from serpentTools.objects.readers import BaseReader

class SensitivityReader(BaseReader):
    
    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'sens')
        self.nMat = None
        self.nZai = None
        self.nPert = None
        self.nEne = None
        self.nMu = None
        self.mats = OrderedDict()
        self.zais = OrderedDict()
        self.perts = OrderedDict()
        self.latGen = None
        self._indxMap = {
            'materials': self.mats, 'nuclides': self.zais,
            'reactions': self.perts}
        self.ene = None
        self.lethargyWidths = None
        self.sensitivities = {}
        self.energyIntegratedSens = {}

    def read(self):
        self._precheck()
        self._read()
        self._postcheck()

    def _precheck(self):
        # maybe check if "SENS" is in the first few lines
        pass

    def _postcheck(self):
        if not self.sensitivities:
            warning("No sensitivity files stored from "
                    "{}".format(self.filePath))

    def _read(self):
        keys = stops = ['%']
        with KeywordParser(self.filePath, keys, stops) as parser:
            for chunk in parser.yieldChunks():
                if 'Number' in chunk[0]:
                    self.__processNumChunk(chunk)
                elif 'included' in chunk[0]:
                    what = chunk[0].split()[1]
                    self.__processIndexChunk(what, chunk)
                elif 'latent' in chunk[0]:
                    split = chunk[0].split()
                    self.latGen = int(split[split.index('latent') - 1])
                elif 'rate ratio' in chunk[0]:
                    self.__processRRChunk(chunk)

    def __processNumChunk(self, chunk):
        chunk = [line for line in chunk if 'SENS' in line]
        for line in chunk:
            split = line.split()
            attrN = 'n' + split[0].split('_')[-1].capitalize()
            if hasattr(self, attrN):
                setattr(self, attrN, int(split[-1][:-1]))
            else:
                raise SerpentToolsException(
                    'Attempted to set attribute {} from number block'.format(
                        attrN))

    def __processIndexChunk(self, what, chunk):
        key = what.lower()
        if key not in self._indxMap:
            raise SerpentToolsException(
                'Could not find proper index map for quantity '
                '{}'.format(what)
            )
        datum = self._indxMap[key]
        indx = 0
        store = False
        for line in chunk:
            if 'SENS' in line:
                store = True
                continue
            elif '];' in line:
                return
            if store:
                start = line.index('\'') + 1 if '\'' in line else 0
                stop = -2
                key = line[start:stop].rstrip()
                datum[key] = indx
                indx += 1

    def __processRRChunk(self, chunk):
        varName = None
        isEnergyIntegrated = False
        varName = None
        for line in chunk:
            if line == '\n' or '%' in line[:5] or '];' in line[:5]:
                continue
            if line[:3] == 'ADJ':
                fullVarName = line.split()[0]
                split = fullVarName.split('_')
                pertIndx = split.index('PERT')
                sensIndx = split.index('SENS')
                varName = '_'.join(split[pertIndx + 1: sensIndx])
                isEnergyIntegrated = split[-2:] == ['E', 'INT']
            elif varName is not None:
                self.__addRR(varName, strListToVec(line), isEnergyIntegrated)

    def __addRR(self, varName, vec, isEnergyIntegrated):
        dest = (self.energyIntegratedSens if isEnergyIntegrated
                else self.sensitivities)
        newShape = [2, self.nPert, self.nZai, self.nMat]
        if not isEnergyIntegrated:
            newShape.insert(1, self.nEne)
        dest[varName] = reshapePermuteSensMat(vec, newShape)

def reshapePermuteSensMat(vec, newShape):
    reshaped = numpy.reshape(vec, newShape)
    newAx = list(reversed(range(len(newShape))))
    return numpy.transpose(reshaped, newAx)


def strListToVec(strList):
    split = strList.split()
    return numpy.array([float(xx) for xx in split])

