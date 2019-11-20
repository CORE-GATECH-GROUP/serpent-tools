"""
Functions to copy an input file ``N`` times with ``N`` randomly generated seeds
"""

from math import log10
import os
from os import path
from shutil import copy
import random

from serpentTools.messages import info

__all__ = ['seedFiles', 'generateSeed']


def _writeSeed(stream, bits, length):
    stream.write('\nset seed {}\n'.format(_seedFromBits(bits, length)))


def _getBitsForLength(length):
    """
    Return the number of bits required to obtain a random digit
    of a given length.
    """
    SLOPE = 0.3010142116935483
    OFFSET = 0.0701126088709696
    return int((length - OFFSET) / SLOPE)


def generateSeed(length):
    """
    Generate a random seed with ``length`` digits

    Parameters
    ----------
    length: int
        Positive number of digits in seed

    Returns
    -------
    int:
        Randomly generated seed with
        ``length`` digits

    Raises
    ------
    ValueError:
        If the value of ``length`` is non-positive
    TypeError:
        If ``length`` is not an integer, nor can be
        coerced into one with :func:`int`
    """
    if not isinstance(length, int):
        length = int(length)
    if length <= 0:
        raise ValueError("length must be positive, not {}".format(length))
    bits = _getBitsForLength(length)
    return _seedFromBits(bits, length)


def _seedFromBits(bits, length):
    seed = random.getrandbits(bits)
    while int(log10(seed)) + 1 != length:
        seed = random.getrandbits(bits)
    return seed


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
    """Write input files utilizing the ``include`` directive."""
    files = []
    for N in range(numSeeds):
        name = fileFmt.format(N)
        files.append(name)
        with open(name, 'w') as stream:
            stream.write('include \"{}\"\n'.format(inputFile))
            _writeSeed(stream, bits, length)
    return files


def _copy(inputFile, numSeeds, fileFmt, bits, length):
    """Write input files while copying the entire base input file."""
    files = []
    for N in range(numSeeds):
        name = fileFmt.format(N)
        copy(inputFile, name)
        files.append(name)
        with open(name, 'a') as stream:
            _writeSeed(stream, bits, length)
    return files


def seedFiles(inputFile, numSeeds, seed=None, outputDir=None, link=False,
              length=10):
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
        with ``'include <inputFile>'`` and the new seed declaration.
    length: int
        Number of digits for random seeds

    Returns
    -------
    list:
        List of the names of all files created

    Raises
    ------
    OSError:
        If the requested input file could not be found
        and ``link`` does not evaluate to true.
    ValueError:
        If the number of requested seeds is not a positive
        integer, nor can be converted to one, or if the length
        of the random seeds cannot be converted to a positive
        integer.
    TypeError:
        Raised if the values passed to ``length`` or ``nseeds``
        cannot be converted to integers with :func:`int`

    See Also
    --------
    :func:`generateSeed`
    :mod:`random`
    :func:`random.seed()`
    :func:`random.getrandbits()`

    """
    if '~' in inputFile:
        inputFile = os.path.expanduser(inputFile)

    if not path.exists(inputFile):
        raise OSError('Input file {} does not exist'.format(inputFile))

    if not isinstance(numSeeds, int):
        numSeeds = int(numSeeds)

    if numSeeds < 1:
        raise ValueError('Require positive number of files to create')

    bits = _getBitsForLength(length)

    random.seed(seed)

    inputPath = path.abspath(path.join(os.getcwd(), inputFile))
    inputRoot = path.dirname(inputPath)

    if outputDir is not None:
        fPrefix = path.abspath(path.join(inputRoot, outputDir))
        if not path.isdir(fPrefix):
            info('Creating directory at {}'.format(fPrefix))
            os.mkdir(fPrefix)
    else:
        fPrefix = inputRoot

    fileFmt = path.join(fPrefix, _makeFileFmt(inputFile))

    writeFunc = _include if link else _copy
    return writeFunc(inputPath, numSeeds, fileFmt, bits, length)
