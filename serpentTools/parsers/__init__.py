"""Package dedicated for reading ``SERPENT`` output files"""
from os import path

from numpy import zeros, empty, empty_like, array, longfloat

try:
    from scipy.sparse import csc_matrix

    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    csr_matrix = array

from serpentTools.settings.messages import warning
from serpentTools.parsers.depletion import DepletionReader
from serpentTools.parsers.branching import BranchingReader


def depmtx(fileP):
    """
    Read the contents of the ``depmtx`` file and return contents

    Parameters
    ----------
    fileP: str
        Path to depletion matrix file

    Returns
    -------
    t: float
        Length of time
    n0: numpy.ndarray
        Initial isotopic vector
    zai: numpy.array
        String identifiers for each isotope in ``n0`` and ``n1``
    a: numpy.array or scipy.sparse.csc_matrix
        Decay matrix. Will be sparse if scipy is installed
    n1: numpy.array
        Final isotopic vector
    """
    if not path.exists(fileP):
        raise IOError('Cannot find depeletion matrix file {}'.format(fileP))
    if not HAS_SCIPY:
        warning('Decay matrix will be returned as full matrix')
    with open(fileP) as f:
        t = float(f.readline().split()[-1][:-1])
        line = f.readline()
        numIso = 0
        n0Storage = {}
        while line[0] == 'N':
            numIso += 1
            vals = line.split()
            indx = int(vals[1][:-1])
            ndens = float(vals[4][:-1])
            n0Storage[indx - 1] = ndens
            line = f.readline()
        n0 = empty((numIso, 1), dtype=longfloat)
        for indx, v in n0Storage.items():
            n0[indx] = v
        zai = []
        while line[0] == 'Z':
            zai.append(line[12:-2])
            line = f.readline()

        line = f.readline()
        a = zeros((numIso, numIso), dtype=longfloat)

        while line[0] == 'A':
            vals = line.split()
            pos = [int(xx[:-1]) for xx in vals[1:3]]
            c = float(vals[-1][:-1])
            a[pos[0] - 1, pos[1] - 1] = c
            line = f.readline()
        n1 = empty_like(n0)
        while line and line[0] == 'N':
            vals = line.split()
            indx = int(vals[1][:-1])
            ndens = float(vals[4][:-1])
            n1[indx - 1] = ndens
            indx += 1
            line = f.readline()

        return t, n0, array(zai), csc_matrix(a) if HAS_SCIPY else a, n1
