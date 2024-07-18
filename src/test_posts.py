import requests
import pytest
from src.utils import BASE_URL, HEADERS, get_token

@pytest.fixture(scope="module")
def token():
    # Supondo que get_token retorna um token válido
    return get_token("user", "pass123")

def test_create_post_valid_data(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(BASE_URL + "/posts", json={"title": "Test Post", "content": "This is a test post."}, headers=headers)
    assert response.status_code == 201

def test_update_post(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(BASE_URL + "/posts/1", json={"title": "Updated Title", "content": "Updated content."}, headers=headers)
    assert response.status_code == 200

def test_delete_post(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(BASE_URL + "/posts/1", headers=headers)
    assert response.status_code == 204
