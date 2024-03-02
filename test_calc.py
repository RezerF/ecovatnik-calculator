from insulation_calc.calculator import EcovataCalculator
from insulation_calc.common.constants import MaterialsCodes
from insulation_calc.common.my_types import MaterialsType
import unittest


class TestCalculator(unittest.TestCase):
    def test_calc(self):
        neded_materials = [
            MaterialsType(MaterialsCodes.IZOSPAN_AM),
            MaterialsType(MaterialsCodes.ECOVATA),
        ]

        calc = EcovataCalculator(100, 150, neded_materials)
        x = calc.get_materials_data_rows()
        self.assertEqual(len(x), 2)
        self.assertEqual(x[0].total_amount, 10375)
        self.assertEqual(x[1].total_amount, 70200)
