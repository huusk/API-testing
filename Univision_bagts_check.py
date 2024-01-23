import requests
import json
import unittest

def make_request(cmd, data):
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json={"cmd": cmd, **data})
    print(response.text)
    return response.json()

def test_login():
    data = {"msisdn": "89422412", "domain": "unitel"}
    python_object = make_request("smscode", data)
    is_data = python_object.get("result", {}).get("sent_msisdn", {})
    print("FAIL: Амжилтгүй" if not is_data else is_data)

def test_check_otp():
    data = {"msisdn": "89422412", "smscode": "0000"}
    python_object = make_request("loginsms", data)
    validate_result_keys(python_object)

def validate_result_keys(result_data):
    result_value = result_data.get("result", {})
    expected_keys = ["domain", "display", "type", "msisdn", "token", "info"]
    for key in expected_keys:
        print(f"{key}: {result_value.get(key)}")
def test_univision_bagts_check():
    data = {"msisdn": "89422412","token":"9BLT3CLFTPBKEXR9Q4HJ"} #Tokeniig bainga solih
    python_object = make_request("getSvodList", data)
    validate_result_keys(python_object)
    result_value = python_object.get("result", {}).get("list", {}).get("additional", [])
    check_keys(result_value, ["date", "name", "isAuto", "period", "externalId", "isActivated", "day", "id"])


def check_keys(result_value, param):
    for i, result_item in enumerate(result_value, start=1):
        print(f"Result {i}")
        for key in result_item:
                status = "PASS" if key in result_item else "FAIL"
                print(f"    {status}: Key '{key}' is {'present' if status == 'PASS' else 'missing'} in the response JSON")


def test_main():
    test_login()
    test_check_otp()
    test_univision_bagts_check()