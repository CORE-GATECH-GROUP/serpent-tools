"""Parser responsible for reading the ``*res.m`` files"""
import re

from numpy import array, vstack

from serpentTools.settings import rc
from serpentTools.objects import splitItems, convertVariableName
from serpentTools.objects.containers import HomogUniv
from serpentTools.objects.readers import XSReader

from serpentTools.messages import (info, warning, debug, SerpentToolsException)

"""
Assigns search strings for different Serpent versions
Currently only versions 2.1.29 and 2.1.30 are supported
"""
MapStrVersions = {'2.1.29': {'meta': 'VERSION ', 'rslt': 'MIN_MACROXS', 'univ': 'GC_UNIVERSE_NAME',
                             'days': 'BURN_DAYS', 'burn': 'BURNUP', 'inxs': 'INF_', 'b1xs': 'B1_'},
                  '2.1.30': {'meta': 'VERSION ', 'rslt': 'MEAN_SRC_WGT', 'univ': 'GC_UNIVERSE_NAME',
                             'days': 'BURN_DAYS', 'burn': 'BURNUP', 'inxs': 'INF_', 'b1xs': 'B1_'}}

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
    univdata: dict
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
        self.__fileObj = None
        self._counter = {'meta': 0, 'rslt': 0, 'univ': 0}
        self._univlist = []
        self.metadata,  self.resdata, self.univdata = {}, {}, {}
        self._regexpStr = re.compile(r'\'.+\'')  # string
        self._regexpVec = re.compile(r'(?<==.)\[.+?\]')  # vector
        self._regexpScl = re.compile(r'=.+;')  # scalar
        self._strtok = re.compile(r'^\w+')  # first word in the line

    def _read(self):
        """Read through the results file and store requested data."""
        info('Preparing to read {}'.format(self.filePath))
        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                self._processResults(tline)
        info('Done reading results file')

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
        values = array(self._str2num(varVals))  # convert the string to float numbers
        if not self.univdata or brState not in self.univdata.keys():
            self.univdata[brState] = \
                HomogUniv(brState[0], brState[1], brState[2], brState[3])
            return
        if self._keysVersion['inxs'] in varNameSer or self._keysVersion['b1xs'] in varNameSer:
            vals, uncs = splitItems(values)
            self.univdata[brState].addData(varNameSer, array(uncs), True)
            self.univdata[brState].addData(varNameSer, array(vals), False)
        else:
            self.univdata[brState].addData(varNameSer, array(values), False)

    def _storeResData(self, varNamePy, varVals):
        """Process time-dependent results data"""
        vals = array(self._str2num(varVals))  # convert the string to float numbers
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
            vals = array(self._str2num(varVals))  # convert string to floats
            self.metadata[varNamePy] = array(vals)  # overwrite existing data

    def _getBUstate(self):
        """Define unique branch state"""
        days, burnup, burnIdx = self._counter['meta'], self._counter['meta'],\
                                self._counter['rslt']  # reset values
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

    def _getNumUniv(self):
        """Removes the repetitive components in the list."""
        univset = set(self._univlist)
        uniquelist = list(univset)
        return len(uniquelist)

    def _str2num(self, varVals):
        """Converts a string to a list of numbers."""
        num_list = [float(x) for x in varVals.split()]
        return num_list

    def _getVarName(self, tline):
        """Obtains the variable name and converts it to a python-style name."""
        currVar = self._strtok.search(tline)
        if currVar is not None:
            # return serpent-style and python-style names
            return currVar.group(), convertVariableName(currVar.group())

    def _getVarValues(self, tline):
        """Obtains the values of any variable."""
        str, vec, scl = self._regexpStr.search(tline),\
                        self._regexpVec.search(tline),\
                        self._regexpScl.search(tline)
        varType, varVals = [], []
        if str is not None:
            varType = 'string'
            varVals = tline[str.span()[0]+1:str.span()[1]-1]
        elif vec is not None:
            varType = 'vector'
            varVals = tline[vec.span()[0]+1:vec.span()[1]-2]
        elif scl is not None:
            varType = 'scalar'
            varVals = tline[scl.span()[0]+1:scl.span()[1]-2]
        return varType, varVals

    def _precheck(self):
        """do a quick scan to ensure this looks like a results file."""
        #MapStrVersions = self._mapSerpentVersion()
        if rc['serpentVersion'] in MapStrVersions:
            self._keysVersion = MapStrVersions[rc['serpentVersion']]
        else:
            raise warning("Version {} is not supported by the "
                                        "ResultsReader".format(rc['serpentVersion']))
        with open(self.filePath) as fid:
            if fid is None:
                raise IOError("Attempting to read on a closed file.\n"
                              "Parser: {}\nFile: {}".format(self, self.filePath))
            for tline in fid:
                if self._keysVersion['meta'] in tline:
                    varType, varVals = self._getVarValues(tline)  # actual serpent version used
                    if rc['serpentVersion'] not in varVals:
                        raise warning("Version {} used is different from the defined in settings {} "
                                                    .format(varVals, rc['serpentVersion']))
                if self._keysVersion['univ'] in tline:
                    varType, varVals = self._getVarValues(tline)  # universe
                    self._univlist.append(varVals)
                    nUniv = self._getNumUniv()
                    if len(self._univlist) > nUniv:
                        self._counter['univ'] = nUniv
                        self._univlist = []
                        return
            if not self._univlist:
                raise SerpentToolsException("No universes are found in the "
                                            "file {}".format(self.filePath))

    def _postcheck(self):
        """ensure the parser grabbed expected materials."""
        if not self.resdata and not self.metadata and not self.univdata:
            raise SerpentToolsException("No results were collected "
                                        "from {}".format(self.filePath))
        if divmod(self._counter['meta'],self._counter['univ'])[0] != self._counter['rslt']:
            debug('  found {} universes, {} time-points, and {} overall result points'.
                  format(self._counter['univ'], self._counter['rslt'], self._counter['meta']))
            raise SerpentToolsException("The file {} is not complete ".format(self.filePath))

