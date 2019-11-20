"""Test the depletion file."""
from unittest import TestCase
from os import remove

from numpy import array
from numpy.testing import assert_equal

from io import BytesIO
from serpentTools.data import getFile
from serpentTools.settings import rc
from serpentTools.parsers.depletion import (
    DepletionReader, getMaterialNameAndVariable, getMatlabVarName,
    prepToMatlab, deconvert,
)
from serpentTools.utils import DEPLETION_PLOT_LABELS

from tests import (
    LoggerMixin, MatlabTesterHelper,
    plotTest, plotAttrTest,
)


DEP_FILE = 'ref_dep.m'
DEP_FILE_PATH = getFile(DEP_FILE)

FILE_WITH_UNDERSCORES = 'underscores_dep.m'
ORIG_FUEL = "fuel"
NEW_FUEL_NAME = "fuel_0"


def setUpModule():
    """
    Set up the module

    *. Create a new file with underscores
    """
    with open(DEP_FILE_PATH) as incoming:
        with open(FILE_WITH_UNDERSCORES, 'w') as out:
            for line in incoming:
                out.write(line.replace(ORIG_FUEL, NEW_FUEL_NAME))


def tearDownModule():
    """
    Tear down the module

    *. Remove new file with underscores
    """
    remove(FILE_WITH_UNDERSCORES)


class _DepletionTestHelper(TestCase):
    """Base class to setup the depletion reader and material tests."""

    PROCESS_TOTAL = True
    MATERIAL = ORIG_FUEL
    FILE = DEP_FILE_PATH
    EXPECTED_VARIABLES = ['BURNUP', 'ADENS', 'ING_TOX']

    @classmethod
    def setUpClass(cls):
        # Silence the debugger but we don't care about checking messages
        logger = LoggerMixin()
        logger.attach()

        cls.expectedMaterials = {cls.MATERIAL, }
        if cls.PROCESS_TOTAL:
            cls.expectedMaterials.add('total')
        # Set some settings to control the output
        with rc as tempRC:
            tempRC['verbosity'] = 'debug'
            tempRC['depletion.materials'] = [cls.MATERIAL, ]
            tempRC['depletion.processTotal'] = cls.PROCESS_TOTAL
            tempRC['depletion.materialVariables'] = (
                cls.EXPECTED_VARIABLES
            )
            cls.reader = DepletionReader(cls.FILE)
            cls.reader.read()
        logger.detach()


class DepletionTester(_DepletionTestHelper):
    """Class that tests the functionality of the depletion reader."""

    def test_metadata(self):
        """Test the metadata storage for the reader."""
        expectedMetadata = {
            'zai':
                [621490, 541350, 922350, 942390, 50100, 666, 0],
            'names':
                ['Sm149', 'Xe135', 'U235', 'Pu239', 'B10', 'lost', 'total'],
            'burnup': [0.00000E+00, 1.93360E-02, 3.86721E-02, 1.16016E-01,
                       1.93360E-01, 2.90041E-01, 3.86721E-01, 6.76762E-01,
                       9.66802E-01, 1.45020E+00, 1.93360E+00, 2.90041E+00,
                       3.86721E+00, 4.83401E+00],
            'days': [0.00000E+00, 5.00000E-01, 1.00000E+00, 3.00000E+00,
                     5.00000E+00, 7.50000E+00, 1.00000E+01, 1.75000E+01,
                     2.50000E+01, 3.75000E+01, 5.00000E+01, 7.50000E+01,
                     1.00000E+02, 1.25000E+02]
        }
        expectedKeys = set(expectedMetadata)
        actualKeys = set(self.reader.metadata.keys())
        self.assertSetEqual(expectedKeys, actualKeys)
        for key, expectedValue in expectedMetadata.items():
            assert_equal(self.reader.metadata[key], expectedValue)

    def test_ReadMaterials(self):
        """Verify the reader stored the correct materials."""
        self.assertSetEqual(set(self.reader.materials.keys()),
                            self.expectedMaterials)

    def test_getitem(self):
        """Verify the getitem approach to obtaining materials."""
        with self.assertRaises(KeyError):
            self.reader['this should not work']
        for name, mat in self.reader.materials.items():
            fromGetItem = self.reader[name]
            self.assertIs(mat, fromGetItem, msg=mat)

    @plotTest
    def test_plotFewIso(self):
        """Test the basic functionality of the depletion plot"""
        mat = self.reader[self.MATERIAL]
        ax = mat.plot('days', 'adens', names='U235')
        plotAttrTest(
            self, ax, xlabel=DEPLETION_PLOT_LABELS['days'],
            ylabel=DEPLETION_PLOT_LABELS['adens'],
            xscale='linear', yscale='linear',
            legendLabels=[],
        )
        # clear the plot for a second go

        ax.clear()
        mat.plot('burnup', 'adens', names=['U235', 'Xe135'], loglog=True)
        plotAttrTest(
            self, ax, xlabel=DEPLETION_PLOT_LABELS['burnup'],
            xscale='log', yscale='log', legendLabels=['U235', 'Xe135'],
        )

    @plotTest
    def test_plotFormatting(self):
        mat = self.reader[self.MATERIAL]
        ax = mat.plot('days', 'adens', names='U235', legend=True,
                      labelFmt="{mat}-{iso}")
        plotAttrTest(
            self, ax, legendLabels=[self.MATERIAL + '-U235'])


