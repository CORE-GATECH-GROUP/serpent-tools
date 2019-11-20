"""Parser responsible for reading the ``*dep.m`` files"""
import re
from warnings import warn

from matplotlib import pyplot

from serpentTools.utils import (
    magicPlotDocDecorator, formatPlot, DEPLETION_PLOT_LABELS,
    convertVariableName, str2vec,
)
from ._collections import DEPLETION_VARIABLES
from serpentTools.engines import KeywordParser
from serpentTools.parsers.base import MaterialReader
from serpentTools.objects.materials import DepletedMaterial
from serpentTools.utils.core import deconvertVariableName
from serpentTools.messages import (
    warning, debug, error, SerpentToolsException, deprecated,
)
from serpentTools.utils import (
    getKeyMatchingShapes,
    logDirectCompare,
    compareDocDecorator,
    DEF_COMP_LOWER,
    DEF_COMP_UPPER,
    DEF_COMP_SIGMA,
)
from serpentTools.io import MatlabConverter

METADATA_KEYS = {'ZAI', 'NAMES', 'BU', 'DAYS'}


class DepPlotMixin(object):

    @magicPlotDocDecorator
    def plot(self, xUnits, yUnits=None, timePoints=None, names=None, zai=None,
             materials=None, ax=None, legend=None, logx=False, logy=False,
             loglog=False, labelFmt=None, xlabel=None, ylabel=None, ncol=1,
             **kwargs):
        """
        Plot properties for all materials in this file together.

        Parameters
        ----------
        xUnits: str
            If ``xUnits`` is given and ``yUnits`` is ``None``, then
            the plotted data will be ``xUnits`` against ``'days'``
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'ingTox'``
        timePoints: list or None
            If given, select the time points according to those
            specified here. Otherwise, select all points

            .. deprecated:: 0.7.0
               Will plot against all time points

        names: str or list or None
            If given, plot  values corresponding to these isotope
            names. Otherwise, plot values for all isotopes.
        zai: int or list or None
            If given, plot values corresponding to these
            isotope ``ZZAAAI`` values. Otherwise, plot for all isotopes

            .. versionadded:: 0.5.1

        materials: None or list
            Selection of materials from ``self.materials`` to plot.
            If None, plot all materials, potentially including ``tot``
        {ax}
        {legend}
        {xlabel} Otherwise, use ``xUnits``
        {ylabel} Otherwise, use ``yUnits``
        {logx}
        {logy}
        {loglog}
        {matLabelFmt}
        {ncol}
        {kwargs} :py:func:`matplotlib.pyplot.plot`

        Returns
        -------
        {rax}

        See Also
        --------
        * :py:func:`~serpentTools.objects.materials.DepletedMaterial.getValues`
        * :py:func:`matplotlib.pyplot.plot`
        * :py:meth:`str.format` - used for formatting labels
        * :py:func:`~serpentTools.objects.materials.DepletedMaterial.plot`

        Raises
        ------
        KeyError
            If x axis units are not ``'days'`` nor ``'burnup'``
        SerpentToolsException
            If the materials dictionary does not contain any items
        """
        if yUnits is None:
            yUnits = xUnits
            xUnits = 'days'

        if not self.materials:
            raise SerpentToolsException("Material dictionary is empty")

        if xUnits not in ('days', 'burnup'):
            raise KeyError("Plot method only uses x-axis data from <days> and "
                           "<burnup>, not {}".format(xUnits))
        missing = set()
        ax = ax or pyplot.gca()
        materials = materials or self.materials.keys()
        labelFmt = labelFmt or '{mat} {iso}'
        for mat in materials:
            if mat not in self.materials:
                missing.add(mat)
                continue

            ax = self.materials[mat].plot(
                xUnits, yUnits, timePoints, names,
                zai, ax, legend=False, xlabel=xlabel, ylabel=ylabel,
                logx=False, logy=False, loglog=False, labelFmt=labelFmt,
                **kwargs)
        if missing:
            warning("The following materials were not found in materials "
                    "dictionary: {}".format(', '.join(missing)))
        formatPlot(ax, legend=legend, ncol=ncol, logx=logx, logy=logy,
                   loglog=loglog,
                   xlabel=xlabel or DEPLETION_PLOT_LABELS[xUnits],
                   ylabel=ylabel or DEPLETION_PLOT_LABELS[yUnits],
                   )

        return ax


