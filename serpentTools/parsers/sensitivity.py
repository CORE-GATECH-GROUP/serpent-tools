"""
Class to read Sensitivity file
"""
from collections import OrderedDict

import numpy
from numpy import empty, float64
from scipy.sparse import csr_matrix

import serpentTools
from serpentTools.engines import KeywordParser
from serpentTools.messages import warning, SerpentToolsException, critical
from serpentTools.objects import convertVariableName
from serpentTools.objects.readers import BaseReader

class SensitivityReader(BaseReader):
    """
    Class for reading sensitivity files

    The arrays that are stored in ``sensitivities`` and
    ``energyIntegratedSens`` are stored under converted names.
    The original names from SERPENT are of the form
    ``ADJ_PERT_KEFF_SENS`` or ``ADJ_PERT_KEFF_SENS_E_INT``, 
    respectively. Since this reader stores the resulting arrays
    in unique locations, the names are converted to a succint form.
    The two arrays listed above would be stored both as ``keff`` 
    in ``sensitivities`` and ``energyIntegratedSens``. 
    All names are converted to ``mixedCaseNames`` to fit the
    style of the project.

    Ordered dictionaries ``materials``, ``zais``, and 
    ``perts`` contain keys of the names of their respective
    data, and the corresponding index, ``iSENS_ZAI_zzaaai``, 
    in the sensitivity arrays. These arrays are zero-indexed,
    so the first item will have an index of zero. The data stored
    in the ``sensitivities`` and ``energyIntegratedSens`` dictionaries
    has the exact same structure as if the arrays were loaded into
    ``MATLAB``/``Octave``, but with zero-indexing.

    Parameters
    ----------
    filePath: str
        Path to sensitivity file

    Attributes
    ----------
    nMat: None or int
        Number of materials
    nZai: None or int
        Number of perturbed isotopes 
    nPert: None or int
        Number of perturbations 
    nEne: None or int
        Number of energy groups
    nMu: None or int
        Number of perturbed materials
    materials: :py:class:`~collections.OrderedDict`
        Ordered dictionary of materials that have
        been perturbed. 
    zais: :py:class:`~collections.OrderedDict`
        Ordered dictionary of nuclides that
        have been perturbed
    perts: :py:class:`~collections.OrderedDict`
        Ordered dictionary of reactions that 
        have been perturbed, e.g `'total xs'`
    latGen: int
        Number of latent generations used to generate
        these sensitivities
    energies: None or :py:class:`numpy.array`
        Array of energy bounds for the sensitivities, from
        lowest to highest
    lethargyWidths: None or :py:class:`numpy.array`
        Array of lethargy widths of each energy group.
    sensitivities: dict
        Dictionary of names of sensitivities and their corresponding
        arrays. 
    energyIntegratedSens: dict
        Dictionary of names of the sensitivities that have been integrated
        against energy, and their corresponding arrays
    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'sens')
        self.nMat = None
        self.nZai = None
        self.nPert = None
        self.nEne = None
        self.nMu = None
        self.materials = OrderedDict()
        self.zais = OrderedDict()
        self.perts = OrderedDict()
        self.latGen = None
        self._indxMap = {
            'materials': self.materials, 'nuclides': self.zais,
            'reactions': self.perts}
        self.energies = None
        self.lethargyWidths = None
        self.sensitivities = {}
        self.energyIntegratedSens = {}

    def _precheck(self):
        # maybe check if "SENS" is in the first few lines
        pass

    def _postcheck(self):
        if not self.sensitivities:
            warning("No sensitivity files stored from "
                    "{}".format(self.filePath))

    def _read(self):
        keys = stops = ['%']
        throughParams = False
        with KeywordParser(self.filePath, keys, stops) as parser:
            for chunk in parser.yieldChunks():
                if not throughParams:
                    chunk0 = chunk[0]
                    if 'Number' in chunk0:
                        self.__processNumChunk(chunk)
                    elif 'included' in chunk0:
                        what = chunk0.split()[1]
                        self.__processIndexChunk(what, chunk)
                    elif 'energy' in chunk0:
                        self.__processEnergyChunk(chunk)
                    elif 'latent' in chunk0:
                        split = chunk0.split()
                        self.latGen = int(split[split.index('latent') - 1])
                        throughParams = True 
                    continue
                self.__processSensChunk(chunk)

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
            if '];' in line:
                return
            if store:
                start = line.index('\'') + 1 if '\'' in line else 0
                stop = -2
                key = line[start:stop].rstrip()
                datum[key] = indx
                indx += 1
        raise SerpentToolsException(
            "Unexpected index chunk {}".format(chunk))

    def __processEnergyChunk(self, chunk):
        for line in chunk:
            if 'SENS' == line[:4]:
                break
        else:
            raise SerpentToolsException("Could not find SENS parameter "
                                        "in energy chunk {}".format(chunk[:3]))
        splitLine = line.split()
        varName = splitLine[0].split('_')[1:]
        varValues = strListToVec(splitLine[3:-1])
        if varName[0] == 'E':
            self.energies = varValues
        elif varName == ['LETHARGY', 'WIDTHS']:
            self.lethargyWidths = varValues
        else:
            warning("Unanticipated energy setting {}"
                    .format(splitLine[0]))

    def __processSensChunk(self, chunk):
        varName = None
        isEnergyIntegrated = False
        varName = None
        for line in chunk:
            if line == '\n' or '%' in line[:5] or '];' == line[:2]:
                continue
            if line[:3] == 'ADJ':
                fullVarName = line.split()[0]
                split = fullVarName.split('_')
                pertIndx = split.index('PERT')
                sensIndx = split.index('SENS')
                varName = '_'.join(split[pertIndx + 1: sensIndx])
                isEnergyIntegrated = split[-2:] == ['E', 'INT']
            elif varName is not None:
                self.__addSens(varName, strListToVec(line), isEnergyIntegrated)
                varName = None

    def __addSens(self, varName, vec, isEnergyIntegrated):
        dest = (self.energyIntegratedSens if isEnergyIntegrated
                else self.sensitivities)
        newShape = [2, self.nPert, self.nZai, self.nMat]
        if not isEnergyIntegrated:
            newShape.insert(1, self.nEne)
        try:
            newName = convertVariableName(varName)
            dest[newName] = reshapePermuteSensMat(vec, newShape)
        except Exception as ee:
            critical("The following error was raised attempting to "
                     "reshape matrix {}".format(varName))
            raise ee

    def _precheck(self):
        with open(self.filePath) as fobj:
            for count in range(5):
                if 'SENS' == fobj.readline()[:4]:
                    return
        warning("Could not find any lines starting with SENS. "
                "Is {} a sensitivity file?".format(self.filePath))
    
    def _postcheck(self):
        if not self.sensitivities:
            raise SerpentToolsException("No sensitivity data stored on reader")
        if not self.energyIntegratedSens:
            raise SerpentToolsException("No energy integrated sensitivities "
                                        "stored on reader")

def reshapePermuteSensMat(vec, newShape):
    """
    Return an array that has been reshaped and permuted like the sens file.
    """
    reshaped = numpy.reshape(vec, newShape, order='F')
    newAx = list(reversed(range(len(newShape))))
    return numpy.transpose(reshaped, newAx)


def strListToVec(strList):
    """Convert a string of list of strings to vector."""
    split = strList.split() if isinstance(strList, str) else strList
    return numpy.array([float(xx) for xx in split])

