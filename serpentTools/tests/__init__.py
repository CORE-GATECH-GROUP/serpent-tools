import os

from serpentTools import ROOT_DIR, settings

TEST_ROOT = os.path.join(ROOT_DIR, 'tests')

settings.rc['verbosity'] = 'critical'
