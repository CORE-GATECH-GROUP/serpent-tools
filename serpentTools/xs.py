"""
Utilities for collecting and exporting group constants from a
branching file
"""

from collections import Iterable
from itertools import product
from warnings import warn
from six import iteritems
from six.moves import range
from numpy import empty, nan, array, ndarray

__all__ = [
    'BranchCollector',
]


class BranchedUniv(object):
    """
    Class for storing cross sections for a single universe across branches

    .. versionadded:: 0.6.2

    .. warning::

        This is experimental, and the structure of
        the underlying data may change. This will
        be stable in version 0.7.0


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

    # Acts largely as a dictionary storing group constants
    # under their cross section names from SERPENT
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
        """Access the xsTables dictionary"""
        return self.xsTables[key]

    def __setitem__(self, key, data):
        shape = data.shape
        assert len(shape) == self._ndims
        for pertIndex, pertState in enumerate(self.states):
            assert len(pertState) == shape[pertIndex], (
                "{} {}".format(shape[pertIndex], pertState))
        self.xsTables[key] = data

    def items(self):
        """Iterate over names of cross sections and associated objects"""
        for name, obj in iteritems(self.xsTables):
            yield name, obj

    @property
    def states(self):
        """
        Iterable describing the names or values of each perturbation
        branch. Length is equal to that of :attr:`perturbations`, and
        the ``i``-th index of ``states`` indicates the values
        perturbation ``perturbations[i]`` experiences.

        See Also
        --------
        :attr:`BranchCollector.states`
        """
        return self.collector.states

    @states.setter
    def states(self, value):
        self.collector.states = value

    @property
    def axis(self):
        """
        Tuple describing axis of underlying data

        .. note::

            When setting, the universe index of the
            axis should not be changed. The changes
            are passed on to :attr:`BranchCollector.axis`
            with an indicator for universe placed in the
            correct spot

        Examples
        --------
        >>> col.axis
        ('Universe', 'BOR', 'TFU', 'Burnup', 'Group')
        >>> u0 = col.universes[0]
        >>> u0.axis == col.axis[1:]
        True
        >>> u0.axis = ['boron conc', 'fuel temp', 'burnup', 'group']
        >>> u0.axis
        ('boron conc', 'fuel temp', 'burnup', 'group')
        >>> col.axis
        ('Universe', 'boron conc', 'fuel temp', 'burnup', 'group')

        See Also
        --------
        :class:`BranchCollector.axis`
        """
        return self.collector.axis[1:]

    @axis.setter
    def axis(self, value):
        if not isinstance(value, tuple):
            value = tuple(value)
        self.collector.axis = ("Universe", ) + value

    @property
    def burnups(self):
        """
        Vector of burnups from coefficient file

        See Also
        --------
        :attr:`BranchCollector.burnups`"""
        return self.collector.burnups

    @burnups.setter
    def burnups(self, value):
        self.collector.burnups = value

    @property
    def perturbations(self):
        """
        Iterable indicating the specific perturbation types

        See Also
        --------
        :attr:`BranchCollector.perturbations`
        """
        return self.collector.perturbations

    @perturbations.setter
    def perturbations(self, value):
        self.collector.perturbations = value


class BranchCollector(object):
    """
    Main class that collects and arranges branched data

    .. versionadded:: 0.6.2

    .. warning::

        This is experimental, and the structure of
        the underlying data may change. This will
        be stable in version 0.7.0

    Parameters
    ----------
    reader: :class:`serpentTools.parsers.branching.BranchingReader`
        Read data from the passed reader

    Attributes
    ----------
    filePath: str
        Location of the read file
    univIndex: tuple
        Ordered tuple of universe as they appear in the first dimension
        of all arrays in :attr:`xsTables`
    universes: dict
        Dictionary of universe-specific cross sections. Each entry
        is a :class:`BranchedUniv` object that stores cross sections
        for a single universe.
    xsTables: dict
        Dictionary of ``{k: x}`` pairs where ``k`` corresponds to
        all cross sections processed and ``x`` are large multidimensional
        cross sections. The structure is described with :attr:`axis`

    """

    __slots__ = (
        'filePath', '_branches', 'xsTables', 'universes', '_axis',
        '_perturbations', 'univIndex', '_burnups', '_states', '_shapes',
    )

    def __init__(self, reader):
        warn("This is an experimental feature, subject to change.",
             UserWarning)
        self.filePath = reader.filePath
        self._branches = reader.branches
        self.xsTables = {}
        self.universes = {}
        self._perturbations = None
        self._states = None
        self._axis = None
        self._burnups = None

    @property
    def perturbations(self):
        """
        Iterable indicating the specific perturbation types

        Can be set to any iterable, so long as the number of
        perturbations is preserved. Ordering is important,
        as changing this does not change the structure
        of any group constants stored

        Example
        -------
        >>> print(col.perturbations)
        ('BOR', 'TFU')
        >>> col.perturbations = ['B', 'T']  # allowed
        >>> col.perturbations = [
        >>>    'boron conc', 'fuel temp', 'ctrl pos',  # not allowed
        >>> ]
        ValueError("Current number of perturbations is 2, not 3")
        """
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
        Iterable describing each perturbation branch.

        Length is equal to that of :attr:`perturbations`, and
        the ``i``-th index of ``states`` indicates the values
        perturbation ``perturbations[i]`` experiences.

        Can be set to any iterable such that the total number
        of perturbations is preserved

        Examples
        --------
        >>> col.states
        (('B1000', 'B750', 'nom'), ('FT1200', 'FT600', 'nom'))
        # set as numpy array
        >>> states = numpy.array([
            [1000., 750., 0.],
            [1200., 600., 900.]
        ])
        >>> col.states = states
        >>> col.states
        array([[1000.,  750.,    0],
               [1200.,  600.,  900]])
        # set as individual numpy vectors
        >>> col.states = (states[0], states[1])
        >>> col.states
        (array([1000., 750., 0.,]), array([1200., 600., 900.,]))
        # pass incorrect shape
        >>> col.states = (
        >>>    (1000, 750, 0), (1200, 600, 900), (0, 1)
        >>> )
        ValueError("Current number of perturbations is 2, not 3")
        # pass incorrect states for one perturbations
        >>> cols.states = (
        >>>     (1000, 750, 500, 0), (1200, 600, 900)
        >>> )
        ValueError("Current number of perturbations for state BOR "
                   "is 3, not 4")
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
        """
        Tuple describing axis of underlying data

        Each index contains a description of the changes in
        group constant data along that axis.
        Can be set to any iterable, but is converted to a
        tuple to prevent in-place changes, such as appending
        to a list or removing one item.
        Passing an ordered object, :class:`list`,
        :class:`tuple`, or :class:`numpy.array` is preferred,
        as the conversion to :class:`tuple` can sort values
        in un-ordered objects like :class:`set` or :class:`dict`
        strangely.

        Examples
        --------
        >>> col.axis
        ("Universe", "BOR", "TFU", "Burnup", "Group")
        >>> infTot = col.xsTables['infTot']
        >>> infTot.shape
        (5, 3, 3, 3, 2)
        # five universes, three BOR perturbations
        # three TFU perturbations, three burnups,
        # two energy groups
        >>> col.axis = ['u', 'b', 't', 'bu', 'g']
        >>> col.axis
        ('u', 'b', 't', 'bu', 'g')
        # pass an unordered set
        >>> col.axis = {'u', 'b', 't', 'bu', 'g'}
        >>> col.axis
        ('bu', 'u', 't', 'g', 'b')
        # incorrectly set axis
        >>> col.axis = [1, 2, 3, 4]
        ValueError("Current axis has 5 dimensions, not 4")
        """
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
        """
        Vector of burnups from coefficient file

        Can be set to any iterable that has same number
        of entries as existing burnup. Automatically
        converts to :class:`numpy.array`

        Examples
        --------

        >>> col.burnups
        array([0., 1., 10.])
        >>> col.burnups = array([0., 5.6, 56.])
        >>> col.burnups
        array([0., 5.6, 56.])
        >>> col.burnups = [0, 1, 10]
        # converted to array of integers
        >>> col.burnups
        array([0, 1, 10])
        >>> col.burnups = [0, 1, 2, 3]  # not allowed
        ValueError("Current burnup vector has 3 items, not 3")
        """
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

    def collect(self, perturbations):
        """
        Parse the contents of the file and collect cross sections

        Parameters
        ----------
        perturbations: tuple
            Tuple where each entry is a state that is perturbed across
            the analysis, e.g. ``("Tfuel", "RhoCool", "CR")``. These
            must appear in the same order as they are ordered in the
            coefficient file.
        """
        if (isinstance(perturbations, str)
           or not isinstance(perturbations, Iterable)):
            self._perturbations = perturbations,
        else:
            self._perturbations = tuple(perturbations)
        sampleBranchKey = self._getBranchStates()
        sampleUniv = self._getUnivsBurnups(sampleBranchKey)
        xsSizes = self._getXsSizes(sampleUniv)

        # Create empty arrays for each xs type
        # Will send off views of this to each universe container
        numUniv = len(self.univIndex)
        numBurnup = len(self._burnups)
        for key, size in iteritems(xsSizes):
            shape = self._shapes + [numUniv, numBurnup, size]
            self.xsTables[key] = empty(shape)

        missing = self._populateXsTable()
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
    def _getXsSizes(sampleUniv):
        sizes = {}
        for gcAttr in ('infExp', 'b1Exp', 'gc'):
            attr = getattr(sampleUniv, gcAttr)
            for key, value in iteritems(attr):
                sizes[key] = value.size
        return sizes

    def _populateXsTable(self):
        missing = {}
        # Create a map of enumerated tuples
        branchMap = map(enumerate, self._states)
        branchIndexer = empty(
            (len(self._states), 2), order='F', dtype=object)

        xsTables = self.xsTables
        keys = set(xsTables.keys())
        for branchMapItem in product(*branchMap):
            branchIndexer[:, :] = branchMapItem
            stateIndex = tuple(branchIndexer[:, 0].astype(int).tolist())
            branchKey = tuple(branchIndexer[:, 1].tolist())
            branch = self._branches.get(branchKey)
            if branch is None:
                missing[branchKey] = stateIndex
                for submat in self.xsTables.values():
                    submat[stateIndex].fill(nan)
                continue
            univIterator = map(enumerate, (self.univIndex, self._burnups))
            for (uIndex, univID), (bIndex, burnup) in product(*univIterator):
                universe = branch.getUniv(univID, burnup)
                thisSlice = stateIndex + (uIndex, bIndex)
                for xsKey in keys:
                    xsTables[xsKey][thisSlice] = universe.get(xsKey)
        return missing

    def _populateUniverses(self):
        self._axis = ("Universe", ) + self._perturbations + ("Burnup", "Group")
        nPerts = len(self._perturbations)
        newAxis = (
            (nPerts,) + tuple(range(nPerts))
            + (nPerts + 1, nPerts + 2))
        origKeys = self.xsTables.keys()
        for key in origKeys:
            self.xsTables[key] = self.xsTables[key].transpose(*newAxis)

        univAxis = self._axis[1:]
        # Create all the univIndex
        for univIndex, univID in enumerate(self.univIndex):
            self.universes[univID] = BranchedUniv(univID, self, univAxis)
        for xsKey, xsMat in iteritems(self.xsTables):
            for univIndex, univID in enumerate(self.univIndex):
                self.universes[univID][xsKey] = xsMat[univIndex]
