from typing import Union, List

from insulation_calc.common.constants import Common, Plotnost, WorksPrices, MaterialsCodes, MaterialsToSqrMetr, \
    WorkCodes
from insulation_calc.common.my_types import MaterialsType, WorksType
from insulation_calc.common.table_row import TableRow
from insulation_calc.common.utils import combine_dicts


class EcovataCalculator:
    def __init__(self, sqr, width, plotnost):
        self.sqr = sqr  # метры
        self.width = width  # миллиметры
        self.plotnost = plotnost  # миллиметры

    @property
    def volume_calculate(self) -> float:
        return round(self.sqr * self.width * Common.METRS_IN_MILLIMETERS, 1)

    @property
    def ves_calculate(self) -> float:
        return round(self.volume_calculate * self.plotnost, 1)

    @property
    def packages_count_calculate(self) -> float:
        return round(self.ves_calculate / Common.VES_UPAKOVKI, 1)

    def ecovata_price_calculate(self, package_price) -> float:
        return round(self.packages_count_calculate * package_price, 1)

    def cost_work_calculate(self, cost_work_per_kg) -> float:
        return round(self.ves_calculate * cost_work_per_kg, 1)


class MaterialsDopWorkCalculator:
    def __init__(self, sqr, is_wood_house=True, is_floor=False, is_wall=False, is_roof=False):
        self.sqr = sqr  # метры
        self.is_wood_house = is_wood_house
        self.is_floor = is_floor
        self.is_wall = is_wall
        self.is_roof = is_roof

    # def __init__(
    #         self,
    #         sqr_floor,
    #         width_floor,
    #         sqr_wall,
    #         width_wall,
    #         sqr_roof,
    #         width_roof,
    #         is_wood_house,
    #         is_floor_dop_work,
    #         is_wall_dop_work,
    #         is_roof_dop_work,
    # ):
    #     self.sqr_floor = sqr_floor
    #     self.width_floor = width_floor
    #     self.sqr_wall = sqr_wall
    #     self.width_wall = width_wall
    #     self.sqr_roof = sqr_roof
    #     self.width_roof = width_roof
    #     self.is_wood_house = is_wood_house  # дом деревянный?
    #     self.is_floor_dop_work = is_floor_dop_work
    #     self.is_wall_dop_work = is_wall_dop_work
    #     self.is_roof_dop_work = is_roof_dop_work
    #
    # def izospan_am_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.IZOSPAN_AM, 1)
    #
    # def setka_arm_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.SETKA_ARM_25x25, 1)
    #
    # def brus_50_50_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.BRUS_SS_50x50x3000, 1)
    #
    # def reika_20_40_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.REIKA_SS_20x40x3000, 1)
    #
    # def samorez_potainoi_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.SAMOREZ_POTAINOI_40x4, 1)
    #
    # def samorez_clop_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.SAMOREZ_CLOP, 1)
    #
    # def bolt_san_tech_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.BOLT_SAN_TECH_8x100, 1)
    #
    # def kronshtein_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.KRONSHTEIN, 1)
    #
    # def skobi_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.SKOBI_53_8, 1)
    #
    # def skotch_isospan_kl_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.SKOTCH_IZOSPAN_KL, 1)
    #
    # def skotch_isostong_lk_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.SKOTCH_IZOSTRONG_LK, 1)
    #
    # def dubel_calculate(self) -> float:
    #     return round(self.sqr * MaterialsToSqrMetr.DUBEL_10x80, 1)
    #
    # def calculate(self):
    #     data = {}
    #     if self.is_floor:
    #         self.izospan_am_calculate()
    #         self.setka_arm_calculate()
    #         self.reika_20_40_calculate()
    #         self.samorez_potainoi_calculate()
    #         self.skobi_calculate()
    #         self.skotch_isostong_lk_calculate()
    #     if self.is_wall:
    #         self.izospan_am_calculate()
    #         self.setka_arm_calculate()
    #         self.brus_50_50_calculate()
    #         self.reika_20_40_calculate()
    #         self.samorez_potainoi_calculate()
    #         self.samorez_clop_calculate()
    #         self.bolt_san_tech_calculate()
    #         self.kronshtein_calculate()
    #         self.skobi_calculate()
    #         self.skotch_isospan_kl_calculate()
    #         self.skotch_isostong_lk_calculate()
    #         self.dubel_calculate()
    #     if self.is_roof:
    #         self.izospan_am_calculate()
    #         self.setka_arm_calculate()
    #         self.reika_20_40_calculate()
    #         self.samorez_potainoi_calculate()
    #         self.skobi_calculate()
    #         self.skotch_isostong_lk_calculate()
    #
    #         return data

    # {v2

    def get_material_count(self, material: MaterialsType):
        return round(self.sqr * material.rashod_na_metr, 1)

    def get_amount_price(self, material):
        return round(self.get_material_count(material) * material.price, 1)

    def calculate_v2(self) -> dict:
        needed_materials = []
        data = {}
        if self.is_floor:
            needed_materials = [
                MaterialsType(MaterialsCodes.IZOSPAN_AM),
                MaterialsType(MaterialsCodes.SETKA_ARM_25x25),
                MaterialsType(MaterialsCodes.REIKA_SS_20x40x3000),
                MaterialsType(MaterialsCodes.SAMOREZ_POTAINOI_40x4),
                MaterialsType(MaterialsCodes.SKOBI_53_8),
                MaterialsType(MaterialsCodes.SKOTCH_IZOSTRONG_LK),
            ]

        if self.is_wall:
            needed_materials = [
                MaterialsType(MaterialsCodes.IZOSPAN_AM),
                MaterialsType(MaterialsCodes.SETKA_ARM_25x25),
                MaterialsType(MaterialsCodes.BRUS_SS_50x50x3000),
                MaterialsType(MaterialsCodes.REIKA_SS_20x40x3000),
                MaterialsType(MaterialsCodes.SAMOREZ_POTAINOI_40x4),
                MaterialsType(MaterialsCodes.SAMOREZ_CLOP),
                MaterialsType(MaterialsCodes.BOLT_SAN_TECH_8x100),
                MaterialsType(MaterialsCodes.KRONSHTEIN),
                MaterialsType(MaterialsCodes.SKOBI_53_8),
                MaterialsType(MaterialsCodes.SKOTCH_IZOSPAN_KL),
                MaterialsType(MaterialsCodes.SKOTCH_IZOSTRONG_LK),
                MaterialsType(MaterialsCodes.DUBEL_10x80),
            ]
        if self.is_roof:
            needed_materials = [
                MaterialsType(MaterialsCodes.IZOSPAN_AM),
                MaterialsType(MaterialsCodes.SETKA_ARM_25x25),
                MaterialsType(MaterialsCodes.REIKA_SS_20x40x3000),
                MaterialsType(MaterialsCodes.SAMOREZ_POTAINOI_40x4),
                MaterialsType(MaterialsCodes.SKOBI_53_8),
                MaterialsType(MaterialsCodes.SKOTCH_IZOSTRONG_LK),
            ]
        for material in needed_materials:
            data.update({material.code: self.get_material_count(material)})
        return data

    # }v2


