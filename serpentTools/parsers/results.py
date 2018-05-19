"""Parser responsible for reading the ``*res.m`` files"""
import re

import six

from numpy import array, vstack

from serpentTools.settings import rc
from serpentTools.objects import splitItems, convertVariableName
from serpentTools.objects.containers import HomogUniv
from serpentTools.objects.readers import XSReader
from serpentTools.utils import str2vec
from serpentTools.messages import (warning, debug, SerpentToolsException)


MapStrVersions = {'2.1.29': {'meta': 'VERSION ', 'rslt': 'MIN_MACROXS', 'univ': 'GC_UNIVERSE_NAME',
                             'days': 'BURN_DAYS', 'burn': 'BURNUP', 'infxs': 'INF_', 'b1xs': 'B1_',
                             'varsUnc': ['MICRO_NG', 'MICRO_E', 'MACRO_NG', 'MACRO_E']}}
MapStrVersions['2.1.30'] = MapStrVersions['2.1.29']
"""
Assigns search strings for different Serpent versions
Versions 2.1.29 and 2.1.30 are supported
"""

class ResultsReader(XSReader):
    """
    Parser responsible for reading and working with result files.

    Attributes
    ------------
    metadata: dict
        Dictionary with serpent descriptive variables as keys and the
        corresponding description. Within the _res.m file this data is
        printed multiple times, but contains the same description
        and thus is stored only once. e.g., 'version': 'Serpent 2.1.29'
    resdata: dict
        Dictionary with serpent time-dependent variables as keys and the
        corresponding values. The data is unique for each burnup step.
        Some variables also contain uncertainties.
        e.g., 'absKeff': [[9.91938E-01, 0.00145],[1.81729E-01, 0.00240]]
    universes: dict
        Dictionary of universe names and their corresponding
        :py:class:`~serpentTools.objects.containers.HomogUniv`
        objects. The keys describe a unique state:
        'universe', burnup (MWd/kg), burnup index, time (days)
        ('0', 0.0, 1, 0.0)

    Parameters
    ----------
    filePath: str
        path to the results file

    Raises
    ------
    SerpentToolsException:  Serpent version is not supported
                            No universes are found in the file
                            No results are collected
                            Corrupted results
    IOError: file is unexpectedly closes while reading
    """

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'xs')
        self.__serpentVersion = rc['serpentVersion']
        self._counter = {'meta': 0, 'rslt': 0, 'univ': 0}
        self._univlist = []
        self.metadata,  self.resdata, self.universes = {}, {}, {}
        self._regexpStr = re.compile(r'\'.+\'')  # string
        self._regexpVec = re.compile(r'(?<==.)\[.+?\]')  # vector
        self._regexpScl = re.compile(r'=.+;')  # scalar
        self._strtok = re.compile(r'^\w+')  # first word in the line

    def _read(self):
        """Read through the results file and store requested data."""
        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                self._processResults(tline)

    def _processResults(self, tline):
        """Performs the main processing of the results."""
        #  Not an empty line or a comment
        if tline.strip() and '%' not in tline and '=' in tline and 'idx = ' not in tline:
            self._whereAmI(tline)  # identify position in file
            varNameSer, varNamePy= self._getVarName(tline)  # obtain the name of the variable
            # should this variable be stored
            if not self._checkAddVariable(varNameSer):
                return
            varType, varVals = self._getVarValues(tline)  # values to be stored
            if self._posFile == 'meta':
                self._storeMetaData(varNamePy, varType, varVals)
            if self._posFile == 'rslt':
                self._storeResData(varNamePy, varVals)
            if self._posFile == 'univ':
                self._storeUnivData(varNameSer, varVals)

    def _whereAmI(self, tline):
        """Identify the position in the file."""
        if self._keysVersion['meta'] in tline:
            self._posFile = 'meta'
            self._counter['meta'] += 1
        elif self._keysVersion['rslt'] in tline:
            self._posFile = 'rslt'
            self._counter['rslt'] = divmod(self._counter['meta']-1, self._counter['univ'])[0] + 1
        elif self._keysVersion['univ'] in tline:
            self._posFile = 'univ'
            varType, varVals = self._getVarValues(tline)  # universe name
            self._univlist.append(varVals)

    def _storeUnivData(self, varNameSer, varVals):
        """Process universes' data"""
        brState = self._getBUstate()  # obtain the branching tuple
        values = str2vec(varVals) # convert the string to float numbers
        if not self.universes or brState not in self.universes.keys():
            self.universes[brState] = \
                HomogUniv(brState[0], brState[1], brState[2], brState[3])
            return
        if varNameSer not in self._keysVersion['varsUnc']:
            vals, uncs = splitItems(values)
            self.universes[brState].addData(varNameSer, array(uncs), True)
            self.universes[brState].addData(varNameSer, array(vals), False)
        else:
            self.universes[brState].addData(varNameSer, array(values), False)

    def _storeResData(self, varNamePy, varVals):
        """Process time-dependent results data"""
        vals = str2vec(varVals) # convert the string to float numbers
        if varNamePy in self.resdata.keys():  # extend existing matrix
            currVar = self.resdata[varNamePy]
            ndim = 1
            if len(currVar.shape) == 2:
                ndim = currVar.shape[0]
            if ndim < self._counter['rslt']:
                # append this data only once!
                try:
                    self.resdata[varNamePy] = vstack([self.resdata[varNamePy]
                                                         , vals])
                except:
                    raise SerpentToolsException("Error in appending {}  into "
                                                "{} of '.resdata' dict"
                                                .format(varNamePy, vals))
        else:
            self.resdata[varNamePy] = array(vals)  # define a new matrix

    def _storeMetaData(self, varNamePy, varType, varVals):
        """Store general descriptive data"""
        if varType == 'string':
            self.metadata[varNamePy] = varVals
        else:  # vector or scalar
            vals = str2vec(varVals) # convert string to floats
            self.metadata[varNamePy] = array(vals)  # overwrite existing data

    def _getBUstate(self):
        """Define unique branch state"""
        days, burnup, burnIdx = self._counter['meta'], self._counter['meta'],\
                                self._counter['rslt']  # assign indices
        if convertVariableName(self._keysVersion['days']) in self.resdata.keys():
            varPyDays = convertVariableName(self._keysVersion['days'])  # Py style
            if burnIdx > 1:
                days = self.resdata[varPyDays][-1, 0]
            else:
                days = self.resdata[varPyDays][-1]
        if convertVariableName(self._keysVersion['burn']) in self.resdata.keys():
            varPyBU = convertVariableName(self._keysVersion['burn'])  # Py style
            if burnIdx > 1:
                burnup = self.resdata[varPyBU][-1, 0]
            else:
                burnup = self.resdata[varPyBU][-1]
        return (self._univlist[-1], burnup, burnIdx, days)

    def _getVarName(self, tline):
        """Obtains the variable name and converts it to a python-style name."""
        currVar = self._strtok.search(tline)
        if currVar is not None:
            # return serpent-style and python-style names
            return currVar.group(), convertVariableName(currVar.group())

    def _getVarValues(self, tline):
        """Obtains the values of any variable."""
        strMatch, vecMatch, sclMatch = self._regexpStr.search(tline),\
                        self._regexpVec.search(tline),\
                        self._regexpScl.search(tline)
        varType, varVals = [], []
        if strMatch is not None:
            varType = 'string'
            varVals = tline[strMatch.span()[0]+1:strMatch.span()[1]-1]
        elif vecMatch is not None:
            varType = 'vector'
            varVals = tline[vecMatch.span()[0]+1:vecMatch.span()[1]-2]
        elif sclMatch is not None:
            varType = 'scalar'
            varVals = tline[sclMatch.span()[0]+1:sclMatch.span()[1]-2]
        return varType, varVals

    def getUniv(self, univ, burnup=None, index=None, timeDays=None):
        """
        Return a specific universe given the ID and time of interest

        If more than one time parameter is given, the hierarchy of search is:
        index (highest priority), burnup, timeDays (lowest priority)

        Parameters
        ----------
        univ: str
            Unique str for the desired universe
        burnup: float or int
            Burnup [MWd/kgU] of the desired universe
        timeDays: float or int
            Time [days] of the desired universe
        index: int
            Point of interest in the burnup/days index

        Returns
        -------
        :py:class:`~serpentTools.objects.containers.HomogUniv`
            Requested universe

        Raises
        ------
        KeyError:
            If the requested universe could not be found
        SerpentToolsException:
            If burnup, days and index are not given
        """
        if index is None and burnup is None and timeDays is None:
            raise SerpentToolsException('Burnup, time or index are required inputs')
        searchIndex = 2 if index is not None else 1 if burnup is not None else 3
        searchValue = index if index is not None else burnup if burnup is not None else timeDays
        if searchIndex == 2 and searchValue < 1:  # index must be non-zero
            raise KeyError(
                'Index read is {}, however only integers above zero are allowed'
                    .format(searchValue))
        for key, dictUniv in six.iteritems(self.universes):
            if key[0] == univ and key[searchIndex] == searchValue:
                debug('Found universe that matches with keys {}'
                      .format(key))
                return self.universes[key]
        searchName = 'index ' if index else 'burnup ' if burnup else 'timeDays '
        raise KeyError(
            'Could not find a universe that matched requested universe {} and '
            '{} {}'.format(univ, searchName, searchValue))

    def _precheck(self):
        """do a quick scan to ensure this looks like a results file."""
        if self.__serpentVersion in MapStrVersions:
            self._keysVersion = MapStrVersions[self.__serpentVersion]
        else:
            warning("Version {} is not supported by the "
                                        "ResultsReader".format(self.__serpentVersion))
        univSet = set()
        verWarning= True
        with open(self.filePath) as fid:
            if fid is None:
                raise IOError("Attempting to read on a closed file.\n"
                              "Parser: {}\nFile: {}".format(self, self.filePath))
            for tline in fid:
                if verWarning and self._keysVersion['meta'] in tline:
                    verWarning = False
                    varType, varVals = self._getVarValues(tline)  # version
                    if self.__serpentVersion not in varVals:
                        warning("Version {} is used, but version {} is defined"
                                " in settings".format(varVals,
                                                      self.__serpentVersion))
                if self._keysVersion['univ'] in tline:
                    varType, varVals = self._getVarValues(tline)  # universe
                    if varVals in univSet:
                        break
                    else:
                        univSet.add(varVals)  # add the new universe
            if not univSet:
                raise SerpentToolsException("No universes are found in the "
                                            "file {}".format(self.filePath))
            else:
                self._counter['univ'] = len(univSet)

    def _postcheck(self):
        """ensure the parser grabbed expected materials."""
        if divmod(self._counter['meta'],self._counter['univ'])[0] != self._counter['rslt']:
            raise SerpentToolsException(
                "The file {} is not complete. The reader found {} universes, "
                "{} time-points, and {} overall result points ".format(self.filePath,
                self._counter['univ'], self._counter['rslt'], self._counter['meta']))
        if not self.resdata and not self.metadata:
            for keys, dictUniv in six.iteritems(self.universes):
                if not dictUniv.hasData():
                    raise SerpentToolsException("metadata, resdata and universes are all empty "
                                        "from {}".format(self.filePath))

