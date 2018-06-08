"""Objects used to support the parsing."""

class BaseObject(object):
    """Most basic class shared by all other classes."""

    def compare(self, other, rtol=0., atol=0., sigma=3, strictMissing=True):
        """
        Compare the results of this reader to another.

        Parameters
        ----------
        other:
            Other reader instance against which to compare.
            Must be a similar class as this one.
        rtol: float
            Relative tolerance for arrays.
        atol: float
            Absolute tolerance for arrays
        sigma: int
            Size of confidence interval to apply to
            potentially random values
        strictMissing: bool
            If ``True``, raise Exceptions for missing data

        Returns
        -------
        bool:
            ``True`` if the readers are in agreement with
            each other according to the parameters specified

        Raises
        ------
        TypeError
            If ``other`` is not of the same class as this class
            nor a subclass of this class
        :py:class:`~serpentTools.messages.MissingDataError`
            If data is missing from ``other`` and ``strictMissing``
        """
        if not (isinstance(other, self.__class__) or
                issubclass(other.__class__, self.__class__)):
            oName = other.__class__.__name__
            name = self.__class__.__name__
            raise TypeError(
                    "Cannot compare against {} - not instance nor subclass "
                    "of {}".format(oName, name))

            return self._compare(other, rtol, atol, sigma, strictMissing)

    def _compare(self, other, rtol, atol, sigma, strictMissing):
        """Actual comparison method for similar classes."""
        raise NotImplementedError
