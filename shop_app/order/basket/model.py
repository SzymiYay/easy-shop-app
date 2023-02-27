from ..product.model import Product

from dataclasses import dataclass


@dataclass
class Basket:
    items: list[Product]