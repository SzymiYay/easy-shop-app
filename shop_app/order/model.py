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

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> 'Order':
        for p in data['basket']:
            p['price'] = Decimal(p['price'])
            p['type'] = ProductType[p['type']]

        order = Order(**data)

        order.client = Client(**data['client'])
        order.basket = Basket(data['basket'])

        for i, p in enumerate(order.basket.items):
            order.basket.items[i] = Product(**p)

        return order
