"""
Class to read Sensitivity file
"""
from collections import OrderedDict
from itertools import product

from six import iteritems
from numpy import transpose, hstack
from matplotlib.pyplot import axes

from serpentTools.utils.plot import magicPlotDocDecorator, formatPlot
from serpentTools.engines import KeywordParser
from serpentTools.messages import warning, SerpentToolsException, critical
from serpentTools.utils import convertVariableName, str2vec
from serpentTools.parsers.base import BaseReader


class SensitivityReader(BaseReader):
    """
    Class for reading sensitivity files

    The arrays that are stored in ``sensitivities`` and
    ``energyIntegratedSens`` are stored under converted names.
    The original names from SERPENT are of the form
    ``ADJ_PERT_KEFF_SENS`` or ``ADJ_PERT_KEFF_SENS_E_INT``,
    respectively. Since this reader stores the resulting arrays
    in unique locations, the names are converted to a succint form.
    The two arrays listed above would be stored both as ``keff``
    in ``sensitivities`` and ``energyIntegratedSens``.
    All names are converted to ``mixedCaseNames`` to fit the
    style of the project.

    Ordered dictionaries ``materials``, ``zais``, and
    ``perts`` contain keys of the names of their respective
    data, and the corresponding index, ``iSENS_ZAI_zzaaai``,
    in the sensitivity arrays. These arrays are zero-indexed,
    so the first item will have an index of zero. The data stored
    in the ``sensitivities`` and ``energyIntegratedSens`` dictionaries
    has the exact same structure as if the arrays were loaded into
    ``MATLAB``/``Octave``, but with zero-indexing.

    Parameters
    ----------
    filePath: str
        Path to sensitivity file

    Attributes
    ----------
    nMat: None or int
        Number of materials
    nZai: None or int
        Number of perturbed isotopes
    nPert: None or int
        Number of perturbations
    nEne: None or int
        Number of energy groups
    nMu: None or int
        Number of perturbed materials
    materials: :py:class:`~collections.OrderedDict`
        Ordered dictionary of materials that have
        been perturbed.
    zais: :py:class:`~collections.OrderedDict`
        Ordered dictionary of nuclides that
        have been perturbed
    perts: :py:class:`~collections.OrderedDict`
        Ordered dictionary of reactions that
        have been perturbed, e.g `'total xs'`
    latGen: int
        Number of latent generations used to generate
        these sensitivities
    energies: None or :py:class:`numpy.array`
        Array of energy bounds for the sensitivities, from
        lowest to highest
    lethargyWidths: None or :py:class:`numpy.array`
        Array of lethargy widths of each energy group.
    sensitivities: dict
        Dictionary of names of sensitivities and their corresponding
        arrays.
    energyIntegratedSens: dict
        Dictionary of names of the sensitivities that have been integrated
        against energy, and their corresponding arrays
    """

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, 'sens')
        self.nMat = None
        self.nZai = None
        self.nPert = None
        self.nEne = None
        self.nMu = None
        self.materials = OrderedDict()
        self.zais = OrderedDict()
        self.perts = OrderedDict()
        self.latGen = None
        self._indxMap = {
            'materials': self.materials, 'nuclides': self.zais,
            'reactions': self.perts}
        self.energies = None
        self.lethargyWidths = None
        self.sensitivities = {}
        self.energyIntegratedSens = {}

    def _read(self):
        keys = stops = ['%']
        throughParams = False
        with KeywordParser(self.filePath, keys, stops) as parser:
            for chunk in parser.yieldChunks():
                if not throughParams:
                    chunk0 = chunk[0]
                    if 'Number' in chunk0:
                        self.__processNumChunk(chunk)
                    elif 'included' in chunk0:
                        what = chunk0.split()[1]
                        self.__processIndexChunk(what, chunk)
                    elif 'energy' in chunk0:
                        self.__processEnergyChunk(chunk)
                    elif 'latent' in chunk0:
                        split = chunk0.split()
                        self.latGen = int(split[split.index('latent') - 1])
                        throughParams = True
                    continue
                self.__processSensChunk(chunk)
        if self.zais:
            old = self.zais
            self.zais = OrderedDict()
            for key, value in iteritems(old):
                if key == 'total':
                    self.zais[key] = value
                    continue
                self.zais[int(key)] = value

    def __processNumChunk(self, chunk):
        chunk = [line for line in chunk if 'SENS' in line]
        for line in chunk:
            split = line.split()
            attrN = 'n' + split[0].split('_')[-1].capitalize()
            if hasattr(self, attrN):
                setattr(self, attrN, int(split[-1][:-1]))
            else:
                raise SerpentToolsException(
                    'Attempted to set attribute {} from number block'.format(
                        attrN))

    def __processIndexChunk(self, what, chunk):
        key = what.lower()
        if key not in self._indxMap:
            raise SerpentToolsException(
                'Could not find proper index map for quantity '
                '{}'.format(what)
            )
        datum = self._indxMap[key]
        indx = 0
        store = False
        for line in chunk:
            if 'SENS' in line:
                store = True
                continue
            if '];' in line:
                return
            if store:
                start = line.index('\'') + 1 if '\'' in line else 0
                stop = -1
                key = line[start:stop].replace('\'', '').strip()
                if '%' in key:
                    key = key.split('% ')[1]
                datum[key] = indx
                indx += 1
        raise SerpentToolsException(
            "Unexpected index chunk {}".format(chunk))

    def __processEnergyChunk(self, chunk):
        for line in chunk:
            if 'SENS' == line[:4]:
                break
        else:
            raise SerpentToolsException("Could not find SENS parameter "
                                        "in energy chunk {}".format(chunk[:3]))
        splitLine = line.split()
        varName = splitLine[0].split('_')[1:]
        varValues = str2vec(splitLine[3:-1])
        if varName[0] == 'E':
            self.energies = varValues
        elif varName == ['LETHARGY', 'WIDTHS']:
            self.lethargyWidths = varValues
        else:
            warning("Unanticipated energy setting {}"
                    .format(splitLine[0]))

    def __processSensChunk(self, chunk):
        varName = None
        isEnergyIntegrated = False
        varName = None
        for line in chunk:
            if line == '\n' or '%' in line[:5] or '];' == line[:2]:
                continue
            if line[:3] == 'ADJ':
                fullVarName = line.split()[0]
                split = fullVarName.split('_')
                pertIndx = split.index('PERT')
                sensIndx = split.index('SENS')
                varName = '_'.join(split[pertIndx + 1: sensIndx])
                isEnergyIntegrated = split[-2:] == ['E', 'INT']
            elif varName is not None:
                self.__addSens(varName, str2vec(line), isEnergyIntegrated)
                varName = None

    def __addSens(self, varName, vec, isEnergyIntegrated):
        dest = (self.energyIntegratedSens if isEnergyIntegrated
                else self.sensitivities)
        newShape = [2, self.nPert, self.nZai, self.nMat]
        if not isEnergyIntegrated:
            newShape.insert(1, self.nEne)
        try:
            newName = convertVariableName(varName)
            dest[newName] = reshapePermuteSensMat(vec, newShape)
        except Exception as ee:
            critical("The following error was raised attempting to "
                     "reshape matrix {}".format(varName))
            raise ee

    def _precheck(self):
        with open(self.filePath) as fobj:
            for count in range(5):
                if 'SENS' == fobj.readline()[:4]:
                    return
        warning("Could not find any lines starting with SENS. "
                "Is {} a sensitivity file?".format(self.filePath))

    def _postcheck(self):
        if not self.sensitivities:
            raise SerpentToolsException("No sensitivity data stored on reader")
        if not self.energyIntegratedSens:
            raise SerpentToolsException("No energy integrated sensitivities "
                                        "stored on reader")

    @magicPlotDocDecorator
    def plot(self, resp, zai=None, pert=None, mat=None, sigma=3,
             normalize=True, ax=None, labelFmt=None,
             title=None, logx=True, logy=False, loglog=False, xlabel=None,
             ylabel=None, legend=True, ncol=1):
        """
        Plot sensitivities due to some or all perturbations.

        .. note::

            Without passing ``zai``, ``pert``, or ``mat``
            arguments, this method will plot all permutations of
            sensitivities for a given response.

        Parameters
        ----------
        resp: str
            Name of the specific response to be examined. Must be a key
            in ``sensitivities`` and ``energyIntegratedSens``
        zai: None or str or int or iterable
            Plot sensitivities due to these isotopes. Passing ``None``
            will plot against all isotopes.
        pert: None or str or list of strings
            Plot sensitivities due to these perturbations. Passing ``None``
            will plot against all perturbations.
        mat: None or str or list of strings
            Plot sensitivities due to these materials. Passing ``None``
            will plot against all materials.
        {sigma}
        normalize: True
            Normalize plotted data per unit lethargy
        {ax}
        labelFmt: None or str
            Formattable string to be applied to the labels.
            The following entries will be formatted for each plot
            permuation::

                {m} - name of the material
                {z} - isotope zai
                {p} - specific perturbation
                {r} - response being plotted

        {logx}
        {logy}
        {loglog}
        {xlabel}
        {ylabel}
        {legend}
        {ncol}

        Returns
        -------
        {rax}

        Raises
        ------
        KeyError
            If response or any passed perturbation settings are not
            present on the object

        See Also
        --------
        * :py:meth:`str.format` - used for formatting labels

        """
        for subDict in {'sensitivities', 'energyIntegratedSens'}:
            if resp not in getattr(self, subDict):
                raise KeyError("Response {} missing from {}"
                               .format(resp, subDict))
        labelFmt = labelFmt or "mat: {m} zai: {z} pert: {p}"
        if isinstance(zai, (str, int)):
            zai = {zai, }
        zais = self._getCleanedPertOpt('zais', zai)
        perts = self._getCleanedPertOpt('perts', pert)
        mats = self._getCleanedPertOpt('materials', mat)

        ax = ax or axes()

        sigma = max(int(sigma), 0)
        resMat = self.sensitivities[resp]
        values = resMat[..., 0]
        if normalize:
            values = values.copy() / self.lethargyWidths

        errors = resMat[..., 1] * values * sigma

        energies = self.energies * 1E6
        for z, m, p in product(zais, mats, perts):
            iZ = self.zais[z]
            iM = self.materials[m]
            iP = self.perts[p]
            yVals = values[iM, iZ, iP]
            yVals = hstack((yVals, yVals[-1]))
            yErrs = errors[iM, iZ, iP]
            yErrs = hstack((yErrs, yErrs[-1]))
            label = labelFmt.format(r=resp, z=z, m=m, p=p)
            ax.errorbar(energies, yVals, yErrs, label=label,
                        drawstyle='steps-post')

        xlabel = 'Energy [eV]' if xlabel is None else xlabel
        ylabel = ylabel if ylabel is not None else (
            'Sensitivity {} {}'.format(
                'per unit lethargy' if normalize else '',
                r'$\pm{}\sigma$'.format(sigma) if sigma else ''))
        ax = formatPlot(ax, loglog=loglog, logx=logx, logy=logy, ncol=ncol,
                        legend=legend, xlabel=xlabel, ylabel=ylabel.strip())
        return ax

    def _getCleanedPertOpt(self, key, value):
        """Return a set of all or some of the requested perturbations."""
        assert hasattr(self, key), key
        opts = getattr(self, key).keys()
        if value is None:
            return list(opts)
        requested = set([value, ]) if isinstance(value, str) else set(value)
        missing = {str(xx) for xx in requested.difference(set(opts))}
        if missing:
            raise KeyError("Could not find the following perturbations: "
                           "{}".format(', '.join(missing)))
        return requested


def reshapePermuteSensMat(vec, newShape):
    """
    Return an array that has been reshaped and permuted like the sens file.
    """
    reshaped = vec.reshape(newShape, order='F')
    newAx = list(reversed(range(len(newShape))))
    return transpose(reshaped, newAx)
