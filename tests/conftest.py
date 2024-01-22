import pytest
import requests
import data


@pytest.fixture
def user_create_and_delete():
    payload = data.generate_credentials()
    response = requests.post(url=data.main_url+data.create_url, data=payload)
    access_token = response.json()["accessToken"]
    yield response, payload, access_token
    requests.delete(url=data.main_url+data.create_url, headers={'Authorization': access_token})
