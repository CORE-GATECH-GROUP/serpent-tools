from os.path import join, dirname
from setuptools import setup

import versioneer

with open('README.md') as readme:
    longDesc = readme.read()

classifiers = [
    'License :: OSI Approved :: MIT License',
]

installRequires = [
    'six',
    'numpy>=1.11.1',
    'matplotlib>=1.5.0',
    'ruamel.yaml<0.15',
    'drewtils>=0.1.8',  # file parsing tools
]

installVarYamlFrom = join('serpentTools', 'settings', 'variables.yaml')

pythonRequires = '>=3.5'

setupArgs = {
    'name': 'serpentTools',
    'python_requires': pythonRequires,
    'packages': ['serpentTools', 'serpentTools.parsers',
                 'serpentTools.objects', 'serpentTools.settings'],
    'url': 'https://github.com/CORE-GATECH-GROUP/serpent-tools',
    'description': ('A suite of parsers designed to make interacting with '
                    'SERPENT output files simple, scriptable, and flawless'),
    'long_description': longDesc,
    'test_suite': 'serpentTools.tests',
    'author': 'Andrew Johnson',
    'author_email': 'ajohnson400@gatech.edu',
    'maintainer': 'Dan Kotlyar',
    'maintainer_email': 'dan.kotlyar@me.gatech.edu',
    'classifiers': classifiers,
    'install_requires': installRequires,
    'keywords': 'SERPENT file parsers transport',
    'license': 'MIT',
    'version': versioneer.get_version(),
    'cmdclass': versioneer.get_cmdclass(),
    'data_files': [(dirname(installVarYamlFrom), [installVarYamlFrom])]
}

setup(**setupArgs)
