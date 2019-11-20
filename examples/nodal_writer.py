# Copyright (c) 2017-2019 Serpent-Tools developer team, GTRC
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
# AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
Script and templates for writing branched xs from
serpentTools data file demo.coe

Each cross section is represented as a series of points along
a perturbation matrix, given at the top of the file. These
perturbations can be fuel temperature, control rod
insertion, soluble boron concentration, or other metrics that
may be of interest to reactor physicists. Burnup is also considered
a perturbation state for the sake of this script.

The perturbations are listed at the top of the file, according to
the following form::

    P0 : P0[0], P0[1], ...,
    P1 : P1[0], P1[1], ...,
    ...
    BU : BU[0], BU[1], ...,

where ``P0`` is the name of a perturbation and the vector
``P0[0], P0[1], ...`` represents the values of that perturbation.
It is not required that all perturbations have the same number of
values.

The remaining section of the file contains the group constants
for that singular universe. The values are presented per group, with
scattering being treated a little differently. More on that later.
Each group constant is presented along each perturbation according to
their order in the perturbation table above. This specific file
includes two perturbations and burnup (boron concentration and fuel
temperature), with three values for all perturbations, burnup included.
Therefore, each group-wise cross section block would have 27 entries for
a full perturbation table. The values are ordered as follows:

    (B0, F0, BU0), (B0, F0, BU1), (B0, F0, BU2),
    (B0, F1, BU:), (B0, F2, BU:), (B1, F:, BU:),
    (B2, F:, BU:)

Here, the Python-esque ``:`` operator is used to represent a slice of
all elements in the perturbation vector. The above block indicates that
first burnup is incremented for a single boron concentration and fuel
temperature. After all burnups have been given, then the fuel temperature is
incremented and all burnups are again written in order. After cycling through
all fuel temperatures, the boron index is incrememented. The pattern continues
until all boron states have been written, and the full perturbation table is
written.

The simulation file used is intended for two group calculation, and all values,
except scattering matrices, will be given group 1 first, then group 2.
The scattering matrices are currently given for four "groups", as a 2x2
scattering matrix is represented as a four-element vector. The four
"groups" as explained in the file are

    1. Group 1 -> Group 1
    2. Group 1 -> Group 2
    3. Group 2 -> Group 1
    4. Group 2 -> Group 2

"""

from io import StringIO


class Writer(object):
    """
    Class for writing an example cross section file.

    Parameters
    ----------
    collector: xs.Collector
        Object that read the branching file and stored the cross sections
        along the perturbation vector
    xsPerLine: int
        Number of cross sections / group constants to write per line
    floatFmt: str
        Formattable string used when writing floating point values
    strFmt: str
        Formattable string used when writing the names of the perturbations
    xsRemap: None or dict
        Dictionary used to find a replacement name for cross sections when
        writing.  Between each cross section block, the name of cross
        section and group will be written as ``# {name} group {g}``.
        When ``xsRemap`` is ``None``, the names are ``mixedCase`` as
        they appear in ``HomogUniv`` objects, e.g.  ``'infTot'``,
        ``'diffCoeff'``, etc. If ``xsRemap`` is a dictionary, it can
        be used to write a different name. Passing ``{'infTot': 'Total
        cross section'}`` would write ``'Total cross seciton'``
        instead of ``'infTot'``, but all other names would be unchanged.
    """

    def __init__(self, collector, xsPerLine=4, floatFmt="{:15.8E}",
                 strFmt="{:20s}", xsRemap=None):
        self.collector = collector
        self.perLine = 4
        self.floatFmt = floatFmt
        self.strFmt = strFmt
        xsRemap = {} if xsRemap is None else xsRemap
        assert isinstance(xsRemap, dict)
        self.xsRemap = xsRemap

    def write(self, universe, stream=None, mode='w'):
        """
        Write the contents of a single universe

        Parameters
        ----------
        universe: int or key
            Key of universe that exists in ``self.collector``. Typically
            integer values of homogenized universes from coefficient file
        stream: None or str or writeable
            If ``None``, return a string containing what would have been
            written to file. If a string, then write to this file. Otherwise,
            ensure that the object has a ``write`` method and write to this
            object
        mode: {'a', 'w'}
            Write or append to file. Only needed if stream is a string
        """

        universe = self.collector.universes[universe]
        if stream is None:
            return self._write(StringIO(), universe).getvalue()
        if isinstance(stream, str):
            assert mode in {'a', 'w'}, "Must be writable"
            with open(stream, mode) as out:
                return self._write(out, universe)
        assert hasattr(stream, 'write')
        return self._write(stream, universe)

    def _write(self, stream, universe):
        self._fullXsLine = "".join([self.floatFmt, ] * self.perLine) + "\n"
        stream.write("# Cross sections for universe {}\n"
                     .format(universe.univID))
        self._writePerts(stream)

        # Get index of group to write perturbed cross sections for each group
        groupIndex = len(universe.axis) - 1
        transpAx = (groupIndex, ) + tuple(range(groupIndex))

        for xsName, xsTable in universe.xsTables.items():
            name = self.xsRemap.get(xsName, xsName)
            xsData = xsTable.transpose(transpAx)

            self._writeUnivXs(stream, xsData, name)
        return stream

    def _writePerts(self, stream):
        for pertIndex, pert in enumerate(self.collector.perturbations):
            self._writeSinglePert(stream, pert,
                                  self.collector.states[pertIndex])
        self._writeSinglePert(
            stream, "Burnup [MWd/kgU]", self.collector.burnups)

    def _writeSinglePert(self, stream, name, values):
        stream.write(self.strFmt.format(name))
        for val in values:
            stream.write(self.floatFmt.format(val))
        stream.write('\n')

    def _writeUnivXs(self, stream, xsData, name):
        for groupIndex, groupMat in enumerate(xsData, start=1):
            stream.write("# {} group {}\n".format(name, groupIndex))
            groupVec = groupMat.ravel()
            start = 0
            nFull, nExtra = divmod(groupVec.size, self.perLine)
            for _step in range(nFull):
                stream.write(self._fullXsLine.format(
                    *groupVec[start:start + self.perLine]))
                start += self.perLine
            for step in range(nExtra):
                stream.write(self.floatFmt.format(groupVec[start + step]))
            stream.write("\n")
