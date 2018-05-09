"""
Script to make the default settings file
"""
from sys import version_info
from serpentTools import __version__
from serpentTools.settings import rc

pyVersion = '{}.{}.{}'.format(*version_info[:3])
print("Making settings file with\n  python: {}"
      "\n  serpentTools: {}".format(pyVersion, __version__))
FILE_PATH = 'defaultSettings.rst'

settingsString = rc.prettyPrint()
with open(FILE_PATH, 'w') as fp:
    fp.write(settingsString)

print('  done')
