import random
import string
from api_methods.orders import Order


class Helpers(Order):
    def add_ingredients(self):
        order_data = {"ingredients": []}
        order_data["ingredients"].append(Order.get_ingredients(self).json()["data"][0].get("_id"))
        order_data["ingredients"].append(Order.get_ingredients(self).json()["data"][1].get("_id"))
        return order_data

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_credentials():
        email = Helpers.generate_random_string(10)
        password = Helpers.generate_random_string(10)
        name = Helpers.generate_random_string(10)
        payload = {
            "email": f'{email}@ya.ru',
            "password": password,
            "name": name
        }
        return payload
