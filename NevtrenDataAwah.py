import requests
import json

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

def test_data_list():
    data = {"msisdn": "89422412"}
    python_object = make_request("data", data)
    result_value = python_object.get("result", {}).get("dataPackages", [])
    check_keys(result_value, ["name", "promoPrice", "price", "period", "type", "description", "isPromo", "id" , "pill", "amount"])

def check_keys(result_value, param):
    for i, result_item in enumerate(result_value, start=1):
        print(f"Result {i}")
        for j, result_value in enumerate(result_item.get("packages", []), start=1):
            print(f"  Package {j}")
            print(f"Packageld:{result_value.get('id')}")
            for key in param:
                status = "PASS" if key in result_value else "FAIL"
                print(f"    {status}: Key '{key}' is {'present' if status == 'PASS' else 'missing'} in the response JSON")

def test_payment_options():
    python_object = make_request("paymentOptions", {})
    qpay_list = python_object.get('result', {}).get('qpay', [])
    values_to_test = ["mbank", "khanbank", "statebank", "most", "xacbank", "capitronbank", "tdbbank", "bogdbank", "statebankmongolia"]

    for value in values_to_test:
        print(f"PASS: Value '{value}' is present in the 'qpay' list") if value in qpay_list else print(f"FAIL: Value '{value}' is missing in the 'qpay' list")

def test_data_avah():
    data = {"amount": "5000", "vat": {"vat_corp": "", "vat_type": "self", "isOnce": "YES"}, "cmd": "checkCard", "id": "2", "msisdn": "89422412", "option": "khanbank"}
    python_object = make_request("checkCard", data)
    values_to_test = ["appStore", "playStore", "url", "trid"]

    for value in values_to_test:
        print(f"PASS: Value '{value}' is present in the 'result'") if value in python_object['result'] else print(f"FAIL: Value '{value}' is missing in the 'qpay' list")
def test_main():
    test_login()
    test_check_otp()
    test_data_list()
    test_payment_options()
    test_data_avah()
