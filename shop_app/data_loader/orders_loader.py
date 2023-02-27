from ..order.model import Order, Client, Product

from typing import Any
from collections import Counter, defaultdict


def get_orders(order_data: list[dict[str, Any]]) -> list[Order]:
    return [Order.from_dict(order) for order in order_data]


def count_products(products: list[Product]) -> dict[Product, int]:
    cnt = Counter()

    for p in products:
        cnt[p] += 1

    return dict(cnt)


def _convert_orders(orders: list[Order]) -> dict[Client, dict[Product, int]]:
    grouped_by_clients = defaultdict(list)

    for order in orders:
        grouped_by_clients[order.client] += order.basket.items

    return dict([(client, count_products(products)) for (client, products) in grouped_by_clients.items()])
