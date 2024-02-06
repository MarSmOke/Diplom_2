import allure
from api_methods.orders import Order


class TestGetOrder:
    @allure.title("Authorized user gets orders successfully")
    @allure.description("Gel all orders for authorized user")
    def test_get_orders_successful(self, user_create_and_delete):
        token = user_create_and_delete[2]
        order = Order()
        response_get = order.get_order(token)
        assert response_get.status_code == 200 and response_get.json()["success"] is True

    @allure.title("Get user's orders without authorization")
    @allure.description("User without token, expected error")
    def test_get_orders_error(self):
        token = None
        order = Order()
        response = order.get_order(token)
        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"