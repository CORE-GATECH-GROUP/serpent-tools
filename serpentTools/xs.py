"""
Utilities for collecting and exporting group constants from a
branching file
"""

from collections import Iterable
from itertools import product
from warnings import warn
from six import iteritems
from numpy import empty, nan, array

__all__ = [
    'BranchCollector',
]


class BranchedDataTable(object):
    """
    Class for storing multi-dimensional tables for cross sections

    Parameters
    ----------
    name: str
        Name of the value that this data table represents, e.g.
        ``'infTot'``,
    data: :class:`numpy.ndarray`
        (Potentially) multi-dimensional data spanning perturbations
        and burnup
    universe: :class:`BranchedUniv`
        Parent universe.
    """
    # Basically just a wrapper over a numpy array for now.
    # Could be used in the future to house interpolation/extrapolation
    # routines.
    # This would require numeric data on the pertStates.
    __slots__ = (
        'name', 'data', 'universe',
    )

    def __init__(self, name, data, universe):
        self.universe = universe
        self.name = name
        self.data = data

    @property
    def shape(self):
        """Tuple reflecting shape of underlying data"""
        return self.data.shape

    @property
    def size(self):
        """Integer of number of values in underlying data"""
        return self.data.size

    @property
    def pertStates(self):
        """
        Tuple of tuples describing perturbation states

        See Also
        --------
        :attr:`BranchCollector.pertStates`
        """
        return self.universe.pertStates

    @property
    def axis(self):
        """
        Tuple mapping dimensions of :attr:`data` corresponds to perturbations

        See Also
        --------
        :class:`BranchCollector.axis`
        """
        return self.universe.axis

    @property
    def burnups(self):
        """Vector of burnups"""
        return self.universe.burnups

    @property
    def perts(self):
        """
        Names of specific perturbations

        See Also
        --------
        :attr:`BranchCollector.perts`
        """
        return self.universe.perts


class BranchedUniv(object):
    """
    Class for storing cross sections for a single universe across branches

    Parameters
    ----------
    univID: str or int
        Unique ID for this universe
    collector: :class:`BranchCollector`
        Class that parses and places branched coefficient data
    ndims: int or iterable
        Number of perturbation dimensions

    Attributes
    ----------
    filePath: str
        Location of the file that stores the data on this object
    univID: str or int
        Unique ID for this universe
    collector: :class:`BranchCollector`
        Class that parses and places branched coefficient data
    xsTables: dict
        Dictionary with keys representing specific values, e.g.
        ``'infTot'`` and ``'b1Diffcoeff'``. Corresponding values
        are :class:`BranchedDataTable` objects that store
        cross section and group constant data across perturbation states

    """

    # Acts largely as a dictionary storing :class:`BranchedDataTable`
    # objects under their cross section names from SERPENT
    # Subclass of dictionary?
    __slots__ = (
        'filePath', 'univID', 'collector',
        '_ndims', 'xsTables',
    )

    def __init__(self, univID, collector, ndims=None):
        assert (
            isinstance(collector, BranchCollector)
            or issubclass(collector, BranchCollector))
        self.filePath = collector.filePath
        self.univID = univID
        self.collector = collector
        if ndims is None:
            self._ndims = len(collector.axis[1:])
        else:
            if hasattr(ndims, '__iter__'):
                ndims = len(ndims)
            elif isinstance(ndims, (int, float)):
                ndims = int(ndims)
            assert ndims > 0
            self._ndims = ndims
        self.xsTables = {}

    def __getitem__(self, key):
        return self.xsTables[key]

    def __setitem__(self, key, data):
        shape = data.shape
        assert len(shape) == self._ndims
        for pertIndex, pertState in enumerate(self.pertStates):
            assert len(pertState) == shape[pertIndex], (
                "{} {}".format(shape[pertIndex], pertState))
        self.xsTables[key] = BranchedDataTable(key, data, self)

    def items(self):
        """Iterate over names of cross sections and associated objects"""
        for name, obj in iteritems(self.xsTables):
            yield name, obj

    @property
    def pertStates(self):
        return self.collector.pertStates

    @property
    def axis(self):
        return self.collector.axis[1:]

    @property
    def burnups(self):
        return self.collector.burnups

    @property
    def perts(self):
        return self.collector.perts


