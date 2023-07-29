from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HouseAnnotation:
    price: float
    square: float

@dataclass(frozen=True, slots=True)
class ConsumerAnnotation:
    account: float
    name: str