from .data_loader.json.json_service import load_from_json
from .data_loader.orders_loader import get_orders, _convert_orders
from .order.service import OrdersService
from .order.product.model import ProductType
from .logger.model import CustomFormatter, MyLogger

from typing import Final

import logging


def main() -> None:
    """LOGGING"""
    logger = MyLogger.get_logger()

    """APP"""
    logger.warning('STARTING APP')
    FILENAME: Final[str] = 'shop_app/data/orders.json'

    orders_data = load_from_json(FILENAME)
    logger.info('Successfully loaded orders data from JSON file')

    orders = get_orders(orders_data)
    logger.info('Successfully converted orders data to Order objects')

    order_service = OrdersService(_convert_orders(orders))
    logger.info('Successfully created OrdersService object')

    logger.debug('Getting all orders')
    print(order_service.orders)

    logger.debug('Client with greatest payment')
    print(order_service.get_client_with_greatest_payment())

    logger.debug('Client and greatest payment in the category')
    print(order_service.get_client_and_greatest_payment_in_category(ProductType.ELECTRONICS))

    logger.debug('Age and type')
    print(order_service.get_age_and_type())

    logger.debug('Category and average price')
    print(order_service.get_category_and_average_price())

    logger.debug('Clients for each category')
    print(order_service.get_category_and_clients())

    logger.debug('Debt for every client')
    print(order_service.get_clients_and_debt())

    logger.warning('ENDING APP')
