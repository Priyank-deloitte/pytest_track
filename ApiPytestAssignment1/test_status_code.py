import pytest
import requests


@pytest.fixture
def api_url():
    return "https://api.instantwebtools.net/v1/airlines"


def test_verify_status_user(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200


def test_get_user1(api_url):
    response = requests.get(f"{api_url}/1")
    assert response.status_code == 200
    user = response.json()
    assert user["name"] == "Sri Lankan Airways"