class DepletedMaterialTester(_DepletionTestHelper):
    """Class that tests the functionality of the DepletedMaterial class"""

    def setUp(self):
        self.material = self.reader.materials[self.MATERIAL]
        self.requestedDays = [0.0, 0.5, 1.0, 5.0, 10.0, 25.0, 50.0]
        self.fuelBU = self.material.burnup

    def test_materials(self):
        """Verify the materials are read in properly."""
        self.assertIn(self.MATERIAL, self.reader.materials)
        expectedAdens = array([
            [0.00000E+00, 2.44791E-10, 1.07741E-09, 7.54422E-09, 1.54518E-08,
             2.45253E-08, 3.05523E-08, 3.98843E-08, 4.28827E-08, 4.37783E-08,
             4.46073E-08, 4.58472E-08, 4.73590E-08, 4.84031E-08],
            [0.00000E+00, 3.92719E-09, 5.62744E-09, 6.09339E-09, 6.14629E-09,
             6.05726E-09, 6.14402E-09, 6.13795E-09, 6.10821E-09, 6.13674E-09,
             6.18320E-09, 6.18233E-09, 6.08629E-09, 6.35706E-09],
            [5.58287E-04, 5.57764E-04, 5.57298E-04, 5.55440E-04, 5.53500E-04,
             5.51257E-04, 5.48871E-04, 5.41946E-04, 5.35434E-04, 5.24946E-04,
             5.14643E-04, 4.95299E-04, 4.78407E-04, 4.58932E-04],
            [0.00000E+00, 1.63219E-08, 6.37555E-08, 4.71450E-07, 1.11725E-06,
             2.08488E-06, 3.13490E-06, 6.42737E-06, 9.58635E-06, 1.44874E-05,
             1.90933E-05, 2.73021E-05, 3.42000E-05, 4.11589E-05],
            [0.00000E+00, 9.58524E-34, 6.02782E-33, 6.83433E-32, 2.06303E-31,
             5.02500E-31, 1.07151E-30, 4.79600E-30, 1.75720E-29, 1.46446E-28,
             3.98274E-28, 1.04091E-27, 3.12542E-27, 6.72465E-27],
            [0.00000E+00, 2.90880E-14, 5.57897E-14, 1.62569E-13, 2.75249E-13,
             4.06673E-13, 5.46031E-13, 9.58962E-13, 1.35027E-12, 1.99694E-12,
             2.64702E-12, 3.90487E-12, 5.05218E-12, 6.43096E-12],
            [6.88332E-02, 6.88337E-02, 6.88341E-02, 6.88357E-02, 6.88374E-02,
             6.88394E-02, 6.88415E-02, 6.88476E-02, 6.88535E-02, 6.88632E-02,
             6.88729E-02, 6.88917E-02, 6.89087E-02, 6.89291E-02],
        ])
        expectedIngTox = array([
            [0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00],
            [0.00000E+00, 3.56712E+07, 5.11147E+07, 5.53470E+07, 5.58276E+07,
             5.50189E+07, 5.58069E+07, 5.57517E+07, 5.54817E+07, 5.57408E+07,
             5.61628E+07, 5.61549E+07, 5.52826E+07, 5.77420E+07],
            [1.68091E+00, 1.67934E+00, 1.67793E+00, 1.67234E+00, 1.66650E+00,
             1.65974E+00, 1.65256E+00, 1.63171E+00, 1.61210E+00, 1.58053E+00,
             1.54951E+00, 1.49126E+00, 1.44041E+00, 1.38177E+00],
            [0.00000E+00, 7.63264E+00, 2.98141E+01, 2.20465E+02, 5.22464E+02,
             9.74958E+02, 1.46598E+03, 3.00564E+03, 4.48288E+03, 6.77478E+03,
             8.92865E+03, 1.27673E+04, 1.59930E+04, 1.92472E+04],
            [0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00],
            [0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,
             0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00],
            [5.22355E+01, 1.16651E+09, 1.10827E+09, 1.25209E+09, 1.44102E+09,
             1.49595E+09, 1.66322E+09, 1.80206E+09, 1.79453E+09, 1.79100E+09,
             1.80188E+09, 1.75346E+09, 1.60021E+09, 1.89771E+09],
        ])
        self.assertListEqual(self.material.zai,
                             self.reader.metadata['zai'])
        assert_equal(self.material.adens, expectedAdens)
        assert_equal(self.material['ingTox'], expectedIngTox)

    def test_getValues_burnup_full(self):
        """ Verify that getValues can produce the full burnup vector."""
        actual = self.material.getValues('days', 'burnup', )
        assert_equal(actual, self.fuelBU)

    def test_getValues_burnup_slice(self):
        """Verify depletedMaterial getValues correctly slices a vector."""
        actual = self.material.getValues('days', 'burnup', self.requestedDays)
        expected = [0.0E0, 1.90317E-2, 3.60163E-2, 1.74880E-1, 3.45353E-01,
                    8.49693E-01, 1.66071E0]
        assert_equal(actual, expected)

    def test_getValues_adens(self):
        """Verify getValues can return a requested subsection."""
        names = ['Xe135', 'U235', 'lost']
        zai = [541350, 922350, 666]
        expected = array([
            [0.00000E+00, 3.92719E-09, 5.62744E-09, 6.14629E-09, 6.14402E-09,
             6.10821E-09, 6.18320E-09],
            [5.58287E-04, 5.57764E-04, 5.57298E-04, 5.53500E-04, 5.48871E-04,
             5.35434E-04, 5.14643E-04],
            [0.00000E+00, 2.90880E-14, 5.57897E-14, 2.75249E-13, 5.46031E-13,
             1.35027E-12, 2.64702E-12],
        ], float)
        usingNames = self.material.getValues('days', 'adens', names=names,
                                             timePoints=self.requestedDays)
        usingZai = self.material.getValues('days', 'adens', zai=zai,
                                           timePoints=self.requestedDays)
        assert_equal(usingNames, expected, err_msg="Using <names> argument")
        assert_equal(usingZai, expected, err_msg="Using <zai> argument")

    def test_getValues_raisesError_badTime(self):
        """Verify that a ValueError is raised for non-present requested days.""" # noqa
        badDays = [-1, 0, 50]
        with self.assertRaises(KeyError):
            self.material.getValues('days', 'adens', timePoints=badDays)

    def test_fetchData(self):
        """Verify that key errors are raised when bad data are requested."""
        with self.assertRaises(KeyError):
            self.material['fake units']

    def test_plotter(self):
        """Verify the plotting functionality is operational."""
        self.material.plot('days', 'adens',
                           names=['Xe135', 'U235'])


