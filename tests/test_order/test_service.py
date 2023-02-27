from shop_app.data_loader.orders_loader import _convert_orders, get_orders
from shop_app.data_loader.json.json_service import load_from_json
from shop_app.order.service import OrdersService
from shop_app.order.product.model import ProductType

from decimal import Decimal

import unittest
import json


class TestOrdersService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        orders_data = load_from_json('shop_app/data/orders.json')
        orders = get_orders(orders_data)
        cls.os = OrdersService(_convert_orders(orders))

    def test_get_client_with_greatest_payment(self):
        result = self.os.get_client_with_greatest_payment()
        self.assertEqual(result[0].name, 'JAKUB')
        self.assertEqual(result[0].surname, 'NOWAK')
        self.assertEqual(result[0].age, 45)
        self.assertEqual(result[0].money, 500000)
        self.assertEqual(result[1], Decimal('245500'))

    def test_get_client_and_greatest_payment_in_category(self):
        result = self.os.get_client_and_greatest_payment_in_category(ProductType.ELECTRONICS)
        self.assertEqual(result[0].name, 'ANDRZEJ')
        self.assertEqual(result[0].surname, 'KOWALSKI')
        self.assertEqual(result[0].age, 20)
        self.assertEqual(result[0].money, 25000)
        self.assertEqual(result[1][ProductType.ELECTRONICS], Decimal('7200'))
        self.assertEqual(result[1][ProductType.BOOKS], Decimal('120'))
        self.assertEqual(result[1][ProductType.MOTORIZATION], 0)

    def test_get_age_and_type(self):
        result = self.os.get_age_and_type()
        expected_result = {20: {ProductType.ELECTRONICS: 5, ProductType.BOOKS: 2},
                           45: {ProductType.ELECTRONICS: 1, ProductType.MOTORIZATION: 1},
                           10: {ProductType.ELECTRONICS: 1}}
        self.assertEqual(result, expected_result)

    def test_get_category_and_average_price(self):
        result = self.os.get_category_and_average_price()
        expected_result = {ProductType.ELECTRONICS: Decimal('2486.5'),
                           ProductType.BOOKS: Decimal('85'),
                           ProductType.MOTORIZATION: Decimal('240000')}
        self.assertEqual(result, expected_result)

    def test_get_category_and_clients(self):
        """
        {
            <ProductType.ELECTRONICS: 1>:
            {
                3: [Client(name='ANDRZEJ', surname='KOWALSKI', age=20, money=25000)],
                2: [Client(name='ANDRZEJ', surname='GRABARZ', age=20, money=250)],
                1: [Client(name='JAKUB', surname='NOWAK', age=45, money=500000), Client(name='JAN', surname='WISNIEWSKI', age=10, money=150)]
            },
            <ProductType.BOOKS: 2>:
            {
                1: [Client(name='ANDRZEJ', surname='KOWALSKI', age=20, money=25000), Client(name='ANDRZEJ', surname='GRABARZ', age=20, money=250)]
            },
            <ProductType.MOTORIZATION: 3>:
            {
                1: [Client(name='JAKUB', surname='NOWAK', age=45, money=500000)]
            }
        }
        """
        pass

    def test_get_clients_and_debt(self):
        """
        {
            Client(name='ANDRZEJ', surname='KOWALSKI', age=20, money=25000): Decimal('0'),
            Client(name='ANDRZEJ', surname='GRABARZ', age=20, money=250): Decimal('819'),
            Client(name='JAKUB', surname='NOWAK', age=45, money=500000): Decimal('0'),
            Client(name='JAN', surname='WISNIEWSKI', age=10, money=150): Decimal('1050')
        }
        """
        pass


if __name__ == '__main__':
    unittest.main()
