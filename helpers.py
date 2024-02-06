import random
import string
from api_methods.orders import Order


class Helpers:
    @staticmethod
    def add_ingredients():
        order_data = {"ingredients": []}
        order = Order()
        order_data["ingredients"].append(order.get_ingredients().json()["data"][0].get("_id"))
        order_data["ingredients"].append(order.get_ingredients().json()["data"][1].get("_id"))
        return order_data

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_credentials(self):
        email = self.generate_random_string(10)
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)
        payload = {
            "email": f'{email}@ya.ru',
            "password": password,
            "name": name
        }
        return payload
