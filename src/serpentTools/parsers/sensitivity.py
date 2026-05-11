"""
Class to read Sensitivity file
"""
from collections import OrderedDict
from itertools import product

from numpy import transpose, hstack, fabs
from matplotlib import pyplot
from matplotlib.pyplot import gca

from serpentTools.utils.plot import magicPlotDocDecorator, formatPlot
from serpentTools.engines import KeywordParser
from serpentTools.messages import warning, SerpentToolsException, critical
from serpentTools.utils import convertVariableName, str2vec
from serpentTools.utils.mtDecoder import decodeMts
from serpentTools.utils.zaiDecoder import decodeZai
from serpentTools.parsers.base import BaseReader


class SensitivityReader(BaseReader):
    """
    Class for reading sensitivity files

    The arrays that are stored in :attr:`sensitivities` and
    :attr:`energyIntegratedSens` are stored under converted names.
    The original names from SERPENT are of the form
    ``ADJ_PERT_KEFF_SENS`` or ``ADJ_PERT_KEFF_SENS_E_INT``,
    respectively. Since this reader stores the resulting arrays
    in unique locations, the names are converted to a succint form.
    The two arrays listed above would be stored both as ``keff``
    in :attr:`sensitivities` and :attr:`energyIntegratedSens`.
    All names are converted to ``mixedCaseNames`` to fit the
    style of the project.

    Ordered dictionaries :attr:`materials`, :attr:`zais` and
    :attr:`perts` contain keys of the names of their respective
    data, and the corresponding index, ``iSENS_ZAI_zzaaai``,
    in the sensitivity arrays. These arrays are zero-indexed,
    so the first item will have an index of zero. The data stored
    in the :attr:`sensitivities` and :attr:`energyIntegratedSens` dictionaries
    has the exact same structure as if the arrays were loaded into
    ``MATLAB``/``Octave``, but with zero-indexing.

    The matrices in :attr:`sensitivities` are ordered as they
    would be in MATLAB. The five dimensions correspond to:

    1. :attr:`materials` that were contained perturbed isotopes
    2. :attr:`zais` that were perturbed
    3. :attr:`perts` - reactions that were perturbed, e.g.
       ``'total xs'``
    4. :attr:`energies` - which energy group contained the
       perturbation. Will have one fewer dimensions than
       the number of values in :attr:`energies`, corresponding
       to the number of energy groups.
    5. [value, relative uncertainty] pairs

    The matrices in :attr:`energyIntegratedSens` will have the same
    structure, but with the :attr:`energies` dimension removed.

    .. note::

        Arrays generated using the history option ``sens opt history 1``
        are not currently stored on the reader. See feature request
        :issue:`367`

    Parameters
    ----------
    filePath : str
        Path to sensitivity file

    Attributes
    ----------
    nMat : None or int
        Number of materials
    nZai : None or int
        Number of perturbed isotopes
    nPert : None or int
        Number of perturbations
    nEne : None or int
        Number of energy groups
    nMu : None or int
        Number of perturbed materials
    materials : :class:`~collections.OrderedDict`
        Ordered dictionary of materials that have
        been perturbed.
    zais : :class:`~collections.OrderedDict`
        Ordered dictionary of nuclides that
        have been perturbed
    perts : :class:`~collections.OrderedDict`
        Ordered dictionary of reactions that
        have been perturbed, e.g `'total xs'`
    latGen : int
        Number of latent generations used to generate
        these sensitivities
    energies : None or :class:`numpy.array`
        Array of energy bounds for the sensitivities, from
        lowest to highest
    lethargyWidths : None or :class:`numpy.array`
        Array of lethargy widths of each energy group.
    sensitivities : dict
        Dictionary of names of sensitivities and their corresponding
        arrays.
    energyIntegratedSens : dict
        Dictionary of names of the sensitivities that have been integrated
        against energy, and their corresponding arrays

    """

    _RECONVERT_ATTR_MAP = {
        "nMat": ("sensNumMat", "SENS_N_MAT"),
        "nZai": ("sensNumZai", "SENS_N_ZAI"),
        "nPert": ("sensNumPert", "SENS_N_PERT"),
        "nEne": ("sensNumEne", "SENS_N_ENE"),
        "nMu": ("sensNumMu", "SENS_N_MU"),
        "latGen": ("sensLatGen", "SENS_N_LATGEN"),
        "energies": ("sensEne", "SENS_E"),
        "lethargyWidths": ("sensLethWidth", "SENS_LETHARGY_WIDTHS"),
    }
    _RECONVERT_LIST_MAP = {
        "materials": ("sensMats", "SENS_MAT_LIST"),
        "zais": ("sensZais", "SENS_ZAI_LIST"),
        "perts": ("sensPerts", "SENS_PERT_LIST"),
    }
    _RECONVERT_SENS_FMT = [
        ["sens{}", "sens{}_eneInt"],
        ["ADJ_PERT_{}_SENS", "ADJ_PERT_{}_SENS_E_INT"],
    ]

    def __init__(self, filePath):
        BaseReader.__init__(self, filePath, "sens")
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
            "materials": self.materials,
            "nuclides": self.zais,
            "reactions": self.perts,
        }
        self.energies = None
        self.lethargyWidths = None
        self.sensitivities = {}
        self.energyIntegratedSens = {}
        self.covarianceUncertainty = {}
        self.covarianceVariance = {}
        self.covarianceZaimts = []

    def _read(self):
        keys = stops = ["%"]
        throughParams = False
        zaimts = []
        with KeywordParser(self.filePath, keys, stops) as parser:
            for chunk in parser.yieldChunks():
                chunk0 = chunk[0]
                if "Information on covariance blocks" in chunk0:
                    zaimts = self._processCovarianceBlockInfoChunk(chunk)
                    continue
                if "Uncertainty from nuclear data covariances" in chunk0:
                    self._processCovarianceUncertaintyChunk(chunk, zaimts)
                    continue
                if "Variance from nuclear data covariances" in chunk0:
                    self._processCovarianceVarianceChunk(chunk, zaimts)
                if not throughParams:
                    if "Number" in chunk0:
                        self._processNumChunk(chunk)
                    elif "included" in chunk0:
                        what = chunk0.split()[1]
                        self._processIndexChunk(what, chunk)
                    elif "energy" in chunk0:
                        self._processEnergyChunk(chunk)
                    elif "latent" in chunk0:
                        split = chunk0.split()
                        self.latGen = int(split[split.index("latent") - 1])
                        throughParams = True
                    continue
                self._processSensChunk(chunk)
        if self.zais:
            old = self.zais
            self.zais = OrderedDict()
            for key, value in old.items():
                if key == "total":
                    self.zais[key] = value
                    continue
                self.zais[int(key)] = value

    def _processNumChunk(self, chunk):
        chunk = [line for line in chunk if "SENS" in line]
        for line in chunk:
            split = line.split()
            attrN = "n" + split[0].split("_")[-1].capitalize()
            if hasattr(self, attrN):
                setattr(self, attrN, int(split[-1][:-1]))
            else:
                raise SerpentToolsException(
                    "Attempted to set attribute {} from number block".format(
                        attrN
                    )
                )

    def _processIndexChunk(self, what, chunk):
        key = what.lower()
        if key not in self._indxMap:
            raise SerpentToolsException(
                "Could not find proper index map for quantity "
                "{}".format(what)
            )
        datum = self._indxMap[key]
        indx = 0
        store = False
        for line in chunk:
            if "SENS" in line:
                store = True
                continue
            if "];" in line:
                return
            if store:
                start = line.index("'") + 1 if "'" in line else 0
                stop = -1
                key = line[start:stop].replace("'", "").strip()
                if "%" in key:
                    key = key.split("% ")[1]
                datum[key] = indx
                indx += 1
        raise SerpentToolsException("Unexpected index chunk {}".format(chunk))

    def _processEnergyChunk(self, chunk):
        for line in chunk:
            if "SENS" == line[:4]:
                break
        else:
            raise SerpentToolsException(
                "Could not find SENS parameter "
                "in energy chunk {}".format(chunk[:3])
            )
        splitLine = line.split()
        varName = splitLine[0].split("_")[1:]
        varValues = str2vec(splitLine[3:-1])
        if varName[0] == "E":
            self.energies = varValues
        elif varName == ["LETHARGY", "WIDTHS"]:
            self.lethargyWidths = varValues
        else:
            warning("Unanticipated energy setting {}".format(splitLine[0]))

    def _processCovarianceChunk(self, chunk, zaimts, kind):
        if kind == "uncertainty":
            target = self.covarianceUncertainty
            key = "UNCERTAINTY"
        elif kind == "variance":
            target = self.covarianceVariance
            key = "VARIANCE"
        else:
            raise SerpentToolsException(
                "Unknown covariance chunk type {}".format(kind)
            )

        for line in chunk:
            if key in line:
                cleaned = self._cleanLine(line)
                block, values = cleaned.split("=", 1)
                response = block.strip()
                if "_COV_DATA_" in response:
                    response = response.split("_COV_DATA_", 1)[0]
                response = convertVariableName(response)
                respValues = [float(un) for un in values.split()]
                respData = target.setdefault(response, OrderedDict())
                respData["total"] = (respValues[0], respValues[1])
                if not zaimts:
                    zaimts = list(self.covarianceZaimts)
                for zaimt, pu, un in zip(
                    (str(z).strip() for z in zaimts),
                    respValues[2::2],
                    respValues[3::2],
                ):
                    respData[zaimt] = (pu, un)

    def _processCovarianceUncertaintyChunk(self, chunk, zaimts):
        return self._processCovarianceChunk(chunk, zaimts, "uncertainty")

    def _processCovarianceVarianceChunk(self, chunk, zaimts):
        return self._processCovarianceChunk(chunk, zaimts, "variance")

    def _processCovarianceBlockInfoChunk(self, chunk):
        for line in chunk:
            if "ZAIMTS" in line:
                cleaned = self._cleanLine(line)
                _, zaimtsStr = cleaned.split("=")
                block = " ".join(zaimtsStr.split())
                if not block:
                    continue
                self.covarianceZaimts.append(block)
        return self.covarianceZaimts

    def _cleanLine(self, line):
        removedChars = "[];"
        return line.translate(str.maketrans("", "", removedChars)).strip()

    def _processSensChunk(self, chunk):
        varName = None
        isEnergyIntegrated = False
        for line in chunk:
            if line == "\n" or "%" in line[:5] or "];" == line[:2]:
                continue
            if line[:3] == "ADJ":
                fullVarName = line.split()[0]
                nameProps = self._getAdjVarProps(fullVarName.split("_"))
                varName = nameProps.get("name")

                if varName is None:
                    raise ValueError(
                        "Cannot get response name from {}".format(fullVarName)
                    )

                isEnergyIntegrated = nameProps.get("energyFlag", False)
                latentGen = nameProps.get("latent")

            elif varName is not None:
                self._addSens(
                    varName, str2vec(line), isEnergyIntegrated, latentGen
                )
                varName = None

    @staticmethod
    def _getAdjVarProps(parts):
        props = {}
        nameStart = None

        for ix, word in enumerate(parts):
            if word == "PERT":
                nameStart = ix + 1
            elif word == "SENS":
                if nameStart is None:
                    raise ValueError(
                        "Cannot get response name from {}".format(parts)
                    )
                props["name"] = "_".join(parts[nameStart:ix])
            elif word == "INT":
                props["energyFlag"] = parts[ix - 1] == "E"
            elif word == "GEN":
                props["latent"] = int(parts[ix - 1])

        return props

    def _addSens(self, varName, vec, isEnergyIntegrated, latentGen):
        if latentGen is not None:
            return
        dest = (
            self.energyIntegratedSens
            if isEnergyIntegrated
            else self.sensitivities
        )
        newShape = [2, self.nPert, self.nZai, self.nMat]
        if not isEnergyIntegrated:
            newShape.insert(1, self.nEne)
        try:
            newName = convertVariableName(varName)
            dest[newName] = reshapePermuteSensMat(vec, newShape)
        except Exception as ee:
            critical(
                "The following error was raised attempting to "
                "reshape matrix {}".format(varName)
            )
            raise ee

    def _precheck(self):
        with open(self.filePath) as fobj:
            for count in range(5):
                if "SENS" == fobj.readline()[:4]:
                    return
        warning(
            "Could not find any lines starting with SENS. "
            "Is {} a sensitivity file?".format(self.filePath)
        )

    def _postcheck(self):
        if not self.sensitivities:
            raise SerpentToolsException("No sensitivity data stored on reader")
        if not self.energyIntegratedSens:
            raise SerpentToolsException(
                "No energy integrated sensitivities " "stored on reader"
            )

    @magicPlotDocDecorator
    def plot(
        self,
        resp,
        zai=None,
        pert=None,
        mat=None,
        mevscale=False,
        egrid=None,
        sigma=3,
        normalize=True,
        ax=None,
        labelFmt=None,
        title=None,
        logx=True,
        logy=False,
        loglog=False,
        xlabel=None,
        ylabel=None,
        legend=None,
        ncol=1,
        **kwargs
    ):
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
            in :attr:`sensitivities` and :attr:`energyIntegratedSens`
        zai : None or str or int or iterable
            Plot sensitivities due to these isotopes. Passing ``None``
            will plot against all isotopes.
        pert : None or str or list of strings
            Plot sensitivities due to these perturbations. Passing ``None``
            will plot against all perturbations.
        mat : None or str or list of strings
            Plot sensitivities due to these materials. Passing ``None``
            will plot against all materials.
        mevscale  : bool, optional
            Flag for plotting energy grid in MeV units. If ``True``, the energy
            axis is expressed in MeV. Default is ``False``.
        egrid  : numpy.array, optional
            User-defined energy grid boundaries displayed on the sensitivities
            as vblack, dashed vertical lines. Default is ``None``.
        {sigma}
        normalize : True
            Normalize plotted data per unit lethargy
        {ax}
        labelFmt : None or str
            Formattable string to be applied to the labels.
            The following entries will be formatted for each plot
            permutation::

                {m} - name of the material
                {z} - isotope zai
                {p} - specific perturbation
                {r} - response being plotted

        {title}
        {logx}
        {logy}
        {loglog}
        {xlabel}
        {ylabel}
        {legend}
        {ncol}
        {kwargs} :meth:`matplotlib.pyplot.Axes.errorbar`

            .. versionadded: 0.9.4

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
        * :meth:`str.format` - used for formatting labels

        """
        for subDict in {"sensitivities", "energyIntegratedSens"}:
            if resp not in getattr(self, subDict):
                raise KeyError(
                    "Response {} missing from {}".format(resp, subDict)
                )
        if "label" in kwargs:
            if labelFmt:
                raise ValueError("Passing label= and labelFmt= is not allowed")
            labelFmt = kwargs.pop("label")
        elif labelFmt is None:
            labelFmt = "mat: {m} zai: {z} pert: {p}"

        kwargs.setdefault("drawstyle", "steps-post")

        if isinstance(zai, (str, int)):
            zai = {
                zai,
            }
        zais = self._getCleanedPertOpt("zais", zai)
        perts = self._getCleanedPertOpt("perts", pert)
        mats = self._getCleanedPertOpt("materials", mat)

        ax = ax or gca()

        sigma = max(int(sigma), 0)
        resMat = self.sensitivities[resp]
        values = resMat[..., 0]
        if normalize:
            values = values.copy() / self.lethargyWidths

        errors = resMat[..., 1] * values * sigma

        energies = self.energies if mevscale else self.energies * 1e6
        for z, m, p in product(zais, mats, perts):
            iZ = self.zais[z]
            iM = self.materials[m]
            iP = self.perts[p]
            yVals = values[iM, iZ, iP]
            yVals = hstack((yVals, yVals[-1]))
            yErrs = errors[iM, iZ, iP]
            yErrs = fabs(hstack((yErrs, yErrs[-1])))
            label = labelFmt.format(r=resp, z=z, m=m, p=p)
            ax.errorbar(energies, yVals, yErrs, label=label, **kwargs)

        if egrid is not None:
            for group in egrid:
                ax.axvline(group, color="k", linestyle="dashed")

        if xlabel is None:
            xlabel = "Energy [MeV]" if mevscale else "Energy [eV]"

        if ylabel is None:
            parts = ["Sensitivity"]
            if normalize:
                parts.append("per unit lethargy")
            if sigma:
                parts.append(r"$\pm{}\sigma$".format(sigma))
            ylabel = " ".join(parts)

        ax = formatPlot(
            ax,
            loglog=loglog,
            logx=logx,
            logy=logy,
            legendcols=ncol,
            legend=legend,
            xlabel=xlabel,
            ylabel=ylabel,
            title=title,
        )
        return ax

    def _gather_matlab(self, reconvert):
        """Gather data for matlab conversion"""
        out = {}
        reconvNameIx = 1 if reconvert else 0
        # get basic indexing
        for attr, reconvNameTpl in self._RECONVERT_ATTR_MAP.items():
            out[reconvNameTpl[reconvNameIx]] = getattr(self, attr)
        # ordered dictionary -> vectors
        for attr, reconvNameTpl in self._RECONVERT_LIST_MAP.items():
            out[reconvNameTpl[reconvNameIx]] = list(getattr(self, attr).keys())
        sensFmt, eneSensFmt = self._RECONVERT_SENS_FMT[reconvNameIx]
        for key, sensMat in self.sensitivities.items():
            out[sensFmt.format(key)] = sensMat
            out[eneSensFmt.format(key)] = self.energyIntegratedSens[key]
        return out

    def _getCleanedPertOpt(self, attrName, value):
        """Return a list of all or some of the requested perturbations."""
        opts = getattr(self, attrName, None)
        assert isinstance(opts, OrderedDict)
        if value is None:
            return list(opts)
        elif isinstance(value, str):
            value = [value]
        available = set(opts)
        if available.issuperset(value):
            return value
        missing = available.intersection(value).symmetric_difference(value)
        raise KeyError(
            "Could not find the following {} perturbations: "
            "{}".format(attrName, missing)
        )

    @staticmethod
    def _splitCovarianceZaimt(zaimt):
        zaimt = zaimt.strip()
        if len(zaimt) <= 5:
            return zaimt, zaimt
        return zaimt[:-5], zaimt[-5:]

    @staticmethod
    def _cleanCovarianceResp(resp, available):
        if resp is None:
            return list(available)
        if isinstance(resp, str):
            resp = [resp]
        cleaned = [
            convertVariableName(str(item).strip()) for item in resp
        ]
        available = set(available)
        if available.issuperset(cleaned):
            return cleaned
        missing = available.intersection(cleaned).symmetric_difference(
            cleaned
        )
        raise KeyError(
            "Could not find the following responses: {}".format(missing)
        )

    def _getCovarianceResponseMap(self, data):
        if not isinstance(data, str):
            raise SerpentToolsException(
                "Expected covariance data selector string."
            )
        dataKey = data.strip().lower()
        if dataKey == "uncertainty":
            return dataKey, self.covarianceUncertainty
        if dataKey == "variance":
            return dataKey, self.covarianceVariance
        raise SerpentToolsException(
            "Unknown covariance data selection {}. Expected "
            "'uncertainty' or 'variance'.".format(data)
        )

    def _getCovarianceResponseItems(self, resp, responseMap):
        return [
            (name, responseMap[name])
            for name in self._cleanCovarianceResp(resp, responseMap.keys())
        ]

    @staticmethod
    def _getCovarianceLabelFmt(labelFmt, responseItems):
        if labelFmt is not None:
            return labelFmt
        labelFmt = "{z1} {m1}, {z2} {m2}"
        if len(responseItems) > 1:
            labelFmt = "{r}: " + labelFmt
        return labelFmt

    @staticmethod
    def _cleanCovarianceFilter(value, cleanMt=False):
        if isinstance(value, (str, int)):
            value = [value]
        if value is None:
            return None
        if cleanMt:
            return {
                str(item).strip().lstrip("0") or "0"
                for item in value
            }
        return {str(item).strip() for item in value}

    @staticmethod
    def _getCovarianceAxes(ax, figsize, dpi):
        if ax is None:
            if figsize is not None or dpi is not None:
                _, ax = pyplot.subplots(figsize=figsize, dpi=dpi)
            else:
                ax = gca()
        else:
            if figsize is not None:
                ax.figure.set_size_inches(figsize)
            if dpi is not None:
                ax.figure.set_dpi(dpi)
        return ax

    @staticmethod
    def _covarianceEntryMatches(parsed, zaiFilter, mtFilter):
        if not zaiFilter and not mtFilter:
            return True
        for zaiEntry, mtEntry, _ in parsed:
            if zaiFilter and zaiEntry not in zaiFilter:
                continue
            if mtFilter and mtEntry not in mtFilter:
                continue
            return True
        return False

    def _formatCovarianceLabel(self, labelFmt, responseName, key, parsed):
        zaiLabels = [
            decodeZai(zaiEntry) for zaiEntry, _, _ in parsed
        ]
        entryLabels = [
            "{}\n{}".format(zaiLabel, mtLabel)
            for zaiLabel, (_, _, mtLabel) in zip(zaiLabels, parsed)
        ]
        if len(entryLabels) == 1:
            entryLabels = [entryLabels[0], entryLabels[0]]
            parsed = [parsed[0], parsed[0]]
            zaiLabels = [zaiLabels[0], zaiLabels[0]]

        return labelFmt.format(
            r=responseName or "",
            zaimt=key,
            labels=entryLabels,
            zais=[z for z, _, _ in parsed],
            zaiLabels=zaiLabels,
            mts=[m for _, m, _ in parsed],
            mtLabels=[r for _, _, r in parsed],
            z1=zaiLabels[0],
            m1=parsed[0][2],
            z2=zaiLabels[1],
            m2=parsed[1][2],
            z1Raw=parsed[0][0],
            z2Raw=parsed[1][0],
        )

    def _getCovariancePlotData(
        self, responseItems, zaiFilter, mtFilter, labelFmt, sigma
    ):
        values = []
        errors = []
        labels = []

        for responseName, responseData in responseItems:
            for key, (value, relUnc) in responseData.items():
                if key == "total":
                    if zaiFilter or mtFilter:
                        continue
                    respPrefix = (
                        "{} ".format(responseName) if responseName else ""
                    )
                    label = "{}total".format(respPrefix).strip()
                else:
                    parsed = []
                    for entry in key.split():
                        zaiEntry, mtEntry = self._splitCovarianceZaimt(entry)
                        mtClean = mtEntry.lstrip("0") or "0"
                        parsed.append(
                            (zaiEntry, mtClean, decodeMts(entry))
                        )

                    if not self._covarianceEntryMatches(
                        parsed, zaiFilter, mtFilter
                    ):
                        continue

                    label = self._formatCovarianceLabel(
                        labelFmt, responseName, key, parsed
                    )

                values.append(value)
                errors.append(
                    fabs(value) * fabs(relUnc) * sigma if sigma else 0.0
                )
                labels.append(label)

        return values, errors, labels

    @staticmethod
    def _drawCovarianceBars(ax, values, errors, labels, fixedAxis):
        axisVals = list(range(len(values)))
        if fixedAxis:
            ax.barh(axisVals, values, xerr=errors)
            ax.set_yticks(axisVals)
            ax.set_yticklabels(labels)
            ax.tick_params(axis="y", pad=10)
        else:
            ax.bar(axisVals, values, yerr=errors)
            ax.set_xticks(axisVals)
            ax.set_xticklabels(labels, rotation=60, ha="right")
            ax.tick_params(axis="x", pad=10)

    @staticmethod
    def _getCovarianceValueLabel(dataKey):
        if dataKey == "variance":
            return "Variance"
        if dataKey == "uncertainty":
            return "Propagated Uncertainty"
        return "Covariance Data"

    def _formatCovarianceAxes(
        self, ax, dataKey, fixedAxis, resp, title, logy,
        xlabel, ylabel, legend, ncol
    ):
        valueLabel = self._getCovarianceValueLabel(dataKey)

        if fixedAxis:
            if xlabel is None:
                xlabel = valueLabel
            if ylabel is None:
                ylabel = "ZAIMT"
        else:
            if xlabel is None:
                xlabel = "ZAIMT"
            if ylabel is None:
                ylabel = valueLabel

        if title is None and resp is None:
            title = f"{ylabel} in response: All "
        else:
            title = f"{ylabel} in response: {resp}"

        return formatPlot(
            ax,
            loglog=False,
            logx=logy if fixedAxis else False,
            logy=False if fixedAxis else logy,
            legendcols=ncol,
            legend=legend,
            xlabel=xlabel,
            ylabel=ylabel,
            title=title,
        )

    @magicPlotDocDecorator
    def plotCovarianceData(
        self,
        data="uncertainty",
        resp=None,
        zai=None,
        mt=None,
        sigma=3,
        ax=None,
        figsize=None,
        dpi=None,
        labelFmt=None,
        fixedAxis=True,
        title=None,
        logy=False,
        xlabel=None,
        ylabel=None,
        legend=None,
        ncol=1,
    ):
        """
        Plots covariance uncertainty and variance data.

        Parameters
        ----------
        data : {"uncertainty", "variance"}
            Selects the covariance dataset to use.
        resp : None or str or iterable
            Responses to include. Defaults to all responses in the
            selected covariance dataset.
        zai : None or str or int or iterable
            Plot covariance data for these ZAIs. Passing ``None``
            will plot all ZAIs.
        mt : None or str or int or iterable
            Plot covariance data for these MTs. Passing ``None``
            will plot all MTs.
        {sigma}
        {ax}
        figsize : tuple, optional
            Figure size in inches (width, height) if ``ax`` is not provided.
        dpi : int, optional
            Dots per inch for the figure if ``ax`` is not provided.
        labelFmt : None or str
            Formattable string to be applied to the labels. The following
            entries will be formatted for each bar::

                {r} - response name
                {z1} - ZAI label for entry 1
                {m1} - MT label for entry 1
                {z2} - ZAI label for entry 2
                {m2} - MT label for entry 2
                {z1Raw} - raw ZAI for entry 1
                {z2Raw} - raw ZAI for entry 2
                {zais} - raw ZAI list
                {zaiLabels} - decoded ZAI labels list
                {mts} - MT list
                {mtLabels} - MT labels list
                {labels} - preformatted "ZAI MT" labels list
                {zaimt} - raw ZAIMT block string

        fixedAxis : bool, optional
            If ``True``, plot horizontal bars with labels on the y-axis.
        {title}
        {logy}
        {xlabel}
        {ylabel}
        {legend}
        {ncol}
        """
        dataKey, responseMap = self._getCovarianceResponseMap(data)
        responseItems = self._getCovarianceResponseItems(resp, responseMap)
        labelFmt = self._getCovarianceLabelFmt(labelFmt, responseItems)
        zaiFilter = self._cleanCovarianceFilter(zai)
        mtFilter = self._cleanCovarianceFilter(mt, cleanMt=True)
        ax = self._getCovarianceAxes(ax, figsize, dpi)
        sigma = max(int(sigma), 0)

        values, errors, labels = self._getCovariancePlotData(
            responseItems, zaiFilter, mtFilter, labelFmt, sigma
        )
        if not labels:
            raise SerpentToolsException(
                "No covariance data matched the provided filters."
            )

        self._drawCovarianceBars(
            ax, values, errors if sigma else None, labels, fixedAxis
        )
        return self._formatCovarianceAxes(
            ax, dataKey, fixedAxis, resp, title, logy,
            xlabel, ylabel, legend, ncol
        )


def reshapePermuteSensMat(vec, newShape):
    """
    Return an array that has been reshaped and permuted like the sens file.
    """
    reshaped = vec.reshape(newShape, order="F")
    newAx = list(reversed(range(len(newShape))))
    return transpose(reshaped, newAx)
