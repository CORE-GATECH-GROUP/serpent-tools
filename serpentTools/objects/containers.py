"""
Supporting object that will be used by the branching reader and
results reader to store data for a single homogenized universe at a single
instance in time.
"""

from serpentTools.objects import _SupportingObject
from serpentTools.settings import messages


class HomogUniv(_SupportingObject):
    """
    Class for storing homogenized universe specifications and retrieving them

     Parameters
    ----------
    -container: str
        name of the parser
    -name: str
        name of the universe
    -bu: float
        burnup value
    -step: float
        temporal step
    -day: float
        depletion day

    Attributes
    ----------
    -name: str
        name of the universe
    -bu: float
        burnup value
    -step: float
        temporal step
    -day: float
        depletion day

    """

    def __init__(self, container, name, bu, step, day):
        _SupportingObject.__init__(self, container)
        self.name = name
        self.bu = bu
        self.step = step
        self.day = day
        # Dictionaries:
        self.b1Exp = {}
        self.infExp = {}
        self.b1Unc = {}
        self.infUnc = {}

    def set(self, variableName, variableValue, uncertainty=False):
        """
        Sets the value of the variable and, optionally, the associate s.d.

        Parameters
        ----------
        variableName: str
            Variable Name
        variableValue: str/tuple/list
            Variable Value
        uncertainty:   bool
            Boolean Variable- set to True in order to retrieve the
            uncertainty associated to the expected values

        Notes:
        ---------
            Raises a warning if the value of the variable is overwritten

        """

        # 1. Check the input type
        variableName = _SupportingObject._convertVariableName(variableName)
        if not isinstance(uncertainty, bool):
            raise messages.error('The variable uncertainty has type %s.\n ...'
                                 'It should be boolean.', type(uncertainty))
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variableName, uncertainty)
        # 3. Check if variable is already present. Then set the variable.
        if variableName in setter:
            messages.warning('The variable will be overwritten')
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
        x: str/tuple/list
            Variable Value
        dx: str/tuple/list
            Associated uncertainty

        """
        # 1. Check the input values
        variableName = _SupportingObject._convertVariableName(variableName)
        if not isinstance(uncertainty, bool):
            raise messages.error('The variable uncertainty has type %s.\n ...'
                                 'It should be boolean.', type(uncertainty))
        # 2. Pointer to the proper dictionary
        setter = self._lookup(variableName, False)
        x = setter.get(variableName)
        # 3. Return the value of the variable
        if not uncertainty:
            return x
        setter = self._lookup(variableName, True)
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

        messages.error('%s not found.The string must contain either the   ...'
                       'inf, or b1 substring.', variableName)
