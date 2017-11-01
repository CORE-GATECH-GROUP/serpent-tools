"""Parser responsible for reading the ``*coe.m`` files"""

from serpentTools.objects.branchContainer import BranchContainer
from serpentTools.objects.readers import XSReader
from serpentTools.settings.messages import willChange, debug


class BranchingReader(XSReader):
    """
    Parser responsible for reading and working with automated branching files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'branching')
        self.__fileObj = None
        self.branches = {}
        self._whereAmI = {key: None for key in
                          {'runIndx', 'coefIndx', 'buIndx', 'universe'}}

    @willChange('Once #11 is closed, universes will not be stored as '
                'dictionaries')
    def read(self):
        """Read the branching file and store the coefficients."""
        debug('Preparing to read {}'.format(self.filePath))
        with open(self.filePath) as fObj:
            self.__fileObj = fObj
            while self.__fileObj is not None:
                self._processBranchBlock()
        debug('Done reading branching file')

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
        if branchNames not in self.branches:
            branchState = self._processBranchStateData()
            self.branches[branchNames] = (
                BranchContainer(self, coefIndx, branchNames, branchState))
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
        unvID, numVariables = [int(xx) for xx in self._advance()]
        univ = branch.addUniverse(unvID, burnup, burnupIndex)
        for step in range(numVariables):
            splitList = self._advance(possibleEndOfFile=step == numVariables-1)
            varName = splitList[0]
            varValues = splitList[2:]
            if (not any(self.settings['variables'])
                    or varName in self.settings['variables']):
                univ[varName] = varValues

    def write(self, template=None):
        """
        Write the data from the branching sequence using a specified template.

        Parameters
        ----------
        template: str
            Will attempt to make a template in the following order:

                #. By reading the template from the file pointed to by
                   ``template``, or
                #. Making a template directly from the string

            If neither of these succeeds, the method will fail and raise an
            exception.

        Returns
        -------

        """
        raise NotImplementedError
