import requests
from conftest import courier
from urls import API_URLS


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
        assert response.json() == {"code":404,"message":"Учетная запись не найдена"}

    def test_login_courier_without_login(self, courier):
        payload = {
            "password": courier['password']
        }
        response = requests.post(API_URLS.LOGIN_COURIER_ENDPOINT, data=payload)
        assert response.json() == {"code":400,"message":"Недостаточно данных для входа"}

    def test_login_courier_return_id(self, courier):
        payload = {
            "login": courier['login'],
            "password": courier['password']
        }
        response = requests.post(API_URLS.LOGIN_COURIER_ENDPOINT, data=payload)
        current_id = response.json()
        assert 'id' in current_id
        assert response.status_code == 200

