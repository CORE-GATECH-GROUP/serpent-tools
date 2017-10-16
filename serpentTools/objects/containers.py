import numpy
from serpentTools.objects import _SupportingObject


class HomogUniv(_SupportingObject):
    """Class for:
    (1) Storing universe number and, optionally,
    burnup, day, bu step provided by results and branching readers
    (2) Adding and get variables.

    Public methods
    ----------
    -set(VariableName,VariableValue,**kwargs)
    -get(VariableName,** kwargs)
    -inf(VariableName,** kwargs)
    -b1(VariableName,** kwargs)

    Attributes
    ----------
    -name: name of the universe
    -bu:   burnup value
    -step: temporal step
    -day:  depletion day
    """

    def __init__(self, container, name, bu, step, day):
        """ Constructor of the class. Each universe is defined  uniquely
        in terms of the attributes mentioned in the docstring. The input
        container refers to the name of the parser (branching/results reader).
        """
        _SupportingObject.__init__(self, container)
        self.name = name
        self.bu = bu
        self.step = step
        self.day = day
        # It creates 4 dictionaries:
        #    (1) For B1-computed expected values
        #    (2) For the uncertainty associated to B1-computed expected values
        #    (3) For Inf expected values
        #    (4) For the uncertainty associated to Inf-computed expected values
        self.dic_b1_e = {}
        self.dic_Inf_e = {}
        self.dic_b1_u = {}
        self.dic_Inf_u = {}

    def set(self, variablename, variablevalue, uncertainty):
        """
        The function sets the keys in the dictionaries introduced in the
        contructor.

        Parameters
        ----------
        variablename:   variable name
        variablevalue:  variable expected value
        uncertainty:    associated uncertainty

        Returns
        -------

        """

        # Convert variable name in CamelCase
        variablename = _SupportingObject._convertVariableName(variablename)
        # Check if it contains the substring "Inf"
        if "Inf" in variablename:
            if uncertainty == 'e':
                self.dic_Inf_e[variablename] = variablevalue
            elif uncertainty == 'u':
                self.dic_Inf_u[variablename] = variablevalue
            else:
                print('Error')
        elif "B1" in variablename:
            if uncertainty == 'e':
                self.dic_b1_e_e[variablename] = variablevalue
            elif uncertainty == 'u':
                self.dic_b1_u[variablename] = variablevalue
            else:
                print('Error')

    def get(self, variablename, uncertainty):
        """
        Parameters
        ----------
        variablename:   variable expected value
        uncertainty:    variable associated uncertainty

        Returns
        -------
        - x:      variable expected value
        and, optionally,
        - dx:     the associated uncertainty
        """
        # Convert variable name in CamelCase
        variablename = _SupportingObject._convertVariableName(variablename)
        # Check if it contains the substring "Inf"
        if "Inf" in variablename:
            if uncertainty == 'e':
                x = self.dic_Inf_e.get(variablename)
                return x
            elif uncertainty == 'u':
                x = self.dic_Inf_e.get(variablename)
                dx = self.dic_Inf_u.get(variablename)
                return x, dx
            else:
                print('Error')

        elif "B1" in variablename:
            if uncertainty == 'e':
                x = self.dic_b1_e.get(variablename)
                return x

            elif uncertainty == 'u':
                x = self.dic_b1_e.get(variablename)
                dx = self.dic_b1_u.get(variablename)
                return x,dx
            else:
                print('Error')
