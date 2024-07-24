import requests
from conftest import courier
from conftest import fake_data
from urls import API_URLS
from responses_text import RESPONSES_TEXT


class TestCreateCourier:
    def test_create_courier(self, fake_data):
        response = requests.post(API_URLS.CREATE_COURIER_ENDPOINT, data=fake_data)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        id = requests.post(API_URLS.LOGIN_COURIER_ENDPOINT, data={"login": fake_data['login'], "password": fake_data['password']})
        new_courier_id = id.json()['id']
        response_delete = requests.delete(f"{API_URLS.DELETE_COURIER_ENDPOINT}{new_courier_id}")
        assert response_delete.status_code == 200

    def test_create_identical_couriers(self, courier):
        payload = {
            "login": courier['login'],
            "password": courier['password'],
            "firstName": courier['firstName']
        }
        response = requests.post(API_URLS.CREATE_COURIER_ENDPOINT, data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == RESPONSES_TEXT.EXISTING_LOGIN_ERROR

    def test_create_courier_without_password(self, fake_data):
        payload = {
            "login": fake_data["login"],
            "firstName": fake_data["firstName"]
        }
        response = requests.post(API_URLS.CREATE_COURIER_ENDPOINT, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == RESPONSES_TEXT.NOT_ENOUGH_AUTH_DATA_ERROR

    def test_create_courier_with_existing_login(self):
        payload = {
            "login": "dyadka",
            "password": "123456",
            "firstName": "andre"
        }
        response = requests.post(API_URLS.CREATE_COURIER_ENDPOINT, data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == RESPONSES_TEXT.EXISTING_LOGIN_ERROR































