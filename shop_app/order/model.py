from .basket.model import Basket
from .client.model import Client
from .product.model import Product, ProductType

from dataclasses import dataclass
from decimal import Decimal
from typing import Any


@dataclass
class Order:
    client: Client
    basket: Basket