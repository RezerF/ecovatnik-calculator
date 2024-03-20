from insulation_calc.calculator import EcovataCalculator, CommonCalculator
from insulation_calc.common.constants import MaterialsCodes
from insulation_calc.common.my_types import MaterialsType
import unittest


class TestCalculator(unittest.TestCase):
    # def test_calc(self):
    #     needed_materials = [
    #         MaterialsType(MaterialsCodes.IZOSPAN_AM),
    #         MaterialsType(MaterialsCodes.ECOVATA),
    #     ]
    #
    #     calc = EcovataCalculator(100, 150, needed_materials)
    #     x = calc.get_materials_data_rows()
    #     self.assertEqual(len(x), 2)
    #     self.assertEqual(x[0].total_amount, 10375)
    #     self.assertEqual(x[1].total_amount, 70200)

    def test_calc_common_materials(self):
        common_calc = CommonCalculator(
            sqr_floor=1,
            width_floor=200,
            sqr_wall=0,
            width_wall=1,
            sqr_roof=0,
            width_roof=250,
            is_wood_house=True,
            is_floor_dop_work=True,
            is_wall_dop_work=True,
            is_roof_dop_work=True,
        )
        x = common_calc.calculate_dop_work_materials()
        print(x)

    def test_calc_common_work_costs(self):
        common_calc = CommonCalculator(
            sqr_floor=1,
            width_floor=200,
            sqr_wall=1,
            width_wall=200,
            sqr_roof=1,
            width_roof=250,
            is_wood_house=True,
            is_floor_dop_work=True,
            is_wall_dop_work=True,
            is_roof_dop_work=True,
        )
        x = common_calc.calculate_dop_work_costs()
        print(x)

    def test_calc_ecovata(self):
        common_calc = CommonCalculator(
            sqr_floor=100,
            width_floor=200,
            sqr_wall=200,
            width_wall=200,
            sqr_roof=200,
            width_roof=200,
            is_wood_house=False,
            is_floor_dop_work=False,
            is_wall_dop_work=False,
            is_roof_dop_work=False,
        )
        ves = common_calc.calculate_ecovata_common_ves()
        print(ves)
        self.assertEqual(ves, 5500)

    def test_full_calc_wall(self):
        common_calc = CommonCalculator(
            sqr_floor=0,
            width_floor=0,
            sqr_wall=100,
            width_wall=200,
            sqr_roof=0,
            width_roof=0,
            is_wood_house=False,
            is_floor_dop_work=False,
            is_wall_dop_work=True,
            is_roof_dop_work=False,
        )

        dop_materials = common_calc.calculate_dop_work_materials()
        dop_costs = common_calc.calculate_dop_work_costs()
        print(dop_materials, dop_costs, sep="\n\n\n\n")
