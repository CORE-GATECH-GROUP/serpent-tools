"""Objects used to support the parsing."""


class NamedObject(object):
    """Class for named objects like materials and detectors."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.name)


def convertVariableName(variable):
    """Convert a SERPENT variable to camelCase"""
    lowerSplits = [item.lower() for item in variable.split('_')]
    if len(lowerSplits) == 1:
        return lowerSplits[0]
    else:
        return lowerSplits[0] + ''.join([item.capitalize()
                                         for item in lowerSplits[1:]])


