"""Supporting class that stores data for a single branch instance."""

from serpentTools.objects import _SupportingObject


class BranchContainer(_SupportingObject):
    """Class that stores data for a single branch."""

    def __init__(self, parser, branchID, branchNames, stateData):
        _SupportingObject.__init__(self, parser)
        self.branchID = branchID
        self.stateData = stateData
        self.universes = {}
        self.branchNames = branchNames

    def addMetadata(self, key, value):
        """Add branch metadata to the object."""
        self._metadata[self._convertVariableName(key)] = value

