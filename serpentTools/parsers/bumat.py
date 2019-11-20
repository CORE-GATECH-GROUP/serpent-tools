"""Parser responsible for reading the ``*bumat<n>.m`` files"""

from re import compile

from serpentTools.messages import warning, willChange
from serpentTools.parsers.base import MaterialReader


__all__ = [
    'BumatReader',
]


# match burnup values in MWd/kgU and days
BU_REGEX = compile(r'\s+Material compositions\s+\(([0-9E\.\+-]+) '
                   r'MWd/kgU\s+/\s+([0-9E\.\+-]+)')
# match isotope identifier, 1001.09c, and density
NUC_REGEX = compile(r'([0-9]{4,5}\.[0-9]{2}[cs])\s+([0-9Ee\+-\.]+)')


class BumatReader(MaterialReader):
    """
    Parser responsible for reading and working with burned material files.

    ..note::

        This is experimental and will be subject to change depending
        upon the implementation of GH Issue #12

    Parameters
    ----------
    filePath: str
        path to the depletion file

    Attributes
    ----------
    materials: dict
        Dictionary of materials with keys as names and values being
        a dictionary of parameters. **The storage of materials is
        subject to change**
    burnup: float
        Burnup [MWd/kgU] for this file
    days: float
        Burnup [days] for this file
    """

    HAS_BEEN_WARNED = False

    def __init__(self, filePath):
        if not BumatReader.HAS_BEEN_WARNED:
            BumatReader.warn()
        MaterialReader.__init__(self, filePath, 'bumat')
        self.burnup = None
        self.days = None

    @classmethod
    @willChange(
        "Storage of material in materials dictionary will utilize "
        "custom container objects in the future.")
    def warn(cls):
        cls.HAS_BEEN_WARNED = True

    def __getitem__(self, key):
        return self.materials[key]

    def _precheck(self):
        pass

    def _postcheck(self):
        if not self.materials:
            warning("No materials found in {}".format(self.filePath))
            return
        for attr in ['burnup', 'days']:
            if getattr(self, attr) is None:
                warning("Value of {} is None".format(attr))
        noNucs = set()
        for mname, subDict in self.materials.items():
            if not subDict['nuclides']:
                noNucs.add(mname)
        if noNucs:
            warning("The following materials did not have any nuclides:\n{}"
                    .format(noNucs))

    def _read(self):

        self.materials = {}
        buMatch = None
        curMat = None
        with open(self.filePath) as stream:
            for line in stream:
                line = line.strip()
                if not line:
                    continue
                # check burnup
                if buMatch is None:
                    buMatch = BU_REGEX.search(line)
                    if buMatch is not None:
                        self.burnup, self.days = [
                            float(xx) for xx in buMatch.groups()]
                        continue
                elif line[0] == '%':
                    continue
                entries = line.split()
                if entries[0] == 'mat':
                    curMat = entries[1]
                    density = float(entries[2])
                    if len(entries) > 3:
                        extras = ' '.join(entries[3:])
                    else:
                        extras = ''
                    self.materials[curMat] = {
                        'density': density,
                        'extras': extras,
                        'nuclides': {},
                    }
                    continue
                isoMatch = NUC_REGEX.search(line)
                if not isoMatch:
                    continue
                isotope, density = isoMatch.groups()[:2]
                self.materials[curMat]['nuclides'][isotope] = float(density)