class DopWorkWorkCalculator:
    def __init__(self, sqr, is_wood_house=True, is_floor=False, is_wall=False, is_roof=False):
        self.sqr = sqr  # метры
        self.is_wood_house = is_wood_house
        self.is_floor = is_floor
        self.is_wall = is_wall
        self.is_roof = is_roof

    def obreshetki_montaj_calculate(self) -> float:
        if not self.is_wood_house and self.is_wall:
            return round(self.sqr * WorksPrices.OBRESHETKI_MONTAJ_PO_KIRPICHU, 1)
        return round(self.sqr * WorksPrices.OBRESHETKI_MONTAJ_PO_DEREVU, 1)

    def gidro_paroisol_montaj_calculate(self) -> float:
        return round(self.sqr * WorksPrices.GIDRO_PAROISOL_MONTAJ, 1)

    def setka_arm_montaj_calculate(self) -> float:
        return round(self.sqr * WorksPrices.SETKA_ARMIRUU_MONTAJ, 1)

    def kontr_obreshetka_montaj_calculate(self) -> float:
        return round(self.sqr * WorksPrices.KONTR_OBRESHETKA_MONTAJ, 1)

    def get_works_count(self):
        return self.sqr

    def calculate(self):
        needed_works = []
        data = {}
        if self.is_wall:
            needed_works = [
                WorksType(WorkCodes.OBRESHETKI_MONTAJ_PO_DEREVU if self.is_wood_house else WorkCodes.OBRESHETKI_MONTAJ_PO_KIRPICHU),
                WorksType(WorkCodes.GIDRO_PAROISOL_MONTAJ),
                WorksType(WorkCodes.SETKA_ARMIRUU_MONTAJ),
                WorksType(WorkCodes.KONTR_OBRESHETKA_MONTAJ),
            ]
        elif self.is_floor:
            needed_works = [
                WorksType(WorkCodes.GIDRO_PAROISOL_MONTAJ),
                WorksType(WorkCodes.SETKA_ARMIRUU_MONTAJ),
                WorksType(WorkCodes.KONTR_OBRESHETKA_MONTAJ),
            ]
        elif self.is_roof:
            needed_works = [
                WorksType(WorkCodes.GIDRO_PAROISOL_MONTAJ),
                WorksType(WorkCodes.SETKA_ARMIRUU_MONTAJ),
                WorksType(WorkCodes.KONTR_OBRESHETKA_MONTAJ),
            ]

        for work in needed_works:
            data.update({work.code: self.get_works_count()})

        return data


