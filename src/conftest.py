import pytest
from src.utils import get_token

@pytest.fixture(scope="module")
def token():
    return get_token("user", "pass123")