class UnderscoreDepMaterialTester(DepletedMaterialTester):
    """Class that reads from a file with underscored fuel names"""

    MATERIAL = NEW_FUEL_NAME
    FILE = FILE_WITH_UNDERSCORES


class DepletionUtilTester(TestCase):
    """
    Test case that tests some utilities used by the DepletionReader
    """

    BAD_0 = "MAT_FUEL_DOES_NOT_EXIST"
    BAD_1 = "BAD_FUEL_ADENS"

    VAR_CHUNK = ['{} = [\n'.format(BAD_0), ]

    def test_getMaterialAndVariable(self):
        """Test the function for extracting names and variables"""
        valid = {
            'MAT_fuel_ADENS': ('fuel', 'ADENS'),
            'TOT_ING_TOX': ('total', 'ING_TOX'),
            'MAT_FUEL_2_H': ('FUEL_2', 'H'),
        }
        for matVar, (expName, expVar) in valid.items():
            actName, actVar = getMaterialNameAndVariable(matVar)
            self.assertEqual(expName, actName, msg=matVar)
            self.assertEqual(expVar, actVar, msg=matVar)
        with self.assertRaises(ValueError):
            getMaterialNameAndVariable(self.BAD_0)
            getMaterialNameAndVariable(self.BAD_1)

    def test_getMatlabVarName(self):
        self.assertEqual(self.BAD_0, getMatlabVarName(self.VAR_CHUNK))
        self.assertEqual(self.BAD_0, getMatlabVarName(self.VAR_CHUNK[0]))


