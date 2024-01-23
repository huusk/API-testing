import requests
import json

def make_request(cmd, data):
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json={"cmd": cmd, **data})
    print(response.text)
    return response.json()

def test_getPayment():
    data = {"msisdn": "89422412"}
    python_object = make_request("getPayment", data)
    validate_result_keys2(python_object)
    print(python_object)
def validate_result_keys2(result_data):
    result_value = result_data.get("result", {})
    expected_keys = ["currentMonth", "payment", "invoiceDate", "invoiceStatus"]
    for value in expected_keys:
        if value in result_value:
            print(f"PASS: Value '{value}' is present in the 'qpay' list")
        else:
            print(f"FAIL: Value '{value}' is missing in the 'qpay' list")

def test_payment_options():
    python_object = make_request("paymentOptions", {})
    qpay_list = python_object.get('result', {}).get('qpay', [])
    values_to_test = ["mbank", "khanbank", "statebank", "most", "xacbank", "capitronbank", "tdbbank", "bogdbank", "statebankmongolia"]

    for value in values_to_test:
        print(f"PASS: Value '{value}' is present in the 'qpay' list") if value in qpay_list else print(f"FAIL: Value '{value}' is missing in the 'qpay' list")

def test_checkPay():
    data = {"vat": {"vat_corp": "", "vat_type": "self", "isOnce": "YES"}, "topay": [{"amount": "100", "msisdn": "", "upoint": 0}],"msisdn": "89422412", "option": "khanbank","upoint": "0"}
    python_object = make_request("checkPay", data)
    validate_result_keys(python_object)

def validate_result_keys(result_data):
        result_value = result_data.get("result", {})
        expected_keys = ["appStore", "playStore", "url", "trid"]
        for value in expected_keys:
            if value in result_value:
                print(f"PASS: Value '{value}' is present in the 'checkPay' list")
            else:
                print(f"FAIL: Value '{value}' is missing in the 'checkPay' list")
def test_main():
    test_getPayment()
    test_payment_options()
    test_checkPay()