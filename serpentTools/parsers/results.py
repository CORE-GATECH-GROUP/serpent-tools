"""Parser responsible for reading the ``*res.m`` files"""


from serpentTools.objects.readers import XSReader


class ResultsReader(XSReader):
    """
    Parser responsible for reading and working with result files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """
    def __init__(self, filePath):
        XSReader.__init__(self, filePath, ['branching', 'xs'])
