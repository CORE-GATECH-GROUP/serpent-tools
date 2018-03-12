"""Parser responsible for reading the ``*dep.m`` files"""
from serpentTools.engines import KeywordParser
from serpentTools.messages import warning, info, debug, error

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

    def _read(self):
        """Read through the depletion file and store requested data."""
        info('Preparing to read {}'.format(self.filePath))
        keys = ['MAT', 'TOT'] if self.settings['processTotal'] else ['MAT']
        keys.extend(self.settings['metadataKeys'])
        separators = ['\n', '];', '\r\n']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                if 'MAT' in chunk[0]:
                    self._addMaterial(chunk)
                elif 'TOT' in chunk[0]:
                    self._addTotal(chunk)
                else:
                    self._addMetadata(chunk)
        if 'days' in self.metadata:
            for mKey in self.materials:
                self.materials[mKey].days = self.metadata['days']
        info('Done reading depletion file')
        debug('  found {} materials'.format(len(self.materials)))

    def _addMetadata(self, chunk):
        options = {'ZAI': 'zai', 'NAMES': 'names', 'DAYS': 'days',
                   'BU': 'burnup'}
        for varName, metadataKey in options.items():
            if varName in chunk[0]:
                if varName in ['ZAI', 'NAMES']:
                    values = [line.strip() for line in chunk[1:]]
                    if varName == 'NAMES':
                        values = [item.split()[0][1:] for item in values]
                else:
                    line = self._cleanSingleLine(chunk)
                    values = numpy.array([float(item)
                                          for item in line.split()])
                self.metadata[metadataKey] = values
                return

    @staticmethod
    def _cleanSingleLine(chunk):
        return chunk[0][chunk[0].index('[') + 1:chunk[0].index(']')]

    def _precheck(self):
        """do a quick scan to ensure this looks like a xsplot file."""
        if '_xs' not in self.filePath:
            warning("This file doesn't look like the file format serpent
                     gives for xsplot stuff.")

        with open(self.filePath) as fh:
            # first chunk should be energy bins
            line = next(fh)
            if line != 'E = [\n':
                error("It looks like {} doesn't start with an energy bin "
                      "structure. Are you sure it's an xsplot file?".format(
                      self.filePath))

    def _postcheck(self):
        """ensure the parser grabbed expected stuff."""
        pass
