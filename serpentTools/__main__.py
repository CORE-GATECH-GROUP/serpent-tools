"""
Main entry point for top-level scripting

Called with::

    $ python -m serpentTools

"""
import re
import argparse
from os.path import splitext

import serpentTools
from serpentTools import settings
from serpentTools.messages import info, error
from serpentTools.parsers import inferReader
from serpentTools.io import MatlabConverter

_VERB_MAP = {'v': {1: 'info', 2: 'debug'},
             'q': {1: 'error', 2: 'critical'}}
_VERB_MSG = {}
for key, items in _VERB_MAP.items():
    _VERB_MSG[key] = ', '.join(
        ['{}: {}'.format(key * num, value)
         for num, value in items.items()])


def __buildParser():
    mainParser = argparse.ArgumentParser(prog='serpentTools')
    mainParser.add_argument('--version', action='version',
                            version=serpentTools.__version__)

    noiseLevel = mainParser.add_mutually_exclusive_group()
    noiseLevel.add_argument('-v', action='count',
                            help='increase verbosity {}'
                            .format(_VERB_MSG['v']))
    noiseLevel.add_argument('-q', action='count',
                            help='suppress warnings and errors {}'
                            .format(_VERB_MSG['q']))

    mainParser.add_argument('-c', '--config-file', type=str,
                            help='path to settings file')

    subParsers = mainParser.add_subparsers(title='sub-commands',
                                           help='sub-command help')

    # Add file seeding sub-command
    seedParser = subParsers.add_parser('seed',
                                       help='copy an input file with unique '
                                            'random number seeds')
    seedParser.add_argument('file', type=str,
                            help='input file to copy')
    seedParser.add_argument('N', type=int,
                            help='integer number of files to create')
    seedParser.add_argument('--seed', type=int, default=None,
                            help='Seed to start with the builtin random '
                                 'generator')
    seedParser.add_argument('-l', '--length', type=int, default=10,
                            help='Number of digits in random seeds')
    seedParser.add_argument('--output-dir', type=str, default=None,
                            help='Copy files into this directory')
    seedParser.add_argument('--link', action='store_true',
                            help='Reference input file with include statement,'
                                 ' rather than copying the whole file')
    seedParser.set_defaults(func=_seedInterface)

    # print the default settings to stdout
    listSettingsP = subParsers.add_parser('list',
                                          help='show the default settings')
    listSettingsP.add_argument('-p', '--pattern', type=str, default='.*',
                               help='show settings that match this pattern')
    listSettingsP.set_defaults(func=_listDefaults)

    # convert input file to matlab
    matlabParser = subParsers.add_parser(
        'to-matlab', help="convert output file to .mat file")
    matlabParser.add_argument('file', type=str,
                              help="output file to read and convert")
    matlabParser.add_argument(
        '-o', '--output', type=str, default=None,
        help='Name of output file to write. '
             'If not given, replace extension with .mat')
    matlabParser.add_argument(
        '-a', '--append', default=False, action='store_true',
        help="Append to existing file if found. Otherwise overwrite. "
             "Default: False")
    matlabParser.add_argument(
        '--format', type=str, choices={'5', '4'}, default='5',
        help="Format of file to write. 4 for MATLAB 4, 5 for MATLAB 5+. "
             "Default: 5")
    matlabParser.add_argument(
        '-l', '--longNames', default=False, action='store_true',
        help="Allow variable names up to 63 characters. "
        "Otherwise, enforce 31 character names. Default: False")
    matlabParser.add_argument(
        '--large', help="Don't compress arrays when writing.",
        action='store_true', default=False)
    matlabParser.add_argument(
        '--oned', type=str, choices={'row', 'col'}, default='row',
        help="Write 1D arrays are row or column vectors")
    matlabParser.set_defaults(func=_toMatlab)

    return mainParser


def _toMatlab(args):
    """
    Write contents of a file to matlab.

    Return codes:
        0: all good
        1: need scipy
        3: conversion for file type not supported yet
    """
    inFile = args.file
    outFile = args.output
    if not outFile:
        base = splitext(inFile)[0]
        outFile = base + '.mat'

    # inferReader returns the class, but we need an instance
    reader = inferReader(inFile)(inFile)
    try:
        converter = MatlabConverter(reader, outFile)
    except ImportError:
        error("scipy >= 1.0 required to convert to matlab")
        return 1
    except NotImplementedError:
        error("Conversion not supported for {} reader at this time. "
              .format(reader.__class__.__name__))
        error("Please alert the developers of your need.")
        return 3
    reader.read()
    converter.convert(True, append=args.append,
                      format=args.format, longNames=args.longNames,
                      compress=not args.large, oned=args.oned)
    if not args.q:
        if args.v:
            info("Wrote contents of {} to {}".format(inFile, outFile))
        else:
            print(outFile)

    return 0


def _seedInterface(args):
    """Interface to launch the uniquely-seeded file generation"""
    from serpentTools.seed import seedFiles
    files = seedFiles(args.file, args.N, seed=args.seed,
                      outputDir=args.output_dir,
                      link=args.link, length=args.length)
    if not args.q:
        print('\n'.join(files))
    return 0


def _listDefaults(args):
    """List the default settings"""
    from serpentTools.settings import defaultSettings
    pattern = re.compile(args.pattern)
    for name in sorted(defaultSettings.keys()):
        if re.match(pattern, name):
            values = defaultSettings[name]
            print('{}: {}'.format(name, values[
                'default' if args.q else 'description']))
            if not args.q:
                print('  default: {}'.format(values['default']))
            if args.v and values.get('options', 'default') != 'default':
                print('  options: {}'.format(values['options']))


def __process(args):
    if 'config_file' in args and args.config_file is not None:
        settings.rc.loadYaml(args['config_file'])

    if args.v:
        level = min(args.v, max(_VERB_MAP['v'].keys()))
        settings.rc.setValue('verbosity', _VERB_MAP['v'][level])
    elif args.q:
        level = min(args.q, max(_VERB_MAP['q'].keys()))
        settings.rc.setValue('verbosity', _VERB_MAP['q'][level])


def main():
    """Driver function for CLI"""
    parser = __buildParser()
    args = parser.parse_args()
    __process(args)
    if 'func' in args:
        return args.func(args)


if __name__ == '__main__':
    from sys import exit
    exit(main())
