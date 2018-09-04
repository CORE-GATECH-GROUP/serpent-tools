"""
Main entry point for top-level scripting

Called with::

    $ python -m serpentTools

"""
import re
import argparse

import six

import serpentTools
from serpentTools import settings

_VERB_MAP = {'v': {1: 'info', 2: 'debug'},
             'q': {1: 'error', 2: 'critical'}}
_VERB_MSG = {}
for key, items in six.iteritems(_VERB_MAP):
    _VERB_MSG[key] = ', '.join(
        ['{}: {}'.format(key * num, value)
         for num, value in six.iteritems(items)])


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

    return mainParser


def _seedInterface(args):
    """Interface to launch the uniquely-seeded file generation"""
    from serpentTools.seed import seedFiles
    seedFiles(args.file, args.N, seed=args.seed, outputDir=args.output_dir,
              link=args.link, length=args.length)


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
        args.func(args)


if __name__ == '__main__':
    main()
