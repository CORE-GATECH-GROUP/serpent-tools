"""Parser responsible for reading the ``*res.m`` files"""


import re

from drewtils.parsers import KeywordParser

from serpentTools.objects.readers import XSReader

from serpentTools.settings import messages


class ResultsReader(XSReader):
    """
    Parser responsible for reading and working with result files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """
    def __init__(self, filePath):
        XSReader.__init__(self, filePath, ['branching', 'xs'])

    def read(self):
        """Read through the depletion file and store requested data."""
        messages.info('Preparing to read {}'.format(self.filePath))
        keys = ['MAT', 'TOT'] if self.settings['processTotal'] else ['MAT']
        keys.extend(self.settings['metadataKeys'])
        separators = ['\n', '];']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                if 'MAT' not in chunk[0] and 'TOT' not in chunk[0]:
                    self._addMetadata(chunk)
                elif (('TOT' in chunk[0] and self.settings['processTotal'])
                      or 'MAT' in chunk[0]):
                    self._addMaterial(chunk)
        messages.info('Done reading depletion file')
        messages.debug('  found {} materials'.format(len(self.materials)))