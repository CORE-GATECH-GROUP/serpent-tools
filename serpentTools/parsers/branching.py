"""Parser responsible for reading the ``*coe.m`` files"""

from numpy import array

from serpentTools.utils import splitValsUncs
from serpentTools.objects import BranchContainer, UnivTuple, HomogUniv
from serpentTools.parsers.base import XSReader
from serpentTools.messages import debug, error


class BranchingReader(XSReader):
    """
    Parser responsible for reading and working with automated branching files.

    Parameters
    ----------
    filePath: str
        path to the depletion file

    Attributes
    ----------
    branches: dict
        Dictionary of branch names and their corresponding
        :class:`~serpentTools.objects.BranchContainer` objects
    """

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'branching')
        self.__fileObj = None
        self.branches = {}
        self._whereAmI = {key: None for key in
                          {'runIndx', 'coefIndx', 'buIndx', 'universe'}}
        self._totalBranches = None
        self._hasUncs = None

    @property
    def hasUncs(self):
        """boolean if uncertainties are present in the file"""
        return self._hasUncs

    def _read(self):
        """Read the branching file and store the coefficients."""
        with open(self.filePath) as fObj:
            self.__fileObj = fObj
            while self.__fileObj is not None:
                self._processBranchBlock()

    def _advance(self, possibleEndOfFile=False):
        if self.__fileObj is None:
            raise IOError("Attempting to read on file that has been closed.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        line = self.__fileObj.readline()
        if line == '':
            if possibleEndOfFile:
                self.__fileObj = None
                return None
            raise EOFError('Unexpected end of file {}'.format(self.filePath))
        return line.split()

    def _processBranchBlock(self):
        fromHeader = self._processHeader()
        if fromHeader is None:
            return
        thisBranch, totUniv = fromHeader
        burnup, burnupIndex = self._advance()[:-1]
        self._whereAmI['buIndx'] = int(burnupIndex)
        for univNum in range(totUniv):
            self._whereAmI['universe'] = univNum
            debug(
                'Reading run {runIndx} of {coefIndx} - universe {universe} at '
                'burnup step {buIndx}'.format(**self._whereAmI))
            self._processBranchUniverses(thisBranch, float(burnup),
                                         self._whereAmI['buIndx'])

    def _processHeader(self):
        """Read over all data up to universe loop."""
        header = self._advance(possibleEndOfFile=True)
        if header is None:
            return
        indx, runTot, coefIndx, totCoef, totUniv = header
        self._whereAmI['runIndx'] = int(indx)
        self._whereAmI['coefIndx'] = int(coefIndx)
        branchNames = tuple(self._advance()[1:])
        if len(branchNames) == 1:
            branchNames = branchNames[0]
        if branchNames not in self.branches:
            branchState = self._processBranchStateData()
            self.branches[branchNames] = (
                BranchContainer(self.filePath, coefIndx, branchNames,
                                branchState))
        else:
            self._advance()
        return self.branches[branchNames], int(totUniv)

    def _processBranchStateData(self):
        keyValueList = self._advance()[1:]
        stateData = {}
        mappings = {'intVariables': int, 'floatVariables': float}

        for keyIndex in range(0, len(keyValueList), 2):
            key, value = keyValueList[keyIndex: keyIndex + 2]
            stateData[key] = value
            for mapKey, mapFunc in mappings.items():
                if key in self.settings[mapKey]:
                    stateData[key] = mapFunc(value)
                    break
        return stateData

    def _processBranchUniverses(self, branch, burnup, burnupIndex):
        """Add universe data to this branch at this burnup."""
        unvID, numVariables = self._advance()
        numVariables = int(numVariables)
        if burnup < 0:
            key = UnivTuple(unvID, None, burnupIndex - 1, -burnup)
        else:
            key = UnivTuple(unvID, burnup, burnupIndex - 1, None)
        univ = HomogUniv(*key)
        branch[key] = univ
        for step in range(numVariables):
            splitList = self._advance(
                possibleEndOfFile=(step == numVariables - 1))
            varName = splitList[0]
            varValues = [float(xx) for xx in splitList[2:]]
            if not varValues:
                continue
            if self._checkAddVariable(varName):
                if self._hasUncs:
                    vals, uncs = splitValsUncs(varValues)
                    univ.addData(varName, array(vals), uncertainty=False)
                    univ.addData(varName, array(uncs), uncertainty=True)
                else:
                    univ.addData(varName, array(varValues), uncertainty=False)

    def iterBranches(self):
        """Iterate over branches yielding paired branch IDs and containers"""
        for bID, b in self.branches.items():
            yield bID, b

    def _precheck(self):
        """Total number of branches and check for uncertainties"""
        with open(self.filePath) as fObj:
            try:
                self._totalBranches = int(fObj.readline().split()[1])
            except Exception as ee:
                error("COE output at {} likely malformatted or misnamed\n{}"
                      .format(self.filePath, str(ee)))
            # skip first few lines with integer until first named value
            for _x in range(4):
                fObj.readline()
            lsplt = fObj.readline().split()
            nvals = int(lsplt[1])
            self._hasUncs = not nvals == len(lsplt) - 2

    def _postcheck(self):
        """Make sure Serpent finished printing output."""

        if self._totalBranches != self._whereAmI['runIndx']:
            error("Serpent appears to have stopped printing coefficient\n"
                  "mode output early for file {}".format(self.filePath))
