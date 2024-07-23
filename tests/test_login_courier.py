import requests
from faker import Faker
from base.create_courier import register_new_courier_and_return_login_password


class TestLoginCourier():
    def test_login_courier(self):
        login_pass = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)
        assert response.status_code == 200
        id = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data={"login": {payload['login']}, "password": {payload['password']}})
        new_courier_id = id.json()['id']
        response_delete = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{new_courier_id}")
        assert response_delete.status_code == 200

    def test_invalid_login_courier(self):
        login_pass = register_new_courier_and_return_login_password()
        login = login_pass[0]
        faker = Faker()
        payload = {
            "login": login,
            "password": faker.password()
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)
        assert response.json() == {"code":404,"message":"Учетная запись не найдена"}

    def test_login_courier_without_login(self):
        login_pass = register_new_courier_and_return_login_password()
        password = login_pass[1]
        payload = {
            "password": password
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)
        assert response.json() == {"code":400,"message":"Недостаточно данных для входа"}

    def test_login_courier_return_id(self):
        login_pass = register_new_courier_and_return_login_password()
        login = login_pass[0]
        password = login_pass[1]
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)
        current_id = response.json()
        assert 'id' in current_id
        id = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
                           data={"login": {payload['login']}, "password": {payload['password']}})
        new_courier_id = id.json()['id']
        response_delete = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{new_courier_id}")
        assert response_delete.status_code == 200

