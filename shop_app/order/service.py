from .client.model import Client
from .product.model import Product, ProductType
from .model import Order

from dataclasses import dataclass
from collections import defaultdict, Counter
from decimal import Decimal


@dataclass
class OrdersService:
    orders: dict[Client, dict[Product, int]]

    """
    {
        Client(name='ANDRZEJ', surname='KOWALSKI', age=20, money=25000): 
            {
                Product(name='laptop', type=<ProductType.ELECTRONICS: 1>, price=Decimal('2400')): 2, 
                Product(name='phone', type=<ProductType.ELECTRONICS: 1>, price=Decimal('2400')): 1, 
                Product(name='Pan Tadeusz', type=<ProductType.BOOKS: 2>, price=Decimal('120')): 1
            }, 
        Client(name='ANDRZEJ', surname='GRABARZ', age=20, money=250): 
            {
                Product(name='tv', type=<ProductType.ELECTRONICS: 1>, price=Decimal('999')): 1, 
                Product(name='nintendo', type=<ProductType.ELECTRONICS: 1>, price=Decimal('20')): 1, 
                Product(name='Krzyzacy', type=<ProductType.BOOKS: 2>, price=Decimal('50')): 1
            }, 
        Client(name='JAKUB', surname='NOWAK', age=45, money=500000): 
            {
                Product(name='TV', type=<ProductType.ELECTRONICS: 1>, price=Decimal('5500')): 1, 
                Product(name='car', type=<ProductType.MOTORIZATION: 3>, price=Decimal('240000')): 1
            }, 
        Client(name='JAN', surname='WISNIEWSKI', age=10, money=150): 
            {
                Product(name='phone', type=<ProductType.ELECTRONICS: 1>, price=Decimal('1200')): 1
            }
    }
    """

    def get_client_with_greatest_payment(self) -> Client:
        clients_and_payment = defaultdict(int)

        for order in self.orders.items():
            clients_and_payment[order[0]] = sum([product.price * quantity for (product, quantity) in order[1].items()])

        return max(clients_and_payment.items(), key=lambda pair: pair[1])

    def get_client_and_greatest_payment_in_category(self, category: ProductType) -> Client:
        grouped_by_clients = {}

        for (client, products) in self.orders.items():
            grouped_by_clients[client] = self._category_and_price(products)

        return max(grouped_by_clients.items(), key=lambda pair: pair[1][category])

    def get_age_and_type(self) -> dict[int, dict[ProductType, int]]:
        grouped_by_age = {}

        for (client, products) in self.orders.items():
            grouped_by_age[client.age] = dict(
                Counter(grouped_by_age.get(client.age, {})) + Counter(self._category_and_quantity(products))
            )

        return grouped_by_age

    def get_category_and_average_price(self) -> dict[ProductType, float]:
        all_products = [
            product
            for (client, products) in self.orders.items()
            for product in products.items()
        ]

        grouped_by_category = defaultdict(float)

        for p_type in ProductType:
            products_of_type = [p for p in all_products if p_type == p[0].type]
            grouped_by_category[p_type] = sum([product.price * quantity for (product, quantity) in products_of_type]) \
                                          / len([quantity for (_, quantity) in products_of_type])

        return dict(grouped_by_category)

    def get_category_and_clients(self):
        all_products = [
            (client, *product)
            for (client, products) in self.orders.items()
            for product in products.items()
        ]

        grouped_by_category = {}

        for p_type in ProductType:
            grouped_by_category[p_type] = [
                (client, quantity) for (client, product, quantity) in all_products if p_type == product.type
            ]

        grouped_by_category_and_quantity = {
            p_type: self._count_client_orders(clients)
            for (p_type, clients) in grouped_by_category.items()
        }

        for (p_type, clients) in grouped_by_category_and_quantity.items():
            grouped_by_category[p_type] = self._group_by_quantity(clients)

        return grouped_by_category

    def get_clients_and_debt(self) -> dict[Client, int]:
        group_by_clients = {}

        for (client, products) in self.orders.items():
            diff = client.money - self._get_full_price(products)
            group_by_clients[client] = abs(diff) if diff < 0 else Decimal('0')

        return group_by_clients

    @staticmethod
    def _category_and_price(products: dict[Product, int]) -> dict[ProductType, int]:
        grouped_by_category = {}

        for p_type in ProductType:
            grouped_by_category[p_type] = sum(
                [product.price * quantity
                 for (product, quantity) in products.items()
                 if p_type == product.type]
            )

        return grouped_by_category

    @staticmethod
    def _category_and_quantity(products: dict[Product, int]) -> dict[ProductType, int]:
        grouped_by_category = {}

        for p_type in ProductType:
            grouped_by_category[p_type] = sum(
                [quantity
                 for (product, quantity) in products.items()
                 if product.type == p_type]
            )

        return grouped_by_category

    @staticmethod
    def _count_client_orders(clients: list[tuple[Client, int]]):
        cnt = Counter()

        for (client, quantity) in clients:
            cnt[client] += quantity

        return dict(cnt)

    @staticmethod
    def _group_by_quantity(clients: dict[Client, int]) -> dict[int, list[Client]]:
        group_by_quantity = defaultdict(list)

        for (client, quantity) in clients.items():
            group_by_quantity[quantity].append(client)

        return dict(group_by_quantity)

    @staticmethod
    def _get_full_price(products: dict[Product, int]) -> int:
        return sum([product.price * quantity for (product, quantity) in products.items()])
