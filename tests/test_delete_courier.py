import requests
from conftest import courier_without_del


class TestDeleteCourier():
    def test_delete_courier(self, courier_without_del):
        courier_id = courier_without_del['id']
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
        assert response.status_code == 200
        assert response.json() == {"ok": True}




