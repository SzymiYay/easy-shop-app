from shop_app.data_loader.orders_loader import get_orders, _convert_orders, count_products

import unittest
import json


class TestOrdersLoader(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        with open('shop_app/data/orders.json', 'r') as jf:
            cls.orders = json.load(jf)

    def test_get_orders(self):
        orders = get_orders(self.orders)
        self.assertEqual(4, len(orders))
        self.assertEqual(4, len(orders[0].basket.items))
        self.assertEqual(3, len(orders[1].basket.items))

    def convert_orders(self):
        orders = get_orders(self.orders)
        converted_orders = _convert_orders(orders)
        self.assertEqual(2, len(converted_orders))
        self.assertEqual(4, len(converted_orders[orders[0].client]))
        self.assertEqual(3, len(converted_orders[orders[1].client]))


if __name__ == '__main__':
    unittest.main()
