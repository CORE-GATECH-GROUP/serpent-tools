"""Parser responsible for reading the ``*_xsplot.m`` files"""
import warnings
import re

from numpy import array, float64

from serpentTools.messages import error, warning
from serpentTools.engines import KeywordParser
from serpentTools.parsers.base import BaseReader
from serpentTools.objects.xsdata import XSData


def _cleanChunk(string):
    """rstrip, but also removes = ["""
    newstring = string.rstrip()
    if '=' in newstring:
        i = newstring.index('=')
        return newstring[:i - 1]
    return newstring


class XSPlotReader(BaseReader):
    """
    Parser responsible for reading and working with xsplot output files.
    These files can be generated using:

    http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual#set_xsplot

    Parameters
    ----------
    filePath: str
        path to the xsplot result file

    Attributes
    ----------
    xsections: dict
        Contains :class:`~serpentTools.objects.XSData` objects with keys
        given by their names. There should be one XSData instance for each
        isotope and material present in the problem.
    energies : numpy.ndarray or None
        Array of energy grids, shared across all XSData instances
    majorant : numpy.ndarray or None
        L-inf norm among all macroscopic cross sections used in the problem.
    metadata: dict
        Alias for accessing :attr:`energies` and :attr:`majorant`.
        Attribute-based access is prefered, as this property will
        likely be removed in the future

    """
    _misc = {"pspec", }

    def __init__(self, filePath):
        super().__init__(filePath, 'xsplot')
        self.xsections = {}
        self.energies = None
        self.majorant = None

    def __len__(self):
        """Number of xsdata objects stored"""
        return len(self.xsections)

    def __iter__(self):
        """Iterate over all keys in :attr:`xsections`"""
        return iter(self.xsections)

    def __contains__(self, key):
        """Return true or false if ``key`` in :attr:`xsections`"""
        return key in self.xsections

    def __getitem__(self, key):
        """Return item corresponding to ``key`` in :attr:`xsections`"""
        return self.xsections[key]

    def keys(self):
        """Key-view into :attr:`xsections`"""
        return self.xsections.keys()

    def values(self):
        """Values-view into :attr:`xsections`"""
        return self.xsections.values()

    def items(self):
        """Item-view ``(k, v)`` into :attr:`xsections`"""
        return self.xsections.items()

    def get(self, key, default=None):
        """Return the value of ``key`` from :attr:`xsections` or ``default``

        Parameters
        ----------
        key : str
            Name of isotope or material that may or may not exist
            in :attr:`xsections`
        default : object
            Item to return if ``key`` not found

        Returns
        -------
        object
            :class:`~serpentTools.objects.XSData` that corresponds
            to ``key`` if ``key`` is found. Otherwise return ``default``

        """
        return self.xsections.get(key, default)

    @property
    def metadata(self):
        out = {}
        if self.energies is not None:
            out["egrid"] = self.energies
        if self.majorant is not None:
            out["majorant_xs"] = self.majorant
        return out

    def _read(self):
        """Read through the depletion file and store requested data."""
        keys = ['E', r'i\d{4,5}', r'm\w']
        separators = ['\n', '];', '\r\n']

        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():

                lead = chunk[0].strip()
                data = chunk[1:]
                if lead.startswith("E = ["):
                    # The energy grid
                    self.energies = array(data, dtype=float64)

                elif lead.endswith('majorant_xs = ['):
                    # L-inf norm on all XS on all materials
                    self.majorant = array(data, dtype=float64)

                elif lead.endswith('_mt = ['):
                    xsname = lead[:lead.index("_mt")]
                    isiso = lead[0] == 'i'
                    self.xsections[xsname] = XSData(xsname, self.metadata,
                                                    isIso=isiso)
                    self.xsections[xsname].setMTs(chunk)

                elif lead.endswith('_xs = ['):
                    xsname = lead[:lead.index("_xs")]
                    self.xsections[xsname].setData(chunk)

                elif lead.endswith('_nu = ['):
                    xsname = lead[:lead.index("_nu")]
                    self.xsections[xsname].setNuData(chunk)

                elif lead.endswith("bra_f = ["):
                    xsname = lead[:lead.index("_f")]
                    self.xsections[xsname].setData(chunk)

                else:
                    self._processMisc(lead, data)

    def _processMisc(self, lead, data):
        variable = lead.split()[0]
        for key in self._misc:
            start = variable.find(key)
            if start == -1:
                continue
            xsname = re.sub("_$", "", variable[:start])
            cleaned = list(map(str.split, data))
            self.xsections[xsname].misc[key] = array(cleaned, dtype=float)
            return

        warnings.warn(
            "Unidentifiable entry in {}: {}".format(self.filePath, lead)
        )

    def _precheck(self):
        """do a quick scan to ensure this looks like a xsplot file."""
        if '_xs' not in self.filePath:
            warning("This file doesn't look like the file format serpent"
                    "gives for xsplot stuff.")

        with open(self.filePath) as fh:
            # first chunk should be energy bins
            line = next(fh)
            if line != 'E = [\n':
                error("It looks like {} doesn't start with an energy bin "
                      "structure. Are you sure it's an xsplot file?"
                      .format(self.filePath))

    def _postcheck(self):
        """ensure the parser grabbed expected stuff."""
        try:
            for xs in self.xsections.values():
                assert xs.hasExpectedData()
        except AssertionError:
            error("Seems either the file was cut off, or data incomplete."
                  "The incomplete XS is {}".format(xs.name))

        # check energy grid found
        try:
            assert 'egrid' in self.metadata.keys()
        except AssertionError as e:
            e.args += 'No energy grid found in xsplot parser.'
