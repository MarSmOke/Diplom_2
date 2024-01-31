import requests
import urls
import allure


class UpdateUserData:
    @allure.step('Update user data')
    def update_data(self, payload, token):
        response = requests.patch(url=urls.main_url + urls.user_url, data=payload,
                                  headers={'Authorization': f'{token}'})
        return response
