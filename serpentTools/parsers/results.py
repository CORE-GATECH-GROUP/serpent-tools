"""Parser responsible for reading the ``*res.m`` files"""
import re


from numpy import array, empty
import matplotlib.pyplot as plt


from serpentTools.settings import rc
from serpentTools.objects import splitItems, convertVariableName
from serpentTools.objects.containers import HomogUniv
from serpentTools.objects.readers import XSReader
from serpentTools.messages import info, SerpentToolsException, warning


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
        
    Raises
    ------
    SerpentToolsException
        If the file is corrupted (empty, not complete), 
        or the Serpent version cannot be supported
    """

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'xs')
        self.__fileObj = None
        self._idxSect = [False, False, False]
        self._counter = {'univ': 0, 'step': 0}
        self.metadata = {}   # metadata - data that does not change (e.g. execution path)
        self.resdata = {}    # results (e.g. k-eff)
        self.univdata = {}   # universe data (e.g. cross-sections)
        self._univID = {}
        self._days = 0
        self._bu = 0
        self._buIdx = 0

    def read(self):
        """Read through the results file and store requested data."""
        self._preProcessData()  # pre-process the data
        info('Preparing to read {}'.format(self.filePath))
        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                self._processResultsChunk(tline)
        info('Done reading results file')

    def _processResultsChunk(self, tline):
        """Performs the main processing of the results."""
        flagStore = self._positionInFile(tline)
        condStore = self._checkStoreData(flagStore)
        # If not an empty line or a comment
        if condStore and tline.strip() != '' and not re.search(r'\%', tline):
            currKey = re.search(r'^\w+', tline)
            if currKey is not None:
                keyName = convertVariableName(currKey.group())
                if keyName in self._resKeys:
                    values = self._getDictVal(tline)
                    if self._idxSect[0] and self._checkAddVariable(currKey.group()):
                        self.metadata[keyName] = values
                    elif self._idxSect[1]:
                        if keyName in convertVariableName(self._strSearch['days']) or keyName in \
                                convertVariableName(self._strSearch['bu']) or keyName in \
                                convertVariableName(self._strSearch['buIdx']):
                            self.resdata[keyName][self._counter['step'] - 1, :] = values
                        elif self._checkAddVariable(currKey.group()):
                            self.resdata[keyName][self._counter['step'] - 1, :] = values
                    else:
                        self._processUnivData(flagStore, currKey.group(), values)


    def _processUnivData(self, flagStore, varName, values):
        """Creates a univ container and stores the data"""
        if flagStore:
            self._currUniv = values
            if self._daysStr in self.resdata.keys() and self._buStr in self.resdata.keys():
                idxStep = self._counter['step']-1
                self._days = self.resdata[self._daysStr][idxStep, 0]
                self._bu = self.resdata[self._buStr][idxStep, 0]
                self._buIdx = self.resdata[self._buIdxStr][idxStep, 0]
                self._brachID = (self._currUniv, self._bu, self._buIdx, self._days)
            self.univdata[self._brachID] = HomogUniv(self._currUniv, self._bu, self._buIdx, self._days)
        else:
            if self._checkAddVariable(varName):
                if self._strSearch['inf'] in varName[0:4] or self._strSearch['b1'] in varName[0:4]:
                    vals, uncs = splitItems(values)
                    self.univdata[self._brachID].addData(varName, array(uncs), True)
                    self.univdata[self._brachID].addData(varName, array(vals), False)
                else:
                    self.univdata[self._brachID].addData(varName, array(values), False)

    def _preProcessData(self):
        """Pre-process data before collecting it"""
        self._versionSerpent()  # Get the utilized Serpent version
        self._numUnivSteps()  # Count the number of universes repetitions for memory allocation
        vals = [self._univID[item] for item in self._univID]
        if vals == {}:
            raise SerpentToolsException("No universes are present in the file.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        if len(vals) > 1 and not vals[1:] == vals[:-1]:
            raise SerpentToolsException("The repetitions of universes in the file is not equal.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        self._ChunkPosition()  # identify the 1st block for defining the dictionary
        if self._ChunkPos == 0:
            raise SerpentToolsException("The results file is corrupted.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        self._defineResultDict()  # Obtain the names of the variables to be stored
        if self._resKeys == []:
            raise SerpentToolsException("No variables appear in the results file.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))

    def _defineResultDict(self):
        """ Initializes the dictionary for ALL results included in .res.m"""
        self._idxSect = [False, False, False]
        self._resKeys = []  # Includes a complete set of .res variables
        fObj = open(self.filePath, 'r')
        numChar = 0  # count the number of characters
        nUniv = len(self._univID)  # number of steps
        nSteps = [self._univID[item] for item in self._univID][0]
        for tline in fObj:
            self._positionInFile(tline)
            if numChar < self._ChunkPos[0]:
                numChar += len(tline)
                continue
            # Not an empty line and not a comment
            if tline.strip() != '' and not re.search(r'\%', tline):
                currKey = re.search(r'^\w+', tline)
                if currKey:
                    keyName = convertVariableName(currKey.group())
                    self._initResData(keyName, nSteps, tline)
            numChar += len(tline)
            if numChar >= self._ChunkPos[1]:
                break
        fObj.close()
        self._idxSect = [False, False, False]

    def _initResData(self, key, nSteps, tline):
        """Initializes the dimensions of the variable"""
        if key not in self._resKeys:
            # Type of data (general meta, universes)
            self._resKeys.append(key)
            nvals = len(self._getDictVal(tline))
            if self._idxSect[0]:
                self.metadata[key] = ''
            elif self._idxSect[1]:
                self.resdata[key] = \
                    empty((nSteps, nvals))

    def _versionSerpent(self):
        """Identifies the utilized version"""
        with open(self.filePath, 'r') as fObject:
            if fObject is None:
                raise IOError("Attempting to read on file that does not exist.\n"
                              "Parser: {}\nFile: {}".format(self, self.filePath))
            for tline in fObject:
                # If not an empty line or a comment
                if re.search('VERSION', tline):
                    version = self._getDictVal(tline)
                    self._mapStrVersions(version)
                    break

    def _numUnivSteps(self):
        """Identifies how many universes and burnup steps are included"""
        #  Default number of universes and burnup steps
        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                # If not an empty line or a comment
                if re.search(self._strSearch['universe'], tline):
                    currUniv = self._getDictVal(tline)
                    self._addUniv(currUniv)

    def _addUniv(self, currUniv):
        """Add the current universe or add its counter"""
        if currUniv in self._univID:
            self._univID[currUniv] += 1
        else:
            self._univID[currUniv] = 1

    def _getDictVal(self, tline):
        """Gets the values to the dictionary"""
        SepOptions = {
            'list': r'\=.\[.+\]',
            'singleVal': r'\=.+',
            'string': r'\=.+\'.+\' '}
        if re.search(SepOptions['string'], tline) is not None:
            strMatch = re.search(SepOptions['string'], tline)
            idxpos = [pos for pos, char in enumerate(strMatch.group()) if char == '\'']
            return strMatch.group()[idxpos[0] + 1:idxpos[1]]
        elif re.search(SepOptions['list'], tline) is not None:
            strMatch = re.search(SepOptions['list'], tline)
            strMatch = self._ReplaceNaN(strMatch.group())  # remove NaN & Inf
            strMatch = self._stripRedundantChar(strMatch, ['[', ']', '=', ';'])
            return self._str2num(strMatch)
        elif re.search(SepOptions['singleVal'], tline) is not None:
            strMatch = re.search(SepOptions['singleVal'], tline)
            strMatch = self._stripRedundantChar(strMatch.group(), ['=', ';'])
            return self._str2num(strMatch)
        else:
            raise IOError("Corrupted line.\n"
                          "Parser: {}\nFile: {}\nLine: {}".format(self, self.filePath, tline))

    def _ChunkPosition(self):
        """Identifies the first block for the definition of the dictionary"""
        self._ChunkPos = [0, 0]  # [start, end] position of the first block
        cond = [False, False]
        fObj = open(self.filePath, 'r')
        numChar = 0  # counts the number of characters
        for tline in fObj:
            if re.search(self._strSearch['start'], tline) is not None:
                cond[0] = True
                self._ChunkPos[0] = numChar  # equivalent to tell()
            if re.search(self._strSearch['end'], tline) is not None and self._ChunkPos[0]:
                cond[1] = True
                self._ChunkPos[1] = numChar
                break
            numChar += len(tline)
            self._ChunkPos[1] = numChar
        fObj.close()

    def _positionInFile(self, tline):
        """The function identifies the position in the file and returns
        The sections are: general, meta, cross-sections"""
        if re.search(self._strSearch['start'], tline):
            self._idxSect = [True, False, False]
            return True
        elif re.search(self._strSearch['meta'], tline):
            self._idxSect = [False, True, False]
            return True
        elif re.search(self._strSearch['universe'], tline):
            self._idxSect = [False, False, True]
            return True
        return False

    def _checkStoreData(self, flagIn):
        """Checks whether the data should be stored in the dictionary"""
        flag = False
        idx = [i for i, item in enumerate(self._idxSect) if item]
        if idx != []:
            if idx[0] == 0 and self._counter['univ'] == 0 and self._counter['step'] == 0:
                flag = True # General data
            elif idx[0] == 1 and self._counter['univ'] == 0:
                flag = True
                if flagIn:
                    self._counter['step'] += 1  # Step data
            elif idx[0] == 2:
                flag = True
                if flagIn:
                    self._counter['univ'] += 1  # Universe data
                    if self._counter['univ'] >= len(self._univID):
                        self._counter['univ'] = 0
        else:
            flag = False  # Redundant data
        return flag

    def _mapStrVersions(self, version):
        """Assigns search strings for different Serpent versions"""
        MapStrVersions = {'Serpent 2.1.29':
                              {'start': 'VERSION ',
                               'end': 'counter',
                               'meta': 'Collision and reaction sampling',
                               'universe': 'GC_UNIVERSE_NAME',
                               'days':'BURN_DAYS',
                               'bu':'BURNUP',
                               'buIdx':'BURN_STEP',
                               'inf':'_INF',
                               'b1':'_B1'}}
        if version in MapStrVersions.keys():
            self._strSearch = MapStrVersions[version]
            self._daysStr = convertVariableName(self._strSearch['days'])
            self._buStr = convertVariableName(self._strSearch['bu'])
            self._buIdxStr = convertVariableName(self._strSearch['buIdx'])
            if rc['serpentVersion'] not in version:
                warning('The user version {} is not matching the results'
                        ' file version  {}'.format(rc['serpentVersion'], version))
        else:
            raise SerpentToolsException(
                'This version {} is not supported'.format(version)
            )

    def _stripRedundantChar(self, tlineOld, stripChars):
        """Removes redundant characters (e.g. []=) from the string"""
        tline = tlineOld
        for item in stripChars:
            tline = tline.replace(item, '')
        return tline

    def _str2num(self, string):
        """Converts a string of numbers to an array of numbers """
        numbers = [float(item) for item in string.split() if self._is_float(item)]
        return numbers

    def _is_float(self, string):
        """Checks whether the string can be converted to float"""
        try:
            num = float(string)
        except ValueError:
            return False
        return True

    def _ReplaceNaN(self, tlineOld):
        """Checks if there are NaNs or Inf and replace with zeros"""
        errVars = ['NaN', 'nan', 'NAN', 'INF', 'inf', 'Inf']
        tline = tlineOld
        for item in errVars:
            tline = tline.replace(item, '0.0E+00')
        return tline

    def plot(self, keyName, stepOption = None, brState = None, xlabel = None, ylabel = None):
        """Plot 1D results
        resdata (e.g. k-eff) is plotted vs. time/burnup
        univdata (e.g. cross-sections) is plotted vs. energy

        Parameters
        ----------
        keyName: Variable to be plotted
            Should appear in either resdata or univdata
        stepOption: 'burnup' or 'days' (default)
            If an incorrect entry is given then 'days' are used as default
        brState: (universe, burnup, burnIdx, days) state
        xlabel: description of x-axis (not mandatory)
        ylabel: description of y-axis (not mandatory)
        """

        xdata = None
        ydata = None
        plotFig = False
        if stepOption == None:
            stepOption = 'days'
        if keyName in self.resdata.keys():
            ydata = self.resdata[keyName][0:, 0]
            if 'burnup' in stepOption:
                xdata = self.resdata['burnup']
                if xlabel == None:
                    xlabel = 'Burnup, MWd/kg'
            else:
                xdata = self.resdata['burnDays']
                if xlabel == None:
                    xlabel = 'Time, days'
            if len(ydata) == len(xdata):
                plotFig = True
                plt.plot(xdata, ydata)
                plt.xlabel(xlabel)
                if ylabel == None:
                    ylabel = keyName
                plt.ylabel(ylabel)
            else:
                warning('No plot... xdata {} and ydata {} dimensions'
                        ' are not equal, '.format(len(xdata), len(ydata)))
        # obtain all the data points
        allStates = [st for st in self.univdata.keys()]
        if brState != None and brState in allStates:
            currState = self.univdata[brState]
            if keyName in currState.infExp.keys():
                ydata = [val for val in currState.infExp[keyName][0::2]
                         for _ in(0, 1)]
            elif keyName in currState.b1Exp.keys():
                ydata = [val for val in currState.b1Exp[keyName][0::2]
                         for _ in(0, 1)]
            else:
                warning(
                    'No plot... variable {} is not in univdata'.format(keyName))
            # obtain the energy grid: E0, E1, E2, ...
            if 'macroE' in currState.metadata.keys():
                energy = currState.metadata['macroE']
                energy[0] = 100  # set max. Energy to 100 MeV
                energy[len(energy) - 1] = 0.00001  # set min. E to 1E-5 MeV
                # create energy bins [E0, E1], [E1, E2], [E2, E3] ...
                xdata = [val for val in energy for _ in (0, 1)]
                xdata.pop(len(xdata) - 1)
                xdata.pop(0)
            else:
                warning(
                    'No plot... variable {} is not in univdata.metadata'
                        .format('macroE'))
            if ydata != None and xdata != None and len(ydata) == len(xdata):
                plotFig = True
                plt.loglog(xdata, ydata)
                if xlabel == None:
                    xlabel = 'Energy, MeV'
                plt.xlabel(xlabel)
                if ylabel == None:
                    ylabel = keyName
                plt.ylabel(ylabel)
            else:
                warning('No plot... xdata {} and ydata {} dimensions'
                        ' are not equal, '.format(len(xdata), len(ydata)))
        if not plotFig:
            warning('No plot... variable {} is not in resdata or the branching '
                    'state does not exist '.format(keyName))

# DEBUG
if __name__ == '__main__':
    filePath = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\Reactor-Simulation-tools\\Serpent Tools\\serpent-tools\\serpentTools\\tests\\pwr_res.m"
    res = ResultsReader(filePath)
    res.read()


