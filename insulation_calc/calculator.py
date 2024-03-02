from typing import Union, List

from common.constants import Common, Plotnost, WorksPrices, MaterialsCodes, MaterialsToSqrMetr
from common.my_types import MaterialsType, WorksType
from common.table_row import TableRow


class EcovataCalculator:
    def __init__(self, sqr, width):
        self.sqr = sqr  # метры
        self.width = width  # миллиметры

    @property
    def volume_calculate(self) -> float:
        return round(self.sqr * self.width * Common.METRS_IN_MILLIMETERS, 1)

    @property
    def ves_calculate(self) -> float:
        return round(self.volume_calculate * Plotnost.VERTICAL, 1)

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

    def izospan_am_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.IZOSPAN_AM, 1)

    def setka_arm_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SETKA_ARM_25x25, 1)

    def brus_50_50_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.BRUS_SS_50x50x3000, 1)

    def reika_20_40_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.REIKA_SS_20x40x3000, 1)

    def samorez_potainoi_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SAMOREZ_POTAINOI_40x4, 1)

    def samorez_clop_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SAMOREZ_CLOP, 1)

    def bolt_san_tech_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.BOLT_SAN_TECH_8x100, 1)

    def kronshtein_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.KRONSHTEIN, 1)

    def skobi_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SKOBI_53_8, 1)

    def skotch_isospan_kl_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SKOTCH_IZOSPAN_KL, 1)

    def skotch_isostong_lk_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SKOTCH_IZOSTRONG_LK, 1)

    def dubel_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.DUBEL_10x80, 1)

    def calculate(self):
        data = {}
        if self.is_floor:
            self.izospan_am_calculate()
            self.setka_arm_calculate()
            self.reika_20_40_calculate()
            self.samorez_potainoi_calculate()
            self.skobi_calculate()
            self.skotch_isostong_lk_calculate()
        if self.is_wall:
            self.izospan_am_calculate()
            self.setka_arm_calculate()
            self.brus_50_50_calculate()
            self.reika_20_40_calculate()
            self.samorez_potainoi_calculate()
            self.samorez_clop_calculate()
            self.bolt_san_tech_calculate()
            self.kronshtein_calculate()
            self.skobi_calculate()
            self.skotch_isospan_kl_calculate()
            self.skotch_isostong_lk_calculate()
            self.dubel_calculate()
        if self.is_roof:
            self.izospan_am_calculate()
            self.setka_arm_calculate()
            self.reika_20_40_calculate()
            self.samorez_potainoi_calculate()
            self.skobi_calculate()
            self.skotch_isostong_lk_calculate()

            return data

    def get_material_count(self, material):
        return round(self.sqr * material.rashod_na_metr, 1)

    def calculate_v2(self, ):
        data = {}
        if self.is_floor:
            neded_materials = [
                MaterialsType(MaterialsCodes.IZOSPAN_AM),
                MaterialsType(MaterialsCodes.SETKA_ARM_25x25),
                MaterialsType(MaterialsCodes.REIKA_SS_20x40x3000),
                MaterialsType(MaterialsCodes.SAMOREZ_POTAINOI_40x4),
                MaterialsType(MaterialsCodes.SKOBI_53_8),
                MaterialsType(MaterialsCodes.SKOTCH_IZOSTRONG_LK),
            ]

        if self.is_wall:
            neded_materials = [
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
            neded_materials = [
                MaterialsType(MaterialsCodes.IZOSPAN_AM),
                MaterialsType(MaterialsCodes.SETKA_ARM_25x25),
                MaterialsType(MaterialsCodes.REIKA_SS_20x40x3000),
                MaterialsType(MaterialsCodes.SAMOREZ_POTAINOI_40x4),
                MaterialsType(MaterialsCodes.SKOBI_53_8),
                MaterialsType(MaterialsCodes.SKOTCH_IZOSTRONG_LK),
            ]
        return data

    # def get_count(self, material):
    #     # if material.code == MaterialsCodes.ECOVATA:
    #     #     return self.ves_calculate
    #     return round(self.sqr * material.rashod_na_metr, 1)
    #
    # def get_amount_price(self, material):
    #     return round(self.get_count(material) * material.price, 1)
    #
    # def get_materials_data_rows(self) -> List[TableRow]:
    #     rows = []
    #     for material in self.materials:
    #         rows.append(TableRow(
    #             material.naming,
    #             self.get_count(material),
    #             material.unit_measure,
    #             material.price,
    #             self.get_amount_price(material)).get_row()
    #                     )
    #     return rows


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

    def calculate(self):
        data = {}
        if self.is_wall:
            data.update({"obreshetki_montaj": self.obreshetki_montaj_calculate()})
            data.update({"gidro_paroisol_montaj": self.gidro_paroisol_montaj_calculate()})
            data.update({"setka_arm_montaj": self.setka_arm_montaj_calculate()})
            data.update({"kontr_obreshetka_montaj": self.kontr_obreshetka_montaj_calculate()})
        elif self.is_floor:
            data.update({"gidro_paroisol_montaj": self.gidro_paroisol_montaj_calculate()})
            data.update({"setka_arm_montaj": self.setka_arm_montaj_calculate()})
            data.update({"kontr_obreshetka_montaj": self.kontr_obreshetka_montaj_calculate()})
        elif self.is_roof:
            data.update({"gidro_paroisol_montaj": self.gidro_paroisol_montaj_calculate()})
            data.update({"setka_arm_montaj": self.setka_arm_montaj_calculate()})
            data.update({"kontr_obreshetka_montaj": self.kontr_obreshetka_montaj_calculate()})

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

    def calculate(self):
        if self.sqr_floor:
            ins_calc = EcovataCalculator(self.sqr_floor, self.width_floor)
            ecovata_ves_floor = ins_calc.ves_calculate
            if self.is_floor_dop_work:
                dop_work_calc = DopWorkWorkCalculator(sqr=self.sqr_floor, is_floor=True)
                dop_work_cost_floor_data = dop_work_calc.calculate()
                material_dop_work_calc = MaterialsDopWorkCalculator(sqr=self.sqr_floor, is_floor=True)
                dop_work_material_cost_floor_data = material_dop_work_calc.calculate()
        if self.sqr_wall:
            ins_calc = EcovataCalculator(self.sqr_wall, self.width_wall)
            ecovata_ves_wall = ins_calc.ves_calculate
            if self.is_wall_dop_work:
                dop_work_calc = DopWorkWorkCalculator(sqr=self.sqr_wall, is_wood_house=self.is_wood_house, is_wall=True)
                dop_work_cost_wall_data = dop_work_calc.calculate()
        if self.sqr_roof:
            ins_calc = EcovataCalculator(self.sqr_roof, self.width_roof)
            ecovata_ves_roof = ins_calc.ves_calculate
            if self.is_roof_dop_work:
                dop_work_calc = DopWorkWorkCalculator(sqr=self.sqr_wall, is_roof=True)
                dop_work_cost_roof_data = dop_work_calc.calculate()
