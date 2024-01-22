import requests
import data


def register_user(payload):
    response = requests.post(url=data.main_url+data.create_url, data=payload)
    return response

