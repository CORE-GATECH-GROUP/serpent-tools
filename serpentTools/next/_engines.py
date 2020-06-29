"""Classes for simple file processing

Provided through the drewtils python project
Distributed under an MIT License

Copyright (c) Andrew Johnson, 2017-2020

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import re


class _TextProcessor(object):
    """Parent class for text processors."""

    def __init__(self, stream):
        self.stream = stream
        self.line = ""

    def _step(self):
        self.line = self.stream.readline()
        return self.line

    def _match(self, regexp):
        return re.match(regexp, self.line)

    def _search(self, regexp):
        return re.search(regexp, self.line)

    def seekToTop(self):
        """Reset the file pointer to the start of the file."""
        self.stream.seek(0)


class KeywordParser(_TextProcessor):
    r"""
    Class for parsing a file for chunks separated by various keywords.

    Parameters
    ----------
    stream : readable buffer
        Stream to be processed.
    keys : iterable of str
        List of keywords/phrases that will indicate the start of a chunk
    separators : iterable of str, optional
        List of additional phrases that can separate two chunks.
        If not given, will default to empty line ``'\n'``.
    eof : str, optional
        String to indicate the end of the file

    Attributes
    ----------
    line : str
        Most recently read line
    stream : readable buffer
        Stream that is currently processed

    """

    def __init__(self, stream, keys, separators=None, eof=""):
        super().__init__(stream)
        self._startMatch = re.compile("|".join([str(arg) for arg in keys]))
        separators = set(keys).union(separators or {"\n"})
        self._endMatch = re.compile("|".join([str(arg) for arg in separators]))
        self._end = eof

    def __iter__(self):
        """Yield all chunks in the stream

        Yields
        ------
        list of str
            Successive chunks of text

        """
        chunk = []
        while self._step() != self._end:
            if self._match(self._endMatch):
                if chunk:
                    yield chunk
                chunk = [self.line] if self._match(self._startMatch) else []
            elif chunk:
                chunk.append(self.line)
        if chunk:
            yield chunk
