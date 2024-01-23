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
def test_Info():
    data = {"msisdn": "89422412","token":"A8FF6YJRNYW7DK8CJO0F"}
    python_object = make_request("info", data)
    validate_result_keys(python_object)

def validate_result_keys(result_data):
    result_value = result_data.get("result", {})
    expected_keys = ["isPay", "balance", "domain", "display", "bill", "expireDate","" "type", "msisdn", "user"]
    for key in expected_keys:
        status = "PASS" if key in expected_keys else "FAIL"
        print(f"    {status}: Key '{key}' is {'present' if status == 'PASS' else 'missing'} in the response JSON")

def test_usageDetails():
    data = {"msisdn": "89422412","token":"A8FF6YJRNYW7DK8CJO0F"}
    python_object = make_request("usageDetails", data)
    validate_result_keys(python_object)
    print(python_object)
def validate_result_keys(result_data):
    result_value = result_data.get("result", {})
    expected_keys = ["date", "package", "domain", "additional", "main"]
    for key in expected_keys:
        status = "PASS" if key in expected_keys else "FAIL"
        print(f"    {status}: Key '{key}' is {'present' if status == 'PASS' else 'missing'} in the response JSON")
def test_main():
    test_login()
    test_check_otp()
    test_Info()
    test_usageDetails()