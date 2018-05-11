"""
Write out magic strings to magicPlotDocDecorator

"""
from os.path import join
from sys import version_info
import serpentTools

pyVersion = '{}.{}.{}'.format(*version_info[:3])

magicStrings = serpentTools.plot.PLOT_MAGIC_STRINGS
magicOpts = [
    '#. ``{key}``: {value}'.format(key=key, value=magicStrings[key])
    for key in sorted(magicStrings.keys())]

targetFile = join('develop', 'magicPlotOpts.rst')
print("Making magic plot conversion options with \n  python: {}"
      "\n  serpentTools: {}".format(pyVersion, serpentTools.__version__))
with open(targetFile, 'w') as target:
    target.write('\n'.join(magicOpts))

print('  done')
