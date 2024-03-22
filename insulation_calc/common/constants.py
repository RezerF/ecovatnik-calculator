class MaterialsPrices:
    # ECOVATA = 1080
    ECOVATA = 72
    IZOSPAN_AM = 83
    SETKA_ARM_25x25 = 109  # СД (Ч) СЕТКА АРМИРУЮЩАЯ 2Х25
    BRUS_SS_50x50x3000 = 250
    REIKA_SS_20x40x3000 = 112
    SAMOREZ_POTAINOI_40x4 = 3.68  # Саморезы по дереву 40x4,0 мм потайная головка конструкционные (для контр обрешотки)
    SAMOREZ_CLOP = 1.34  # Саморезы клопы 38 (41)x4,2 мм  (креление кранштейна к брусу 50*50)
    BOLT_SAN_TECH_8x100 = 14  # Болт 8х100 мм DIN 571 оцинкованный  (крепление кранштейна к стене)
    KRONSHTEIN = 66  # Кронштейн для вентилируемых фасадов регулируемый 200х50х50х2мм
    SKOBI_53_8 = 62  # Скобы для степлера тип 53 8 мм (1000 шт.)
    SKOTCH_IZOSPAN_KL = 51  # ИЗОСПАН KL+ усиленная двухсторонняя клейкая лента 25п.м
    SKOTCH_IZOSTRONG_LK = 24  # Лента соединительная Изостронг LK 15 мм х 22,5п.м
    DUBEL_10x80 = 9  # Дюбель распорный Hard-Fix 10x80 мм нейлон (для монтажа кронштейа к бетонной или кирпичной стене)


class WorksPrices:
    ECOVATA_MONTAJ = 22
    OBRESHETKI_MONTAJ_PO_DEREVU = 400  # Монтаж деревянной обрешетки по дереву
    OBRESHETKI_MONTAJ_PO_KIRPICHU = 520  # Монтаж деревянной обрешетки по дереву
    GIDRO_PAROISOL_MONTAJ = 150  # Монтаж ветро-влагозащитной мембраны
    SETKA_ARMIRUU_MONTAJ = 150  # Монтаж армирующей сетки
    KONTR_OBRESHETKA_MONTAJ = 150  # Монтаж контробрешетки


class Plotnost:
    HORISONTAL = 35
    VERTICAL = 65
    INCLINED = 55


class Common:
    METRS_IN_MILLIMETERS = 0.001  # метров в миллиметре
    VES_UPAKOVKI = 15


class MaterialsToSqrMetr:
    IZOSPAN_AM = 1.25
    SETKA_ARM_25x25 = 1.25
    BRUS_SS_50x50x3000 = 0.92
    REIKA_SS_20x40x3000 = 0.62
    SAMOREZ_POTAINOI_40x4 = 8.35
    SAMOREZ_CLOP = 5.6
    BOLT_SAN_TECH_8x100 = 1.84
    KRONSHTEIN = 1.84
    SKOBI_53_8 = 0.06
    SKOTCH_IZOSPAN_KL = 1.17
    SKOTCH_IZOSTRONG_LK = 1.17
    DUBEL_10x80 = 1.84


class NamingMapping:
    # МАТЕРИАЛЫ
    ECOVATA = 'Утеплитель целлюлозный "Эковата"'
    IZOSPAN_AM = 'Ветро-влагозащитная мембрана Изоспан АМ 70'
    SETKA_ARM_25x25 = 'СЕТКА АРМИРУЮЩАЯ 2Х25'
    BRUS_SS_50x50x3000 = 'Брус сухой строганный 50*50*3000'
    REIKA_SS_20x40x3000 = 'Рейка сухая строганная 20*40*3000'
    SAMOREZ_POTAINOI_40x4 = 'Саморезы по дереву 40x4,0 мм потайная головка конструкционные'
    SAMOREZ_CLOP = 'Саморезы клопы 38 (41)x4,2 мм  '
    BOLT_SAN_TECH_8x100 = 'Болт 8х100 мм DIN 571 оцинкованный  '
    KRONSHTEIN = 'Кронштейн для вентилируемых фасадов регулируемый 200х50х50х2мм'
    SKOBI_53_8 = 'Скобы для степлера тип 53 8 мм (1000 шт.)'
    SKOTCH_IZOSPAN_KL = 'ИЗОСПАН KL+ усиленная двухсторонняя клейкая лента'
    SKOTCH_IZOSTRONG_LK = 'Лента соединительная Изостронг LK 15 мм'
    DUBEL_10x80 = 'Дюбель распорный Hard-Fix 10x80 мм нейлон'

    # РАБОТЫ
    OBRESHETKI_MONTAJ_PO_KIRPICHU = 'Монтаж деревянной обрешетки по кирпичу или бетону'
    OBRESHETKI_MONTAJ_PO_DEREVU = 'Монтаж деревянной обрешетки по дереву'
    GIDRO_PAROISOL_MONTAJ = 'Монтаж ветро-влагозащитной мембраны'
    SETKA_ARMIRUU_MONTAJ = 'Монтаж армирующей сетки'
    KONTR_OBRESHETKA_MONTAJ = 'Монтаж контробрешетки'
    ECOVATA_MONTAJ = 'Можтаж утеплителя целлюлозного '


