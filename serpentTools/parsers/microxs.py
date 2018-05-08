"""Parser responsible for reading the ``*mdx[i].m`` files"""
import re

from numpy import array

from serpentTools.engines import KeywordParser
from serpentTools.objects import splitItems
from serpentTools.objects.readers import MicroXSReader

from serpentTools.messages import (info, debug, SerpentToolsException)


class MdxReader(MicroXSReader):
    """
    Parser responsible for reading and working with micro-xs (mdx) files.

     .. note::

    Fission yields are unique for the system
    Micro-xs are stored for each universe

    Parameters
    ----------
    filePath: str
        path to the mdx file

    Errors
    ------
        If the Serpent version cannot be supported
    """

    def __init__(self, filePath):
        MicroXSReader.__init__(self, filePath, 'microxs')
        self.__fileObj = None
        self._univlist = list()
        self._parentFY = []
        self._energyFY = []
        self._univ = []

    def _read(self):
        """Read through the results file and store requested data."""
        info('Preparing to read {}'.format(self.filePath))
        keys = ['NFY', 'XS', 'FLUX']
        separators = ['\n', '];', '\r\n']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                if 'NFY' in chunk[0] and self.settings['getFY']:
                    self._storeFissionYields(chunk)
                elif 'FLUX' in chunk[0] and self.settings['getFlx']:
                    self._storeFluxRatio(chunk)
                elif 'XS' in chunk[0] and self.settings['getXS']:
                    self._storeMicroXS(chunk)

    def _storeFissionYields(self, chunk):
        """Store fission yields data"""
        fissProd, IndYield, CumYield = [], [], []
        currVar = re.search(r'^\w+', chunk[0])
        self._parentFY = self._str2num(re.split('_', currVar.group())[-1 -1])  # 922350
        if 'E' in re.split('_', currVar.group())[-1]:
            regexpScl = re.search(r'=.+;', chunk[0])  # scalar
            self._energyFY = self._str2num(chunk[0][regexpScl.span()[0] + 1:regexpScl.span()[1] - 2])
            return  # thermal/epi/fast
        else:
            for tline in chunk:
                if '[' in tline or ']' in tline:
                    continue
                if '%' in tline:
                    tline = tline[:tline.index('%')]
                if len(tline.split()) == 3:
                    val1, val2, val3 = self._str2num(tline)
                    fissProd.append(val1), IndYield.append(val2), CumYield.append(val3)
            self.nfy[(self._parentFY, self._energyFY)] = {'fissProd': array(fissProd),
                                                          'IndYield': array(IndYield), 'CumYield': array(CumYield)}

    def _storeFluxRatio(self, chunk):
        """Store flux ratios"""
        currVar = re.search(r'^\w+', chunk[0])
        self._univ = re.split('_', currVar.group())[-1]  # obtain the universe id
        regexpVec = re.search(r'(?<==.)\[.+?\]', chunk[0])  # group flux values
        self.fluxRatio[self._univ], self.fluxUnc[self._univ] = \
            splitItems(self._str2num(chunk[0][regexpVec.span()[0] + 1:regexpVec.span()[1] - 2]))

    def _storeMicroXS(self, chunk):
        """Store micro cross-section and uncertainty values"""
        currXS, currUnc = {}, {}
        currVar = re.search(r'^\w+', chunk[0])  # obtain variable name
        self._univ = re.split('_', currVar.group())[-1]  # obtain the universe id
        self._univlist.append(self._univ)
        for tline in chunk:
            if '[' in tline or ']' in tline:
                continue
            if '%' in tline:
                tline = tline[:tline.index('%')]
            if len(tline.split()) > 3:
                values = self._str2num(tline)
                # isotope, reaction type and isomeric state
                reactionData = (values[0], values[1], values[2])
                currXS[reactionData], currUnc[reactionData] = splitItems(values[3:])
        self.microXS[self._univ] = currXS
        self.uncXS[self._univ] = currUnc

    @staticmethod
    def _str2num(tline):
        """Converts a string to a list of numbers."""
        vals = [float(x) for x in tline.split()]
        if len(tline.split()) < 2:
            vals = vals[0]
        return vals

    def _precheck(self):
        """do a quick scan to ensure this looks like a mdx file."""
        with open(self.filePath) as fid:
            if fid is None:
                raise IOError("Attempting to read on a closed file.\n"
                              "Parser: {}\nFile: {}".format(self, self.filePath))
            for tline in fid:
                if 'NFY' in tline:
                    return
            raise SerpentToolsException("Fission yields values were not "
                                        "found in {}".format(self.filePath))

    def _postcheck(self):
        """ensure the parser grabbed expected results."""
        if not self._univlist:
            raise SerpentToolsException("No universes data was found "
                                        "from {}".format(self.filePath))
        if not self.microXS and not self.microXS \
                and not self.fluxRatio and not self.nfy:
            raise SerpentToolsException("No micro-XS data exists in {}"
                                        .format(self.filePath))
        if not self.microXS and len(self._univlist) != len(self.microXS):
            raise SerpentToolsException("Number of universes {0} in microXS "
                                        "variable is not equal to the number "
                                        "of total universes {1} in {2}"
                                            .format(len(self.microXS),
                                                    len(self._univlist),
                                                    self.filePath))
        debug('  found {} materials'.format(len(self._univlist)))

    def getFY(self, parent, energy, daughter):
        """Grep a specific fission yield."""
        IndYield, CumYield = 0, 0
        if (parent, energy) not in self.nfy.keys():
            info("There is no parent {0} with energy {1} in {2}"
                 .format(parent, energy, self.filePath))
            return
        FP = self.nfy[(parent, energy)]['fissProd']
        IndYield = self.nfy[(parent, energy)]['IndYield']
        CumYield = self.nfy[(parent, energy)]['CumYield']
        if daughter:
            IndYield = IndYield[FP == daughter]
            CumYield = CumYield[FP == daughter]
        return IndYield, CumYield





