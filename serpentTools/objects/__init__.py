"""Objects used to support the parsing."""


class SupportingObject(object):
    """
    Base supporting object.

    Parameters
    ----------
    container: Some parser from serpentTools.parsers
        Container that created this object

    """

    def __init__(self, container):
        self.origin = container.filePath

    def __str__(self):
        return '<{} from {}>'.format(self.__class__.__name__, self.origin)


    @staticmethod
    def _convertVariableName(variable):
        """Converta a SERPENT variable to camelCase."""
        lowerSplits = [item.lower() for item in variable.split('_')]
        if len(lowerSplits) == 1:
            return lowerSplits[0]
        else:
            return lowerSplits[0] + ''.join([item.capitalize()
                                             for item in lowerSplits[1:]])


class NamedObject(SupportingObject):
    """Class for named objects like materials and detectors."""

    def __init__(self, container, name):
        SupportingObject.__init__(self, container)
        self.name = name

    def __str__(self):
        return '<{} {} from {}>'.format(self.__class__.__name__,
                                        self.name, self.origin)
