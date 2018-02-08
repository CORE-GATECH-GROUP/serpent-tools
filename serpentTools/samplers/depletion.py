"""
Class responsible for reading multiple depletion files
and obtaining true uncertainties
"""

from six import iteritems
from serpentTools.parsers.depletion import DepletionReader
from serpentTools.samplers import Sampler
from serpentTools.objects.materials import DepletedMaterial


class DepletionSampler(Sampler):

    def __init__(self, files):
        self.materials = {}
        self.metadata = {}
        Sampler.__init__(self, files, DepletionReader)

    def _precheck(self):
        self._checkParserDictKeys('materials')
        self._checkParserDictKeys('metadata')
        self._checkMetadata()

    def _checkMetadata(self):
        misMatch = {}

        for parser in self.parsers:
            for key, value in iteritems(parser.metadata):
                valCheck = tuple(value)
                if key not in misMatch:
                    misMatch[key] = {}
                    misMatch[key][valCheck] = 1
                    continue
                if valCheck not in misMatch[key]:
                    misMatch[key][valCheck] = 1
                else:
                    misMatch[key][valCheck] += 1
        for mKey, matches in iteritems(misMatch):
            if len(matches) > 1:
                self._raiseErrorMsgFromDict(matches, 'values',
                                            '{} metadata'.format(mKey))
    def _process(self):
        pass
