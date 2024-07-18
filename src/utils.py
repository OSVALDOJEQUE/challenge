import requests

BASE_URL = "http://localhost"
TOKEN_ENDPOINT = "/token"

HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def get_token(username, password):
    data = {
    'username': username,
    'password': password,
}
    response = requests.post(BASE_URL + TOKEN_ENDPOINT, data=data, headers=HEADERS)
    return response.json().get("access_token")
