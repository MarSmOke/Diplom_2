import requests
import urls
import allure


class LoginUser:
    @allure.step('Login user')
    def user_login(self, payload):
        response = requests.post(url=urls.main_url + urls.login_url, data=payload)
        return response

