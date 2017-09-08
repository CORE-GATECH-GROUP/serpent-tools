from setuptools import setup

__version__ = '0.1.0rc1'

_classifiers = [
    'License :: OSI Approved :: MIT License',
]

setupArgs = {
    'name': 'serpentTools',
    'packages': ['serpentTools'],
    'version': __version__,
    'url': 'https://github.com/CORE-GATECH-GROUP/serpent-tools',
    'description': ('A suite of parsers designed to make interacting with '
                    'SERPENT output files simple, scriptable, and flawless'),
    'test_suite': 'serpentTools.tests',
    'author': 'Andrew Johnson',
    'author_email': 'ajohnson400@gatech.edu',
    'maintainer': 'Dan Kotlyar',
    'maintainer_email': 'dan.kotlyar@me.gatech.edu',
    'classifiers': _classifiers,
    'keywords': 'SERPENT file parsers transport',
    'license': 'MIT'
}

setup(**setupArgs)
