import requests
import pytest

def test_status_code():
    response = requests.get('https://api/zippopotam.us/us/90210')
    assert response.status_code == 200, "Response code FAILED"



# import requests
#
# try:
#     response = requests.get("https://www.example.com")
#     response.raise_for_status()  # Raise an exception for error status codes
#
#     # Print the response body based on its content type:
#     if response.headers.get("Content-Type") == "application/json":
#         print(response.json())
#     else:
#         print(response.text)
#
# except requests.exceptions.RequestException as e:
#     print("Error fetching response:", e)