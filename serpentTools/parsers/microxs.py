"""Parser responsible for reading the ``*mdx[i].m`` files"""
import re

from numpy import array

from serpentTools.engines import KeywordParser
from serpentTools.objects import splitItems
from serpentTools.objects.readers import BaseReader

from serpentTools.messages import SerpentToolsException


class MicroXSReader(BaseReader):
    """
    Parser responsible for reading and working with micro-xs (mdx) files.

    Attributes
    ------------
    nfy: dict
        Nested dictionary with tuples (parent, energy) as keys.
        Parent is the isotope undergoing fission, e.g. 922350
        and energy is the impending neutron energy causing fission
        in MeV.
        The values are nested dictionaries with the following structure:
            'fissProd': array
                contains the fission product ids
                e.g., [541350, 551350, ... ]
            'indYield': array
                contains the independent yields
                e.g., [0.053, 0.015, ... ]
            'cumYield': array
                contains the cumulative yields
                e.g., [0.060, 0.016, ... ]
    fluxRatio: dict
        Dictionary with universes id as keys and the
        corresponding group-wise flux values.
        e.g., fluxRatio['0']= [9.91938E+14, 1.81729E+15, ...]
    fluxUnc: dict
        Dictionary with universes id as keys and the
        corresponding group-wise flux uncertainty values.
        e.g., fluxRatio['0']= [0.00023, 0.00042, ...]
    xsVal: dict
        Nested dictionary with universes as as keys, e.g. '0'.
        The values are nested dictionary with tuples as keys
        (isotope, reaction, flag) and group xs as values.
        e.g., (922350, 18, 0)
    xsUnc: dict
        Nested dictionary with universes as as keys, e.g. '0'.
        The values are nested dictionary with tuples as keys
        (isotope, reaction, flag) and group xs uncertainties.

    Parameters
    ----------
    filePath: str
        path to the *mdx[n].m file

    Raises
    ------
    SerpentToolsException:
                            No results exist in the file
                            No results are collected
    IOError: file is unexpectedly closes while reading
    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'microxs')
        self._energyFY = []
        self._strtok = re.compile(r'^\w+')  # first word in the line
        self._regexpScl = re.compile(r'=.+;')  # scalar
        self._regexpVec = re.compile(r'(?<==.)\[.+?\]')  # vector
        self.nfy = {}
        self.xsVal, self.xsUnc = {}, {}
        self.fluxRatio, self.fluxUnc = {}, {}

    def _read(self):
        """read through the results file and store requested data."""
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
        """store fission yields data"""
        fissProd, indYield, cumYield = [], [], []
        currVar = self._strtok.search(chunk[0])
        # Obtain the parent ID: AAZZZ0/1, e.g., 922350
        parentFY = self._str2num(re.split('_', currVar.group())[-1 -1])
        if 'E' in re.split('_', currVar.group())[-1]:  # e.g., NFY_902270_1E
            sclVal = self._regexpScl.search(chunk[0])
            # energy must be stored on the reader
            self._energyFY = self._str2num(chunk[0][sclVal.span()[0] +
                                                    1:sclVal.span()[1] - 2])
            return  # thermal/epi/fast
        else:
            for tline in chunk:
                if '[' in tline or ']' in tline:
                    continue
                if '%' in tline:
                    tline = tline[:tline.index('%')]
                if len(tline.split()) == 3:
                    val1, val2, val3 = self._str2num(tline)
                    fissProd.append(val1), indYield.append(val2), cumYield.append(val3)
            self.nfy[(parentFY, self._energyFY)] = {'fissProd': array(fissProd),
                                                    'indYield': array(indYield),
                                                    'cumYield': array(cumYield)}

    def _storeFluxRatio(self, chunk):
        """store flux ratios"""
        currVar = self._strtok.search(chunk[0])
        # obtain the universe id
        univ = re.split('_', currVar.group())[-1]
        vals = self._regexpVec.search(chunk[0])  # group flux values
        self.fluxRatio[univ], self.fluxUnc[univ] = \
            splitItems(self._str2num(chunk[0][vals.span()[0] +
                                              1:vals.span()[1] - 2]))

    def _storeMicroXS(self, chunk):
        """store micro cross-section and uncertainty values"""
        currXS, currUnc = {}, {}
        currVar = self._strtok.search(chunk[0])
        # obtain the universe id
        univ = re.split('_', currVar.group())[-1]
        for tline in chunk:
            if '[' in tline or ']' in tline:
                continue
            if '%' in tline:
                tline = tline[:tline.index('%')]
            if len(tline.split()) > 3:
                values = self._str2num(tline)
                # isotope, reaction type and isomeric state
                reactionData = (values[0], values[1], values[2])
                currXS[reactionData], currUnc[reactionData] = \
                    splitItems(values[3:])
        self.xsVal[univ] = currXS
        self.xsUnc[univ] = currUnc

    @staticmethod
    def _str2num(tline):
        """converts a string to a list of numbers."""
        vals = [float(x) for x in tline.split()]
        if len(tline.split()) < 2:
            vals = vals[0]
        return vals

    def _precheck(self):
        """do a quick scan to ensure this looks like mdx file."""
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
        if not self.xsVal and not self.fluxRatio and not self.nfy:
            raise SerpentToolsException("xs, fluxes and fission yields are all"
                                        " empty in {}".format(self.filePath))

    def getFY(self, parent, energy, daughter, flagEnergy=True):
        """
        Return a specific fission yield given the parent ID, neutron energy
         and daughter ID

        If the energy does not exist in the results, the fission yield
        corresponding to the closest energy is returned

        Parameters
        ----------
        parent: int or float
            ID of the parent undergoing fission
        energy: float
            neutron energy in MeV
        daughter: int or float
            ID of the fission product
        flagEnergy: boolean
            If set to true, the function will return the fission yield
            that matches to the closest energy given by the user

        Returns
        -------
        Independent and cumulative fission yields: float or empty
            IndYield and CumYield
            if fission product exists, float values are returned,
            otherwise empty values are returned

        Raises
        ------
        SerpentToolsException:
            If energy is a negative number
            If parent or fission product are not found
        """
        IndYield, CumYield = 0, 0
        if energy < 0:
            raise SerpentToolsException("Energy entry {0} must be positive"
                                        " in {1}".format(energy, self.filePath))
        eneList = []
        if flagEnergy:
            # obtain the different energies for a specific parent
            eneList = [items[1] for items in self.nfy.keys() if parent == items[0]]
            # obtain the closest energy value
            energy = min(eneList,
                         key=lambda x: abs(x - energy)) if eneList else energy
        if (parent, energy) not in self.nfy.keys():
            raise SerpentToolsException("There is no parent {0} with energy "
                                        "{1} in {2}".format(parent,energy,
                                                            self.filePath))

        FP = self.nfy[(parent, energy)]['fissProd']
        IndYield = self.nfy[(parent, energy)]['indYield']
        CumYield = self.nfy[(parent, energy)]['cumYield']
        if daughter:
            IndYield = IndYield[FP == daughter]
            CumYield = CumYield[FP == daughter]
        return IndYield, CumYield


    def getXS(self, universe, isotope, reaction, isomeric=0):
        """
        Return the group-wise micro cross-sections for a
        specific isotope, and reaction

        Parameters
        ----------
        universe: string
            universe ID, e.g., `0`
        isotope: int or float
            ID of the isotope (ZZAAA0/1)
        reaction: int
            MT reaction, e.g., 102 --> (n,gamma)
        Special flag: int or float
            Isomeric state or fission yield distribution number
            Default is zero

        Returns
        -------
        Group-wise micro cross-sections: list
            if the isotope, reaction or isomeric state
            do not exist, an empty list is returned

        Raises
        ------
        SerpentToolsException:
            If the universe does not exist
            If the isotope's format is incorrect (not ZZAAA0/1)
        """
        if universe not in self.xsVal.keys():
            raise SerpentToolsException("Universe {0} does not exist in {1}"
                                        .format(universe, self.filePath))
        if isotope < 10010 or isotope > 1000000:
            raise SerpentToolsException("Isotope {0} is not properly formatted"
                                        " ZZAAA0/1 in {1}"
                                        .format(isotope, self.filePath))
        if (isotope, reaction, isomeric) in self.xsVal[universe]:
            return self.xsVal[universe][(isotope, reaction, isomeric)], \
                   self.xsUnc[universe][(isotope, reaction, isomeric)]
        else:
            return [], []




