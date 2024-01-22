import requests
import data


def user_login(payload):
    response = requests.post(url=data.main_url+data.login_url, data=payload)
    return response

