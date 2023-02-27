from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto


class ProductType(Enum):
    ELECTRONICS = auto()
    BOOKS = auto()
    MOTORIZATION = auto()


@dataclass(frozen=True)
class Product:
    name: str
    type: ProductType
    price: Decimal
