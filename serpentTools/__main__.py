"""
Main entry point for top-level scripting

Called with::

    $ python -m serpentTools

"""

import argparse

import six

import serpentTools
from serpentTools import settings

_VERB_MAP = {'v': {1: 'info', 2: 'debug'},
             'q': {1: 'error', 2: 'critical'}}
for key, items in six.iteritems(_VERB_MAP):
    _VERB_MAP[key]['msg'] = ', '.join(
        ['{}: {}'.format(key * num, value)
         for num, value in six.iteritems(items)])


def __buildParser():
    mainParser = argparse.ArgumentParser(prog='serpentTools')
    mainParser.add_argument('--version', action='version',
                            version=serpentTools.__version__)

    noiseLevel = mainParser.add_mutually_exclusive_group()
    noiseLevel.add_argument('-v', action='count',
                            help='increase verbosity {}'
                            .format(_VERB_MAP['v']['msg']))
    noiseLevel.add_argument('-q', action='count',
                            help='suppress warnings and errors {}'
                            .format(_VERB_MAP['q']['msg']))

    mainParser.add_argument('-c', '--config-file', type=str,
                            help='path to settings file')

    return mainParser


def __process(args):
    if 'config_file' in args and args.config_file is not None:
        settings.rc.loadYaml(args['config_file'])
        
    if 'v' in args:
        settings.rc.setValue('verbosity', _VERB_MAP['v'][args.v])
    elif 'q' in args:
        settings.rc.setValue('verbosity', _VERB_MAP['q'][args.q])

def main():
    """Driver function for CLI"""
    parser = __buildParser()
    args = parser.parse_args()
    print(args)
    __process(args)



if __name__ == '__main__':
    main()
