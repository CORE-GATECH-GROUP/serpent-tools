"""
Interfaces for reading result files
"""
import pathlib
import numbers
from collections import namedtuple, defaultdict
from collections.abc import Iterable
import io
import warnings
from enum import Enum, auto
import re

from serpentTools.messages import SerpentToolsException
from serpentTools.parsers.results import (
    METADATA_CONV,
    ListOfArrays,
    varTypeFactory,
)
from serpentTools.utils import (
    str2vec,
    splitValsUncs,
    STR_REGEX,
    VEC_REGEX,
    SCALAR_REGEX,
    FIRST_WORD_REGEX,
    convertVariableName,
)
from serpentTools.next.base import SerpentFile

from serpentTools.objects.containers import HomogUniv, UnivTuple


class ResultFile(SerpentFile):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.resdata = {}
        self.universes = {}
        self.metadata = {}

    def __getitem__(self, key):
        return self.resdata[key]

    @classmethod
    def fromSerpent(
        cls, source, sourcename=None, postcheck=True, strict=True, **kwargs,
    ):

        return super().fromSerpent(
            source,
            sourcename=sourcename,
            postcheck=postcheck,
            strict=strict,
            **kwargs,
        )

    @classmethod
    def _fromSerpentStream(
        cls, source, sourcename, postcheck, strict, **kwargs,
    ):
        reader = ResultReader(**kwargs)
        # TODO Support post-read checking
        rf = cls(filename=sourcename)
        return reader.read(source, assignTo=rf)


# Reading the file

DataKeys = namedtuple("DataKeys", ["meta", "result", "universe", "version"])

DATA_SECTION_STARTS = {
    "2.1.29": DataKeys(
        "VERSION", "MIN_MACROXS", "GC_UNIVERSE_NAME", "VERSION"
    ),
}


DATA_SECTION_STARTS["2.1.30"] = DATA_SECTION_STARTS["2.1.29"]
DATA_SECTION_STARTS["2.1.31"] = DATA_SECTION_STARTS["2.1.29"]


def _getDataStarts(version) -> DataKeys:
    keys = DATA_SECTION_STARTS.get(version)
    if keys is not None:
        return keys

    # Why did this not work?
    if version == "latest":
        return DATA_SECTION_STARTS["2.1.31"]

    if isinstance(version[0], numbers.Integral):
        # Support passing tuple of ints (2, 1, 30)
        vkey = ".".join(map(str, version))
        keys = DATA_SECTION_STARTS.get(vkey)
        if keys is not None:
            return keys
        raise KeyError(
            "Could not find version string {} from tuple {}. "
            "Currently supported versions: {}".format(
                vkey, version, sorted(DATA_SECTION_STARTS)
            )
        )

    raise KeyError(
        "Could not find version string {}. Currently supported version: "
        "{}".format(version, sorted(DATA_SECTION_STARTS))
    )


class FilePosition(Enum):
    META = auto()
    RESULT = auto()
    UNIV = auto()
    INVALID = auto()


class _ResFileEngine:
    def __init__(self, stream: io.TextIOBase, seekable=True):
        self._stream = stream

    def seek(self, position, whence=io.SEEK_SET):
        if not self._stream.seekable():
            raise OSError("{} is not seekable".format(self._stream))
        return self._stream.seek(position, whence)

    @property
    def seekable(self) -> bool:
        return self._stream.seekable()

    @property
    def closed(self) -> bool:
        return self._stream.closed()

    def tell(self):
        return self._stream.tell()

    def readline(self) -> str:
        return self._stream.readline()

    def read(self) -> str:
        return self._stream.read()

    def close(self):
        self._stream.close()

    def __enter__(self):
        return self

    def __exit__(self, excType, excValue, traceback):
        self.close()

    @staticmethod
    def _checkLine(line: str) -> bool:
        if line.isspace():
            return False

        if any(
            [line.startswith(start) for start in {"%", "if", "end", "else"}]
        ):
            return False

        if re.match(r"\s*idx\s*=", line) is not None:
            return False

        return True

    def __iter__(self):
        line = self.readline()
        if not line:
            raise EOFError

        while line:
            if self._checkLine(line):
                yield line.strip()
            line = self.readline()


BurnupState = namedtuple("BurnupState", ["step", "day", "burnup"])


class _DefaultUnivDict(dict):
    def __missing__(self, key):
        return HomogUniv(*key)


