"""Parser responsible for reading the ``mdx[i].m`` files"""

from collections import namedtuple

from numpy import array

from serpentTools.engines import KeywordParser
from serpentTools.utils import (
    splitValsUncs, str2vec,
    VEC_REGEX, SCALAR_REGEX, FIRST_WORD_REGEX,
)
from serpentTools.parsers.base import BaseReader

from serpentTools.messages import SerpentToolsException


MicroXSTuple = namedtuple("MicroXSTuple", ["zai", "mt", "metastable"])

try:
    MicroXSTuple.__doc__ = """Convenient indexer for microscopic cross sections

Using attributes is recommended over positions, although both are
identical. The former is more likely to be consistent across future
versions.

Attributes
----------
zai : int
   Isotope ZZAAAI identifier, e.g. ``922350``
mt : int
    Reaction MT, e.g. ``18``
metastable : int
    0 if reaction results in a metastable isotope, 1 otherwise

Example
-------

>>> mx = MicroXSTuple(922380, 18, 0)
>>> mx.zai
922390
>>> mx.mt == mx[1]
True

"""
except AttributeError:
    # can't set namedtuple docs for PY2
    pass


class MicroXSReader(BaseReader):
    """
    Parser responsible for reading and working with micro-xs (mdx) files.

    Parameters
    ----------
    filePath : str
        path to the ``*mdx[n].m`` file

    Attributes
    ------------
    nfy : dict
        Nested dictionary with tuples (parent, energy) as keys.
        Parent is the isotope undergoing fission, e.g. 922350
        and energy is the impending neutron energy causing fission
        in MeV.
        The values are nested dictionaries with the following structure::

            "fissProd": list of fission product ZAI ids, e.g. [541350, 551350, ...]
            "indYield": list of independent yields
            "cumYield": list of cumulative yields

    fluxRatio : dict
        Dictionary with universes id as keys and the
        corresponding group-wise flux values.
        e.g., ``fluxRatio['0'] = [9.91938E+14, 1.81729E+15]``
    fluxUnc : dict
        Dictionary with universes id as keys and the
        corresponding group-wise flux uncertainty values.
        e.g., ``fluxRatio['0'] = [0.00023, 0.00042]``
    xsVal : dict
        Expected value on microscopic cross sections, sorted by
        universe then by isotope, reaction, and metastable flag.
        Nested dictionary with universes as keys, e.g. '0'.
        The values are nested dictionary with :class:`MicroXSTuple`
        as keys (isotope, reaction, flag) and group xs as values.
        e.g., ``(922350, 18, 0)``
    xsUnc : dict
        Uncertainties on microscopic cross sections, sorted by
        universe then by isotope, reaction, and metastable flag.
        Nested dictionary with universes as keys, e.g. '0'.
        The values are nested dictionary with :class:`MicroXSTuple`
        as keys (isotope, reaction, flag) and group xs as values.
        e.g., ``(922350, 18, 0)``

    Raises
    ------
    SerpentToolsException
        No results exist in the file, or no results are collected

    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'microxs')
        self._energyFY = []
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
        currVar = FIRST_WORD_REGEX.search(chunk[0]).group()  # NFY_902270_1
        # Obtain the parent ID: AAZZZ0/1, e.g., 922350
        parentFY = int(str2vec(currVar.split('_')[-2]))
        if 'E' in currVar.split('_')[-1]:  # e.g., NFY_902270_1E
            sclVal = SCALAR_REGEX.search(chunk[0])
            # energy must be stored on the reader
            self._energyFY = float(str2vec(
                chunk[0][sclVal.span()[0] + 1:sclVal.span()[1] - 2]))
            return  # thermal/epi/fast
        for tline in chunk:
            if '[' in tline or ']' in tline:
                continue
            tline = tline[:tline.find('%')]
            if len(tline.split()) == 3:
                val1, val2, val3 = str2vec(tline, out=list)
                fissProd.append(val1)
                indYield.append(val2)
                cumYield.append(val3)
        self.nfy[(parentFY, self._energyFY)] = {'fissProd': array(fissProd),
                                                'indYield': array(indYield),
                                                'cumYield': array(cumYield)}

    def _storeFluxRatio(self, chunk):
        """store flux ratios"""
        chunk0 = chunk[0]
        currVar = FIRST_WORD_REGEX.search(chunk0).group()
        # obtain the universe id
        univ = currVar.split('_')[-1]
        search = VEC_REGEX.search(chunk0)  # group flux values
        vals = str2vec(chunk0[search.span()[0] + 1:search.span()[1] - 2])
        self.fluxRatio[univ], self.fluxUnc[univ] = splitValsUncs(vals)

    def _storeMicroXS(self, chunk):
        """store micro cross-section and uncertainty values"""
        currXS, currUnc = {}, {}
        currVar = FIRST_WORD_REGEX.search(chunk[0]).group()
        # obtain the universe id
        univ = currVar.split('_')[-1]
        for tline in chunk:
            if '[' in tline or ']' in tline:
                continue
            if '%' in tline:
                tline = tline[:tline.index('%')]
            if len(tline.split()) > 3:
                values = str2vec(tline)
                # isotope, reaction type and isomeric state
                reactionKey = MicroXSTuple(*(int(x) for x in values[:3]))
                currXS[reactionKey], currUnc[reactionKey] = splitValsUncs(
                    values[3:])
        self.xsVal[univ] = currXS
        self.xsUnc[univ] = currUnc

    def _precheck(self):
        """do a quick scan to ensure this looks like mdx file."""
        with open(self.filePath) as fid:
            if fid is None:
                raise IOError("Attempting to read on a closed file.\n"
                              "Parser: {}\nFile: {}".format(self,
                                                            self.filePath))
            for tline in fid:
                if 'NFY' in tline or 'XS_' in tline:
                    return
            raise SerpentToolsException("Fission yields and/or XS values were "
                                         "not found in {}".format(self.filePath))

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
        indYield: float
                    Independent fission yield
        cumYield: float
                    Cumulative fission yield

        Raises
        ------
        SerpentToolsException:
            If energy is a negative number
            If parent or fission product are not found
        """
        if energy < 0:
            raise SerpentToolsException("Energy entry {0} must be positive"
                                        " in {1}".format(energy,
                                                         self.filePath))
        if flagEnergy:
            # obtain the different energies for a specific parent
            eneList = [items[1] for items in self.nfy.keys() if
                       parent == items[0]]
            # obtain the closest energy value
            energy = min(eneList,
                         key=lambda x: abs(x - energy)) if eneList else energy
        if (parent, energy) not in self.nfy.keys():
            raise SerpentToolsException("There is no parent {0} with energy "
                                        "{1} in {2}".format(parent, energy,
                                                            self.filePath))
        FP = self.nfy[(parent, energy)]['fissProd']
        IndYield = self.nfy[(parent, energy)]['indYield']
        CumYield = self.nfy[(parent, energy)]['cumYield']
        if daughter in FP:
            return (float(IndYield[FP == daughter]),
                    float(CumYield[FP == daughter]))
        raise SerpentToolsException(
            "There is no fission product {0} for parent {1} at energy {2} in "
            "{3}".format(daughter, parent, energy, self.filePath))

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
        xsVal: numpy.ndarray
                    Group-wise cross-section values
        xsUnc: numpy.ndarray
                    Group-wise uncertainty values

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
        key = (isotope, reaction, isomeric)
        if key in self.xsVal[universe]:
            return (self.xsVal[universe][key],
                    self.xsUnc[universe][key])
        raise SerpentToolsException("There is no isotope {0} with reaction {1}"
                                    " and isomeric flag {2} in {3}"
                                    .format(isotope, reaction, isomeric,
                                            self.filePath))
