"""
Function to copy an input file N times with N randomly generated seeds
"""

import os
from os import path
from shutil import copy
import random

from six.moves import range

from serpentTools.messages import error, debug

__all__ = ['seedFiles']
SLOPE = 0.3010142116935483
OFFSET = 0.0701126088709696


def _writeSeed(stream, bits, length):
    seed = random.getrandbits(bits)
    while len(str(seed)) != length:
        seed = random.getrandbits(bits)
    stream.write('\nset seed {}\n'.format(seed))


def _makeFileFmt(inputFile):
    baseName = path.basename(inputFile)
    if '.' in baseName:
        s = baseName.split('.')
        base = s[0]
        ext = '.' + '.'.join(s[1:])
    else:
        base = baseName
        ext = ''
    return base + '_{}' + ext


def _include(inputFile, numSeeds, fileFmt, bits, length):
    for N in range(numSeeds):
        name = fileFmt.format(N)
        with open(name, 'w') as stream:
            stream.write('include \"{}\"\n'.format(inputFile))
            _writeSeed(stream, bits, length)


def _copy(inputFile, numSeeds, fileFmt, bits, length):
    for N in range(numSeeds):
        name = fileFmt.format(N)
        copy(inputFile, name)
        with open(name, 'a') as stream:
            _writeSeed(stream, bits, length)


def seedFiles(inputFile, numSeeds, seed=None, outputDir=None, link=False,
              digits=10):
    """
    Copy input file multiple times with unique seeds.

    Parameters
    ----------
    inputFile: str
        Path to input file
    numSeeds: int
        Number of files to create
    seed: int
        Optional argument to set the seed of the builtin random
        number generator
    outputDir: str
        Path to desired output directory. Files will be copied here.
        If the folder does not exist, try to make the directory. Assumes path
        relative to directory that contains the input file
    link: bool
        If True, do not copy the full file. Instead, create a new file
        with 'include <inputFile>' and the new seed declaration.
    digits: int
        Average number of digits for random seeds

    See Also
    --------
    :py:mod:`random`
    :py:func:`random.seed()`
    :py:func:`random.getrandbits()`

    """
    if '~' in inputFile:
        inputFile = os.path.expanduser(inputFile)

    if not path.exists(inputFile):
        error('Input file {} does not exist'.format(inputFile))
        return

    if numSeeds < 1:
        error('Require positive number of files to create')
        return

    if digits < 1:
        error('Require positive number of digits in random seeds')
    bits = int((digits - OFFSET) / SLOPE)

    random.seed(seed)

    inputPath = path.abspath(path.join(os.getcwd(), inputFile))
    inputRoot = path.dirname(inputPath)

    if outputDir is not None:
        fPrefix = path.abspath(path.join(inputRoot, outputDir))
        if not path.isdir(fPrefix):
            debug('Creating directory at {}'.format(fPrefix))
            os.mkdir(fPrefix)
    else:
        fPrefix = inputRoot

    fileFmt = path.join(fPrefix, _makeFileFmt(inputFile))

    writeFunc = _include if link else _copy
    writeFunc(inputPath, numSeeds, fileFmt, bits, digits)

    return
