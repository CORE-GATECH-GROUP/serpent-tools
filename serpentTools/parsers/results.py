"""Parser responsible for reading the ``*res.m`` files"""
import re


from drewtils.parsers import KeywordParser

from serpentTools.objects.readers import BaseReader
from serpentTools.objects.readers import MaterialReader


class ResultsReader(BaseReader):
    """
    Parser responsible for reading and working with result files.

    Parameters
    ----------
    filePath: str
        path to the depletion file

    Attributes
    ----------
    materials: dict
        Dictionary with material names as keys and the corresponding
        :py:class:`~serpentTools.objects.DepletedMaterial` class
        for that material as values
    metadata: dict
        Dictionary with file-wide data names as keys and the
        corresponding dataas values, e.g. 'zai': [list of zai numbers]
    settings: dict
        names and values of the settings used to control operations
        of this reader

    :note:

        Does not support depleted materials with underscores,
        i.e. ``fuel_1`` will not be matched with the current methods
    """

    def __init__(self, filePath):
        MaterialReader.__init__(self, filePath, 'results_reader')
        self.matchMatNVar = r'(idx'
        """
        Captures material name and variable from string::

            B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
             --> ('fuel1', 'ADENS')

        """

    def read(self):
        """Read through the results file and store requested data."""
        keys = ['idx', '=', ]
        separators = ['\n', '];']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                if 'idx' in chunk[0] and '=' in chunk[0]:
                    self._addMetaXSdata(chunk)
                else:
                    self._addMetaXSdata(chunk)


    def _addMetaXSdata(self, chunk):
        options = {'INF_SP0': 'sigma_sct0', 'INF_SP1': 'sigma_sct1', 'INF_SP2': 'sigma_sct2',
                   'INF_ABS': 'sigma_abs'}
        for varName, metadataKey in options.items():
            if varName in chunk[0]:
                values = [line.strip() for line in chunk[1:]]
        return

if __name__ == '__main__':
    filePath = 'test_res.m'
    r1 = ResultsReader(filePath)
    r1.read()
    print('---done---\n')