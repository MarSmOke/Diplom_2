import requests
import data


def update_data(payload, token):
    response = requests.patch(url=data.main_url+data.user_url, data=payload, headers={'Authorization': f'{token}'})
    return response