class CommonCalculator:
    def __init__(
            self,
            sqr_floor,
            width_floor,
            sqr_wall,
            width_wall,
            sqr_roof,
            width_roof,
            is_wood_house,
            is_floor_dop_work,
            is_wall_dop_work,
            is_roof_dop_work,
    ):
        self.sqr_floor = sqr_floor
        self.width_floor = width_floor
        self.sqr_wall = sqr_wall
        self.width_wall = width_wall
        self.sqr_roof = sqr_roof
        self.width_roof = width_roof
        self.is_wood_house = is_wood_house  # дом деревянный?
        self.is_floor_dop_work = is_floor_dop_work
        self.is_wall_dop_work = is_wall_dop_work
        self.is_roof_dop_work = is_roof_dop_work

    def calculate_ecovata_common_ves(self):
        ecovata_ves_floor = 0
        ecovata_ves_wall = 0
        ecovata_ves_roof = 0
        if self.sqr_floor:
            ins_calc = EcovataCalculator(self.sqr_floor, self.width_floor, Plotnost.HORISONTAL)
            ecovata_ves_floor = ins_calc.ves_calculate
        if self.sqr_wall:
            ins_calc = EcovataCalculator(self.sqr_wall, self.width_wall, Plotnost.VERTICAL)
            ecovata_ves_wall = ins_calc.ves_calculate
        if self.sqr_roof:
            ins_calc = EcovataCalculator(self.sqr_roof, self.width_roof, Plotnost.INCLINED)
            ecovata_ves_roof = ins_calc.ves_calculate

        return ecovata_ves_floor + ecovata_ves_wall + ecovata_ves_roof

    def calculate_dop_work_materials(self):

        print("\n\n", self.sqr_wall, self.width_wall, sep="+++++++")
        dop_work_material_count_wall_data = {}
        dop_work_material_count_roof_data = {}
        dop_work_material_count_floor_data = {}
        if self.sqr_floor:
            if self.is_floor_dop_work:
                material_dop_work_calc = MaterialsDopWorkCalculator(sqr=self.sqr_floor, is_floor=True)
                dop_work_material_count_floor_data = material_dop_work_calc.calculate_v2()
        if self.sqr_wall:
            if self.is_wall_dop_work:
                material_dop_work_calc = MaterialsDopWorkCalculator(sqr=self.sqr_wall, is_wall=True)
                dop_work_material_count_wall_data = material_dop_work_calc.calculate_v2()
        if self.sqr_roof:
            if self.is_roof_dop_work:
                material_dop_work_calc = MaterialsDopWorkCalculator(sqr=self.sqr_roof, is_roof=True)
                dop_work_material_count_roof_data = material_dop_work_calc.calculate_v2()

        common_materials_count = combine_dicts(
            dop_work_material_count_floor_data,
            dop_work_material_count_wall_data,
            dop_work_material_count_roof_data
        )

        result_data = {}
        for key, value in common_materials_count.items():
            obj = MaterialsType(key)
            result_data[key] = {
                "name": obj.naming,
                "count": value,
                "unit_measurement": obj.unit_measure,
                "unit_price": obj.price,
                "amount_price": obj.amount_price(value)}

        # add ecovata to result dict
        common_ves_ecovata = self.calculate_ecovata_common_ves()
        print("\n\n", self.sqr_wall, self.width_wall, sep="=========")
        print(common_ves_ecovata)
        ecovata = MaterialsType(MaterialsCodes.ECOVATA)
        result_data[ecovata.code] = {
            "name": ecovata.naming,
            "count": common_ves_ecovata,
            "unit_measurement": ecovata.unit_measure,
            "unit_price": ecovata.price,
            "amount_price": ecovata.amount_price(common_ves_ecovata)
        }

        return result_data

    def calculate_dop_work_costs(self):
        dop_work_cost_floor_data = {}
        dop_work_cost_wall_data = {}
        dop_work_cost_roof_data = {}
        if self.sqr_floor:
            if self.is_floor_dop_work:
                dop_work_calc = DopWorkWorkCalculator(sqr=self.sqr_floor, is_floor=True)
                dop_work_cost_floor_data = dop_work_calc.calculate()
        if self.sqr_wall:
            if self.is_wall_dop_work:
                dop_work_calc = DopWorkWorkCalculator(sqr=self.sqr_wall, is_wood_house=self.is_wood_house, is_wall=True)
                dop_work_cost_wall_data = dop_work_calc.calculate()
        if self.sqr_roof:
            if self.is_roof_dop_work:
                dop_work_calc = DopWorkWorkCalculator(sqr=self.sqr_roof, is_roof=True)
                dop_work_cost_roof_data = dop_work_calc.calculate()

        common_dop_woks_costs = combine_dicts(
            dop_work_cost_floor_data,
            dop_work_cost_wall_data,
            dop_work_cost_roof_data
        )

        result_data = {}
        for key, value in common_dop_woks_costs.items():
            obj = WorksType(key)
            result_data[key] = {
                "name": obj.naming,
                "count": value,
                "unit_measurement": obj.unit_measure,
                "unit_price": obj.price,
                "amount_price": obj.amount_price(value)}

        # add ecovata to result dict
        common_ves_ecovata = self.calculate_ecovata_common_ves()
        ecovata_montaj = WorksType(WorkCodes.ECOVATA_MONTAJ)
        result_data[ecovata_montaj.code] = {
            "name": ecovata_montaj.naming,
            "count": common_ves_ecovata,
            "unit_measurement": ecovata_montaj.unit_measure,
            "unit_price": ecovata_montaj.price,
            "amount_price": ecovata_montaj.amount_price(common_ves_ecovata)
        }

        return result_data
