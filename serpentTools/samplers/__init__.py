"""
Package responsible for reading multiple files
of the same type and obtaining true standard deviations
"""
from glob import glob
from os.path import exists

from six import iteritems

from serpentTools.settings import rc
from serpentTools.messages import (warning, debug, MismatchedContainersError, 
                                   error)

MISSING_KEY_FLAG = "<missing>"


def extendFiles(files):
    """Return a set of files where some may contain * globs"""
    out = set()
    if isinstance(files, str):
        files = [files]
    for ff in files:
        if '*' in ff:
            for globbed in glob(ff):
                out.add(globbed)
        else:
            out.add(ff)
    return out


class Sampler(object):

    def __init__(self, files, parser):
        self.settings = rc.getReaderSettings('sampler')
        self.files = extendFiles(files)
        self.__parserCls = parser
        self.parsers = set()
        self.map = {}
        self.read()
        if not self.settings['skipPrecheck']:
            self._precheck()
        else:
            debug('Skipping pre-check')
        self.process()

    def read(self):
        """Read all the files and create parser objects"""
        self.map = {}
        self.parsers = set()
        allExistFlag = self.settings['allExist']
        missing = []
        raiseErrors = self.settings['raiseErrors']
        for filePath in self.files:
            if not exists(filePath):
                if allExistFlag:
                    raise OSError('File {} does not exist'
                                  .format(filePath))
                else:
                    missing.append(filePath)
                continue
            try:
                parser = self.__parserCls(filePath)
                parser.read()
            except Exception as ee:
                if raiseErrors:
                    raise ee
                else:
                    warning('The following error occurred while reading file '
                            '{}:\n\t{}'.format(filePath, str(ee)))
                    continue
            self.parsers.add(parser)
            self.map[filePath] = parser
        if missing:
            warning('The following files did not exist and were not processed '
                    '\n\t{}'.format(', '.join(missing)))

    def _checkParserDictKeys(self, attrName, objName=None, sort=True):
        objName = objName or attrName
        matches = {}
        for parser in self.parsers:
            if not hasattr(parser, attrName):
                if MISSING_KEY_FLAG not in matches:
                    matches[MISSING_KEY_FLAG] = {parser.filePath}
                else:
                    matches[MISSING_KEY_FLAG].add(parser.filePath)
                continue
            d = getattr(parser, attrName)
            keys = tuple(d.keys())
            if sort:
                keys = tuple(sorted(keys))
            if keys not in matches:
                matches[keys] = {parser.filePath}
            else:
                matches[keys].add(parser.filePath)
        if len(matches) > 1:
            self._raiseErrorMsgFromDict(matches, attrName, objName)

    @staticmethod
    def _raiseErrorMsgFromDict(misMatches, header, objName):
        msg = 'Files do not contain a consistent set of {}'.format(objName)
        critMsgs = [msg, header + ": Parser files"]
        for key, values in iteritems(misMatches):
            critMsgs.append('{}: {}'.format(key, ', '.join(values)))
        for critMsg in critMsgs:
            error(critMsg)
        raise MismatchedContainersError(msg)

    def __iter__(self):
        for parser in self.parsers:
            yield parser

    def process(self):
        """Process the repeated files to obtain true uncertainties"""
        debug('Processing data from {} parsers'.format(len(self.parsers)))
        self._process()
        debug('Done')

    def _process(self):
        raise NotImplementedError

    def _precheck(self):
        """Run through a series of checks to make sure data is consistent"""
        pass
