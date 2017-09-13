from setuptools import setup

version = '0.1.0rc8'

classifiers = [
    'License :: OSI Approved :: MIT License',
]

installRequires = [
    'numpy>=1.11.1',
    'matplotlib>=1.5.0',
    'PyYAML>=3.12',
    'dict-digger>=0.2.1',  # for parsing the settings
    'drewtils>=0.1.3',  # file parsing tools
]

pythonRequires = '>=3.5'

setupArgs = {
    'name': 'serpentTools',
    'python_requires': pythonRequires,
    'packages': ['serpentTools', 'serpentTools.parsers'],
    'version': version,
    'url': 'https://github.com/CORE-GATECH-GROUP/serpent-tools',
    'description': ('A suite of parsers designed to make interacting with '
                    'SERPENT output files simple, scriptable, and flawless'),
    'test_suite': 'serpentTools.tests',
    'author': 'Andrew Johnson',
    'author_email': 'ajohnson400@gatech.edu',
    'maintainer': 'Dan Kotlyar',
    'maintainer_email': 'dan.kotlyar@me.gatech.edu',
    'classifiers': classifiers,
    'install_requires': installRequires,
    'keywords': 'SERPENT file parsers transport',
    'license': 'MIT'
}

setup(**setupArgs)
