"""Parser responsible for reading the ``*dep.m`` files"""
import re

import numpy

from drewtils.parsers import KeywordParser

from serpentTools.parsers import _MaterialReader
from serpentTools.objects import DepletedMaterial


class DepletionReader(_MaterialReader):
    """
    Parser responsible for reading and working with depletion files.

    Parameters
    ----------
    filePath: str
        path to the depletion file

    :note:

        Does not support depleted materials with underscores,
        i.e. ``fuel_1`` will not be matched with the current methods
    """

    def __init__(self, filePath):
        _MaterialReader.__init__(self, filePath, 'depletion')
        self._matPatterns = self._makeMaterialRegexs()
        self.matchMatNVar = r'[A-Z]{3}_([0-9a-zA-Z]*)_([A-Z]*_?[A-Z]*)'
        """
        Captures material name and variable from string::
        
            MAT_fuel1_ADENS --> ('fuel1', 'ADENS')
            MAT_fUeL1g_ING_TOX --> ('fUeL1', 'ING_TOX')
    
        """
        self.matchTotNVar = r'[A-Z]{3}_([A-Z]*_?[A-Z]*)'
        """
        Captures variables for total block from string::

            TOT_ADENS --> ('ADENS', )
            ING_TOX --> ('ING_TOX', )

        """

    def _makeMaterialRegexs(self):
        """Return the patterns by which to find the requested materials."""
        patterns = self.settings['materials'] or ['.*']
        # match all materials if nothing given
        return [re.compile(mat) for mat in patterns]

    def read(self):
        """Read through the depletion file and store requested data."""
        keys = self.settings['metadataKeys']
        keys.extend(['MAT', 'TOT'] if self.settings['processTotal']
                    else ['MAT'])
        separators = ['\n', '];']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                if 'MAT' not in chunk[0] and 'TOT' not in chunk[0]:
                    self._addMetadata(chunk)
                elif (('TOT' in chunk[0] and self.settings['processTotal'])
                      or 'MAT' in chunk[0]):
                    self._addMaterial(chunk)

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
                    values = numpy.array([float(item) for item in line.split()])
                self.metadata[metadataKey] = values
                return

    @staticmethod
    def _cleanSingleLine(chunk):
        return chunk[0][chunk[0].index('[') + 1:chunk[0].index(']')]

    def _addMaterial(self, chunk):
        """Add data from a MAT chunk."""
        name, variable = self._getGroupsFromChunk(self.matchMatNVar, chunk)
        if any([re.match(pat, name) for pat in self._matPatterns]):
            self._processChunk(chunk, name, variable)

    def _addTotal(self, chunk):
        """Add data from a TOT chunk"""
        variable = self._getGroupsFromChunk(self.matchTotNVar, chunk)
        self._processChunk(chunk, 'total', variable)

    def _getGroupsFromChunk(self, regex, chunk):
        match = re.match(regex, chunk[0])
        if match:
            return match.groups()
        raise Exception('{} not determine match from the following chunk:\n'
                        '{}'.format(self, ''.join(chunk)))

    def _processChunk(self, chunk, name, variable):
        if variable not in self.settings['materialVariables']:
            pass
        if name not in self.materials:
            self.materials[name] = DepletedMaterial(self, name)
        if len(chunk) == 1:  # single line values, e.g. volume or burnup
            cleaned = self._cleanSingleLine(chunk)
        else:
            cleaned = []
            for line in chunk:
                if '[' in line or ']' in line:
                    continue
                cleaned.append(line[:line.index('%')])
        self.materials[name].addData(variable, cleaned)
