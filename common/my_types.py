from attrs import define, field

from common.constants import NamingMapping, UnitMeasureMapping, MaterialsToSqrMetr, MaterialsPrices


@define
class BaseType:
    code = field()

    @property
    def naming(self) -> str:
        return getattr(NamingMapping, self.code)

    @property
    def unit_measure(self) -> str:
        return getattr(UnitMeasureMapping, self.code)

    @property
    def price(self):
        return getattr(MaterialsPrices, self.code)

    @property
    def rashod_na_metr(self):
        return getattr(MaterialsToSqrMetr, self.code)


@define
class MaterialsType(BaseType):
    pass


@define
class WorksType(BaseType):
    pass