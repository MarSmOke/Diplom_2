import requests
import urls
import allure


class Order:
    @allure.step('Create order')
    def create_order(self, payload, token):
        response = requests.post(url=urls.main_url + urls.order_url, data=payload,
                                 headers={'Authorization': f'{token}'})
        return response

    @allure.step('Get order')
    def get_order(self, token):
        response = requests.get(url=urls.main_url + urls.order_url, headers={'Authorization': f'{token}'})
        return response

    @allure.step('Get ingredients')
    def get_ingredients(self):
        response = requests.get(url=urls.main_url + urls.ingredients_url)
        return response
