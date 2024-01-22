import allure
import data
from api_methods.orders import *


class TestCreateOrder:
    @allure.title("Order creation with token")
    @allure.description("Order is created by authorized user")
    def test_create_order_with_token(self, user_create_and_delete):
        token = user_create_and_delete[2]
        response = create_order(data.add_ingredients(), token)
        assert response.status_code == 200 and response.json()["order"].get("status") == "done"

    @allure.title("Order creation without token")
    @allure.description("Order is created by unauthorized user")
    def test_create_order_without_token(self):
        token = None
        response = create_order(data.add_ingredients(), token)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Order creation without ingredients")
    @allure.description("Order is not created without ingredients")
    def test_create_order_without_ingredients_error(self):
        token = None
        response = create_order({"ingredients": []}, token)
        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Order creation with incorrect id")
    @allure.description("Order is not created with incorrect id")
    def test_create_order_with_incorrect_hash_error(self):
        token = None
        response = create_order({"ingredients": ["60d3b41abdacab0026a733c6"]}, token)
        assert response.status_code == 400 and response.json()["message"] == "One or more ids provided are incorrect"

    @allure.title("Order creation with incorrect hash")
    @allure.description("Order is not created with incorrect hash")
    def test_create_order_with_incorrect_hash_error(self):
        token = None
        response = create_order({"ingredients": ["60d3b"]}, token)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
