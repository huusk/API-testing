import requests
import pytest
import random
from lxml import etree
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
def test_response_one():
    response = requests.get("http://api.zippopotam.us/us/90210")
    json_response = response.json()
    assert len(json_response['places'])==1

#Exercise 6
def test_response_body_elements():
    response = requests.get("https://api.zippopotam.us/us/90210")
    body = response.json()
    assert body['post code'] == '90210'

def test_name():
    another_resp = requests.get('https://api.zippopotam.us/us/90210')
    body = another_resp.json()
    # assert body['post code'] == "90210"
    assert body['places'][0]['place name'] == 'Beverly Hills'


def create_new_post_object():

    return {
        "name": "JHusleee",
        "address": {
            "street": "Main Street",
            "number": random.randint(1000, 9999),
            "zipCode": 90210,
            "city": "Beverly Hills"
        }
    }
def test_send_json_with_unique_number():
    response = requests.post("https://postman-echo.com/post", json=create_new_post_object())
    print(response.request.body)
    assert response.status_code == 200

# def test_get_xml():
#     resp = requests.get("http://parabank.parasoft.com/parabank/services/bank/accounts/12345")
#     response_xml = etree.fromstring(resp.content)
#     xml_tree = etree.ElementTree(response_xml)
#     first_name = xml_tree.find("customerId")
#     assert first_name.text == "12212"

# def test_greater_than_five():
#     response = requests.get("https://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts")
#     response_body_as_xml = etree.fromstring()

# def test_with_authorization():
#     response = requests.get('http://my.secure.api', headers={'Authorization': 'Bearer fskjvcsndnvkjcndsjvnkjdsnjfe647875489273878'})
#
# data_set = {
#     ('us', '90210', 'Beverly Hills'),
#     ('it', '50123', 'Firenze'),
#     ('ca', 'B2A', 'North Sydney South Central')
# }
# @pytest.mark.parametrize('country_code, zip_code, expected_place', data_set)
# def test_for_place_name(country_code, zip_code, expected_place):
#     response = requests.get(f'https://api.zippopotam.us/{country_code}/{zip_code}')
#     body = response.json()
#     assert body['places'][0]['place name'] == expected_place