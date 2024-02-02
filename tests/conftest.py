import pytest
import requests
import urls
from helpers import Helpers


@pytest.fixture
def user_create_and_delete():
    helper = Helpers()
    payload = helper.generate_credentials()
    response = requests.post(url=urls.main_url+urls.create_url, data=payload)
    access_token = response.json()["accessToken"]
    yield response, payload, access_token
    requests.delete(url=urls.main_url+urls.create_url, headers={'Authorization': access_token})
