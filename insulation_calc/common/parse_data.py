from insulation_calc.common.utils import get_data_cfg

static_data = get_data_cfg()
material_prices = static_data.MaterialsPrices
works_prices = static_data.WorksPrices
materlials_to_sqr_meter = static_data.MaterialsToSqrMetr
naming_mapping = static_data.NamingMapping
unit_measurement = static_data.UnitMeasurement


class MaterialsPrices:
    ECOVATA = material_prices.ECOVATA
    IZOSPAN_AM = material_prices.IZOSPAN_AM
    SETKA_ARM_25x25 = material_prices.SETKA_ARM_25x25
    BRUS_SS_50x50x3000 = material_prices.BRUS_SS_50x50x3000
    REIKA_SS_20x40x3000 = material_prices.REIKA_SS_20x40x3000
    SAMOREZ_POTAINOI_40x4 = material_prices.SAMOREZ_POTAINOI_40x4
    SAMOREZ_POTAINOI_80x5 = material_prices.SAMOREZ_POTAINOI_80x5
    BOLT_SAN_TECH_8x100 = material_prices.BOLT_SAN_TECH_8x100
    KRONSHTEIN = material_prices.KRONSHTEIN
    SKOBI_53_8 = material_prices.SKOBI_53_8
    SKOTCH_IZOSPAN_KL = material_prices.SKOTCH_IZOSPAN_KL
    DUBEL_10x80 = material_prices.DUBEL_10x80


class WorksPrices:
    ECOVATA_MONTAJ = works_prices.ECOVATA_MONTAJ
    OBRESHETKI_MONTAJ_PO_DEREVU = works_prices.OBRESHETKI_MONTAJ_PO_DEREVU
    OBRESHETKI_MONTAJ_PO_KIRPICHU = works_prices.OBRESHETKI_MONTAJ_PO_KIRPICHU
    GIDRO_PAROISOL_MONTAJ = works_prices.GIDRO_PAROISOL_MONTAJ
    SETKA_ARMIRUU_MONTAJ = works_prices.SETKA_ARMIRUU_MONTAJ
    KONTR_OBRESHETKA_MONTAJ = works_prices.KONTR_OBRESHETKA_MONTAJ


class MaterialsToSqrMetr:
    IZOSPAN_AM = materlials_to_sqr_meter.IZOSPAN_AM
    SETKA_ARM_25x25 = materlials_to_sqr_meter.SETKA_ARM_25x25
    BRUS_SS_50x50x3000 = materlials_to_sqr_meter.BRUS_SS_50x50x3000
    REIKA_SS_20x40x3000 = materlials_to_sqr_meter.REIKA_SS_20x40x3000
    SAMOREZ_POTAINOI_40x4 = materlials_to_sqr_meter.SAMOREZ_POTAINOI_40x4
    SAMOREZ_POTAINOI_80x5 = materlials_to_sqr_meter.SAMOREZ_POTAINOI_80x5
    BOLT_SAN_TECH_8x100 = materlials_to_sqr_meter.BOLT_SAN_TECH_8x100
    KRONSHTEIN = materlials_to_sqr_meter.KRONSHTEIN
    SKOBI_53_8 = materlials_to_sqr_meter.SKOBI_53_8
    SKOTCH_IZOSPAN_KL = materlials_to_sqr_meter.SKOTCH_IZOSPAN_KL
    DUBEL_10x80 = materlials_to_sqr_meter.DUBEL_10x80


class NamingMapping:
    # МАТЕРИАЛЫ
    ECOVATA = naming_mapping.ECOVATA
    IZOSPAN_AM = naming_mapping.IZOSPAN_AM
    SETKA_ARM_25x25 = naming_mapping.SETKA_ARM_25x25
    BRUS_SS_50x50x3000 = naming_mapping.BRUS_SS_50x50x3000
    REIKA_SS_20x40x3000 = naming_mapping.REIKA_SS_20x40x3000
    SAMOREZ_POTAINOI_40x4 = naming_mapping.SAMOREZ_POTAINOI_40x4
    SAMOREZ_POTAINOI_80x5 = naming_mapping.SAMOREZ_POTAINOI_80x5
    BOLT_SAN_TECH_8x100 = naming_mapping.BOLT_SAN_TECH_8x100
    KRONSHTEIN = naming_mapping.KRONSHTEIN
    SKOBI_53_8 = naming_mapping.SKOBI_53_8
    SKOTCH_IZOSPAN_KL = naming_mapping.SKOTCH_IZOSPAN_KL
    DUBEL_10x80 = naming_mapping.DUBEL_10x80

    # РАБОТЫ
    OBRESHETKI_MONTAJ_PO_KIRPICHU = naming_mapping.OBRESHETKI_MONTAJ_PO_KIRPICHU
    OBRESHETKI_MONTAJ_PO_DEREVU = naming_mapping.OBRESHETKI_MONTAJ_PO_DEREVU
    GIDRO_PAROISOL_MONTAJ = naming_mapping.GIDRO_PAROISOL_MONTAJ
    SETKA_ARMIRUU_MONTAJ = naming_mapping.SETKA_ARMIRUU_MONTAJ
    KONTR_OBRESHETKA_MONTAJ = naming_mapping.KONTR_OBRESHETKA_MONTAJ
    ECOVATA_MONTAJ = naming_mapping.ECOVATA_MONTAJ


class UnitMeasurement:
    M2 = unit_measurement.M2
    M3 = unit_measurement.M3
    KG = unit_measurement.KG
    PIECES = unit_measurement.PIECES
    PM = unit_measurement.PM
    PACKAGE = unit_measurement.PACKAGE
    RUB = unit_measurement.RUB
