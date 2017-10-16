import numpy
from serpentTools.objects import _SupportingObject
from serpentTools.settings import messages


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
        self.b1Exp = {}
        self.infExp = {}
        self.b1Unc = {}
        self.infUnc = {}

    def set(self, variablename, variablevalue, uncertainty='False'):

        if "inf" in variablename:
            if uncertainty == 'False':
                if variablename in self.infExp[variablename]:
                    messages.warning('The variable will be overwritten')
                self.infExp[variablename] = variablevalue
            elif uncertainty == 'True':
                if variablename in self.infExp[variablename]:
                    messages.warning('The variable will be overwritten')
                self.infUnc[variablename] = variablevalue
        elif "b1" in variablename:
            if uncertainty == 'False':
                if variablename in self.infExp[variablename]:
                    messages.warning('The variable will be overwritten')
                self.b1Exp[variablename] = variablevalue
            elif uncertainty == 'True':
                if variablename in self.infExp[variablename]:
                    messages.warning('The variable will be overwritten')
                self.b1Unc[variablename] = variablevalue

    def get(self, variablename, uncertainty='False'):

        # 1. Check the input values
        variablename = _SupportingObject._convertVariableName(variablename)
        if not isinstance(uncertainty, bool):
            raise messages.error("Uncertainty must be a boolean variable")

        # 2. Retrieve the values from the dictionaries
        if "inf" in variablename:
            if uncertainty == 'False':
                x = self.infExp.get(variablename)
                return x
            elif uncertainty == 'True':
                x = self.infExp.get(variablename)
                dx = self.infUnc.get(variablename)
                return x, dx
        elif "b1" in variablename:
            if uncertainty == 'False':
                x = self.b1Exp.get(variablename)
                return x

            elif uncertainty == 'True':
                x = self.b1Exp.get(variablename)
                dx = self.b1Unc.get(variablename)
                return x,dx

