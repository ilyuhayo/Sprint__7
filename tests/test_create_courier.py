import requests
from faker import Faker
from conftest import courier

class TestCreateCourier:
    def test_create_courier(self):
        faker = Faker()
        payload = {
            "login": faker.user_name(),
            "password": faker.password(),
            "firstName": faker.first_name()
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        id = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data={"login": {payload['login']}, "password": {payload['password']}})
        new_courier_id = id.json()['id']
        response_delete = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{new_courier_id}")
        assert response_delete.status_code == 200

    def test_create_identical_couriers(self, courier):
        payload = {
            "login": courier['login'],
            "password": courier['password'],
            "firstName": courier['firstName']
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    def test_create_courier_without_password(self):
        faker = Faker()
        payload = {
            "login": faker.user_name(),
            "firstName": faker.first_name()
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_with_existing_login(self):
        payload = {
            "login": "dyadka",
            "password": "123456",
            "firstName": "andre"
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}






















