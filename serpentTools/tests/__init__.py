from os import path, remove
from shutil import copy

from serpentTools import ROOT_DIR

TEST_ROOT = path.join(ROOT_DIR, 'tests')


class SamplerMixin(object):
    """Helper class that copies files and retains them for deletion"""

    def __init__(self):
        self.fileMap = {}

    def _copyTestFiles(self, test, src, numFiles):
        if '.' in src:
            dotIndx = src.index('.')
            base = src[:dotIndx]
            ext = src[dotIndx:]
        else:
            base = src
            ext = ''
        fileFmt = base + '_{}'.format(test) + '_cp{}' + ext
        if test not in self.fileMap:
            self.fileMap[test] = set()

        for n in range(numFiles):
            thisF = fileFmt.format(n)
            copy(src, thisF)
            self.fileMap[test].add(thisF)

    def _removeTestFiles(self, test):
        for fileP in self.fileMap.pop(test):
            if path.isfile(fileP):
                remove(fileP)

    def _removeAllTestFiles(self):
        tests = list(self.fileMap.keys())
        for test in tests:
            self._removeTestFiles(test)
        self.fileMap = {}