class ResultReader:
    def __init__(
        self,
        serpentVersion="latest",
        groups=None,
        extras=None,
        infXS=True,
        b1XS=True,
    ):
        self._keystarts = None
        self._variables = set()
        self.serpentVersion = serpentVersion
        self.groups = set() if groups is None else set(groups)
        self.extras = set() if extras is None else set(extras)
        self.infXS = infXS
        self.b1XS = b1XS

    @property
    def serpentVersion(self) -> str:
        return self._serpentVersion

    @serpentVersion.setter
    def serpentVersion(self, version):
        if version == "latest":
            version = "2.1.31"
        elif isinstance(version[0], numbers.Integral):
            version = ".".join(map(str, version))
        elif not isinstance(version, str):
            raise TypeError(
                "Serpent version must be string or triplet of integers. "
                "Got {}".format(version)
            )
        # flush old variables
        self._variables.clear()
        self._serpentVersion = version
        self._keystarts = _getDataStarts(version)

    def __enter__(self):
        return self

    def __exit__(self, excType, excValue, traceback):
        # If we have successfully parsed the file, delete
        # all the temporary attributes
        # Otherwise, keep everything so that any debugging
        # shows a better state of the object
        # All three arguments will be None if no exception
        # is being raised
        if any(o is not None for o in [excType, excValue, traceback]):
            return

        # del (
        #     self._tempArrays,
        #     self._position,
        #     self._counter,
        #     self._currentUniverse,
        #     self._numUniverses,
        #     self._currentBurnup,
        # )

    def read(self, fileOrStream, assignTo=None) -> ResultFile:
        if assignTo is None:
            # Create a basic results file
            rf = ResultFile()
        elif isinstance(assignTo, ResultFile):
            rf = assignTo
        elif issubclass(assignTo, ResultReader):
            rf = assignTo()
        else:
            raise TypeError(
                "Assign to must be an instance or un-initialized subclass "
                "of {}".format(ResultFile)
            )

        with self:
            # Decorator???
            if isinstance(fileOrStream, str):
                with open(fileOrStream) as stream:
                    self._read(stream)
            elif isinstance(fileOrStream, pathlib.Path):
                with fileOrStream.open() as stream:
                    self._read(stream)
            elif isinstance(fileOrStream, io.BufferedIOBase):
                self._read(io.TextIOWrapper(fileOrStream))
            elif isinstance(fileOrStream, io.TextIOBase):
                self._read(fileOrStream)
            else:
                raise TypeError(
                    "Canot convert {} to text stream".format(
                        type(fileOrStream)
                    )
                )

            self._transferTo(rf)

        return rf

    def _read(self, stream: io.TextIOBase):
        # Define some helper attributes
        # to be deleted in __exit__
        self._position = FilePosition.INVALID
        self._counter = defaultdict(int)
        self._currentUniverse = None
        self._tempArrays = defaultdict(ListOfArrays)
        self._currentBurnup = None
        self._thisMetadata = {}
        self._thisUniverses = _DefaultUnivDict()
        # Maybe keep this one around?
        self._universeDataConverters = {}

        parser = _ResFileEngine(stream)

        # TODO Better group expansion
        # TODO Maybe only perform this if we've added groups / extras?
        self._variables = self.extras.union(self.groups)
        self._numUniverses = self._preCountUniverses(parser)

        for line in parser:

            self._updateFilePosition(line)

            match = FIRST_WORD_REGEX.search(line)
            assert match is not None
            serpentName = line[match.span()[0]:match.span()[1]]
            # Check if we have found a new universe
            if (
                self._position == FilePosition.UNIV
                and serpentName == self._keystarts.universe
            ):
                _vtype, uname = self._parseVariableLine(line)
                if self._currentBurnup is None:
                    self._currentBurnup = self._getBurnupPosition()
                key = UnivTuple(
                    uname,
                    self._currentBurnup.burnup,
                    self._currentBurnup.step,
                    self._currentBurnup.day,
                )
                self._currentUnivKey = key
                continue

            if not self._checkAddVariable(serpentName):
                continue

            # Actually process and store the information
            kind, values = self._parseVariableLine(line)
            pyname = convertVariableName(serpentName)

            if self._position == FilePosition.RESULT:
                self._addResultData(pyname, values)
            elif self._position == FilePosition.UNIV:
                self._addUniverseData(serpentName, values)
            elif self._position == FilePosition.META:
                self._addMetadata(pyname, kind, values)

    def _updateFilePosition(self, line: str):
        if line.startswith(self._keystarts.meta):
            self._position = FilePosition.META
            self._counter[FilePosition.META] += 1
        elif line.startswith(self._keystarts.result):
            self._position = FilePosition.RESULT
            if self._numUniverses:
                # TODO Remove these off by ones
                currentStep = (
                    self._counter[FilePosition.META] - 1
                ) // self._numUniverses + 1
                if currentStep != self._counter[FilePosition.RESULT]:
                    # new time step
                    self._currentBurnup = None
                    self._counter[FilePosition.RESULT] = currentStep
            else:
                self._counter[FilePosition.RESULT] += 1
        elif line.startswith(self._keystarts.universe):
            self._position = FilePosition.UNIV

    def _preCountUniverses(self, stream: _ResFileEngine) -> int:
        # Check the number of universes in the file
        universes = set()
        warnOnDiffVersion = True

        # TODO Put this somewhere else and raise a better error
        assert stream.seekable

        position = stream.tell()

        for line in stream:
            if warnOnDiffVersion and line.startswith(self._keystarts.version):
                # Quick check that the version requested is the version
                # found in the file
                warnOnDiffVersion = False
                _valtype, value = self._parseVariableLine(line)

                # Assume version key like "Serpent <version>"
                if not value.endswith(self.serpentVersion):
                    warnings.warn(
                        "Serpent version found in file {} does not match "
                        "expected version {}. Proceeding anyways".format(
                            value, self.serpentVersion,
                        )
                    )
                continue
            if line.startswith(self._keystarts.universe):
                _valtype, univid = self._parseVariableLine(line)
                if univid in universes:
                    break
                universes.add(univid)

        # Reset stream position to before we started
        stream.seek(position, io.SEEK_SET)
        return len(universes)

    @staticmethod
    def _parseVariableLine(line: str):
        # TODO Use different regular expressions with match groups
        stringMatch = STR_REGEX.search(line)
        if stringMatch is not None:
            # drop initial single quotes
            span = stringMatch.span()
            return "string", line[span[0] + 1: span[1] - 1]
        vectorMatch = VEC_REGEX.search(line)
        if vectorMatch is not None:
            # drop beginning and ending bracket
            span = vectorMatch.span()
            return "vector", line[span[0] + 1: span[1] - 1]
        scalarMatch = SCALAR_REGEX.search(line)
        if scalarMatch is not None:
            # drop ending ;
            span = scalarMatch.span()
            return "scalar", line[span[0] + 1: span[1] - 1]
        raise ValueError("Not sure how to process <{}>".format(line))

    def _checkAddVariable(self, serpentName: str) -> bool:
        """Determine if a variable is to be processed

        Handles a few select cases

        1. The user has not requested any variables explicitely ->
           process everything
        2. This varible exists in the user requested variables and
           should be processed
        3. This variable is a homogenized group constant, e.g. INF_TOT
           or B1_SCATT_PROD. A little more logic here, since we support
           skipping infinite and/or b1 group constants with an attribute,
           and the variables set may not include INF_TOT in favor of just
           TOT. If those conditions are met, then the variable is processed

        If none of these are met, the variable should not be processed

        """
        if not self._variables:
            return True
        if serpentName in self._variables:
            return True
        if (
            serpentName.startswith("INF_")
            and self.infXS
            and serpentName[4:] in self._variables
        ):
            return True
        if (
            serpentName.startswith("B1_")
            and self.b1XS
            and serpentName[3:] in self._variables
        ):
            return True
        return False

    def _addMetadata(self, mdatakey, kind, values):
        if kind == "string":
            self._thisMetadata[mdatakey] = values
        elif kind == "scalar":
            self._thisMetadata[mdatakey] = float(values)
        elif kind == "vector":
            self._thisMetadata[mdatakey] = str2vec(values)
        else:
            raise ValueError(
                "Unsupported option metadata type {}".format(kind)
            )

    def _addResultData(self, pyname: str, values: str):
        data = str2vec(values)
        stored = self._tempArrays[pyname]
        # Don't want to append information from the same time step
        if len(stored) >= self._counter[FilePosition.RESULT]:
            return
        try:
            stored.append(data)
        except Exception as ee:
            raise SerpentToolsException(
                "Error appending {} data: {}".format(pyname, data)
            ) from ee

    def _getBurnupPosition(self) -> BurnupState:
        # TODO Remove these off by ones
        burnstep = self._counter[FilePosition.RESULT] - 1

        # Using hard coded day / burnup indicators
        # as they are variables that exist in the Serpent file
        # and changes to their names would _hopefully_ come with
        # some deprecation period or at least a notice
        days = self._tempArrays.get("burnDays")
        if days is None:
            currentDay = 0
        elif burnstep:
            currentDay = days[-1][0]
        else:
            currentDay = days[0][0]

        burnups = self._tempArrays.get("burnup")
        if burnups is None:
            currentBurnup = 0
        elif burnstep:
            currentBurnup = burnups[-1][0]
        else:
            currentBurnup = burnups[0][0]

        return BurnupState(burnstep, currentDay, currentBurnup)

    def _addUniverseData(self, serpentName: str, values: str):
        if self._currentUnivKey is None:
            raise ValueError(
                "No universe information (name, burnup, etc) found before "
                "group constant data"
            )
        universe = self._thisUniverses[self._currentUnivKey]

        # Get specific converter for this variable
        # Some can be simple str2vec, others must by split
        # by values and uncertainties
        converter = self._universeDataConverters.get(serpentName)
        if converter is None:
            converter = self._universeDataConverters[
                serpentName
            ] = varTypeFactory(serpentName)

        values, maybeUncs = converter(values)

        # Add expected value first, then uncertainty
        universe.addData(serpentName, values, uncertainty=False)
        if maybeUncs is not None:
            universe.addData(serpentName, values, uncertainty=True)

    def _transferTo(self, rf: ResultFile):
        while self._tempArrays:
            key, temp = self._tempArrays.popitem()
            data = temp.A
            # Only insert first row if not burnup present
            if data.shape[0] == 1:
                rf.resdata[key] = data.reshape(data.size)
            else:
                rf.resdata[key] = data

        while self._thisUniverses:
            ukey, univ = self._thisUniverses.popitem()
            rf.universes[ukey] = univ

        # Clean up metadata
        # TODO Don't re-convert floating scalars
        for converter, keys in METADATA_CONV.items():
            for key in keys.intersection(self._thisMetadata):
                rf.metadata[key] = converter(self._thisMetadata.pop(key))