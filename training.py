import requests
import pytest

def test_status_code():
    response = requests.get('https://api/zippopotam.us/us/90210')
    assert response.status_code == 200, "Response code FAILED"