import requests
from src.utils import BASE_URL, HEADERS

def test_create_user_valid_data():
    data = {
    "email": "u@example.com",
    "username": "string",
    "full_name": "string",
    "password": "string"
    }
    
    response = requests.post(BASE_URL + "/users", json=data, headers=HEADERS)
    assert response.status_code == 201

def test_create_user_invalid_data():
    data = {"username": "", "password": "","full_name":"", "password": ""}
    response = requests.post(BASE_URL + "/users", data=data, headers=HEADERS)
    assert response.status_code == 400
