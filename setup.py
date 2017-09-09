from setuptools import setup

_version = '0.1.0rc2'

_classifiers = [
    'License :: OSI Approved :: MIT License',
]

_requires = [
    'drewtils>=0.1.2',  # file parsing tools
]

setupArgs = {
    'name': 'serpentTools',
    'packages': ['serpentTools'],
    'version': _version,
    'url': 'https://github.com/CORE-GATECH-GROUP/serpent-tools',
    'description': ('A suite of parsers designed to make interacting with '
                    'SERPENT output files simple, scriptable, and flawless'),
    'test_suite': 'serpentTools.tests',
    'author': 'Andrew Johnson',
    'author_email': 'ajohnson400@gatech.edu',
    'maintainer': 'Dan Kotlyar',
    'maintainer_email': 'dan.kotlyar@me.gatech.edu',
    'classifiers': _classifiers,
    'install_requires': _requires,
    'keywords': 'SERPENT file parsers transport',
    'license': 'MIT'
}

setup(**setupArgs)
