"""
Collection of base classes from which other objects inherit.
"""

from serpentTools.messages import (
    warning, info,
)
from serpentTools.utils import (
    compareDocDecorator, DEF_COMP_LOWER, DEF_COMP_SIGMA,
    DEF_COMP_UPPER
)
from serpentTools.utils.compare import (
    finalCompareMsg,
)
from serpentTools.settings import rc


class BaseObject(object):
    """Most basic class shared by all other classes."""

    @compareDocDecorator
    def compare(self, other, lower=DEF_COMP_LOWER, upper=DEF_COMP_UPPER,
                sigma=DEF_COMP_SIGMA, verbosity=None):
        """
        Compare the results of this reader to another.

        For values without uncertainties, the upper and lower
        arguments control what passes and what messages get
        raised. If a quantity in ``other`` is less than
        ``lower`` percent different that the same quantity
        on this object, consider this allowable and make
        no messages.
        Quantities that are greater than ``upper`` percent
        different will have a error messages printed and
        the comparison will return ``False``, but continue.
        Quantities with difference between these ranges will
        have warning messages printed.

        Parameters
        ----------
        other:
            Other reader instance against which to compare.
            Must be a similar class as this one.
        {compLimits}
        {sigma}
        verbosity: None or str
            If given, update the verbosity just for this comparison.

        Returns
        -------
        bool:
            ``True`` if the objects are in agreement with
            each other according to the parameters specified

        Raises
        ------
        {compTypeErr}
        ValueError
            If upper > lower,
            If sigma, lower, or upper are negative
        """
        upper = float(upper)
        lower = float(lower)
        sigma = int(sigma)
        if upper < lower:
            raise ValueError("Upper limit must be greater than lower. "
                             "{} is not greater than {}"
                             .format(upper, lower))
        for item, key in zip((upper, lower, sigma),
                             ('upper', 'lower', 'sigma')):
            if item < 0:
                raise ValueError("{} must be non-negative, is {}"
                                 .format(key, item))

        self._checkCompareObj(other)

        previousVerb = None
        if verbosity is not None:
            previousVerb = rc['verbosity']
            rc['verbosity'] = verbosity

        self._compareLogPreMsg(other, lower, upper, sigma)

        areSimilar = self._compare(other, lower, upper, sigma)

        if areSimilar:
            herald = info
        else:
            herald = warning
        herald(finalCompareMsg(self, other, areSimilar))
        if previousVerb is not None:
            rc['verbosity'] = previousVerb

        return areSimilar

    def _compare(self, other, lower, upper, sigma):
        """Actual comparison method for similar classes."""
        raise NotImplementedError

    def _checkCompareObj(self, other):
        """Verify that the two objects are same class or subclasses."""
        if not (isinstance(other, self.__class__) or
                issubclass(other.__class__, self.__class__)):
            oName = other.__class__.__name__
            name = self.__class__.__name__
            raise TypeError(
                "Cannot compare against {} - not instance nor subclass "
                "of {}".format(oName, name))

    def _compareLogPreMsg(self, other, lower=None, upper=None, sigma=None,
                          quantity=None):
        """Log an INFO message about this specific comparison."""
        leader = "Comparing {}> against < with the following tolerances:"
        tols = [leader.format((quantity + ' from ') if quantity else ''), ]
        for leader, obj in zip(('>', '<'), (self, other)):
            tols.append("{} {}".format(leader, obj))
        for title, val in zip(('Lower', 'Upper'), (lower, upper)):
            if val is None:
                continue
            tols.append("{} tolerance: {:5.3F} [%]".format(title, val))
        if sigma is not None:
            sigmaStr = ("Confidence interval for statistical values: {:d} "
                        "sigma or {} %")
            sigmaDict = {1: 68, 2: 95}
            tols.append(
                sigmaStr.format(sigma, sigmaDict.get(sigma, '>= 99.7')
                                if sigma else 0))
        info('\n\t'.join(tols))


class NamedObject(BaseObject):
    """Class for named objects like materials and detectors."""

    def __init__(self, name):
        BaseObject.__init__(self)
        self.name = name

    def __str__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.name)
