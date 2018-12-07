from os.path import join
from os import getenv
from glob import glob
try:
    from setuptools import setup
    HAS_SETUPTOOLS = True
except ImportError:
    import warnings
    from distutils.core import setup
    warnings.warn('Installing with distutils. Use of setuptools is preferred')
    HAS_SETUPTOOLS = False

import versioneer


DATA_EXTS = {'*.m', '*.coe'}


def getDataFiles():
    """Return all matlab files from ``serpentTools/data``"""

    files = []
    for ext in DATA_EXTS:
        files.extend(glob(join('serpentTools', 'data', ext)))
    return files


with open('README.rst') as readme:
    longDesc = readme.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
]

installRequires = [
    'six>=1.11.0',
    'numpy>=1.15.1',
    'matplotlib>=2.0',
    'pyyaml==3.13',
]

if not getenv('TRAVIS', None) == 'true':
    # hack to install scipy if not on cluster
    # PR 45/44
    installRequires.append('scipy')

pythonRequires = '>=2.7,!=3.0,!=3.1,!=3.2,!=3.3,!=3.4'

setupArgs = {
    'name': 'serpentTools',
    'packages': ['serpentTools', 'serpentTools.parsers', 'serpentTools.utils',
                 'serpentTools.data', 'serpentTools.tests',
                 'serpentTools.objects', 'serpentTools.samplers'],
    'url': 'https://github.com/CORE-GATECH-GROUP/serpent-tools',
    'description': ('A suite of parsers designed to make interacting with '
                    'SERPENT output files simple, scriptable, and flawless'),
    'long_description': longDesc,
    'maintainer': 'Andrew Johnson',
    'maintainer_email': 'ajohnson400@gatech.edu',
    'author': 'serpentTools developer team',
    'classifiers': classifiers,
    'keywords': 'SERPENT file parsers transport',
    'license': 'MIT',
    'version': versioneer.get_version(),
    'package_data': {
        'serpentTools.data': ['data/{}'.format(ext) for ext in DATA_EXTS],
    },
    'cmdclass': versioneer.get_cmdclass(),
    'data_files': [
        ('serpentTools', ['serpentTools/variables.yaml', ]),
        ('serpentTools/data', getDataFiles()),
    ],
}
if HAS_SETUPTOOLS:
    setupArgs.update({
        'python_requires': pythonRequires,
        'install_requires': installRequires,
        'test_suite': 'serpentTools.tests'
    })

setup(**setupArgs)

if not HAS_SETUPTOOLS:
    warnings.warn(
        'The following packages are required to use serpentTools version '
        '{}:\n{}\nPlease ensure they are installed prior to use'
        .format(versioneer.get_version(), '\n'.join(installRequires)))
