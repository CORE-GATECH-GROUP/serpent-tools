"""Parser responsible for reading the ``*coe.m`` files"""

from serpentTools.objects.readers import XSReader
from serpentTools.objects.branchContainer import BranchContainer


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
        self.__fileObj__ = None
        self.branches = {}
        self._loopLevel = [True, True, True]
        # looping over branches, universes, and coefficients

    def read(self):
        """Read the branching file and store the coefficients."""
        with open(self.filePath) as fObj:
            self.__fileObj__ = fObj
            while self._loopLevel[0]:
                self._processBranchBlock(fObj)

    def _advance(self):
        if self.__fileObj__ is None:
            raise IOError("Attempting to read on file that has been closed.\n"
                          "Parser: {}\nFile: {}".format(self, self.filePath))
        line = self.__fileObj__.readline()
        if line == '':
            self.__fileObj__ = None
            return None
        return line.split()

    def _processBranchBlock(self, fObj):
        thisBranch, totUniv = self._processHeader()
        burnup, burnupIndex = self._advance()[:-1]
        for univNum in range(totUniv):
            self._processBranchUniverses(thisBranch, burnup, burnupIndex)

    def _processHeader(self):
        """Read over all data up to universe loop."""
        indx, runTot, branchId, totBranch, totUniv = self._advance()
        self._loopLevel[0] = indx == runTot
        if branchId not in self.branches:
            branchNames = self._advance()[1:]
            branchState = self._processBranchStateData()
            self.branches[branchId] = (
                BranchContainer(self, branchId, branchNames, branchState))
        else:
            self._advance()
            self._advance()
        return self.branches[branchId], totUniv

    def _processBranchStateData(self):
        keyValueList = self._advance()[1:]
        stateData = {}
        mappings = {'intVariables': int, 'floatVariables': float}
        for keyIndex in range(0, len(keyValueList), 2):
            key, value = keyValueList[keyIndex: keyIndex + 1]
            for mapKey, mapFunc in mappings.items():
                if key in self.settings[mapKey]:
                    stateData[key] = mapFunc(value)
                    break
        return stateData

    def _processBranchUniverses(self, branch, burnup, burnupIndex):
        """Add universe data to this branch at this burnup."""
        #TODO This

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
