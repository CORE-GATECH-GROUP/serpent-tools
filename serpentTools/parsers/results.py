"""Parser responsible for reading the ``*res.m`` files"""
from numbers import Real
import re

from numpy import array, empty, asarray

from serpentTools.settings import rc
from serpentTools.utils import convertVariableName
from serpentTools.objects.containers import HomogUniv, UnivTuple
from serpentTools.parsers._collections import RES_DATA_NO_UNCS
from serpentTools.objects.base import (DEF_COMP_LOWER,
                                       DEF_COMP_SIGMA, DEF_COMP_UPPER)
from serpentTools.utils import (
    str2vec,
    splitValsUncs,
    getCommonKeys,
    logDirectCompare,
    compareDocDecorator,
    getKeyMatchingShapes,
    getLogOverlaps,
    STR_REGEX,
    VEC_REGEX,
    SCALAR_REGEX,
    FIRST_WORD_REGEX,
    deconvertVariableName,
)
from serpentTools.messages import (
    warning, SerpentToolsException,
    info,
)

METADATA_CONV = {
    int: {
        'debug',
        'confidentialData',
        'pop',
        'cycles',
        'skip',
        'batchInterval',
        'srcNormMode',
        'seed',
        'ufsMode',
        'ufsOrder',
        'neutronTransportMode',
        'photonTransportMode',
        'groupConstantGeneration',
        'b1BurnupCorrection',
        'implicitReactionRates',
        'optimizationMode',
        'reconstructMicroxs',
        'reconstructMacroxs',
        'mgMajorantMode',
        'spectrumCollapse',
        'mpiTasks',
        'ompThreads',
        'mpiReproducibility',
        'ompReproducibility',
        'shareBufArray',
        'shareRes2Array',
    },
    float: {
        'cpuMhz',
    },
}
"""
Convert items in metadata dictionary from arrays to these data types
"""

VAR_NO_CONV = {
    "DF_SURFACE",
}

DF_CONV = {
    # No uncertainty, convert to int
    int: {
        "DF_SYM",
        "DF_N_SURF",
        "DF_N_CORN",
    },
    # No uncertainty, convert to float
    float: {
        "DF_VOLUME",
    },
    # No uncertainty, convert to array of float
    str2vec: {
        "DF_SURF_AREA",
        "DF_MID_AREA",
        "DF_CORN_AREA,",
        'MICRO_NG',
        'MICRO_E',
        'MACRO_NG',
        'MACRO_E',
    },
}
"""
Functions for converting variable data to various types
"""

UNIV_K_RE = re.compile('_K[EI][NF]F')


def varTypeFactory(key):
    if key in VAR_NO_CONV:
        return lambda x: (x, None)
    for typeFunc in DF_CONV:
        # no conversion for strings
        if key in DF_CONV[typeFunc]:
            return lambda x: (typeFunc(x), None)
    # Perform array conversion, return expected values and uncertainties
    if UNIV_K_RE.search(key) is not None:
        return lambda x: str2vec(x, out=tuple)
    return lambda x: splitValsUncs(x)


__all__ = ['ResultsReader', ]


class ListOfArrays(list):
    """Helper class for creating arrays by appending rows

    Parameters
    ----------
    values : numpy.ndarray, optional
        Initial row to insert into array

    Attributes
    ----------
    A : numpy.ndarray
        Array where each row ``A[i]`` is the ``i``-th row or
        sub-array that was appended
    """

    def __init__(self, values=None):
        super().__init__()
        self._shape = None
        self._dtype = None
        if values is not None:
            self.append(values)

    @property
    def A(self):
        return array(self)

    def append(self, value):
        """Append a row into the final array

        Parameters
        ----------
        value : numpy.ndarray or array-like
            Some object that can be coerced to a numpy.ndarray.
            Must have same shape and data type (e.g. float) as
            previously appended rows

        """
        value = asarray(value)
        if not self:
            self._shape = value.shape
            self._dtype = value.dtype
        elif self._shape != value.shape:
            raise ValueError(
                "Shapes do not agree: Current {} vs. incoming {}".format(
                    self._shape, value.shape))
        elif self._dtype != value.dtype:
            raise TypeError(
                "Types do not agree: Current {} vs. incoming {}".format(
                    self._dtype, value.dtype))
        super().append(value)


