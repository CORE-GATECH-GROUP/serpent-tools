"""
Package responsible for reading multiple files
of the same type and obtaining true standard deviations
"""
from glob import glob
from os.path import exists

from serpentTools.settings import rc
from serpentTools.messages import (warning, debug, MismatchedContainersError,
                                   error, SamplerError, info)
from serpentTools.parsers.base import BaseReader

MISSING_KEY_FLAG = "<missing>"


def extendFiles(files):
    """Return a set of files where some may contain * globs"""
    out = set()
    if isinstance(files, str):
        files = [files]
    for ff in files:
        if '*' in ff:
            unGlob = glob(ff)
            if not unGlob:
                warning("No files matched with pattern {}".format(ff))
                continue
            for globbed in unGlob:
                out.add(globbed)
        else:
            out.add(ff)
    return out


class Sampler(object):
    """Base class for reading multiple files of of a similar type

    Parameters
    ----------
    files: str or iterable
        Single file or iterable (list) of files from which to read.
        Supports file globs, ``*det0.m`` expands to all files that
        end with ``det0.m``
    parser: subclass of BaseReader
        Class that will be used to read all files

    Attributes
    ----------
    files: set
        Unordered set containing full paths of unique files read
    settings: dict
        Dictionary of sampler-wide settings
    parsers: set
        Unordered set of all parsers that were successful
    map: dict
        Dictionary where key, value pairs are files and their corresponding
        parsers

    Raises
    ------
    serpentTools.messages.SamplerError
        If ``parser`` is not a subclass of ``BaseReader``
    """

    def __init__(self, files, parser):
        if not issubclass(parser, BaseReader):
            raise SamplerError(
                "parser argument must be a subclass of BaseReader, not "
                "{}".format(parser.__name__))
        self.settings = rc.getReaderSettings('sampler')
        self.files = extendFiles(files)
        if not self.files:
            raise SamplerError("No files stored on Sampler.")
        self.__parserCls = parser
        self.parsers = set()
        self.map = {}
        self.read()

    def read(self):
        """Read all the files and create parser objects"""
        self._readAll()
        if not self.settings['skipPrecheck']:
            self._precheck()
        else:
            debug('Skipping pre-check')
        self.process()
        if self.settings['freeAll']:
            info("Removing all parsers and containers from memory since "
                 "setting <sampler.freeAll> is ``True``")
            self.free()

    def _readAll(self):
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
                    error('The following error occurred while reading file {} '
                          'and was suppressed since setting <raiseErrors> is '
                          'True}:\n{}'.format(filePath, str(ee)))
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
        for key, values in misMatches.items():
            critMsgs.append('{}: {}'.format(key, ', '.join(values)))
        error('\n'.join(str(item) for item in critMsgs))
        raise MismatchedContainersError(msg)

    def __iter__(self):
        for parser in self.parsers:
            yield parser

    def __len__(self):
        return len(self.parsers)

    def __contains__(self, item):
        return item in self.files

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

    def free(self):
        """Remove all parsers and individual containers from memory"""
        self._free()  # call subclass specific before wiping all parsers
        self.parsers = set()
        self.map = {}

    def _free(self):
        raise NotImplementedError


class SampledContainer(object):
    """
    Base class for containers that produce averages and deviations from
    multiple files

    Parameters
    ----------
    N: int
        Number of containers to expect
    expectedContainer: class
        What class to expect for all incoming containers
    """

    docFree = """If ``<sampler.freeAll>``
        is True, then ``free`` will be called after all files have been read
        and processed."""

    def __init__(self, N, expectedContainer):
        self.N = N
        self._index = 0
        self.__expectedClass = expectedContainer

    def free(self):
        pass

    def loadFromContainer(self, container):
        """
        Copy data from a similar container.

        Parameters
        ----------
        container:
            Incoming container from which to take data.

        Raises
        ------
        serpentTools.messages.MismatchedContainersError
            If the incoming container is not the expected type
            declared at construction
        serpentTools.messages.SamplerError
            If more containers have been loaded than specified at
            construction

        """
        if not isinstance(container, self.__expectedClass):
            raise MismatchedContainersError(
                'Sampled container expects {} type containers, not '
                '{}'.format(self.__expectedClass, type(container)))
        if self._index == self.N:
            name = self.name if hasattr(self, 'name') else ''
            otherName = container.__class__.__name__
            msg = ("{} {} has already loaded {} {} objects and cannot exceed "
                   "this bound ".format(self.__class__.__name__, name, self.N,
                                        otherName))
            raise SamplerError(msg)
        self._loadFromContainer(container)
        self._index += 1

    def _loadFromContainer(self, container):
        raise NotImplementedError

    def finalize(self):
        """Produce final uncertainties from all aggregated runs"""
        if self._index != self.N:
            warning("Data from only {} of {} files has been loaded".format(
                self._index, self.N))
        self._finalize()

    def _finalize(self):
        raise NotImplementedError
