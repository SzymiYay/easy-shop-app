from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Client:
    name: str
    surname: str
    age: int
    money: Decimal
