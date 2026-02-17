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
from serpentTools.utils.mt_decoder import MTS_MAP, decode_mts
from serpentTools.utils.zai_decoder import decodeZai
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
                resp_values = [float(un) for un in values.split()]
                resp_data = target.setdefault(response, OrderedDict())
                resp_data["total"] = (resp_values[0], resp_values[1])
                if not zaimts:
                    zaimts = list(self.covarianceZaimts)
                for zaimt, pu, un in zip(
                    (str(z).strip() for z in zaimts),
                    resp_values[2::2],
                    resp_values[3::2],
                ):
                    resp_data[zaimt] = (pu, un)

    def _processCovarianceUncertaintyChunk(self, chunk, zaimts):
        return self._processCovarianceChunk(chunk, zaimts, "uncertainty")

    def _processCovarianceVarianceChunk(self, chunk, zaimts):
        return self._processCovarianceChunk(chunk, zaimts, "variance")

    def _processCovarianceBlockInfoChunk(self, chunk):
        for line in chunk:
            if "ZAIMTS" in line:
                cleaned = self._cleanLine(line)
                _, zaimts_str = cleaned.split("=")
                block = " ".join(zaimts_str.split())
                if not block:
                    continue
                self.covarianceZaimts.append(block)
        return self.covarianceZaimts

    def _cleanLine(self, line):
        removed_chars = "[];"
        return line.translate(str.maketrans("", "", removed_chars)).strip()

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
        fixed_axis=True,
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

        fixed_axis : bool, optional
            If ``True``, plot horizontal bars with labels on the y-axis.
        {title}
        {logy}
        {xlabel}
        {ylabel}
        {legend}
        {ncol}
        """

        def _split_zaimt(zaimt):
            zaimt = zaimt.strip()
            if len(zaimt) <= 5:
                return zaimt, zaimt
            return zaimt[:-5], zaimt[-5:]

        def _clean_resp(resp, available):
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

        if not isinstance(data, str):
            raise SerpentToolsException(
                "Expected covariance data selector string."
            )
        data_key = data.strip().lower()
        if data_key == "uncertainty":
            response_map = self.covarianceUncertainty
        elif data_key == "variance":
            response_map = self.covarianceVariance
        else:
            raise SerpentToolsException(
                "Unknown covariance data selection {}. Expected "
                "'uncertainty' or 'variance'.".format(data)
            )
        response_items = [
            (name, response_map[name])
            for name in _clean_resp(resp, response_map.keys())
        ]

        if labelFmt is None:
            labelFmt = "{z1} {m1}, {z2} {m2}"
            if len(response_items) > 1:
                labelFmt = "{r}: " + labelFmt

        if isinstance(zai, (str, int)):
            zai = [zai]
        if isinstance(mt, (str, int)):
            mt = [mt]

        zai_filter = None
        if zai is not None:
            zai_filter = {str(item).strip() for item in zai}

        mt_filter = None
        if mt is not None:
            mt_filter = {str(item).strip().lstrip("0") or "0" for item in mt}

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
        sigma = max(int(sigma), 0)

        values = []
        errors = []
        labels = []

        for response_name, response_data in response_items:
            for key, (value, rel_unc) in response_data.items():
                if key == "total":
                    if zai_filter or mt_filter:
                        continue
                    resp_prefix = "{} ".format(response_name) if response_name else ""
                    label = "{}total".format(resp_prefix).strip()
                else:
                    entries = key.split()
                    parsed = []
                    for entry in entries:
                        zai_entry, mt_entry = _split_zaimt(entry)
                        mt_clean = mt_entry.lstrip("0") or "0"
                        parsed.append(
                            (zai_entry, mt_clean, decode_mts(entry))
                        )

                    if zai_filter or mt_filter:
                        for zai_entry, mt_entry, _ in parsed:
                            if zai_filter and zai_entry not in zai_filter:
                                continue
                            if mt_filter and mt_entry not in mt_filter:
                                continue
                            break
                        else:
                            continue

                    zai_labels = [
                        decodeZai(zai_entry) for zai_entry, _, _ in parsed
                    ]
                    entry_labels = [
                        "{}\n{}".format(zai_label, mt_label)
                        for zai_label, (_, _, mt_label) in zip(
                            zai_labels, parsed
                        )
                    ]
                    if len(entry_labels) == 1:
                        entry_labels = [entry_labels[0], entry_labels[0]]
                        parsed = [parsed[0], parsed[0]]
                        zai_labels = [zai_labels[0], zai_labels[0]]

                    label = labelFmt.format(
                        r=response_name or "",
                        zaimt=key,
                        labels=entry_labels,
                        zais=[z for z, _, _ in parsed],
                        zaiLabels=zai_labels,
                        mts=[m for _, m, _ in parsed],
                        mtLabels=[r for _, _, r in parsed],
                        z1=zai_labels[0],
                        m1=parsed[0][2],
                        z2=zai_labels[1],
                        m2=parsed[1][2],
                        z1Raw=parsed[0][0],
                        z2Raw=parsed[1][0],
                    )

                values.append(value)
                errors.append(
                    fabs(value) * fabs(rel_unc) * sigma if sigma else 0.0
                )
                labels.append(label)

        if not labels:
            raise SerpentToolsException(
                "No covariance data matched the provided filters."
            )

        axis_vals = list(range(len(values)))
        err_vals = errors if sigma else None
        if fixed_axis:
            ax.barh(axis_vals, values, xerr=err_vals)
            ax.set_yticks(axis_vals)
            ax.set_yticklabels(labels)
            ax.tick_params(axis="y", pad=10)
        else:
            ax.bar(axis_vals, values, yerr=err_vals)
            ax.set_xticks(axis_vals)
            ax.set_xticklabels(labels, rotation=60, ha="right")
            ax.tick_params(axis="x", pad=10)

        if data_key == "variance":
            value_label = "Variance"
        elif data_key == "uncertainty":
            value_label = "Propagated Uncertainty"
        else:
            value_label = "Covariance Data"

        if fixed_axis:
            if xlabel is None:
                xlabel = value_label
            if ylabel is None:
                ylabel = "ZAIMT"
        else:
            if xlabel is None:
                xlabel = "ZAIMT"
            if ylabel is None:
                ylabel = value_label

        if title is None and resp is None:
            title = f"{ylabel} in response: All "
        else:
            title = f"{ylabel} in response: {resp}"

        ax = formatPlot(
            ax,
            loglog=False,
            logx=logy if fixed_axis else False,
            logy=False if fixed_axis else logy,
            legendcols=ncol,
            legend=legend,
            xlabel=xlabel,
            ylabel=ylabel,
            title=title,
        )
        return ax


def reshapePermuteSensMat(vec, newShape):
    """
    Return an array that has been reshaped and permuted like the sens file.
    """
    reshaped = vec.reshape(newShape, order="F")
    newAx = list(reversed(range(len(newShape))))
    return transpose(reshaped, newAx)
