from os.path import join
from glob import glob
try:
    from setuptools import setup
    HAS_SETUPTOOLS = True
except ImportError:
    import warnings
    from distutils.core import setup
    warnings.warn('Installing with distutils. Use of setuptools is preferred')
    HAS_SETUPTOOLS = False


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
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

with open('./requirements.txt') as req:
    installRequires = req.read()

pythonRequires = ">=3.5,<3.9"

version = "0.9.3"

setupArgs = {
    'name': 'serpentTools',
    'packages': ['serpentTools', 'serpentTools.parsers', 'serpentTools.utils',
                 'serpentTools.data', 'serpentTools.io',
                 'serpentTools.objects', 'serpentTools.samplers'],
    'url': 'https://github.com/CORE-GATECH-GROUP/serpent-tools',
    'description': ('A suite of parsers designed to make interacting with '
                    'SERPENT output files simple, scriptable, and flawless'),
    'long_description': longDesc,
    'long_description_content_type': 'text/x-rst',
    'maintainer': 'Andrew Johnson',
    'maintainer_email': 'ajohnson400@gatech.edu',
    'author': 'serpentTools developer team',
    'classifiers': classifiers,
    'keywords': 'SERPENT file parsers transport',
    'license': 'MIT',
    'version': version,
    'package_data': {
        'serpentTools.data': ['data/{}'.format(ext) for ext in DATA_EXTS],
    },
    'include_package_data': True,
    'data_files': [
        ('serpentTools', ['serpentTools/variables.yaml', ]),
        ('serpentTools/data', getDataFiles()),
    ],
}
if HAS_SETUPTOOLS:
    setupArgs.update({
        'python_requires': pythonRequires,
        'install_requires': installRequires,
    })

setup(**setupArgs)

if not HAS_SETUPTOOLS:
    warnings.warn(
        'The following packages are required to use serpentTools version '
        '{}:\n{}\nPlease ensure they are installed prior to use'
        .format(version, '\n'.join(installRequires)))
