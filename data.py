import random
import string
from api_methods.orders import *

main_url = 'https://stellarburgers.nomoreparties.site/api/'
create_url = 'auth/register'
login_url = 'auth/login'
user_url = 'auth/user'
order_url = 'orders'
token_url = 'auth/token'
ingredients_url = 'ingredients'


def add_ingredients():
    order_data = {"ingredients": []}
    order_data["ingredients"].append(get_ingredients().json()["data"][0].get("_id"))
    order_data["ingredients"].append(get_ingredients().json()["data"][1].get("_id"))
    return order_data


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_credentials():
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": f'{email}@ya.ru',
        "password": password,
        "name": name
    }
    return payload
