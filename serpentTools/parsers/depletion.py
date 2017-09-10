"""Parser responsible for reading the ``*dep.m`` files"""

from serpentTools.objects import KeywordParser
from serpentTools.parsers import _MaterialReader


class DepletionReader(_MaterialReader):
    """
    Parser responsible for reading and working with depletion files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """
    pass

    def __init__(self, filePath):
        _MaterialReader.__init__(self, filePath)

    def read(self):
        """Read through the depletion file and store requested data."""
        keys = ['ZAI', 'NAMES', 'DAYS', 'BU']
        separators = ['\n', '];']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                if 'MAT' not in chunk:
                    self._addMetadata(chunk)
                # TODO Process material data

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
                    chunk = chunk[0]  # burnup and days stored as single line
                    line = chunk[chunk.index('[') + 1:chunk.index(']')]
                    values = [float(item) for item in line.split()]
                self.metadata[metadataKey] = values
                return
