import requests
import urls
import allure


class CreateUser:
    @allure.step('Create user')
    def register_user(self, payload):
        response = requests.post(url=urls.main_url + urls.create_url, data=payload)
        return response

