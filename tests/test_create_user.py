import allure
import pytest
from api_methods.create_user import CreateUser


class TestCreateUser:
    @allure.title("Successful user registration")
    @allure.description("User registration with valid data")
    def test_create_user_successful(self, user_create_and_delete):
        response = user_create_and_delete[0]
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("User re-registration")
    @allure.description("User registration with existing data, expected error")
    def test_create_user_duplication_error(self, user_create_and_delete):
        create_user = CreateUser()
        response = create_user.register_user(user_create_and_delete[1])
        assert response.status_code == 403 and response.json()["message"] == "User already exists"

    @allure.title("User registration without one of mandatory fields")
    @allure.description("User registration without login, email or name, expected error")
    @pytest.mark.parametrize('payload',
                             [{"email": "test-data_sm@yandex.ru", "password": "password"},
                              {"password": "password", "name": "Username"},
                              {"email": "test-data_sm@yandex.ru", "name": "Username"}])
    def test_create_courier_without_required_field_error(self, payload):
        create_user = CreateUser()
        response = create_user.register_user(payload)
        assert response.status_code == 403 and response.json()["message"] == "Email, password and name are required fields"