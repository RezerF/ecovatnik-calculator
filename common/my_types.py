from attrs import asdict, define, field


@define
class Materials:
    name: str = field()
    unit_measure: str = field()
    price: float = field()


print(Materials("vata", "kg", 1231))
print(asdict(Materials("vata", "kg", 1231)))


@define
class Works:
    name: str = field()
    unit_measure: str = field()
    price: float = field()
