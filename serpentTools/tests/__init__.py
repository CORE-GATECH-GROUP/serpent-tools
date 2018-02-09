"""
Module for testing the ``serpentTools`` package

.. note::

    The relative error tolerances must be low, :math:`O(1)`, because the
    error values themselves are incredibly low. In writing these tests,
    a relative error of 1E-2 resulted in a 5% difference between
    error quantities, which are all :math:`O(1E-3)`. A tight absolute
    tolerance can still be achieved.

"""
from os import path

from numpy import stack

from serpentTools import ROOT_DIR

TEST_ROOT = path.join(ROOT_DIR, 'tests')

def computeMeansErrors(*arrays):
    """
    Return the matrices of element-wise means and standard deviations

    This function assumes that:

    1. Each element in ``arrays`` is a numpy array
    2. Each element in ``arrays`` is of equal dimensionality

    The arrays are all stacked to create a new array with one
    additional axis at index 0. The mean and standard deviation are
    computed along this new axis so that the returned arrays
    are of equal dimensionality to the incoming arrays

    Parameters
    ----------
    arrays: iterable
        Arrays to be stacked

    Returns
    -------
    numpy.ndarray
        Element-wise mean of all incoming arrays
    numpy.ndarray
        Element-wise standard deviation of all incoming arrays
    """
    workMat = stack(arrays)
    return workMat.mean(axis=0), workMat.std(axis=0)
