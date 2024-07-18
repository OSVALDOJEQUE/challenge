import requests
from src.utils import BASE_URL, HEADERS

def test_create_user_valid_data():
    response = requests.post(BASE_URL + "/users", data={"username": "newUser","email":"neuser@example.com","full_name":"full_name","disabled":False , "password": "newPass"}, headers=HEADERS)
    assert response.status_code == 201

def test_create_user_invalid_data():
    response = requests.post(BASE_URL + "/users", json={"username": "", "password": ""}, headers=HEADERS)
    assert response.status_code == 400