class ResultsReader:
    """
    Parser responsible for reading and working with result files.

    Parameters
    ----------
    version : str, optional
        Serpent version string to be expected. If not given, defaults
        to the latest version supported [2.1.31]
    variableGroups : iterable of str, optional
        Names of variable groups describing similar data, e.g. ``xs`` or
        ``times``
    variables : iterable of str, optional
        Names of variables exactly how they apppear in the output file
        to be processed, e.g. ``ANA_KEFF``
    getInfXS : bool
        Flag to process infinite medium homogenized universe data
    getB1XS : bool
        Flag to process critical leakage / B1 homogenized universe
        data

    Attributes
    ----------
    version : str
        Serpent version anticipated by the reader.
    variables : set of str
        Names of variables as they would appear in the output file
        to be parsed. If empty, all variables will be processed.
        Otherwise, only those that appear in this set will be
        processed
    getInfXS : bool
        Flag to process infinite medium homogenized universe data
    getB1XS : bool
        Flag to process critical leakage / B1 homogenized universe
        data

    """

    __METADATA_COMP_SKIPS = {
        'title',
        'inputFileName',
        'workingDirectory',
        'startDate',
        'completeDate',
        'seed',
    }
    """Metadata keys that will not be compared."""

    def __init__(self, version=None, variableGroups=None, variables=None,
                 getInfXS=True, getB1XS=True):
        self.version = version or "2.1.31"
        self._sectionStartWords = self._getSectionStartWords(self.version)
        self._burnupKeys = {k: convertVariableName(self._sectionStartWords[k])
                            for k in {"days", "burnup"}}
        self.variables = self._expandVariables(variableGroups, variables)
        self.getInfXS = getInfXS
        self.getB1XS = getB1XS

    def _getSectionStartWords(self, version):
        versions = {"2.1.29", "2.1.30", "2.1.31"}
        if version not in versions:
            warning(
                "Version {} not supported by {}. Must be one of {}".format(
                    version, self.__class__.__name__, ", ".join(versions)))
            warning(" Proceeding anyway. Please report strange behavior "
                    "to developers")
        return {
            'meta': 'VERSION ', 'rslt': 'MIN_MACROXS',
            'univ': 'GC_UNIVERSE_NAME', 'days': 'BURN_DAYS',
            'burnup': 'BURNUP', 'infxs': 'INF_', 'b1xs': 'B1_',
            'varsUnc': ['MICRO_NG', 'MICRO_E', 'MACRO_NG', 'MACRO_E'],
        }

    @staticmethod
    def _expandVariables(groups, named):
        if groups is None and named is None:
            return set()
        with rc as temprc:
            if groups is not None:
                temprc["xs.variableGroups"] = groups
            if named is not None:
                temprc["xs.variableExtras"] = named
            return temprc.expandVariables()

    def _precheck(self, stream):
        """Do a quick scan to ensure this looks like a results file."""
        univSet = set()
        verWarning = True
        tline = stream.readline()
        while tline:
            if verWarning and self._sectionStartWords['meta'] in tline:
                verWarning = False
                varType, varVals = self._getVarValues(tline)  # version
                if self.version not in varVals:
                    warning("SERPENT {} found, but version {} is "
                            "defined in settings"
                            .format(varVals, self.version))
                    warning("  Attemping to read anyway. Please report "
                            "strange behaviors/failures to developers.")
            elif self._sectionStartWords['univ'] in tline:
                varType, varVals = self._getVarValues(tline)  # universe
                if varVals in univSet:
                    break
                univSet.add(varVals)  # add the new universe
            tline = stream.readline()
        self._numUniv = len(univSet)

    def processStream(self, stream):
        """Update data dictionaries given a readable stream

        Parameters
        ----------
        stream : io.TextIOBase
            Readable stream of result data, like from an opened
            result file.

        Returns
        -------
        resdata : dict
            Dictionary of result data, e.g. ``anaKeff``, to be
            updated with the contents of ``stream``
        universes : dict
            Dictionary of homogenized universe data to be
            updated with the contents of ``stream``
        metadata : dict
            Dictionary of metadata, e.g. ``version``, to be
            updated with the contents of ``stream``

        Raises
        ------
        AttributeError
            If the stream is not seekable and therefore the number of
            universes
        """
        if not stream.seekable():
            # TODO Do we really need this?
            raise AttributeError(
                "Unable to rewind stream and count number of universes")

        self._counter = {'meta': 0, 'rslt': 0}
        self._univlist = []
        self._varTypeLookup = {}
        self._tempArrays = {}

        metadata = {}
        universes = {}
        resdata = {}

        start = stream.tell()
        self._precheck(stream)
        stream.seek(start, 0)

        for line in stream:
            self._processResults(line, metadata, universes)

        while self._tempArrays:
            # Consume temporary arrays
            key, temp = self._tempArrays.popitem()
            value = temp.A

            # Only insert first row if no burnup present
            if value.shape[0] == 1:
                resdata[key] = value.reshape(value.size)
            else:
                resdata[key] = value

        self._postcheck(resdata, universes, metadata)

        return resdata, universes, metadata

    def _processResults(self, tline, metadata, universes):
        """Performs the main processing of the results."""
        #  Not an empty line or a comment
        if (tline.strip() and '%' not in tline and '=' in tline
                and 'idx = ' not in tline):
            self._whereAmI(tline)  # identify position in file
            # obtain the name of the variable
            varNameSer, varNamePy = self._getVarName(tline)
            if not self._checkAddVariable(varNameSer):
                return
            varType, varVals = self._getVarValues(tline)  # values to be stored
            if self._posFile == 'meta':
                self._storeMetaData(metadata, varNamePy, varType, varVals)
            if self._posFile == 'rslt':
                self._storeResData(varNamePy, varVals)
            if self._posFile == 'univ':
                self._storeUnivData(universes, varNameSer, varVals)

    def _whereAmI(self, tline):
        """Identify the position in the file."""
        if self._sectionStartWords['meta'] in tline:
            self._posFile = 'meta'
            self._counter['meta'] += 1
        elif self._sectionStartWords['rslt'] in tline:
            self._posFile = 'rslt'
            if self._numUniv:
                self._counter['rslt'] = (
                    (self._counter['meta'] - 1) // self._numUniv + 1)
                return
            self._counter['rslt'] = self._counter['meta']
        elif self._sectionStartWords['univ'] in tline:
            self._posFile = 'univ'
            varType, varVals = self._getVarValues(tline)  # universe name
            self._univlist.append(varVals)

    def _checkAddVariable(self, variableName):
        """Check if the data for the variable should be stored"""
        # no variables given -> get all
        if not any(self.variables):
            return True
        # explicitly named
        if variableName in self.variables:
            return True
        if self.getB1XS and variableName.replace('B1_', '') in self.variables:
            return True
        if (self.getInfXS and variableName.replace('INF_', '') in
                self.variables):
            return True
        return False

    def _storeUnivData(self, universes, varNameSer, varVals):
        """Process universes data"""
        brState = self._getBUstate()  # obtain the branching tuple
        univ = universes.get(brState)
        if univ is None:
            univ = universes[brState] = HomogUniv(*brState)
        if varNameSer == self._sectionStartWords['univ']:
            return

        # Get variable specificy type converter
        if varNameSer not in self._varTypeLookup:
            self._varTypeLookup[varNameSer] = varTypeFactory(varNameSer)
        converter = self._varTypeLookup[varNameSer]
        values, uncertainties = converter(varVals)

        # Values without uncertainties
        univ.addData(varNameSer, values, False)
        if uncertainties is not None:
            univ.addData(varNameSer, uncertainties, True)

    def _storeResData(self, varNamePy, varVals):
        """Process time-dependent results data"""
        vals = str2vec(varVals)  # convert the string to float numbers

        stored = self._tempArrays.get(varNamePy)
        if stored is None:
            self._tempArrays[varNamePy] = ListOfArrays(vals)
        elif len(stored) < self._counter['rslt']:
            # append this data only once!
            try:
                stored.append(vals)
            except Exception as ee:
                raise SerpentToolsException(
                    "Error in appending {}  into {} of resdata:\n{}"
                    .format(varNamePy, vals, str(ee)))

    def _storeMetaData(self, metadata, varNamePy, varType, varVals):
        """Store general descriptive data"""
        if varType == 'string':
            metadata[varNamePy] = varVals
        else:  # vector or scalar
            vals = str2vec(varVals)  # convert string to floats
            metadata[varNamePy] = array(vals)  # overwrite existing data

    def _getBUstate(self):
        """Define unique branch state"""
        burnIdx = self._counter['rslt'] - 1
        dayVec = self._tempArrays.get(self._burnupKeys["days"])

        if dayVec is None:
            days = 0
        elif burnIdx:
            days = dayVec[-1][0]
        else:
            days = dayVec[0][0]

        burnupVec = self._tempArrays.get(self._burnupKeys["burnup"])

        if burnupVec is None:
            burnup = 0
        elif burnIdx:
            burnup = burnupVec[-1][0]
        else:
            burnup = burnupVec[0][0]

        return UnivTuple(self._univlist[-1], burnup, burnIdx, days)

    def _getVarName(self, tline):
        """Obtains the variable name and converts it to a python-style name."""
        currVar = FIRST_WORD_REGEX.search(tline)
        if currVar is not None:
            # return serpent-style and python-style names
            return currVar.group(), convertVariableName(currVar.group())

    def _getVarValues(self, tline):
        """Obtains the values of any variable."""
        strMatch = STR_REGEX.search(tline)
        vecMatch = VEC_REGEX.search(tline)
        sclMatch = SCALAR_REGEX.search(tline)
        varType, varVals = [], []
        if strMatch is not None:
            varType = 'string'
            varVals = tline[strMatch.span()[0] + 1:strMatch.span()[1] - 1]
        elif vecMatch is not None:
            varType = 'vector'
            varVals = tline[vecMatch.span()[0] + 1:vecMatch.span()[1] - 2]
        elif sclMatch is not None:
            varType = 'scalar'
            varVals = tline[sclMatch.span()[0] + 1:sclMatch.span()[1] - 2]
        return varType, varVals

    def _inspectData(self, results, universes, metadata):
        """Ensure the parser grabbed expected materials."""
        obtainedRes = (self._counter['meta'] // self._numUniv if self._numUniv
                       else self._counter['meta'])
        if obtainedRes != self._counter['rslt']:
            raise SerpentToolsException(
                "The file {} is not complete. The reader found {} universes, "
                "{} time-points, and {} overall result points "
                .format(self.filePath, self._numUniv,
                        self._counter['rslt'], self._counter['meta']))
        if not results and not metadata:
            for keys, dictUniv in universes.items():
                if dictUniv.hasData():
                    return
            raise SerpentToolsException(
                "metadata, resdata and universes are all empty")

    def _postcheck(self, results, universes, metadata):
        self._inspectData(results, universes, metadata)
        self._cleanMetadata(metadata)
        del (self._varTypeLookup, self._burnupKeys, self._sectionStartWords,
             self._counter, self._univlist, self._tempArrays)

    def _compare(self, other, lower, upper, sigma):
        similar = self.compareMetadata(other)
        similar &= self.compareResults(other, lower, upper, sigma)
        similar &= self.compareUniverses(other, lower, upper, sigma)
        return similar

    @compareDocDecorator
    def compareMetadata(self, other, header=False):
        """
        Return True if the metadata (settings) are identical.

        Parameters
        ----------
        other: :class:`ResultsReader`
            Class against which to compare
        {header}

        Returns
        -------
        bool:
            If the metadata are identical

        Raises
        ------
        {compTypeErr}
        """

        self._checkCompareObj(other)
        if header:
            self._compareLogPreMsg(other, quantity='metadata')
        myKeys = set(self.metadata.keys())
        otherKeys = set(other.metadata.keys())
        similar = not any(myKeys.symmetric_difference(otherKeys))
        commonKeys = getCommonKeys(myKeys, otherKeys, 'metadata')
        skips = commonKeys.intersection(self.__METADATA_COMP_SKIPS)
        if any(skips):
            info("The following items will be skipped in the comparison\n\t{}"
                 .format(', '.join(sorted(skips))))
        for key in sorted(commonKeys):
            if key in self.__METADATA_COMP_SKIPS:
                continue
            selfV = self.metadata[key]
            otherV = other.metadata[key]
            similar &= logDirectCompare(selfV, otherV, 0., 0., key)

        return similar

    @compareDocDecorator
    def compareResults(self, other, lower=DEF_COMP_LOWER,
                       upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA,
                       header=False):
        """
        Compare the contents of the results dictionary

        Parameters
        ----------
        other: :class:`ResultsReader`
            Class against which to compare
        {compLimits}
        {sigma}
        {header}

        Returns
        -------
        bool:
            If the results data agree to given tolerances

        Raises
        ------
        {compTypeErr}
        """
        self._checkCompareObj(other)
        if header:
            self._compareLogPreMsg(other, lower, upper, sigma, 'results')
        myRes = self.resdata
        otherR = other.resdata

        commonTypeKeys = getKeyMatchingShapes(myRes, otherR, 'results')

        similar = len(commonTypeKeys) == len(myRes) == len(otherR)

        for key in sorted(commonTypeKeys):
            mine = myRes[key]
            theirs = otherR[key]
            if key in RES_DATA_NO_UNCS:
                similar &= logDirectCompare(mine, theirs, lower, upper, key)
                continue
            myVals, myUncs = splitValsUncs(mine)
            theirVals, theirUncs = splitValsUncs(theirs)
            similar &= getLogOverlaps(key, myVals, theirVals, myUncs,
                                      theirUncs, sigma, relative=True)
        return similar

    @compareDocDecorator
    def compareUniverses(self, other, lower=DEF_COMP_LOWER,
                         upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA):
        """
        Compare the contents of the ``universes`` dictionary

        Parameters
        ----------
        other: :class:`ResultsReader`
            Reader by which to compare
        {compLimits}
        {sigma}

        Returns
        -------
        bool:
            If the contents of the universes agree to given tolerances

        Raises
        ------
        {compTypeErr}
        """
        self._checkCompareObj(other)
        myUniverses = self.universes
        otherUniverses = other.universes
        keyGoodTypes = getKeyMatchingShapes(myUniverses, otherUniverses,
                                            'universes')

        similar = len(keyGoodTypes) == len(myUniverses) == len(otherUniverses)

        for univKey in keyGoodTypes:
            myUniv = myUniverses[univKey]
            otherUniv = otherUniverses[univKey]
            similar &= myUniv.compare(otherUniv, lower, upper, sigma)
        return similar

    def _cleanMetadata(self, metadata):
        """Replace some items in metadata dictionary with easier data types."""
        origKeys = set(metadata.keys())
        for converter, keys in METADATA_CONV.items():
            for key in keys:
                if key in origKeys:
                    metadata[key] = converter(metadata[key])
                    origKeys.remove(key)


def getMixedCaseName(name):
    """
    Return the name of the variable used for exporting - camelCase
    """
    return name


def getSerpentCaseName(name):
    """
    Return the name of the variable used for exporting - SERPENT_CASE
    """
    return deconvertVariableName(name)


def gatherPairedUnivData(universe, uIndex, bIndex, shapeStart, convFunc,
                         expD, uncD, univData):
    """Helper function to update universe dictionary for exporting"""
    for xsKey, xsVal in expD.items():
        outKey = convFunc(xsKey)
        if outKey not in univData:
            if isinstance(xsVal, Real):
                shape = 1,
            else:  # assume array or has shape
                shape = xsVal.shape
            data = empty((shapeStart + shape + (2, )))
            univData[outKey] = data
        else:
            data = univData[outKey]
        data[bIndex, uIndex, ..., 0] = xsVal
        xsUnc = uncD.get(xsKey)
        if xsUnc is None:
            data[bIndex, uIndex, ..., 1] = 0.0
        else:
            data[bIndex, uIndex, ..., 1] = xsUnc
