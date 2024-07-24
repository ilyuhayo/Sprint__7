import requests
from urls import API_URLS


class TestOrderList:
    def test_get_order_list(self):
        response = requests.get(API_URLS.CREATE_ORDER_ENDPOINT)
        order_data = response.json()
        order_list = order_data['orders']
        assert isinstance(order_list, list)