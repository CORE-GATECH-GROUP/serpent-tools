"""Parser responsible for reading the ``*dep.m`` files"""
import re

from matplotlib import pyplot
from six import iteritems

from serpentTools.utils import (
    magicPlotDocDecorator, formatPlot, DEPLETION_PLOT_LABELS,
    convertVariableName, str2vec,
)

from serpentTools.engines import KeywordParser
from serpentTools.parsers.base import MaterialReader
from serpentTools.objects.materials import DepletedMaterial

from serpentTools.messages import (warning, debug, error,
                                   SerpentToolsException)
from serpentTools.utils.compare import getKeyMatchingShapes

METADATA_KEYS = {'ZAI', 'NAMES', 'BU', 'DAYS'}


class DepPlotMixin(object):

    @magicPlotDocDecorator
    def plot(self, xUnits, yUnits, timePoints=None, names=None, zai=None,
             materials=None, ax=None, legend=True, logx=False, logy=False,
             loglog=False, labelFmt=None, xlabel=None, ylabel=None, ncol=1,
             **kwargs):
        """
        Plot properties for all materials in this file together.

        Parameters
        ----------
        xUnits: str
            name of x value to obtain, e.g. ``'days'``, ``'burnup'``
        yUnits: str
            name of y value to return, e.g. ``'adens'``, ``'ingTox'``
        timePoints: list or None
            If given, select the time points according to those
            specified here. Otherwise, select all points
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
        if not self.materials:
            raise SerpentToolsException("Material dictionary is empty")

        if xUnits not in ('days', 'burnup'):
            raise KeyError("Plot method only uses x-axis data from <days> and "
                           "<burnup>, not {}".format(xUnits))
        missing = set()
        ax = ax or pyplot.axes()
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
        self._matPatterns = self._makeMaterialRegexs()
        self._matchMatNVar = r'[A-Z]{3}_([0-9a-zA-Z]*)_([A-Z]*_?[A-Z]*)'
        # Captures material name and variable from string
        #  MAT_fuel1_ADENS --> ('fuel1', 'ADENS')
        #  MAT_fUeL1g_ING_TOX --> ('fUeL1', 'ING_TOX')

        self._matchTotNVar = r'[A-Z]{3}_([A-Z]*_?[A-Z]*)'
        # Captures variables for total block from string::
        #  TOT_ADENS --> ('ADENS', )
        #  ING_TOX --> ('ING_TOX', )
        DepPlotMixin.__init__(self)

    def __getitem__(self, name):
        """Retrieve a material from :attr:`materials`."""
        return self.materials[name]

    def _makeMaterialRegexs(self):
        """Return the patterns by which to find the requested materials."""
        patterns = self.settings['materials'] or ['.*']
        # match all materials if nothing given
        if any(['_' in pat for pat in patterns]):
            warning('Materials with underscores are not supported.')
        return [re.compile(mat) for mat in patterns]

    def _read(self):
        """Read through the depletion file and store requested data."""
        keys = ['MAT', 'TOT'] if self.settings['processTotal'] else ['MAT']
        keys.extend(self.settings['metadataKeys'])
        separators = ['\n', '];', '\r\n']
        with KeywordParser(self.filePath, keys, separators) as parser:
            for chunk in parser.yieldChunks():
                if 'MAT' in chunk[0]:
                    self._addMaterial(chunk)
                elif 'TOT' in chunk[0]:
                    self._addTotal(chunk)
                else:
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

    def _addMaterial(self, chunk):
        """Add data from a MAT chunk."""
        name, variable = self._getGroupsFromChunk(self._matchMatNVar, chunk)
        if any([re.match(pat, name) for pat in self._matPatterns]):
            self._processChunk(chunk, name, variable)

    def _addTotal(self, chunk):
        """Add data from a TOT chunk"""
        variable = self._getGroupsFromChunk(self._matchTotNVar, chunk)[0]
        self._processChunk(chunk, 'total', variable)

    def _getGroupsFromChunk(self, regex, chunk):
        match = re.match(regex, chunk[0])
        if match:
            return match.groups()
        raise Exception('{} not determine match from the following chunk:\n'
                        '{}'.format(self, ''.join(chunk)))

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

        for mKey, mat in iteritems(self.materials):
            assert isinstance(mat, DepletedMaterial), (
                'Unexpected key {}: {} in materials dictionary'.format(
                    mKey, type(mat))
            )
        debug('  found {} materials'.format(len(self.materials)))

        if 'bu' in self.metadata:
            self.metadata['burnup'] = self.metadata.pop('bu')

    def _compare(self, other, lower, upper, sigma):

            commonKeys = getKeyMatchingShapes(
                self.materials, other.materials, 'materials')
            similar = (
                len(self.materials) == len(other.materials) == len(commonKeys))

            for matName in sorted(commonKeys):
                myMat = self[matName]
                otherMat = other[matName]
                similar &= myMat.compare(otherMat, lower, upper, sigma)
            return similar
