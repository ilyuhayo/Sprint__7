import requests
from conftest import courier
from urls import API_URLS
from responses_text import RESPONSES_TEXT


class TestLoginCourier():
    def test_login_courier(self, courier):
        payload = {
            "login": courier['login'],
            "password": courier['password']
        }
        response = requests.post(API_URLS.LOGIN_COURIER_ENDPOINT, data=payload)
        assert response.status_code == 200

    def test_invalid_login_courier(self, courier):
        invalid_password = "wrongpassword123"
        payload = {
            "login": courier['login'],
            "password": invalid_password
        }
        response = requests.post(API_URLS.LOGIN_COURIER_ENDPOINT, data=payload)
        assert response.status_code == 404
        assert response.json()["message"] == RESPONSES_TEXT.ACCOUNT_NOT_FOUND

    def test_login_courier_without_login(self, courier):
        payload = {
            "password": courier['password']
        }
        response = requests.post(API_URLS.LOGIN_COURIER_ENDPOINT, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == RESPONSES_TEXT.NOT_ENOUGH_ENTER_DATA_ERROR

    def test_login_courier_return_id(self, courier):
        payload = {
            "login": courier['login'],
            "password": courier['password']
        }
        response = requests.post(API_URLS.LOGIN_COURIER_ENDPOINT, data=payload)
        current_id = response.json()
        assert 'id' in current_id
        assert response.status_code == 200

