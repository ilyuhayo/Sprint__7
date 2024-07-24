import pytest
import requests
from urls import API_URLS


class TestCreateOrder:
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], [""]])
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }
        response = requests.post(API_URLS.CREATE_ORDER_ENDPOINT, json=payload)
        track = response.json()
        assert 'track' in track
