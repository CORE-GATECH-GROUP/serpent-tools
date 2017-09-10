"""Package dedicated for reading ``SERPENT`` output files"""


class _BaseReader(object):
    """Parent class from which all parsers will inherit"""

    def __init__(self, filePath):
        self.filePath = filePath
        self.metadata = {}

    def read(self):
        """
        Read the file and store the data.

        :note:

          This must be overwritten by each subclass of parser

        """
        raise NotImplementedError


class _MaterialReader(_BaseReader):
    """
    Parent class for files that store materials, i.e. ``bumat`` and ``dep``.
    """

    def __init__(self, filePath):
        _BaseReader.__init__(self, filePath)
        self.materials = {}

    def read(self):
        raise NotImplementedError
