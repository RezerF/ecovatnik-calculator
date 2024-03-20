from attrs import define, field

from insulation_calc.common.constants import NamingMapping, UnitMeasureMapping, MaterialsToSqrMetr, MaterialsPrices, \
    WorksPrices


@define
class BaseType:
    code = field()

    @property
    def naming(self) -> str:
        return getattr(NamingMapping, self.code)

    @property
    def unit_measure(self) -> str:
        return getattr(UnitMeasureMapping, self.code)


@define
class MaterialsType(BaseType):
    @property
    def price(self):
        return getattr(MaterialsPrices, self.code)

    def amount_price(self, count):
        return round(self.price * count, 1)

    @property
    def rashod_na_metr(self):
        return getattr(MaterialsToSqrMetr, self.code)


@define
class WorksType(BaseType):
    @property
    def price(self):
        return getattr(WorksPrices, self.code)

    def amount_price(self, count):
        return round(self.price * count, 1)
