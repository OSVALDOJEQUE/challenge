import requests

BASE_URL = "http://localhost"
TOKEN_ENDPOINT = "/token"
HEADERS = {"Content-Type": "application/json"}

def get_token(username, password):
    response = requests.post(BASE_URL + TOKEN_ENDPOINT, json={"username": username, "password": password}, headers=HEADERS)
    print(response)
    return response.json().get("access_token")
