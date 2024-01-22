import requests
import data
import json


def create_order(payload, token):
    response = requests.post(url=data.main_url+data.order_url, data=payload, headers={'Authorization': f'{token}'})
    return response


def get_order(token):
    response = requests.get(url=data.main_url+data.order_url, headers={'Authorization': f'{token}'})
    return response


def get_ingredients():
    response = requests.get(url=data.main_url+data.ingredients_url)
    return response