class UnitMeasurement:
    M2 = "м2"
    M3 = "куб.м."
    KG = "кг."
    PIECES = "шт."
    PM = "п.м."
    PACKAGE = "упаковок"
    RUB = "руб."


class UnitMeasureMapping:
    # МАТЕРИАЛЫ
    ECOVATA = UnitMeasurement.KG
    IZOSPAN_AM = UnitMeasurement.M2
    SETKA_ARM_25x25 = UnitMeasurement.M2
    BRUS_SS_50x50x3000 = UnitMeasurement.PIECES
    REIKA_SS_20x40x3000 = UnitMeasurement.PIECES
    SAMOREZ_POTAINOI_40x4 = UnitMeasurement.PIECES
    SAMOREZ_CLOP = UnitMeasurement.PIECES
    BOLT_SAN_TECH_8x100 = UnitMeasurement.PIECES
    KRONSHTEIN = UnitMeasurement.PIECES
    SKOBI_53_8 = UnitMeasurement.PACKAGE
    SKOTCH_IZOSPAN_KL = UnitMeasurement.PM
    SKOTCH_IZOSTRONG_LK = UnitMeasurement.PM
    DUBEL_10x80 = UnitMeasurement.PIECES

    # РАБОТЫ
    OBRESHETKI_MONTAJ_PO_KIRPICHU = UnitMeasurement.M2
    OBRESHETKI_MONTAJ_PO_DEREVU = UnitMeasurement.M2
    GIDRO_PAROISOL_MONTAJ = UnitMeasurement.M2
    SETKA_ARMIRUU_MONTAJ = UnitMeasurement.M2
    KONTR_OBRESHETKA_MONTAJ = UnitMeasurement.M2
    ECOVATA_MONTAJ = UnitMeasurement.KG


class MaterialsCodes:
    ECOVATA = "ECOVATA"
    IZOSPAN_AM = "IZOSPAN_AM"
    SETKA_ARM_25x25 = 'SETKA_ARM_25x25'
    BRUS_SS_50x50x3000 = 'BRUS_SS_50x50x3000'
    REIKA_SS_20x40x3000 = 'REIKA_SS_20x40x3000'
    SAMOREZ_POTAINOI_40x4 = 'SAMOREZ_POTAINOI_40x4'
    SAMOREZ_CLOP = 'SAMOREZ_CLOP'
    BOLT_SAN_TECH_8x100 = 'BOLT_SAN_TECH_8x100'
    KRONSHTEIN = 'KRONSHTEIN'
    SKOBI_53_8 = 'SKOBI_53_8'
    SKOTCH_IZOSPAN_KL = 'SKOTCH_IZOSPAN_KL'
    SKOTCH_IZOSTRONG_LK = 'SKOTCH_IZOSTRONG_LK'
    DUBEL_10x80 = 'DUBEL_10x80'


class WorkCodes:
    ECOVATA_MONTAJ = "ECOVATA_MONTAJ"
    OBRESHETKI_MONTAJ_PO_KIRPICHU = "OBRESHETKI_MONTAJ_PO_KIRPICHU"
    OBRESHETKI_MONTAJ_PO_DEREVU = 'OBRESHETKI_MONTAJ_PO_DEREVU'
    GIDRO_PAROISOL_MONTAJ = 'GIDRO_PAROISOL_MONTAJ'
    SETKA_ARMIRUU_MONTAJ = 'SETKA_ARMIRUU_MONTAJ'
    KONTR_OBRESHETKA_MONTAJ = 'KONTR_OBRESHETKA_MONTAJ'