class DepMatlabExportHelper(MatlabTesterHelper):
    """
    Class that tests the saveAsMatlab method for DepletionReaders
    """

    @classmethod
    def setUpClass(cls):
        cls.reader = DepletionReader(DEP_FILE_PATH)
        cls.reader.read()

    def test_toMatlab(self):
        """
        Verify that the reader can write data to a .mat file
        """
        from scipy.io import loadmat
        stream = BytesIO()
        self.reader.toMatlab(stream, self.RECONVERT)
        loaded = loadmat(stream)
        self.check(loaded)
        self.checkMetadata(loaded)

    def check(self, loaded):
        """Check the contents of the data loaded from the .mat file"""
        for materialName, material in self.reader.materials.items():
            for variableName, data in material.data.items():
                expectedName = self.constructExpectedVarName(
                    materialName, variableName)

                # savemat saves vectors as row vectors by default

                if len(data.shape) == 1:
                    data = data.reshape(1, data.size)
                assert expectedName in loaded, (
                    "Variable {} from material {}"
                    .format(materialName, variableName))
                assert_equal(
                    loaded[expectedName], data,
                    err_msg="{} {}".format(materialName, variableName))

    def checkMetadata(self, loaded):
        for key, data in self.reader.metadata.items():
            expected = key.upper() if self.RECONVERT else key
            assert expected in loaded, (
                "Missing {} from metadata".format(expected))

    def constructExpectedVarName(self, material, variable):
        """
        Return name of the array in the .mat file for a material and variable
        """
        raise NotImplementedError


class DepMatlabExportConverter(DepMatlabExportHelper):
    """Mixin class that converts variables back to orgiginal form"""

    RECONVERT = True

    @staticmethod
    def constructExpectedVarName(material, variable):
        return deconvert(material, variable)


class DepMatlabExportNoConverter(DepMatlabExportHelper):
    """Mixin class that does not convert to original form"""

    RECONVERT = False

    @staticmethod
    def constructExpectedVarName(material, variable):
        return prepToMatlab(material, variable)


del DepMatlabExportHelper