class BranchCollector(object):
    """
    Main class that collects and arranges branched data

    Parameters
    ----------
    source: str or :class:`serpentTools.parsers.branching.BranchingReader`
        If string, read the file at this location as a branching
        coefficient file to create a
        :class:`~serpentTools.parsers.branching.BranchingReader`.
        Otherwise, read data from the passed reader

    Attributes
    ----------
    axis: tuple
        Description of each dimension of arrays in ``xsTable``.
        Will be structured as
        ``('Universe', <perturbed parameters>, 'Burnup', 'Data')``,
        where ``'Data'`` is the actual cross section data.
    burnups: :class:`numpy.ndarray`
        Ordered vector of burnups as they appear in the
        second to last dimension of arrays in :attr:`xsTables`
    perts: tuple
        Perturbed states given to :meth:`collect` method
    pertStates: tuple
        tuple of tuples where each entry is a tuple containing the
        order of perturbation values for a specific branch. These
        are ordered as they appear in ``self.perts``. For example::

            >>> c.perts
            ('BOR', 'TFU')
            >>> c.pertStates
            (('B1000', 'B750', 'nom'),
             ('FT1200', 'FT600', 'nom'))

        reveals that the first entry in :attr:`pertStates` corresponds to
        perturbations of the first quantity in :attr:`perts`.
    filePath: str
        Location of the read file
    univIndex: tuple
        Ordered tuple of universe as they appear in the first dimension
        of all arrays in :attr:`xsTable`
    universes: dict
        Dictionary of universe-specific cross sections. Each entry
        is a :clas:`BranchedUniv` object that stores cross sections
        for a single universe.
    xsTable: dict
        Dictionary of ``{k: x}`` pairs where ``k`` corresponds to
        all cross sections processed and ``x`` are large multidimensional
        cross sections. The structure is described with :attr:`axis`

    """

    __slots__ = (
        'filePath', '_branches', 'xsTable', 'universes', 'axis', '_perts',
        'univIndex', 'burnups', '_pertStates', '_shapes',
    )
    # TODO Make pertStates and perts private w/ checked setters

    def __init__(self, reader):
        warn("This is an experimental feature, subject to change.", UserWarning)
        self.filePath = reader.filePath
        self._branches = reader.branches
        self.xsTable = {}
        self.universes = {}
        self._perts = None
        self._pertStates = None

    @property
    def perts(self):
        return self._perts

    @perts.setter
    def perts(self, value):
        if isinstance(value, str) or not isinstance(value, Iterable):
            value = value,
        if len(value) != len(self._perts):
            raise ValueError(
                "Current number of perturbations is {}, not {}"
                .format(len(self._perts), len(value)))
        self._perts = value

    @property
    def pertStates(self):
        """
        Iterable describing the names or values of each perturbation
        branch. Length is equal to that of :attr:`perts`, and
        the ``i``-th index of ``pertStates`` indicates the values
        perturbation ``perts[i]`` experiences.
        """
        return self._pertStates

    @pertStates.setter
    def pertStates(self, value):
        if len(value) != len(self._pertStates):
            raise ValueError(
                "Current number of perturbations is {}, not {}"
                .format(len(self._pertStates), len(value)))

        # check to make sure all perturbation vectors in the
        # requested value are of the same length
        for index, pertVec in enumerate(self._pertStates):
            if len(value[index]) != len(pertVec):
                raise ValueError(
                    "Current number of perturbations for state {} is {}, "
                    "not {}"
                    .format(self._perts[index], len(pertVec), len(value[index])))
        self._pertStates = value

    def collect(self, perts, xsType):
        """
        Parse the contents of the file and collect cross sections

        Parameters
        ----------
        perts: tuple
            Tuple where each entry is a state that is perturbed across
            the analysis, e.g. ``("Tfuel", "RhoCool", "CR")``. These
            must appear in the same order as they are ordered in the
            coefficient file.
        xsType: {'inf', 'b1'}
            What cross section type to extract from the file. Currently
            only supports a single type, but more to come later
        """
        if isinstance(perts, str) or not isinstance(perts, Iterable):
            self._perts = perts,
        else:
            self._perts = tuple(perts)
        xsLookFor = "{}Exp".format(xsType)
        sampleBranchKey = self._getBranchStates()
        sampleUniv = self._getUnivsBurnups(sampleBranchKey)
        xsSizes = self._getXsSizes(sampleUniv, xsLookFor)

        # Create empty arrays for each xs type
        # Will send off views of this to each universe container
        numUniv = len(self.univIndex)
        numBurnup = len(self.burnups)
        for key, size in iteritems(xsSizes):
            shape = self._shapes + [numUniv, numBurnup, size]
            self.xsTable[key] = empty(shape)

        missing = self._populateXsTable(xsLookFor)
        if missing:
            items = ["{}: {}".format(str(k), str(v))
                     for k, v in iteritems(missing)]
            msg = ("The following branch states and indexes are "
                   "unaccounted for:\n{}".format("\n".join(items)))
            warn(msg, RuntimeWarning)

        self.burnups = array(self.burnups)
        self._populateUniverses()
        del self._branches, self._shapes

    def _getBranchStates(self):
        branchSets = tuple([set() for _tpl in self.perts])
        for branchKey in self._branches:
            for stateIndex, state in enumerate(branchKey):
                branchSets[stateIndex].add(state)
        self._pertStates = tuple([tuple(sorted(s)) for s in branchSets])
        self._shapes = [len(s) for s in self._pertStates]
        return branchKey

    def _getUnivsBurnups(self, branchKey):
        branch = self._branches[branchKey]
        univs = set()
        burnups = set()
        for unID, bu, ix in branch.universes:
            univs.add(unID)
            burnups.add(bu)
        self.burnups = tuple(sorted(burnups))
        self.univIndex = tuple(sorted(univs))
        return branch.universes[unID, bu, ix]

    @staticmethod
    def _getXsSizes(sampleUniv, xsAttrName):
        assert hasattr(sampleUniv, xsAttrName), xsAttrName
        # TODO Reshaped scatter matrices?
        sizes = {}
        attr = getattr(sampleUniv, xsAttrName)
        for key, value in iteritems(attr):
            sizes[key] = value.size
        return sizes

    def _populateXsTable(self, xsLookFor):
        missing = {}
        # Create a map of enumerated tuples
        branchMap = map(enumerate, self._pertStates)
        branchIndexer = empty(
            (len(self._pertStates), 2), order='F', dtype=object)

        xsTables = self.xsTable
        for branchMapItem in product(*branchMap):
            branchIndexer[:, :] = branchMapItem
            stateIndex = tuple(branchIndexer[:, 0].astype(int).tolist())
            branchKey = tuple(branchIndexer[:, 1].tolist())
            branch = self._branches.get(branchKey)
            if branch is None:
                missing[branchKey] = stateIndex
                for submat in self.xsTable.values():
                    submat[stateIndex].fill(nan)
                continue
            univIterator = map(enumerate, (self.univIndex, self.burnups))
            for (uIndex, univID), (bIndex, burnup) in product(*univIterator):
                universe = branch.getUniv(univID, burnup)
                thisSlice = stateIndex + (uIndex, bIndex)
                xsDict = getattr(universe, xsLookFor)
                for xsKey, xsValue in iteritems(xsDict):
                    xsTables[xsKey][thisSlice] = xsValue
        return missing

    def _populateUniverses(self):
        self.axis = ("Universe", ) + self.perts + ("Burnup", "Group")
        pertLocs = range(len(self.perts))
        newAxis = (
            pertLocs.stop, *pertLocs, pertLocs.stop + 1, pertLocs.stop + 2)
        origKeys = self.xsTable.keys()
        for key in origKeys:
            self.xsTable[key] = self.xsTable[key].transpose(*newAxis)

        univAxis = self.axis[1:]
        # Create all the univIndex
        for univIndex, univID in enumerate(self.univIndex):
            self.universes[univID] = BranchedUniv(univID, self, univAxis)
        for xsKey, xsMat in iteritems(self.xsTable):
            for univIndex, univID in enumerate(self.univIndex):
                self.universes[univID][xsKey] = xsMat[univIndex]
