

class TableRow:
    def __init__(self, name, count, unit_measurement, unit_price, amount_price):
        self.name = str(name)
        self.count = str(count)
        self.unit_measurement = str(unit_measurement)
        self.unit_price = str(unit_price)
        self.total_amount = str(amount_price)

    def get_row(self):
        return {"Наименование": self.name, "Кол-во (ед.)": self.count, "Ед. изм.": self.unit_measurement,
                "Цена (руб)": self.unit_price, "Стоимость (руб)": self.total_amount}

