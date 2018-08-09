"""
Test the seedFiles function
"""

from math import log10
import re
import random
from tempfile import mkdtemp
from unittest import TestCase
from os import remove, listdir, rmdir

from serpentTools import seedFiles, generateSeed

BASE_INPUT_FILE = "base-seed.sss"
BASE_CONTENTS = "% EMPTY FILE"
LENGTH_SEEDS = 10
NUM_FILES = 5

SEED_REGEX = re.compile(r'set seed (\d+)')
# Match the value used to set the serpent SEED
INCLUDE_REGEX = re.compile(r'include ".*{}"'.format(BASE_INPUT_FILE))


def setUpModule():
    """Initialize the base input file"""
    with open(BASE_INPUT_FILE, 'w') as out:
        out.write(BASE_CONTENTS)


def tearDownModule():
    """Remove the base input file."""
    remove(BASE_INPUT_FILE)


class SeedInspector(TestCase):
    """Class that just ensures that seeds are the correct length"""

    def examineSeed(self, seed):
        self.assertEqual(int(log10(seed)) + 1, LENGTH_SEEDS, msg=seed)


class SeedGeneratorTester(SeedInspector):
    """
    Test the capabilities of the generateSeed function
    """

    def test_badLength(self):
        """Try a variety of bad lengths and check for failure."""
        self.assertRaises(ValueError, generateSeed, -1)
        self.assertRaises(TypeError, generateSeed, {'fail': True})
        self.assertRaises(ValueError, generateSeed, 0)
        self.assertRaises(ValueError, generateSeed, '-1')

    def test_goodLength(self):
        """Check the length of random seeds given a variety of input types"""
        for typeFunc in [int, float, str]:
            actual = generateSeed(typeFunc(LENGTH_SEEDS))
            self.examineSeed(actual)


class SeedFileHelper(SeedInspector):

    @property
    def SEED(self):
        raise NotImplementedError

    @property
    def EXPECTED_SEEDS(self):
        raise NotImplementedError

    def _examineSeed(self, seed, index):
        SeedInspector.examineSeed(self, seed)
        if self.EXPECTED_SEEDS is not None:
            self.assertEqual(seed, self.EXPECTED_SEEDS[index])

    def _examineSeedsInFiles(self, files):
        self.assertEqual(NUM_FILES, len(files), msg="Number of files written.")
        for fileIndex, fileP in enumerate(files):
            self._examineSeedInFile(fileP, fileIndex)
            remove(fileP)

    def _examineSeedInFile(self, fileP, fileIndex):
        with open(fileP) as stream:
            lines = stream.read()
        match = SEED_REGEX.search(lines)
        self.assertTrue(match is not None,
                        msg="No seed setting found in {}".format(fileP))

        groups = match.groups()
        self.assertEqual(1, len(groups),
                         msg=("Did not find a solitary seed declaration "
                              "in {}".format(fileP)))
        actualSeed = int(groups[0])
        self._examineSeed(actualSeed, fileIndex)

    def _examineLinksInFiles(self, files):
        for fileP in files:
            with open(fileP) as stream:
                includeMatch = INCLUDE_REGEX.search(stream.read())
                self.assertTrue(includeMatch is not None, msg=fileP)

    def test_noOutdir_noLink(self):
        """
        Write the files and verify contents with no output dir nor linking.
        """
        files = seedFiles(BASE_INPUT_FILE, NUM_FILES, self.SEED,
                          outputDir=None, link=False)
        self._examineSeedsInFiles(files)

    def test_noOutdir_withLink(self):
        """
        Write the files and verify contents with no output dir.
        """
        files = seedFiles(BASE_INPUT_FILE, NUM_FILES, self.SEED,
                          outputDir=None, link=True)
        self._examineLinksInFiles(files)
        self._examineSeedsInFiles(files)

    def _setupAndTestWithDirectories(self, dirName):
        files = seedFiles(BASE_INPUT_FILE, NUM_FILES, self.SEED,
                          outputDir=dirName, link=False)
        itemsInDir = listdir(dirName)
        self.assertEqual(len(itemsInDir), NUM_FILES, msg=itemsInDir)
        self._examineSeedsInFiles(files)
        rmdir(dirName)

    def test_outDir(self):
        """Verify the file writer can write into existing directories."""
        tempDir = mkdtemp()
        self._setupAndTestWithDirectories(tempDir)

    def test_outDir_makeNew(self):
        """Verify the file writer can create new directories."""
        outDir = 'rm-seed-d'
        self._setupAndTestWithDirectories(outDir)


class SeedlessFileWriter(SeedFileHelper):
    """
    Test the writer without passing a value of ``seed`` to the function
    """

    EXPECTED_SEEDS = SEED = None


class SeededFileWriter(SeedFileHelper):
    """
    Test the reproducability of the file writer by explictely passing a seed.
    """

    @classmethod
    def setUpClass(cls):
        """
        Generate expected seeds before resetting the random state
        """
        cls.SEED = 123456789
        state = random.getstate()
        random.seed(cls.SEED)
        cls.EXPECTED_SEEDS = []
        for _n in range(NUM_FILES):
            candidate = generateSeed(LENGTH_SEEDS)
            cls.EXPECTED_SEEDS.append(candidate)
        random.setstate(state)


class SeedWriterErrorChecker(TestCase):
    """Check the error conditions for seedFiles."""

    def test_missingInput(self):
        """Verify an error is raised if the input does not exist"""
        with self.assertRaises(OSError):
            seedFiles("THIS SHOULD FAIL", NUM_FILES)

    def test_nonPosNumber(self):
        """Verify an error is raised if the number of files is non-positive"""
        badInputs = [0, -1, '0']
        for badN in badInputs:
            self.assertRaises(ValueError, seedFiles, BASE_INPUT_FILE, badN)


del SeedFileHelper


if __name__ == '__main__':
    from unittest import main
    main()
