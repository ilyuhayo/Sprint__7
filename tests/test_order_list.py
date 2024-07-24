import requests


class TestOrderList:
    def test_get_order_list(self):
        response = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders")
        order_data = response.json()
        order_list = order_data['orders']
        assert isinstance(order_list, list)