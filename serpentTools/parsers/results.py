"""Parser responsible for reading the ``*res.m`` files"""
import re


from numpy import array, empty


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
        info('Preparing to read {}'.format(self.filePath))
        with open(self.filePath, 'r') as fObject:
            for tline in fObject:
                self._processResultsChunk(tline)
        info('Done reading results file')



# DEBUG
if __name__ == '__main__':
    filePath = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\Reactor-Simulation-tools\\Serpent Tools\\serpent-tools\\serpentTools\\tests\\pwr_res.m"
    res = ResultsReader(filePath)
    res.read()


