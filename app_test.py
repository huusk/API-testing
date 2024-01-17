import requests
import pytest



def test_nevtreh_sms():
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test")
    if response.status_code == 200:
        json_response = response.json()

        assert json_response == {
            'cmd': "unit",
            'msisdn': "89132412"
        }, f"Failed to match JSON. Actual response: {json_response}"

        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        # assert response.json() == expected_error_response, f"Failed to match error response. Actual response: {response.json()}"

def test_avtomat_tseneglelt_list():
    response = requests.get("https://endpoint.unitel.mn/unitelapp/test/api/test")
