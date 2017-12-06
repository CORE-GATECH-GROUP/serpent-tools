from serpentTools.settings import rc


class BaseReader(object):
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
        """Read the file and store the data.

        :note:

          This must be overwritten by each subclass of parser

        """
        raise NotImplementedError


class MaterialReader(BaseReader):
    """Parent class for files that store materials."""

    def __init__(self, filePath, readerSettingsLevel):
        BaseReader.__init__(self, filePath, readerSettingsLevel)
        self.materials = {}

    def read(self):
        raise NotImplementedError


class XSReader(BaseReader):
    """Parent class for the branching and results reader"""

    def __init__(self, filePath, readerSettingsLevel):
        BaseReader.__init__(self, filePath, ['xs', readerSettingsLevel])
        self.settings['variables'] = rc.expandVariables()
        self.settings.pop('variableGroups')
        self.settings.pop('variableExtras')

    def read(self):
        raise NotImplementedError
