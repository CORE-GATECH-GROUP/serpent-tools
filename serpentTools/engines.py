# Copyright (c) Andrew Johnson, 2017
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Classes for simple file processing"""

import re

__all__ = ['KeywordParser', 'PatternReader']


class _TextProcessor(object):
    """Parent class for text processors."""

    def __init__(self, path):
        self.path = path
        self._stream = None
        self.line = ''

    def __enter__(self):
        self._stream = open(self.path, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stream.close()
        self._stream = None

    def _step(self):
        self.line = self._stream.readline()
        return self.line

    def _match(self, regexp):
        return re.match(regexp, self.line)

    def _search(self, regexp):
        return re.search(regexp, self.line)

    def _checkOpen(self):
        if self._stream is None:
            raise IOError('Parse must be used in a with <> as <>: block')

    def seekToTop(self):
        """Reset the file pointer to the start of the file."""
        self._stream.seek(0)


class KeywordParser(_TextProcessor):
    r"""
    Class for parsing a file for chunks separated by various keywords.

    Parameters
    ----------
    filePath: str
        Object to be read. Any object with ``read`` and ``close`` methods
    keys: Iterable
        List of keywords/phrases that will indicate the start of a chunk
    separators: Iterable or None
        List of additional phrases that can separate two chunks.
        If not given, will default to empty line ``'\n'``.
    eof: str
        String to indicate the end of the file

    Attributes
    ----------
    line: str
        Most recently read line
    """

    def __init__(self, filePath, keys, separators=None, eof=''):
        _TextProcessor.__init__(self, filePath)
        self._startMatch = self._makeMatchFromIterable(keys)
        separators = set(keys).union(
            set(separators) if separators else set(['\n']))
        self._endMatch = self._makeMatchFromIterable(separators)
        self._end = eof

    def yieldChunks(self):
        """
        Return each chunk of text as a generator.

        Yields
        ------
        list
            The next chunk in the file.
        """
        self._checkOpen()
        chunk = []
        while self._step() != self._end:
            if self._match(self._endMatch):
                if chunk:
                    yield chunk
                chunk = ([self.line] if self._match(self._startMatch) else [])
            elif chunk:
                chunk.append(self.line)
        if chunk:
            yield chunk

    def parse(self):
        """
        Parse the file and return a list of keyword blocks.

        Returns
        -------
        list
            List of key word argument chunks.

        """
        return list(self.yieldChunks())

    @staticmethod
    def _makeMatchFromIterable(args):
        return re.compile('|'.join([str(arg) for arg in args]))


class PatternReader(_TextProcessor):
    """
    Class that can read over a file looking for patterns.

    Parameters
    ----------
    filePath: str
        path to the file that is to be read

    Attributes
    ----------
    line: str
        Most recently read line
    match: regular expression match or None
        Match from the most recently read line
    """

    def __init__(self, filePath):
        _TextProcessor.__init__(self, filePath)
        self.match = None

    def searchFor(self, pattern):
        """
        Return true if the pattern is found.

        Parameters
        ----------
        pattern: str or compiled regular expression

        Returns
        -------
        bool: True if the pattern was found

        """
        self._checkOpen()
        regexp = re.compile(pattern) if isinstance(pattern, str) else pattern
        while self._step():
            self.match = self._search(regexp)
            if self.match:
                return True
        return False

    def yieldMatches(self, pattern):
        """
        Generator that returns all match groups that match pattern.

        Parameters
        ----------
        pattern: str or compiled regular expression
            Seek through the file and yield all match groups for lines that
            contain this patten.

        Yields
        ------
        sequential match groups

        """
        while self.searchFor(pattern):
            yield self.match
