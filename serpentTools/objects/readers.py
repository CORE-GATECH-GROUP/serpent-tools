from serpentTools.settings import rc
from serpentTools.messages import info

class BaseReader:
    """Parent class from which all parsers will inherit.

    Parameters
    ----------
    filePath: str
        path pointing towards the file to be read
    readerSettingsLevel: str or list
        type of reader. Determines which settings to obtain
    """

    def __init__(self, filePath, readerSettingsLevel):
        self.filePath = filePath
        self.metadata = {}
        if isinstance(readerSettingsLevel, str):
            self.settings = rc.getReaderSettings(readerSettingsLevel)
        else:
            self.settings = {}
            for level in readerSettingsLevel:
                self.settings.update(rc.getReaderSettings(level))

    def __str__(self):
        return '<{} reading {}>'.format(self.__class__.__name__, self.filePath)

    def read(self):
        """The main method for reading that not only parses data, but also
        runs pre and post checks.
        """
        info("Reading {}".format(self.filePath))
        self._precheck()
        self._read()
        info("  - done")
        self._postcheck()

    def _read(self):
        """Read the file and store the data.

        :warning:

            This read function has not been implemented yet

        """
        raise NotImplementedError

    def _precheck(self):
        """Pre-checking, e.g., make sure Serpent did not
        exit abnormally, or disk ran out of space while parsing.
        """
        pass

    def _postcheck(self):
        """Make sure data looks reasonable. Could possibly check for
        negative cross sections, negative material densitites, etc (which
        can happen if using the reprocessing interface incorrectly).
        """
        pass


class MaterialReader(BaseReader):
    """Parent class for files that store materials."""

    def __init__(self, filePath, readerSettingsLevel):
        BaseReader.__init__(self, filePath, readerSettingsLevel)
        self.materials = {}


class XSReader(BaseReader):
    """Parent class for the branching and results reader"""

    def __init__(self, filePath, readerSettingsLevel):
        BaseReader.__init__(self, filePath, ['xs', readerSettingsLevel])
        self.settings['variables'] = rc.expandVariables()
        self.settings.pop('variableGroups')
        self.settings.pop('variableExtras')


    def _checkAddVariable(self, variableName):
        """Check if the data for the variable should be stored"""
        # no variables given -> get all
        if not any(self.settings['variables']):
            return True
        # explicitly named
        if variableName in self.settings['variables']:
            return True
        if (self.settings['getB1XS'] and variableName.replace('B1_', '') in
                self.settings['variables']):
            return True
        if (self.settings['getInfXS'] and variableName.replace('INF_', '') in
                self.settings['variables']):
            return True
        return False
