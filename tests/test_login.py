import allure
import pytest
from api_methods.login import LoginUser


class TestLoginUser(LoginUser):
    @allure.title("Successful user login")
    @allure.description("User login with existing credentials")
    def test_login_successful(self, user_create_and_delete):
        response = LoginUser.user_login(self, user_create_and_delete[1])
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Existent user login with invalid data")
    @allure.description("User login with invalid credentials, expected error")
    @pytest.mark.parametrize('payload', [
                             {"email": "test-data_sm3@yandex.ru", "password": "password"},
                             {"email": "test-data_sm@yandex.ru", "password": "password1"}])
    def test_login_invalid_credentials_error(self, payload):
        response = LoginUser.user_login(self, payload)
        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect"
