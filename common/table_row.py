

class TableRow:
    def __init__(self, name, count, unit_measurement, unit_price, amount):
        self.name = name
        self.count = count
        self.unit_measurement = unit_measurement
        self.unit_price = unit_price
        self.total_amount = amount

    def get_row(self):
        return {"Наименование": self.name, "Кол-во (ед.)": self.count, "Ед. изм.": self.unit_measurement,
                "Цена (руб)": self.unit_price, "Стоимость (руб)": self.total_amount}