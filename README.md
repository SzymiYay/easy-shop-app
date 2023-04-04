#### <p align="center">The project is currently in the development phase, and new features are being added!</p>
---

# SHOP SERVICE

The project takes data from a json file. Then from the console we have the ability to manage orders.
Project written in learning Python, JSON, data management, data validation and testing. 

I plan to add a database layer and UI (FastAPI, Flask).


## Built With
- Python
- Pytest
- Unittest
- Poetry
- MySQL
- Docker


## Getting Started
1. Clone the repo
   ```sh
   git clone https://github.com/SzymiYay/easy-shop-app
   ```
2. To start the project, you need to have Python and Poetry installed on your computer.
3. Set on the project directory.
4. Run application:
   ```sh
   poetry run pyhton -m shop_app
   ```
5. Run tests:
   ```sh
   pytest
   ```
   
## Usage
Example JSON:
```json
[
  {
    "client": {
      "name": "ANDRZEJ",
      "surname": "KOWALSKI",
      "age": 20,
      "money": 25000
    },
    "basket": [
      {
        "name": "laptop",
        "type": "ELECTRONICS",
        "price": 2400
      },
      {
        "name": "laptop",
        "type": "ELECTRONICS",
        "price": 2400
      },
      {
        "name": "phone",
        "type": "ELECTRONICS",
        "price": 2400
      },
      {
        "name": "Pan Tadeusz",
        "type": "BOOKS",
        "price": 120
      }
    ]
  }
]
```

From the json file, download the data. Then, using the get_orders function to validate the data, 
place it in an array and create a CarsService object.
Having such an object, you can manage the data in various ways.

```python
def main() -> None:
   FILENAME: Final[str] = 'shop_app/data/orders.json'
   orders_data = load_from_json(FILENAME)
   orders = get_orders(orders_data)
   order_service = OrdersService(_convert_orders(orders))
   
   print(order_service.get_client_with_greatest_payment())
   print(order_service.get_client_and_greatest_payment_in_category(ProductType.ELECTRONICS))
   print(order_service.get_age_and_type())
```


## Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new-feature`)
3. Commit your Changes (`git commit -m 'Add some new-feature'`)
4. Push to the Branch (`git push origin feature/new-feature`)
5. Open a Pull Request


## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact
Szymon Frączek - szymoon09@gmail.com
