"""
Utilities for collecting and exporting group constants from a
branching file
"""

from collections import Iterable
from itertools import product
from warnings import warn
from six import iteritems
from numpy import empty, nan, array, ndarray

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
    def states(self):
        """
        Tuple of tuples describing perturbation states

        See Also
        --------
        :attr:`BranchCollector.states`
        """
        return self.universe.states

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
    def perturbations(self):
        """
        Names of specific perturbations

        See Also
        --------
        :attr:`BranchCollector.perturbations`
        """
        return self.universe.perturbations


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
        for pertIndex, pertState in enumerate(self.states):
            assert len(pertState) == shape[pertIndex], (
                "{} {}".format(shape[pertIndex], pertState))
        self.xsTables[key] = BranchedDataTable(key, data, self)

    def items(self):
        """Iterate over names of cross sections and associated objects"""
        for name, obj in iteritems(self.xsTables):
            yield name, obj

    @property
    def states(self):
        return self.collector.states

    @states.setter
    def states(self, value):
        self.collector.states = value

    @property
    def axis(self):
        """Tuple describing vector of this universe's data"""
        return self.collector.axis[1:]

    @axis.setter
    def axis(self, value):
        if not isinstance(value, tuple):
            value = tuple(value)
        self.collector.axis = ("Universe", ) + value

    @property
    def burnups(self):
        return self.collector.burnups

    @burnups.setter
    def burnups(self, value):
        self.collector.burnups = value

    @property
    def perturbations(self):
        return self.collector.perturbations

    @perturbations.setter
    def perturbations(self, value):
        self.collector.perturbations = value


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
    burnups: :class:`numpy.ndarray`
        Ordered vector of burnups as they appear in the
        second to last dimension of arrays in :attr:`xsTables`
    perturbations: tuple
        Perturbed states given to :meth:`collect` method
    states: tuple
        tuple of tuples where each entry is a tuple containing the
        order of perturbation values for a specific branch. These
        are ordered as they appear in ``self.perturbations``. For example::

            >>> c.perturbations
            ('BOR', 'TFU')
            >>> c.states
            (('B1000', 'B750', 'nom'),
             ('FT1200', 'FT600', 'nom'))

        reveals that the first entry in :attr:`states` corresponds to
        perturbations of the first quantity in :attr:`perturbations`.
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
        'filePath', '_branches', 'xsTable', 'universes', '_axis',
        '_perturbations', 'univIndex', '_burnups', '_states', '_shapes',
    )

    def __init__(self, reader):
        warn("This is an experimental feature, subject to change.",
             UserWarning)
        self.filePath = reader.filePath
        self._branches = reader.branches
        self.xsTable = {}
        self.universes = {}
        self._perturbations = None
        self._states = None
        self._axis = None
        self._burnups = None

    @property
    def perturbations(self):
        """Iterable indicating the specific perturbation types"""
        return self._perturbations

    @perturbations.setter
    def perturbations(self, value):
        if self._perturbations is None:
            raise AttributeError(
                "Collect first to ensure correct data structure.")
        if isinstance(value, str) or not isinstance(value, Iterable):
            value = value,
        if len(value) != len(self._perturbations):
            raise ValueError(
                "Current number of perturbations is {}, not {}"
                .format(len(self._perturbations), len(value)))
        self._perturbations = value

    @property
    def states(self):
        """
        Iterable describing the names or values of each perturbation
        branch. Length is equal to that of :attr:`perturbations`, and
        the ``i``-th index of ``states`` indicates the values
        perturbation ``perturbations[i]`` experiences.
        """
        return self._states

    @states.setter
    def states(self, value):
        if self._states is None:
            raise AttributeError(
                "Collect first to ensure correct data structure.")
        if len(value) != len(self._states):
            raise ValueError(
                "Current number of perturbations is {}, not {}"
                .format(len(self._states), len(value)))

        # check to make sure all perturbation vectors in the
        # requested value are of the same length
        for index, pertVec in enumerate(self._states):
            if len(value[index]) != len(pertVec):
                raise ValueError(
                    "Current number of perturbations for state {} is {}, "
                    "not {}"
                    .format(self._perturbations[index], len(pertVec),
                            len(value[index])))
        self._states = value

    @property
    def axis(self):
        """Tuple describing axis of underlying data"""
        if self._axis is None:
            raise AttributeError("Axis not set. Collect first.")
        return self._axis

    @axis.setter
    def axis(self, value):
        if self._axis is None:
            raise AttributeError(
                "Collect first to ensure correct data structure.")

        # coerce into tuple to enforce some immutability
        if not isinstance(value, tuple):
            value = tuple(value)

        if len(value) != len(self._axis):
            raise ValueError(
                "Current axis has {} dimensions, not {}"
                .format(len(self._axis), len(value)))

        self._axis = value

    @property
    def burnups(self):
        """Vector of burnups from coefficient file"""
        if self._burnups is None:
            raise AttributeError("Burnups not set. Collect first.")
        return self._burnups

    @burnups.setter
    def burnups(self, value):
        if self._burnups is None:
            raise AttributeError(
                "Collect first to ensure correct data structure.")
        if not isinstance(value, ndarray):
            value = array(value)
        if value.size != self._burnups.size:
            raise ValueError(
                "Current burnup vector has {} items, not {}"
                .format(self._burnups.size, value.size))
        self._burnups = value

    def collect(self, perturbations, xsType):
        """
        Parse the contents of the file and collect cross sections

        Parameters
        ----------
        perturbations: tuple
            Tuple where each entry is a state that is perturbed across
            the analysis, e.g. ``("Tfuel", "RhoCool", "CR")``. These
            must appear in the same order as they are ordered in the
            coefficient file.
        xsType: {'inf', 'b1'}
            What cross section type to extract from the file. Currently
            only supports a single type, but more to come later
        """
        if (isinstance(perturbations, str)
           or not isinstance(perturbations, Iterable)):
            self._perturbations = perturbations,
        else:
            self._perturbations = tuple(perturbations)
        xsLookFor = "{}Exp".format(xsType)
        sampleBranchKey = self._getBranchStates()
        sampleUniv = self._getUnivsBurnups(sampleBranchKey)
        xsSizes = self._getXsSizes(sampleUniv, xsLookFor)

        # Create empty arrays for each xs type
        # Will send off views of this to each universe container
        numUniv = len(self.univIndex)
        numBurnup = len(self._burnups)
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

        self._burnups = array(self._burnups)
        self._populateUniverses()
        del self._branches, self._shapes

    def _getBranchStates(self):
        branchSets = tuple([set() for _tpl in self.perturbations])
        for branchKey in self._branches:
            for stateIndex, state in enumerate(branchKey):
                branchSets[stateIndex].add(state)
        self._states = tuple([tuple(sorted(s)) for s in branchSets])
        self._shapes = [len(s) for s in self._states]
        return branchKey

    def _getUnivsBurnups(self, branchKey):
        branch = self._branches[branchKey]
        univs = set()
        _burnups = set()
        for unID, bu, ix in branch.universes:
            univs.add(unID)
            _burnups.add(bu)
        self._burnups = tuple(sorted(_burnups))
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
        branchMap = map(enumerate, self._states)
        branchIndexer = empty(
            (len(self._states), 2), order='F', dtype=object)

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
            univIterator = map(enumerate, (self.univIndex, self._burnups))
            for (uIndex, univID), (bIndex, burnup) in product(*univIterator):
                universe = branch.getUniv(univID, burnup)
                thisSlice = stateIndex + (uIndex, bIndex)
                xsDict = getattr(universe, xsLookFor)
                for xsKey, xsValue in iteritems(xsDict):
                    xsTables[xsKey][thisSlice] = xsValue
        return missing

    def _populateUniverses(self):
        self._axis = ("Universe", ) + self.perturbations + ("Burnup", "Group")
        pertLocs = range(len(self.perturbations))
        newAxis = (
            (pertLocs.stop,) + tuple(pertLocs)
            + (pertLocs.stop + 1, pertLocs.stop + 2))
        origKeys = self.xsTable.keys()
        for key in origKeys:
            self.xsTable[key] = self.xsTable[key].transpose(*newAxis)

        univAxis = self._axis[1:]
        # Create all the univIndex
        for univIndex, univID in enumerate(self.univIndex):
            self.universes[univID] = BranchedUniv(univID, self, univAxis)
        for xsKey, xsMat in iteritems(self.xsTable):
            for univIndex, univID in enumerate(self.univIndex):
                self.universes[univID][xsKey] = xsMat[univIndex]


# shortcut some docstrings
for prop in ('burnups', 'perturbations', 'states'):
    coldoc = getattr(BranchCollector, prop).__doc__
    getattr(BranchedUniv, prop).__doc__ = coldoc
    getattr(BranchedDataTable, prop).__doc__ = coldoc

del prop, coldoc
