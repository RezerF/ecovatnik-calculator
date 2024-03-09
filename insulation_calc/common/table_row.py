

class TableRow:
    def __init__(self, name, count, unit_measurement, unit_price, amount_price):
        self.name = name
        self.count = count
        self.unit_measurement = unit_measurement
        self.unit_price = unit_price
        self.total_amount = amount_price

    def get_row(self):
        return {"Наименование": self.name, "Кол-во (ед.)": self.count, "Ед. изм.": self.unit_measurement,
                "Цена (руб)": self.unit_price, "Стоимость (руб)": self.total_amount}


# {
#  'is_floor_dop_work': 'Не нужна/Делаю своими силами',
#  'sqr_floor': 10,
#  'width_floor': 0,
#  'is_wood_house': 'Кирпич/Газобетон',
#  'is_roof_dop_work': 'Не нужна/Делаю своими силами',
#  'sqr_roof': 100,
#  'width_roof': 0,
#  'width_wall': 200,
#  'sqr_wall': 100,
# 'is_wall_dop_work': 'Не нужна/Делаю своими силами',
# }
