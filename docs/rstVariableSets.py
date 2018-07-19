"""
Script to display the variable groups used by the project
"""

from sys import version_info as pyVersInfo
from serpentTools import __version__ as sssPackVers
from serpentTools.utils import convertVariableName

import yaml

PYTHON_VERSION = '{}.{}.{}'.format(*pyVersInfo[:3])
VAR_FMTR = "  * ``{original}`` →  ``{converted}``\n"
OUT_FILE = 'variableGroups.rst'
IN_FILE = '../serpentTools/variables.yaml'
REF_FMT = '.. _{}-{}:\n\n'
SECTION_CHAR = '-'
SUBSECTION_CHAR = '~'


def makeHeading(title, subsection=False):
    hdr = SECTION_CHAR * (len(title) + 4)
    titleTT = '``{}``'.format(title)
    front = ('' if subsection else hdr)
    return '\n'.join((front, titleTT, hdr)) + '\n\n'


def makeVersionHeading(sVersion):
    tag = REF_FMT.format('vars', sVersion.replace('.', '-'))
    return tag + makeHeading(sVersion)


def makeVarGroupHeading(sVersion, groupName):
    tag = REF_FMT.format(groupName, sVersion.replace('.', '-'))
    return tag + makeHeading(groupName, True)


def varsToBullets(incomingVars):
    lines = "\n"
    for item in sorted(incomingVars):
        lines += VAR_FMTR.format(
            original=item,
            converted=convertVariableName(item))
    return lines + '\n'


if __name__ == '__main__':
    print(("Making variable sets file using\n"
           "  python: {}\n"
           "  serpentTools: {}").format(PYTHON_VERSION, sssPackVers))

    with open(IN_FILE) as stream:
        variables = yaml.safe_load(stream)
    baseDict = variables.pop('base')
    baseGroups = set(baseDict.keys())

    with open(OUT_FILE, 'w') as out:
        for version in sorted(variables, reverse=True):
            varSet = variables[version]
            out.write(makeVersionHeading(version))
            for group in sorted(varSet):
                out.write(makeVarGroupHeading(version, group))
                out.write(varsToBullets(varSet[group]))
        out.write(makeVersionHeading('base'))
        for group in sorted(baseGroups):
            baseVars = baseDict[group]
            out.write(makeVarGroupHeading('base', group))
            out.write(varsToBullets(baseVars))
