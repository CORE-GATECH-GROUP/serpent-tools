"""
Supporting object that will be used by the branching reader and
results reader to store data for a single homogenized universe at a single
instance in time.
"""

from serpentTools.objects import SupportingObject
from serpentTools.messages import warning, SerpentToolsException, debug


class HomogUniv(SupportingObject):
    """
    Class for storing homogenized universe specifications and retrieving them

    Parameters
    ----------
    container: serpentTools.objects.readers.BaseReader or
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
    infExp: dict
        Expected values for infinite medium group constants
    infUnc: dict
        Relative uncertainties for infinite medium group constants
    b1Exp: dict
        Expected values for leakage corrected group constants
    b1Unc: dict
        Relative uncertainties for leakage-corrected group constants
    metadata: dict
        Other values that do not not conform to inf/b1 dictionaries
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
        self.metadata = {}

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
            warning("The variable {} will be overwritten".format(variableName))
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
        if setter is self.metadata:
            warning('No uncertainty is associated to metadata')
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
            return self.metadata


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
        ``(universeID, burnup, burnIndex)``
    """

    def __init__(self, parser, branchID, branchNames, stateData):
        SupportingObject.__init__(self, parser)
        self.branchID = branchID
        self.stateData = stateData
        self.universes = {}
        self.branchNames = branchNames
        self.__orderedUniverses = None
        self.__keys = set()

    def __str__(self):
        return '<BranchContainer for {} from {}>'.format(
            ', '.join(self.branchNames), self.filePath)

    def __contains__(self, item):
        return item in self.__keys or item in self.stateData

    @property
    def orderedUniv(self):
        """Universe keys sorted by ID and by burnup"""
        if not any(self.universes):
            raise SerpentToolsException(
                'No universes stored on branch {}'.format(str(self))
            )
        if self.__orderedUniverses is None:
            self.__orderedUniverses = tuple(sorted(
                self.__keys, key=lambda tpl: (tpl[0], tpl[2])
            ))
        return self.__orderedUniverses

    def addUniverse(self, univID, burnup=0, burnIndex=0, burnDays=0):
        """
        Add a universe to this branch.

        Data for the universes are produced at specific points in time.
        The additional arguments help track when the data for this
        universe were created.

        .. warning::
            This method will overwrite data for universes that already exist

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
        key = tuple(
            [univID, burnup, burnIndex] + ([burnDays] if burnDays else []))
        if key in self.__keys:
            warning('Overwriting existing universe {} in {}'
                    .format(key, str(self)))
        else:
            self.__keys.add(key)
        self.universes[key] = newUniv
        return newUniv

    def getUniv(self, univID, burnup=None, index=None):
        """
        Return a specific universe given the ID and time of interest

        If burnup and index are given, burnup is used to search

        Parameters
        ----------
        univID: int
            Unique ID for the desired universe
        burnup: float or int
            Burnup [MWd/kgU] of the desired universe
        index: int
            Point of interest in the burnup index

        Returns
        -------
        univ: serpentTools.objects.containers.HomogUniv
            Requested Universe

        Raises
        ------
        KeyError:
            If the requested universe could not be found
        SerpentToolsException:
            If neither burnup nor index are given
        """
        if burnup is None and index is None:
            raise SerpentToolsException('Burnup or index are required inputs')
        searchIndex = 2 if index is not None else 1
        searchValue = index if index is not None else burnup
        for key in self.__keys:
            if key[0] == univID and key[searchIndex] == searchValue:
                debug('Found universe that matches with keys {}'
                      .format(key))
                return self.universes[key]
        searchName = 'burnup' + ('' if index is None else ' index')
        raise KeyError(
            'Could not find a universe that matched requested universe {} and '
            '{} {}'.format(univID, searchName, searchValue))
