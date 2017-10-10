"""Objects used to support the parsing."""


class _SupportingObject(object):
    """
    Base supporting object.

    Parameters
    ----------
    container: Some parser from serpentTools.parsers
        Container that created this object
    name: str
        Name of this specific object, e.g. material name, detector name, etc.

    """

    def __init__(self, container):
        self._container = container
        self._filePath = container.filePath

    def __repr__(self):
        return '<{} from {}>'.format(self.whatAmI(), self._filePath)

    def whatAmI(self):
        return type(self).__name__

    def __getattr__(self, item):
        """Search for the item in the containers metadata."""
        if item in self._container.metadata:
            return self._container.metadata[item]
        raise AttributeError('{} has object has no attribute \'{}\''
                             .format(self, item))

    @staticmethod
    def _convertVariableName(variable):
        """Converta a SERPENT variable to camelCase."""
        lowerSplits = [item.lower() for item in variable.split('_')]
        if len(lowerSplits) == 1:
            return lowerSplits[0]
        else:
            return lowerSplits[0] + ''.join([item.capitalize()
                                             for item in lowerSplits[1:]])


class _NamedObject(_SupportingObject):
    """Class for named objects like materials and detectors."""

    def __init__(self, container, name):
        _SupportingObject.__init__(self, container)
        self.name = name

    def __repr__(self):
        return '<{} {} from {}>'.format(self.whatAmI(),
                                        self.name, self._filePath)