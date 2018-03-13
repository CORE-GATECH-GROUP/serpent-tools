"""Parser responsible for reading the ``*dep.m`` files"""
import numpy as np
from serpentTools.engines import KeywordParser
from serpentTools.messages import warning, info, debug, error
from serpentTools.objects.readers import BaseReader
from serpentTools.objects.xsdata import XSData

def _cleanChunk(string):
    """rstrip, but also removes = ["""
    newstring= string.rstrip()
    if '=' in newstring:
        i = newstring.index('=')
        return newstring[:i-1]
    else:
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
    {attrs:s}
    settings: dict
        names and values of the settings used to control operations
        of this reader
    """
    docAttrs="""datalibs: dict
        Dictionary with material names as keys and the corresponding
        :py:class:`~serpentTools.objects.DepletedMaterial` class
        for that material as values
    metadata: dict
        misc stuff 
        """
    __doc__ = __doc__.format(attrs=docAttrs)

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'xsplot')
        self.xsections = {}
        self.metadata = {}

    def _read(self):
        """Read through the depletion file and store requested data."""
        info('Preparing to read {}'.format(self.filePath))
        keys = ['E', 'i[0-9]{4,5}', 'm[a-zA-Z]']
        separators = ['\n', '];', '\r\n']

        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():

                if chunk[0][:5] == 'E = [':
                    # The energy grid
                    self.metadata['egrid']= np.array(chunk[1:], dtype=np.float64)

                elif chunk[0][:15] == 'majorant_xs = [':
                    # L-inf norm on all XS on all materials
                    self.metadata['majorant_xs'] = np.array(chunk[1:],
                                                             dtype=np.float64)

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
                      "structure. Are you sure it's an xsplot file?".format(
                      self.filePath))

    def _postcheck(self):
        """ensure the parser grabbed expected stuff."""
        try:
            for xs in self.xsections.values():
                assert xs.hasExpectedData()
        except AssertionError:
            error("Seems either the file was cut off, or data incomplete."
                  "The incomplete XS is {}".format(xs.name))

        # check energy grid found
        assert 'egrid' in self.metadata.keys()
