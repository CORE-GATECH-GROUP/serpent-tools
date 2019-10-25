.. _parser-engines:

Parsing Engines
===============

.. currentmodule:: serpentTools.engines

The :class:`KeywordParser` and :class:`PatternReader`
contained in ``serpentTools/engines.py`` are part of the 
`drewtils <https://github.com/drewejohnson/drewtils>`_ v0.1.9 package and
are provided under the following license::

The MIT License (MIT)

Copyright (c) Andrew Johnson, 2017

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

These are designed to facilitate the parsing of files with a regular structure.
For example, the depletion files all contain "chunks" of data that are separated
by empty lines. Each chunk leads off with either the name of the material and
associated variable, or the metadata, e.g. ``ZAI``, ``DAYS``. These parsers
help break up these files into more digestible pieces.

.. note::
    
    For developers, it is not required that these classes be used. These are
    bundled with this project to eliminate the need to install extra packages.
    Some of the readers, like the
    :py:class:`~serpentTools.parsers.branching.BranchingReader` are not
    well suited for this type of parsing.

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: myclass.rst

    KeywordParser
    PatternReader

.. currentmodule:: serpentTools.parsers.base

The :class:`CSCStreamProcessor` is provided to help with reading
sparse matrices provided by Serpent. These are current found in the
depletion and fission matrix files.

.. autoclass:: serpentTools.parsers.base.CSCStreamProcessor
