"""Parser responsible for reading the ``*_xsplot.m`` files"""
from numpy import array, float64

from serpentTools.engines import KeywordParser
from serpentTools.messages import warning, info, debug, error
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

    http://serpent.vtt.fi/mediawiki/index.php/It_syntax_manual#set_xsplot

    Parameters
    ----------
    filePath: str
        path to the xsplot result file

    Attributes
    ----------
    xsections: NamedDict
        Contains XSData objects with keys given by their names. There should be
        one XSData instance for each isotope and material present in the
        problem.
    metadata: dict
        Contains data pertinent to all XSData instances collected.
        One particularly important entry is the 'egrid', which is a numpy array
        of values that define the bin structure XS were recorded in by Serpent.
        In addition, Serpent defines the 'majorant_xs', which is the L-inf norm
        among all macroscopic cross sections used in the problem. This gets
        used in the delta tracking routines usually.
    settings: dict
        names and values of the settings used to control operations
        of this reader
    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'xsplot')
        self.xsections = {}
        self.metadata = {}

    def _read(self):
        """Read through the depletion file and store requested data."""
        info('Preparing to read {}'.format(self.filePath))
        keys = ['E', r'i\d{4,5}', r'm\w']
        separators = ['\n', '];', '\r\n']

        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():

                if chunk[0][:5] == 'E = [':
                    # The energy grid
                    self.metadata['egrid'] = array(chunk[1:], dtype=float64)

                elif chunk[0][:15] == 'majorant_xs = [':
                    # L-inf norm on all XS on all materials
                    self.metadata['majorant_xs'] = array(chunk[1:],
                                                         dtype=float64)

                elif chunk[0][-7:] == 'mt = [\n':
                    debug('found mt specification')
                    xsname = chunk[0][:-8]
                    isiso = True if chunk[0][0] == 'i' else False
                    self.xsections[xsname] = XSData(xsname, self.metadata,
                                                    isIso=isiso)
                    self.xsections[xsname].setMTs(chunk)

                elif chunk[0][-7:] == 'xs = [\n':
                    debug('found xs specification')
                    xsname = chunk[0][:-8]
                    self.xsections[xsname].setData(chunk)

                elif chunk[0][-7:] == 'nu = [\n':
                    debug('found nu specification')
                    xsname = chunk[0][:-8]
                    self.xsections[xsname].setNuData(chunk)

                elif 'bra_f' in chunk[0]:
                    warning("There is this weird 'bra_f' XS. these seem to be"
                            " constant. recording to metadata instead.")
                    self.metadata[xsname].setData(chunk)

                else:
                    print(chunk)
                    error('Unidentifiable entry {}'.format(chunk[0]))

        info('Done reading xsplot file')
        debug('  found {} xs listings'.format(len(self.xsections)))

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
