import requests
import json

def test_login():
    data = {
            "cmd": "smscode",
            "msisdn": "89422412",
            "domain": "unitel"
            }
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    python_object = response.json()
    result_value = python_object.get("result", {})
    isData = result_value.get("sent_msisdn", {})
    if not isData:
        print("FAIL: Амжилтгүй")
    else:
        print(isData)
        print("PASS: Амжилттай")
def test_checkOtp():
    data = {
            "cmd": "loginsms",
            "msisdn": "89422412",
            "smscode": "0000"
            }
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    python_object = response.json()
    validate_result_keys(python_object)
def validate_result_keys(result_data):
    result_value = result_data.get("result", {})
    expected_keys = ["domain", "display", "type","msisdn", "token", "info"]
    for key in expected_keys:
        if key not in result_value:
            print(f"FAIL: Key '{key}' is missing in the response JSON")
        else:
            print(f"{key}: {result_value[key]}")


def test_data_list():
    data = {
        "cmd": "unit",
        "msisdn": "89422412"
    }
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)

    python_object = response.json()
    result_value = python_object.get("result", {}).get("unitPackages", [])

    check_keys(result_value, ["name", "unit", "price", "period","cardType","description","isAuto","id"])
def check_keys(result_value, param):
    for i, result_item in enumerate(result_value, start=1):
        print(f"Result {i}")
        for j, package_item in enumerate(result_item.get("packages", []), start=1):
            print(f"  Package {j}")
            print(f"Packageld:{package_item.get('id')}")
            for key in param:
                status = "PASS" if key in package_item else "FAIL"
                print(
                    f"    {status}: Key '{key}' is {'present' if status == 'PASS' else 'missing'} in the response JSON")


def test_paymentOptions():
    data = {
        "cmd": "paymentOptions",
    }
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)

    json_data = response.json()
    result_data = json_data.get('result', {})
    qpay_list = result_data.get('qpay', [])
    values_to_test = ["mbank", "khanbank", "statebank", "most","xacbank","capitronbank","tdbbank","bogdbank","statebankmongolia"]

    for value in values_to_test:
        if value in qpay_list:
            print(f"PASS: Value '{value}' is present in the 'qpay' list")
        else:
            print(f"FAIL: Value '{value}' is missing in the 'qpay' list")

def test_neg_avah():
    data = {
        "amount": "5000",
        "vat": {
            "vat_corp": "",
            "vat_type": "self",
            "isOnce": "YES"
        },
        "cmd": "checkCard",
        "id": "42",
        "msisdn": "89422412",
        "option": "khanbank"
    }
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)

    json_data = response.json()
    result_data = json_data.get('result', {})
    values_to_test = ["appStore", "playStore", "url", "trid"]


    for value in values_to_test:
        if value in result_data:
            print(f"PASS: Value '{value}' is present in the 'qpay' list")
            print(f"url:{result_data.get('url')}")
        else:
            print(f"FAIL: Value '{value}' is missing in the 'qpay' list")



