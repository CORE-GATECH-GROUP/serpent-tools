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
        self.filePath = container.filePath

    def __str__(self):
        return '<{} from {}>'.format(self.__class__.__name__, self.filePath)

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
                                        self.name, self.filePath)


def splitItems(items):
    """
    Split values from their uncertainties

    i.e. 'v1 u2 v2 u2 ...' -> [v1, v2, ...], [u2, u2, ...]
    Also works with a list of items

    Parameters
    ----------
    items: str or list or tuple
        Collection of values and relative uncertainties.
        If a string, will be split at spaces to obtain
        [v1, u1, v2, u2, ...]

    Returns
    -------
    vals: list
        Items at odd indices
    uncs: list
        Items at even indices

    """
    if isinstance(items, str):
        usable = items.split()
    else:
        usable = items

    numItems = len(usable)

    vals = [usable[ii] for ii in range(0, numItems, 2)]
    uncs = [usable[ii] for ii in range(1, numItems, 2)]

    return vals, uncs
