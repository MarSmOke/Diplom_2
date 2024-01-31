import allure
from helpers import Helpers
from api_methods.orders import Order


class TestCreateOrder(Order):
    @allure.title("Order creation with token")
    @allure.description("Order is created by authorized user")
    def test_create_order_with_token(self, user_create_and_delete):
        token = user_create_and_delete[2]
        response = Order.create_order(self, Helpers.add_ingredients(self), token)
        assert response.status_code == 200 and response.json()["order"].get("status") == "done"

    @allure.title("Order creation without token")
    @allure.description("Order is created by unauthorized user")
    def test_create_order_without_token(self):
        token = None
        response = Order.create_order(self, Helpers.add_ingredients(self), token)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Order creation without ingredients")
    @allure.description("Order is not created without ingredients")
    def test_create_order_without_ingredients_error(self):
        token = None
        response = Order.create_order(self, {"ingredients": []}, token)
        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Order creation with incorrect id")
    @allure.description("Order is not created with incorrect id")
    def test_create_order_with_incorrect_hash_error(self):
        token = None
        response = Order.create_order(self, {"ingredients": ["60d3b41abdacab0026a733c6"]}, token)
        assert response.status_code == 400 and response.json()["message"] == "One or more ids provided are incorrect"

    @allure.title("Order creation with incorrect hash")
    @allure.description("Order is not created with incorrect hash")
    def test_create_order_with_incorrect_hash_error(self):
        token = None
        response = Order.create_order(self, {"ingredients": ["60d3b"]}, token)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
