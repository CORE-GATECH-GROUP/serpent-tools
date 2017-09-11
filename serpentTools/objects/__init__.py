"""Objects used to support the parsing."""

import numpy


class _SupportingObject(object):
    """
    Base supporting object.

    Parameters
    ----------
    container: Some parser from :py:mod:`~serpentTools.parsers`
        Container that created this object
    name: str
        Name of this specific object, e.g. material name, detector name, etc.

    """

    def __init__(self, container, name):
        self._container = container
        self.name = name
        self._filePath = container.filePath

    def __repr__(self):
        return '<{} {} from {}>'.format(self.__class__.___name__,
                                        self.name, self._filePath)

    def __getattr__(self, item):
        """Search for the item in the containers metadata."""
        if item in self._container.metadata:
            return self._container.metadata[item]
        raise AttributeError('{} has object has not atribute \'{}\''
                             .format(self, item))


class DepletedMaterial(_SupportingObject):
    """
    Class for storing material data from ``_dep.m`` files.

    Parameters
    ----------
    parser: :py:class:`~serpentTools.parsers.depletion.DepletionReader`
        Parser that found this material.
        Used to obtain file metadata like isotope names and burnup
    name: str
        Name of this material
    """

    def __init__(self, parser, name):
        _SupportingObject.__init__(self, parser, name)
        self._varData = {}

    def __getattr__(self, item):
        """
        Allows the user to get items like ``zai`` and ``adens``
        with ``self.zai`` and ``self.adens``, respectively."""
        if item in self._varData:
            return self._varData[item]
        return _SupportingObject.__getattr__(self, item)

    def addData(self, variable, rawData):
        """
        Add data straight from the file onto a variable.

        Parameters
        ----------
        variable: str
            Name of the variable
        rawData: list
            List of strings corresponding to the raw data from the file
        """
        scratch = []
        for line in rawData:
            if line:
                scratch.append([float(item) for item in line.split()])
        self._varData[variable] = numpy.array(scratch)
