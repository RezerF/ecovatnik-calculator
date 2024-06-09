
from insulation_calc.common.parse_data import UnitMeasurement


class Plotnost:
    HORISONTAL = 35
    VERTICAL = 65
    INCLINED = 55  # наклонка


class Common:
    METRS_IN_MILLIMETERS = 0.001  # метров в миллиметре
    VES_UPAKOVKI = 15


class UnitMeasureMapping:
    # МАТЕРИАЛЫ
    ECOVATA = UnitMeasurement.KG
    IZOSPAN_AM = UnitMeasurement.M2
    SETKA_ARM_25x25 = UnitMeasurement.M2
    BRUS_SS_50x50x3000 = UnitMeasurement.PIECES
    REIKA_SS_20x40x3000 = UnitMeasurement.PIECES
    SAMOREZ_POTAINOI_40x4 = UnitMeasurement.PIECES
    SAMOREZ_POTAINOI_80x5 = UnitMeasurement.PIECES
    BOLT_SAN_TECH_8x100 = UnitMeasurement.PIECES
    KRONSHTEIN = UnitMeasurement.PIECES
    SKOBI_53_8 = UnitMeasurement.PACKAGE
    SKOTCH_IZOSPAN_KL = UnitMeasurement.PM
    DUBEL_10x80 = UnitMeasurement.PIECES

    # РАБОТЫ
    OBRESHETKI_MONTAJ_PO_KIRPICHU = UnitMeasurement.M2
    OBRESHETKI_MONTAJ_PO_DEREVU = UnitMeasurement.M2
    GIDRO_PAROISOL_MONTAJ = UnitMeasurement.M2
    SETKA_ARMIRUU_MONTAJ = UnitMeasurement.M2
    KONTR_OBRESHETKA_MONTAJ = UnitMeasurement.M2
    ECOVATA_MONTAJ = UnitMeasurement.KG
    DEMONTAJ = UnitMeasurement.M2
    BUILD_LESA = UnitMeasurement.M2
    DESTROY_BETON = UnitMeasurement.PIECES


class MaterialsCodes:
    ECOVATA = "ECOVATA"
    IZOSPAN_AM = "IZOSPAN_AM"
    SETKA_ARM_25x25 = 'SETKA_ARM_25x25'
    BRUS_SS_50x50x3000 = 'BRUS_SS_50x50x3000'
    REIKA_SS_20x40x3000 = 'REIKA_SS_20x40x3000'
    SAMOREZ_POTAINOI_40x4 = 'SAMOREZ_POTAINOI_40x4'
    SAMOREZ_POTAINOI_80x5 = 'SAMOREZ_POTAINOI_80x5'
    BOLT_SAN_TECH_8x100 = 'BOLT_SAN_TECH_8x100'
    KRONSHTEIN = 'KRONSHTEIN'
    SKOBI_53_8 = 'SKOBI_53_8'
    SKOTCH_IZOSPAN_KL = 'SKOTCH_IZOSPAN_KL'
    DUBEL_10x80 = 'DUBEL_10x80'


class WorkCodes:
    ECOVATA_MONTAJ = "ECOVATA_MONTAJ"
    OBRESHETKI_MONTAJ_PO_KIRPICHU = "OBRESHETKI_MONTAJ_PO_KIRPICHU"
    OBRESHETKI_MONTAJ_PO_DEREVU = 'OBRESHETKI_MONTAJ_PO_DEREVU'
    GIDRO_PAROISOL_MONTAJ = 'GIDRO_PAROISOL_MONTAJ'
    SETKA_ARMIRUU_MONTAJ = 'SETKA_ARMIRUU_MONTAJ'
    KONTR_OBRESHETKA_MONTAJ = 'KONTR_OBRESHETKA_MONTAJ'
    DEMONTAJ = 'DEMONTAJ'
    BUILD_LESA = 'BUILD_LESA'
    DESTROY_BETON = 'DESTROY_BETON'
