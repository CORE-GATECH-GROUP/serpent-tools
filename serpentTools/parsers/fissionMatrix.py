""" Fission Matrix Reader. Mono-dimensional case"""

import re
import numpy as np
import matplotlib.pyplot as plt
from serpentTools.objects.readers import BaseReader
from serpentTools.messages import warning, error
from serpentTools.plot import cartMeshPlot, formatPlot

# Regular Expressions
fMVal = r'fmtx_t\s+\(\s*(\d+),\s*(\d+)\)\s+=\s+([\d\+\.E-]+)\s;\s ' \
        r'fmtx_t_err\s+\(\s*(\d+),\s*(\d+)\)\s+=\s+([\d\+\.E-]+)'
dimsEx = r'fmtx_t\s+=\s+zeros\((\d+),(\d+)\)'


def signCheck(lista, filePath):
    for x in lista:
        if x < 0:
            raise ValueError("Negative Values in Fission Matrix {}".format(
                filePath))


def dimCheck(dims):
    if dims[0] <= 0 or dims[1] <= 0:
        error('Fission Matrix has Negative Dimensions')
    elif dims[0] != dims[1]:
        error('The Fission Matrix is Rectangular')


class FissionMatrixReader(BaseReader):
    """
    Class for reading 1D Fission Matrix output files.

    Parameters
    ----------
    filePath: str
        path pointing towards the file to be read

    Attributes
    ----------
    fMat: np.array
        Contains Fission Matrix Coefficients
    fMatU: np.array
        Contains Uncertainty associated to Fission Matrix Coefficients
    domEigVal: float
        Dominant Eigenvalue (k-eff)
    domEigVec: np.array
        Dominant Eigenvector Spatial Distribution
    domRatio: float
        Dominance Ratio
    eigValVec: np.array
        Fission Matrix Eigenvalues
    eigVecMat: np.array
        Eigenvectors Matrix
    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'fissMat')
        self.fMat = None
        self.fMatU = None
        self.domEigVal = None
        self.domEigVec = None
        self.domRatio = None
        self.eigValVec = None
        self.eigVecMat = None

    def _precheck(self):
        with open(self.filePath) as check:
            for line in check:
                if line[:4] == 'fmtx' in line:
                    return
        warning('Unable to find fission matrix data '
                'in {}'.format(self.filePath))

    def _read(self):
        """
        Reads the fission matrix output file.

        Raises
        -------
        ValueError
        Negative fission matrix entries


        """
        dims = self.metaFind(dimsEx)
        dimCheck(dims)
        FissMat = np.zeros((int(dims[0]), int(dims[1])))
        FissMatUnc = np.zeros((int(dims[0]), int(dims[1])))
        with open(self.filePath) as fp:
            for lineNo, line in enumerate(fp):
                m = re.match(fMVal, line)
                if m is not None:
                    lista = [float(i) for i in m.groups()]
                    signCheck(lista, self.filePath)
                    FissMat[int(lista[0]) - 1, int(lista[1]) - 1] = lista[2]
                    FissMatUnc[int(lista[0]) - 1, int(lista[1]) - 1] = lista[5]
        self.fMat = FissMat
        self.fMatU = FissMatUnc
        return self.fMat, self.fMatU

    def metaFind(self, regEx):
        with open(self.filePath) as fp:
            for lineNo, line in enumerate(fp):
                metaString = re.match(regEx, line)
                if metaString is not None:
                    metaList = [float(i) for i in metaString.groups()]
                    return metaList

    def fMatPlot(self, title=None, xlabel=None, ylabel=None, cmap=None):
        """
        Plots the fission matrix sparsity pattern

        Parameters
        ----------
        title: str
            Plot title
        xlabel: str
            x-axis label
        ylabel: str
            y-axis label
        cmap: str
            Color map

        """
        self._matPlot(self.fMat, title, xlabel, ylabel, cmap)

    def fMatUPlot(self, title=None, xlabel=None, ylabel=None, cmap=None):
        """
        Plots the sparsity pattern of the uncertainty matrix associated to
        the fission matrix entries

        Parameters
        ----------
        title: str
            Plot title
        xlabel: str
            x-axis label
        ylabel: str
            y-axis label
        cmap: str
            Color map

        """
        self._matPlot(self.fMatU, title, xlabel, ylabel, cmap)

    def _matPlot(self, A, title=None, xlabel=None, ylabel=None, cmap=None):
        plt.figure()
        v = A.shape
        xticks = range(0, v[0])
        ax = cartMeshPlot(A, xticks, xticks[::-1])
        formatPlot(ax, title=title, xlabel=xlabel, ylabel=ylabel, cmap=cmap)

    def fMatEig(self):
        """
        Computes the Fission Matrix Eigenpairs

        Returns
        -------
            self.domEigVal: float
                Dominant Eigenvalue
            self.domEigVec: np.array
                Dominant Eigenvector

        """
        eigValVec, eigVecMat = np.linalg.eig(self.fMat)
        self.eigVecMat = self.eigVecNorm(eigVecMat)
        self.domEigVal = eigValVec[0]
        self.eigValVec = eigValVec
        self.domEigVec = self.eigVecMat[:, 0]
        self.domRatio = self.eigValVec[1] / self.eigValVec[0]
        return self.domEigVal, self.domEigVec

    def eigVecNorm(self, w):
        # Flips and Normalizes the eigenvectors
        cont = 0
        z = w[:, 0]
        lunghezza = len(z)
        for x in np.nditer(z):
            if x < 0:
                cont = cont + 1
        if cont == lunghezza or cont == 0:
            w = w / np.sum(w[:, 0])
        else:
            error('The Dominant Eigenvector is not Positive')
        return w

    def eigVecPlot(self, eigNum, xdata=None, ax=None,
                   title='Neutron fission source', xlabel=None, ylabel=None,
                   cmap=None):
        """
        Plots the spatial distribution of the eigNum-th mode

        Parameters
        ----------
        eigNum: int
            Mode number (eigNum>0)
        xdata: np.array
            x axis data
        ax: object
            Axis object
        title: str
            Plot title
        xlabel: str
            x-axis label
        ylabel: str
            y-axis label
        cmap: str
            Color map

        Returns
        -------
        ax: object
            axis object
        """

        assert (isinstance(eigNum, int), 'The number must be integer')
        lunghezza = len(self.domEigVec)
        if eigNum < 1 or eigNum > lunghezza:
            error('The number must be a positive integer between 1 and {}'
                  .format(lunghezza))
        # Plot
        if xdata is None:
            xdata = range(0, len(self.domEigVec))
        plt.figure()
        ax = ax or plt.axes()
        ax.plot(xdata, self.eigVecMat[:, eigNum - 1])
        ax = formatPlot(ax, title=title, xlabel=xlabel, ylabel=ylabel,
                        cmap=cmap)
        return ax

    def eigValPlot(self, ax=None, title='Fission Matrix Spectrum',
                   xlabel=None, ylabel=None, cmap=None, grid=True):
        """
        The function plots the fission matrix spectrum on the Argand-Gauss
        plain.

        Parameters
        ----------
        ax: object
            Axis object
        title: str
            Plot title
        xlabel: str
            x-axis label
        ylabel: str
            y-axis label
        cmap: str
            color map
        grid: bool
            grid (True), no grid (False)

        Returns
        -------
        ax: object
            axis object
        """
        plt.figure()
        ax = ax or plt.axes()
        ax.plot(self.eigValVec.real, self.eigValVec.imag, 'ro')
        ax = formatPlot(ax, title=title, xlabel=xlabel, ylabel=ylabel,
                        cmap=cmap)
        plt.grid(grid)
        return ax
