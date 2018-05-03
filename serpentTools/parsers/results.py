"""Parser responsible for reading the ``*res.m`` files"""
import re

from numpy import array, vstack

from serpentTools.settings import rc
from serpentTools.objects import splitItems, convertVariableName
from serpentTools.objects.containers import HomogUniv
from serpentTools.objects.readers import XSReader

from serpentTools.messages import (info, debug, SerpentToolsException)


class ResultsReader(XSReader):
    """
    Parser responsible for reading and working with result files.

     .. note::

    Branching points for unique burnup steps and universes,
    will be overwritten
        
    Parameters
    ----------
    filePath: str
        path to the results file
        
    Errors
    ------
        If the Serpent version cannot be supported
    """

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'xs')
        self.__fileObj = None
        self._counter = {'meta': 0, 'rslt': 0, 'univ': 0}
        self._univlist = list()
        self.metadata = {}   # descriptive execution data (e.g. execution path)
        self.resdata = {}    # time-dependent quantities (e.g. k-eff)
        self.univdata = {}  # universes data (e.g. cross-sections)
        self._mapSerpentVersion()

    def _read(self):
        """Read through the results file and store requested data."""
        info('Preparing to read {}'.format(self.filePath))
        self._preRead()
        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                self._processResults(tline)
        info('Done reading results file')

    def _processResults(self, tline):
        """Performs the main processing of the results."""
        #  Not an empty line or a comment
        if tline.strip() and not re.search(r'\%', tline) and \
                re.search(r'=', tline) and not re.search(r'idx = ', tline):
            self._whereAmI(tline)  # identify position in file
            self._getVarName(tline)  # obtain the name of the variable
            # should this variable be stored
            if not self._checkAddVariable(self._varNameSer):
                return
            self._getVarValues(tline)  # values to be stored
            if self._posFile == 'meta':
                self._storeMetaData()
            if self._posFile == 'rslt':
                self._storeResData()
            if self._posFile == 'univ':
                self._storeUnivData()

    def _whereAmI(self, tline):
        """Identify the position in the file and assign the type of data to read."""
        if self._keysVersion['meta'] in tline:
            self._posFile = 'meta'
            self._counter['meta'] += 1
        elif self._keysVersion['rslt'] in tline:
            self._posFile = 'rslt'
            self._counter['rslt'] = divmod(self._counter['meta']-1, self._counter['univ'])[0] + 1
        elif self._keysVersion['univ'] in tline:
            self._posFile = 'univ'
            self._getVarValues(tline)  # obtain universe name
            self._univlist.append(self._varVals)

    def _storeUnivData(self):
        """Process universes' data"""
        self._getBUstate()  # obtain the branching tuple
        values = array(self._str2num())  # convert the string to float numbers
        if not self.univdata or self._brState not in self.univdata.keys():
            self.univdata[self._brState] = \
                HomogUniv(self._brState[0], self._brState[1], self._brState[2], self._brState[3])
            return
        if self._keysVersion['inxs'] in self._varNameSer or self._keysVersion['b1xs'] in self._varNameSer:
            vals, uncs = splitItems(values)
            self.univdata[self._brState].addData(self._varNameSer, array(uncs), True)
            self.univdata[self._brState].addData(self._varNameSer, array(vals), False)
        else:
            self.univdata[self._brState].addData(self._varNameSer, array(values), False)

    def _storeResData(self):
        """Process time-dependent results data"""
        vals = array(self._str2num())  # convert the string to float numbers
        if self._varNamePy in self.resdata.keys():  # extend existing matrix
            currVar = self.resdata[self._varNamePy]
            ndim = 1
            if len(currVar.shape) == 2:
                ndim = currVar.shape[0]
            if ndim < self._counter['rslt']:
                self.resdata[self._varNamePy] = vstack([self.resdata[self._varNamePy], array(vals)])
        else:
            self.resdata[self._varNamePy] = array(vals)  # define a new matrix

    def _storeMetaData(self):
        """Store general descriptive data"""
        if self._varType == 'string':
            self.metadata[self._varNamePy] = self._varVals
        else:  # vector or scalar
            vals = array(self._str2num())  # convert the string to float numbers
            self.metadata[self._varNamePy] = array(vals)  # overwrite exisitng data

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
        self._brState = (self._univlist[-1], burnup, burnIdx, days)

    def _getUniqueList(self):
        """Removes the repetitive components in the list."""
        univset = set(self._univlist)
        uniquelist = list(univset)
        return len(uniquelist)

    def _str2num(self):
        """Converts a string to a list of numbers."""
        num_list = [float(x) for x in self._varVals.split()]
        return num_list

    def _getVarName(self, tline):
        """Obtains the variable name and converts it to a python-style name."""
        self._varNameSer = []
        self._varNamePy = []
        currVar = re.search(r'^\w+', tline)
        if currVar is not None:
            self._varNameSer = currVar.group()  # variable name - Serpent style
            self._varNamePy = convertVariableName(self._varNameSer)  # Py style

    def _getVarValues(self, tline):
        """Obtains the values of any variable."""
        regexpStr = re.search(r'\'.+\'', tline)  # string
        regexpVec = re.search(r'(?<==.)\[.+?\]', tline)  # vector
        regexpScl = re.search(r'=.+;', tline)  # scalar
        if regexpStr is not None:
            self._varType = 'string'
            self._varVals = tline[regexpStr.span()[0]+1:regexpStr.span()[1]-1]
        elif regexpVec is not None:
            self._varType = 'vector'
            self._varVals = tline[regexpVec.span()[0]+1:regexpVec.span()[1]-2]
        elif regexpScl is not None:
            self._varType = 'scalar'
            self._varVals = tline[regexpScl.span()[0]+1:regexpScl.span()[1]-2]

    def _mapSerpentVersion(self):
        """Assigns search strings for different Serpent versions"""
        # reference version (valid for all versions after 2.1.10
        refVersion = {'meta': 'VERSION ',
                    'rslt': 'MIN_MACROXS',
                    'univ': 'GC_UNIVERSE_NAME',
                    'days': 'BURN_DAYS',
                    'burn': 'BURNUP',
                    'inxs': 'INF_',
                    'b1xs': 'B1_'}
        MapStrVersions = {}
        for iVer in range(10, 31):
            # create a new dictionary for each Serpent version
            MapStrVersions['2.1.{}'.format(iVer)] = dict(refVersion)
        # update any change manually
        MapStrVersions['2.1.30']['rslt'] = 'MEAN_SRC_WGT'
        if rc['serpentVersion'] in MapStrVersions.keys():
            self._keysVersion = MapStrVersions[rc['serpentVersion']]
        else:
            raise SerpentToolsException("Version {} is not supported by the "
                                        "ResultsReader".format(rc['serpentVersion']))

    def _preRead(self):
        """do a quick scan to count the number of universes."""
        with open(self.filePath) as fid:
            if fid is None:
                raise IOError("Attempting to read on a closed file.\n"
                              "Parser: {}\nFile: {}".format(self, self.filePath))
            for tline in fid:
                if self._keysVersion['univ'] in tline:
                    self._getVarValues(tline)  # obtain universe name
                    self._univlist.append(self._varVals)
                    nUniv = self._getUniqueList()
                    if len(self._univlist) > nUniv:
                        self._counter['univ'] = nUniv
                        self._univlist = list()
                        return
            if not self._univlist:
                raise SerpentToolsException("No universes are found in the "
                                            "file {}".format(self.filePath))

    def _precheck(self):
        """do a quick scan to ensure this looks like a results file."""
        with open(self.filePath) as fid:
            for line in fid:
                tline = line.split()
                if not tline:
                    continue
                elif 'ABS_KEFF' in tline:
                    return
            raise SerpentToolsException("Criticality values were not "
                                        "found in {}".format(self.filePath))

    def _postcheck(self):
        """ensure the parser grabbed expected materials."""
        if not self.resdata:
            raise SerpentToolsException("No time-dependent results obtained "
                                        "from {}".format(self.filePath))
        if divmod(self._counter['meta'],self._counter['univ'])[0] != self._counter['rslt']:
            debug('  found {} universes, {} time-points, and {} overall result points'.
                  format(self._counter['univ'], self._counter['rslt'], self._counter['meta']))
            raise SerpentToolsException("The file {} is not complete ".format(self.filePath))

