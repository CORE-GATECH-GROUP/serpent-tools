"""
Supporting object that will be used by the branching reader and
results reader to store data for a single homogenized universe at a single
instance in time.
"""

from serpentTools.objects import SupportingObject
from serpentTools import messages


class HomogUniv(SupportingObject):
    """
    Class for storing homogenized universe specifications and retrieving them

    Parameters
    ----------
    # container: serpentTools.objects.readers.BaseReader or
        serpentTools.objects.containers.BranchContainer
        Object to which this universe is attached
    name: str
        name of the universe
    bu: float
        burnup value
    step: float
        temporal step
    day: float
        depletion day

    Attributes
    ----------
    name: str
        name of the universe
    bu: float
        burnup value
    step: float
        temporal step
    day: float
        depletion day

    """

    def __init__(self, container, name, bu, step, day):
        SupportingObject.__init__(self, container)
        self.name = name
        self.bu = bu
        self.step = step
        self.day = day
        # Dictionaries:
        self.b1Exp = {}
        self.infExp = {}
        self.b1Unc = {}
        self.infUnc = {}
        self.metaData = {}

    def addData(self, variableName, variableValue, uncertainty=False):
        """
        Sets the value of the variable and, optionally, the associate s.d.

        .. warning::
            This method will overwrite data for variables that already exist

        Parameters
        ----------
        variableName: str
            Variable Name
        variableValue:
            Variable Value
        uncertainty: bool
            Set to ``True`` in order to retrieve the
            uncertainty associated to the expected values

        Raises
        ------
        TypeError
            If the uncertainty flag is not boolean

        """

        # 1. Check the input type
        variableName = SupportingObject._convertVariableName(variableName)
        if not isinstance(uncertainty, bool):
            raise TypeError('The variable uncertainty has type %s.\n ...'
                            'It should be boolean.', type(uncertainty))
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variableName, uncertainty)
        # 3. Check if variable is already present. Then set the variable.
        if variableName in setter:
            messages.warning(
                "The variable {} will be overwritten".format(variableName))
        setter[variableName] = variableValue

    def get(self, variableName, uncertainty=False):
        """
        Gets the value of the variable VariableName from the dictionaries

        Parameters
        ----------
        variableName: str
            Variable Name
        uncertainty:   bool
            Boolean Variable- set to True in order to retrieve the
            uncertainty associated to the expected values

        Returns
        -------
        x:
            Variable Value
        dx:
            Associated uncertainty

        Raises
        ------
        TypeError
            If the uncertainty flag is not boolean
        KeyError
            If the variable requested is not stored on the
            object

        """
        # 1. Check the input values
        if not isinstance(uncertainty, bool):
            raise TypeError('The variable uncertainty has type %s.\n ...'
                            'It should be boolean.', type(uncertainty))
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variableName, False)
        if variableName not in setter:
            raise KeyError(
                "Variable {} absent from expected value dictionary".format(
                    variableName))
        x = setter.get(variableName)
        # 3. Return the value of the variable
        if not uncertainty:
            return x
        if setter is self.metaData:
            messages.warning('No uncertainty is associated to metadata')
            return x
        setter = self._lookup(variableName, True)
        if variableName not in setter:
            raise KeyError(
                "Variable {} absent from uncertainty dictionary".format(
                    variableName))
        dx = setter.get(variableName)
        return x, dx

    def _lookup(self, variableName, uncertainty):
        if "inf" in variableName:
            if not uncertainty:
                return self.infExp
            else:
                return self.infUnc
        elif "b1" in variableName:
            if not uncertainty:
                return self.b1Exp
            else:
                return self.b1Unc
        else:
            return self.metaData


class BranchContainer(SupportingObject):
    """
    Class that stores data for a single branch.

    The :py:class:`~serpentTools.parsers.branching.BranchingReader` stores
    branch variables and branched group constant data inside these
    container objects. These are used in turn to create
    :py:class:`~serpentTools.objects.containers.HomogUniv` objects for storing
    group constant data.

    Parameters
    ----------
    parser: serpentTools.objects.readers.BaseReader
        Parser that read the file that created this object
    branchID: int
        Index for the run for this branch
    branchNames: tuple
        Name of branches provided for this universe
    stateData: dict
        key: value pairs for branch variables

    Attributes
    ----------
    stateData: dict
        Name: value pairs for the variables defined on each
        branch card
    universes: dict
        Dictionary storing the homogenized universe objects.
        Keys are tuples of
        ``(universeID, burnup, burnIndex, burnDays)``
    """

    def __init__(self, parser, branchID, branchNames, stateData):
        SupportingObject.__init__(self, parser)
        self.branchID = branchID
        self.stateData = stateData
        self.universes = {}
        self.branchNames = branchNames
        self.metadata = {}

    def __str__(self):
        return '<BranchContainer for {} from {}>'.format(
            ', '.join(self.branchNames), self.filePath)

    def addMetadata(self, key, value):
        """Add branch metadata to the object."""
        self.metadata[self._convertVariableName(key)] = value

    def addUniverse(self, univID, burnup=0, burnIndex=0, burnDays=0):
        """
        Add a universe to this branch.

        Data for the universes are produced at specific points in time.
        The additional arguments help track when the data for this
        universe were created

        Parameters
        ----------
        univID: int or str
            Identifier for this universe
        burnup: float or int
            Value of burnup [MWd/kgU]
        burnIndex: int
            Point in the depletion schedule
        burnDays: int or float
            Point in time

        Returns
        -------
        newUniv: serpentTools.objects.containers.HomogUniv
        """
        newUniv = HomogUniv(self, univID, burnup, burnIndex, burnDays)
        key = [univID, burnup, burnIndex] + ([burnDays] if burnDays else [])
        self.universes[tuple(key)] = newUniv
        return newUniv
