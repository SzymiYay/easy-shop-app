from shop_app.order.model import Order
from shop_app.order.product.model import ProductType

import unittest


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.order = {
            "client": {
                "name": "JAKUB",
                "surname": "NOWAK",
                "age": 45,
                "money": 500000
            },
            "basket": [
                {
                    "name": "TV",
                    "type": "ELECTRONICS",
                    "price": 5500
                },
                {
                    "name": "car",
                    "type": "MOTORIZATION",
                    "price": 240000
                }
            ]
        }

    def test_from_dict(self):
        order = Order.from_dict(self.order)
        self.assertEqual(order.client.name, 'JAKUB')
        self.assertEqual(order.client.surname, 'NOWAK')
        self.assertEqual(order.client.age, 45)
        self.assertEqual(order.client.money, 500000)
        self.assertEqual(order.basket.items[0].name, 'TV')
        self.assertEqual(order.basket.items[0].type, ProductType.ELECTRONICS)
        self.assertEqual(order.basket.items[0].price, 5500)
        self.assertEqual(order.basket.items[1].name, 'car')
        self.assertEqual(order.basket.items[1].type, ProductType.MOTORIZATION)
        self.assertEqual(order.basket.items[1].price, 240000)


if __name__ == '__main__':
    unittest.main()