class DepletionReader(DepPlotMixin, MaterialReader):
    """
    Parser responsible for reading and working with depletion files.

    Parameters
    ----------
    filePath: str
        path to the depletion file

    Attributes
    ----------
    {attrs:s}
    settings: dict
        names and values of the settings used to control operations
        of this reader
    """
    docAttrs = """materials: dict
        Dictionary with material names as keys and the corresponding
        :py:class:`~serpentTools.objects.materials.DepletedMaterial` class
        for that material as values
    metadata: dict
        Dictionary with file-wide data names as keys and the
        corresponding data, e.g. ``'zai'``: [list of zai numbers]"""
    __doc__ = __doc__.format(attrs=docAttrs)

    def __init__(self, filePath):
        MaterialReader.__init__(self, filePath, 'depletion')
        patterns = self.settings['materials'] or ['.*']
        # match all materials if nothing given
        self._matPatterns = [re.compile(mat) for mat in patterns]
        DepPlotMixin.__init__(self)

    def __getitem__(self, name):
        """Retrieve a material from :attr:`materials`."""
        return self.materials[name]

    def _read(self):
        """Read through the depletion file and store requested data."""
        keys = ['MAT', 'TOT'] if self.settings['processTotal'] else ['MAT']
        keys.extend(self.settings['metadataKeys'])
        separators = ['\n', '];', '\r\n']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                mvar = getMatlabVarName(chunk)
                if mvar[:3] in ['MAT', 'TOT']:
                    name, variable = getMaterialNameAndVariable(mvar)
                    self._checkAddData(chunk, name, variable)
                    continue
                self._addMetadata(chunk)
        if 'days' in self.metadata:
            for mKey in self.materials:
                self.materials[mKey].days = self.metadata['days']

    def _addMetadata(self, chunk):
        for varName in METADATA_KEYS:
            if varName not in chunk[0]:
                continue
            if varName in ['ZAI', 'NAMES']:
                cleaned = [line.strip() for line in chunk[1:]]
                if varName == 'NAMES':
                    values = [item[1:item.find(" ")] for item in cleaned]
                else:
                    values = str2vec(cleaned, int, list)
            else:
                line = self._cleanSingleLine(chunk)
                values = str2vec(line)
            self.metadata[convertVariableName(varName)] = values
            return
        warning("Unsure about how to process metadata chunk {}"
                .format(chunk[0]))

    @staticmethod
    def _cleanSingleLine(chunk):
        return chunk[0][chunk[0].index('[') + 1:chunk[0].index(']')]

    def _checkAddData(self, chunk, name, variable):
        if name == 'total':
            if not self.settings['processTotal']:
                return
            return self._processChunk(chunk, name, variable)
        for pattern in self._matPatterns:
            if pattern.match(name):
                return self._processChunk(chunk, name, variable)

    def _processChunk(self, chunk, name, variable):
        if (self.settings['materialVariables']
                and variable not in self.settings['materialVariables']):
            return
        if name not in self.materials:
            debug('Adding material {}...'.format(name))
            self.materials[name] = DepletedMaterial(name, self.metadata)
        if len(chunk) == 1:  # single line values, e.g. volume or burnup
            cleaned = self._cleanSingleLine(chunk)
        else:
            cleaned = []
            for line in chunk:
                if '[' in line or ']' in line:
                    continue
                cleaned.append(line[:line.index('%')])
        self.materials[name].addData(variable, cleaned)

    def _precheck(self):
        """do a quick scan to ensure this looks like a material file."""
        with open(self.filePath) as fh:
            for line in fh:
                sline = line.split()
                if not sline:
                    continue
                elif 'MAT' == line.split('_')[0]:
                    return
        error("No materials found in {}".format(self.filePath))

    def _postcheck(self):
        """ensure the parser grabbed expected materials."""
        if not self.materials:
            error("No materials obtained from {}".format(self.filePath))
            return

        for mKey, mat in self.materials.items():
            assert isinstance(mat, DepletedMaterial), (
                'Unexpected key {}: {} in materials dictionary'.format(
                    mKey, type(mat))
            )
        debug('  found {} materials'.format(len(self.materials)))

        if 'bu' in self.metadata:
            self.metadata['burnup'] = self.metadata.pop('bu')

    def _compare(self, other, lower, upper, _sigma):

        similar = self._compareMetadata(other, lower, upper, _sigma)
        if not self._comparePrecheckMetadata(other):
            return False
        similar &= self._compareMaterials(other, lower, upper, _sigma)
        return similar

    def _comparePrecheckMetadata(self, other):
        for key, myVec in self.metadata.items():
            otherVec = other.metadata[key]
            if len(myVec) != len(otherVec):
                error("Stopping comparison early due to mismatched {} vectors"
                      "\n\t>{}\n\t<{}".format(key, myVec, otherVec))
                return False
        return True

    @compareDocDecorator
    def compareMaterials(self, other, lower=DEF_COMP_LOWER,
                         upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA):
        """
        Return the result of comparing all materials on two readers

        Parameters
        ----------
        other: :class:`DepletionReader`
            Reader to compare against
        {compLimits}
        {sigma}

        Returns
        -------
        bool:
            ``True`` if all materials agree to the given tolerances

        Raises
        ------
        {compTypeErr}
        """
        self._checkCompareObj(other)
        self._compareLogPreMsg(other, lower, upper, quantity='materials')

        if not self._comparePrecheckMetadata(other):
            return False

        return self._compareMaterials(other, lower, upper, sigma)

    def _compareMaterials(self, other, lower, upper, sigma):
        """Private method for going directly into the comparison."""
        commonMats = getKeyMatchingShapes(
            self.materials, other.materials, 'materials')
        similar = (
            len(self.materials) == len(other.materials) == len(commonMats))

        for matName in sorted(commonMats):
            myMat = self[matName]
            otherMat = other[matName]
            similar &= myMat.compare(otherMat, lower, upper, sigma)
        return similar

    @compareDocDecorator
    def compareMetadata(self, other, lower=DEF_COMP_LOWER,
                        upper=DEF_COMP_UPPER, sigma=DEF_COMP_SIGMA):
        """
        Return the result of comparing metadata on two readers

        Parameters
        ----------
        other: :class:`DepletionReader`
            Object to compare against
        {compLimits}
        {header}

        Returns
        -------
        bool
            True if the metadata agree within the given tolerances

        Raises
        ------
        {compTypeErr}
        """

        self._checkCompareObj(other)

        self._compareLogPreMsg(other, lower, upper, quantity='metadata')

        return self._compareMetadata(other, lower, upper, sigma)

    def _compareMetadata(self, other, lower, upper, _sigma):
        """Private method for comparing metadata"""

        similar = logDirectCompare(
            self.metadata['names'], other.metadata['names'],
            0, 0, 'names')
        similar &= logDirectCompare(
            self.metadata['zai'], other.metadata['zai'],
            0, 0, 'zai')
        similar &= logDirectCompare(
            self.metadata['days'], other.metadata['days'],
            lower, upper, 'days')
        similar &= logDirectCompare(
            self.metadata['burnup'], other.metadata['burnup'],
            lower, upper, 'burnup')
        return similar

    @deprecated("toMatlab")
    def saveAsMatlab(self, fileP, reconvert=True, metadata=None,
                     append=True, format='5', longNames=True,
                     compress=True, oned='row'):
        """
        Write a binary MATLAB file from the contents of this reader

        .. deprecated:: 0.7.0
            Use :meth:`~serpentTools.DepletionReader.toMatlab`

        Parameters
        ----------
        fileP: str or file-like object
            Name of the file to write
        reconvert: bool
            If this evaluates to true, convert values back into their
            original form as they appear in the output file, e.g.
            ``MAT_TOTAL_ING_TOX``. Otherwise, maintain the ``mixedCase``
            style, ``total_ingTox``.
        metadata: bool or str or list of strings
            If this evaluates to true, then write all metadata to the
            file as well.
        append: bool
            If true and a file exists under ``output``, append to that file.
            Otherwise the file will be overwritten
        format: {'5', '4'}
            Format of file to write. ``'5'`` for MATLAB 5 to 7.2, ``'4'`` for
            MATLAB 4
        longNames: bool
            If true, allow variable names to reach 63 characters,
            which works with MATLAB 7.6+. Otherwise, maximum length is
            31 characters
        compress: bool
            If true, compress matrices on write
        oned: {'row', 'col'}:
            Write one-dimensional arrays as row vectors if
            ``oned=='row'`` (default), or column vectors

        Raises
        ------
        ImportError:
            If :term:`scipy` is not installed

        See Also
        --------
        :func:`scipy.io.savemat`
        """
        if metadata is not None:
            warn("metadata argument is deprecated. All metadata written",
                 FutureWarning)
            # need this path to perserve selecting not to write
            # metadata
        converter = MatlabConverter(self, fileP)
        return converter.convert(reconvert, append, format, longNames,
                                 compress, oned)

    def _gather_matlab(self, reconvert, metadata=None):
        """
        Return a dictionary with all data

        Should only be used by developers for converting to new
        output file types
        """

        # set these here to reduce number of if/elses

        if reconvert:
            converter = deconvert
        else:
            converter = prepToMatlab

        data = {k.upper() if reconvert else k: v
                for k, v in self.metadata.items()}

        for matName, material in self.materials.items():
            for varName, varData in material.data.items():
                data[converter(matName, varName)] = varData

        return data


def getMaterialNameAndVariable(mlabName):
    for serpVar in DEPLETION_VARIABLES:
        leng = len(serpVar)
        if serpVar == mlabName[-len(serpVar):]:
            matName = mlabName[4:-(leng + 1)]
            if not matName:
                if 'TOT' == mlabName[:3]:
                    return 'total', serpVar
                break
            return matName, serpVar
    raise ValueError(
        "Could not find a match for {}. "
        "Please alert developers".format(mlabName))


def getMatlabVarName(chunk):
    if isinstance(chunk, list):
        return getMatlabVarName(chunk[0])
    return chunk[:chunk.index(' ')]


_MAT_FMT_ORIG = "MAT_{}_{}"
_MAT_FMT_CC = "{}_{}"


def deconvert(material, variable):
    """Restore the original name as present in the depletion file"""
    return _MAT_FMT_ORIG.format(material, deconvertVariableName(variable))


def prepToMatlab(material, variable):
    """Create the name of a single variable for MATLAB"""
    return _MAT_FMT_CC.format(material, variable)
