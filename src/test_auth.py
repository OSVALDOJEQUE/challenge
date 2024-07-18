import requests
import pytest
from src.utils import BASE_URL, HEADERS

def test_generate_token_valid_credentials():
    response = requests.post(BASE_URL + "/token", json={"username": "user", "password": "pass123"}, headers=HEADERS)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_generate_token_invalid_credentials():
    response = requests.post(BASE_URL + "/token", json={"username": "invalidUser", "password": "invalidPass"}, headers=HEADERS)
    assert response.status_code == 401
