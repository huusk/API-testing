import requests
import pytest

def get_right_response():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    json_response = response.json()
    assert json_response['name'] == "Leanne Graham"


# def test_get_equals_200():
#     resp = requests.get("http://api.zippopotam.us/us/90210")
#     assert resp.status_code== 122, "Get request failed"
