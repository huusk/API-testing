import requests
import pytest

def test_get_equals_200():
    resp = requests.get("http://api.zippopotam.us/us/90210")
    assert resp.status_code== 200, "Get request failed"

#Exercise 2
def test_content():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers["Content-Type"]=="application/json"
    print(response.json)

#Exercise 3
def test_response_equals():
    response = requests.get("http://api.zippopotam.us/us/90210")
    print(response.content)
    json_response = response.json()
    assert json_response['country']== "United States", "Fail to match json"

#Exercise 4
def test_place_name():
    response = requests.get("http://api.zippopotam.us/us/90210")
    json_response = response.json()
    assert json_response['places'][0]['place name'] == "Beverly Hills", "FAIL"

#Exercise 5
def response_one():
    response = requests.get("http://api.zippopotam.us/us/90210")
    json_response = response.json()
    assert len(json_response['places'])==1