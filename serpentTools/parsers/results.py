"""Parser responsible for reading the ``*res.m`` files"""
import re


from six import iteritems
from numpy import array, empty


from serpentTools.objects import splitItems
from serpentTools.objects.containers import HomogUniv
from serpentTools.objects.readers import XSReader
from serpentTools.messages import debug, info


class ResultsReader(XSReader):
    """
    Parser responsible for reading and working with result files.

    Parameters
    ----------
    filePath: str
        path to the results file
    """

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'xs')
        self.__fileObj = None
        self._strSections = {
            'start': 'Version, title and date',
            'end': 'counter',
            'meta': 'Collision and reaction sampling',
            'xs': 'constant generation',
            'universe': 'GC_UNIVERSE_NAME'}
        self._idxSect = [False, False, False]
        self._counter = {'univ': 0, 'step': 0}
        self.gendata = {}  # general results data (e.g. execution path)
        self.metadata = {}  # metadata (e.g. k-eff)
        self.univdata = {}  # universe data (e.g. cross-sections)
        self._univ = {}

    def read(self):
        """Read through the results file and store requested data."""
        self._preProcessData()  # pre-process the data
        info('Preparing to read {}'.format(self.filePath))
        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                self._processResultsChunk(tline)
        print("Done reading results file ...")

    def _processResultsChunk(self, tline):
        """Performs the main processing of the results."""
        flagStore = self._positionInFile(tline)
        condStore = self._checkStoreData(flagStore)
        # If not an empty line or a comment
        if condStore and tline.strip() != '' and not re.search(r'\%', tline):
            currKey = re.search(r'^\w+', tline)
            if currKey is not None and currKey.group() in self._resKeys:
                values = self._getDictVal(tline)
                if self._idxSect[0]:
                    self.gendata[currKey.group()] = values
                elif self._idxSect[1]:
                    self.metadata[currKey.group()][self._counter['step']-1, :] = values
                else:
                    if flagStore:
                        self._currUniv = values
                    else:
                        self._processBranchUniverses(self._currUniv, currKey.group(), values, 0.0, 0.0,
                                                     self._counter['step'] - 1)
                    # self.univdata[currKey.group()][self._counter['univ']-1, self._counter['step']-1, :] = values


    def _processBranchUniverses(self, unvID, varName, varValues, branch, burnup, burnupIndex):
        """Add universe data at this burnup."""
        univ = HomogUniv(XSReader, unvID, burnup, burnupIndex, day=0.0)
        if self._checkAddVariable(varName):
            vals, uncs = splitItems(varValues)
            univ.addData(varName, array(vals), uncertaity=False)
            univ.addData(varName, array(uncs), unertainty=True)

    def _preProcessData(self):
        """Pre-process data before collecting it"""
        self._numUnivSteps()  # Count the number of universes repetitions for memory allocation
        vals = [self._univ[item] for item in self._univ]
        if vals == {}:
            raise IOError("No universes are present in the file.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        if len(vals) > 1 and not vals[1:] == vals[:-1]:
            raise IOError("The repetitions of universes in the file is not equal.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        self._ChunkPosition()  # identify the 1st block for defining the dictionary
        if self._ChunkPos == 0:
            raise IOError("The results file is corrupted.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        self._defineResultDict()  # Obtain the names of the variables to be stored
        if self._resKeys == []:
            raise IOError("No variables appear in the results file.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))

    def _defineResultDict(self):
        """ Initializes the dictionary for ALL results included in .res.m"""
        self._idxSect = [False, False, False]
        self._resKeys = []  # Includes a complete set of .res variables
        fObj = open(self.filePath, 'r')
        numChar = 0  # count the number of characters
        nUniv = len(self._univ)  # number of steps
        nSteps = [self._univ[item] for item in self._univ][0]
        for tline in fObj:
            self._positionInFile(tline)
            if numChar < self._ChunkPos[0]:
                numChar += len(tline)
                continue
            # Not an empty line and not a comment
            if tline.strip() != '' and not re.search(r'\%', tline):
                currKey = re.search(r'^\w+', tline)
                if currKey:
                    self._initResData(currKey, nSteps, nUniv, tline)
            numChar += len(tline)
            if numChar >= self._ChunkPos[1]:
                break
        fObj.close()
        self._idxSect = [False, False, False]

    def _initResData(self, key, nSteps, nUniv, tline):
        """Initializes the dimensions of the variable"""
        if key.group() not in self._resKeys:
            # Type of data (general meta, universes)
            self._resKeys.append(key.group())
            nvals = len(self._getDictVal(tline))
            if self._idxSect[0]:
                self.gendata[key.group()] = ''
            elif self._idxSect[1]:
                self.metadata[key.group()] = \
                    empty((nSteps, nvals))
            elif self._idxSect[2]:
                self.univdata[key.group()] = \
                    empty((nUniv, nSteps, nvals))

    def _numUnivSteps(self):
        """Identifies how many universes and burnup steps are included"""
        #  Default number of universes and burnup steps
        with open(self.filePath, 'r') as fObject:
            if fObject is None:
                raise IOError("Attempting to read on file that does not exist.\n"
                              "Parser: {}\nFile: {}".format(self, self.filePath))
            for tline in fObject:
                # If not an empty line or a comment
                if re.search(self._strSections['universe'], tline):
                    currUniv = self._getDictVal(tline)
                    self._addUniv(currUniv)

    def _addUniv(self, currUniv):
        """Add the current universe or add its counter"""
        if currUniv in self._univ:
            self._univ[currUniv] += 1
        else:
            self._univ[currUniv] = 1

    def _getDictVal(self, tline):
        """Gets the values to the dictionary"""
        SepOptions = {
            'list': r'\=.\[.+\]',
            'singleVal': r'\=.+',
            'string': r'\=.+\'.+\' '}
        if re.search(SepOptions['string'], tline) is not None:
            strMatch = re.search(SepOptions['string'], tline)
            return self._stripRedundantChar(strMatch.group(), ['\'', '=', ';'])
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
            if re.search(self._strSections['start'], tline) is not None:
                cond[0] = True
                self._ChunkPos[0] = numChar  # equivalent to tell()
            if re.search(self._strSections['end'], tline) is not None and self._ChunkPos[0]:
                cond[1] = True
                self._ChunkPos[1] = numChar
                break
            numChar += len(tline)
            self._ChunkPos[1] = numChar
        fObj.close()

    def _positionInFile(self, tline):
        """The function identifies the position in the file and returns
        The sections are: general, meta, cross-sections"""
        if re.search(self._strSections['start'], tline):
            self._idxSect = [True, False, False]
            return True
        elif re.search(self._strSections['meta'], tline):
            self._idxSect = [False, True, False]
            return True
        elif re.search(self._strSections['universe'], tline):
            self._idxSect = [False, False, True]
            return True
        return False

    def _checkStoreData(self, flagIn):
        """Checks whether the data should be stored in the dictionary"""
        flag = False
        idx = [i for i, item in enumerate(self._idxSect) if item]
        if idx != []:
            if idx[0] == 0 and self._counter['univ'] == 0:
                flag = True # General data
            elif idx[0] == 1 and self._counter['univ'] == 0:
                flag = True
                if flagIn:
                    self._counter['step'] += 1  # Step data
            elif idx[0] == 2:
                flag = True
                if flagIn:
                    self._counter['univ'] += 1  # Universe data
                    if self._counter['univ'] > len(self._univ):
                        self._counter['univ'] = 0
        else:
            flag = False  # Redundant data
        return flag

    def _stripRedundantChar(self, tlineOld, stripChars):
        """Removes redundant characters (e.g. []=) from the string"""
        tline = tlineOld
        for item in stripChars:
            tline = tline.replace(item, '')
        return tline

    def _str2num(self, string):
        """Converts a string of numbers to an array of numbers """
        numbers = [float(item) for item in string.split() if self.is_float(item)]
        return numbers

    def is_float(self, string):
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

# DEBUG
if __name__ == '__main__':
    filePath = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\Reactor-Simulation-tools\\Serpent Tools\\serpent-tools\\serpentTools\\tests\\ref_res.m"
    res = ResultsReader(filePath)
    res.read()
    a=1

