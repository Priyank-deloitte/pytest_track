import pytest
import requests
import jsonpath
import json


@pytest.fixture
def api_url():
    return "https://api.instantwebtools.net/v1"


# Test case for API endpoint 1
def test_api_status_code(api_url):
    response = requests.get(f"{api_url}/passenger?page=0&size=10")
    print(response)
    assert response.status_code == 200


# Verifying using json path
def test_id(api_url):
    size = 10
    response = requests.get(f"{api_url}/passenger?page=0&size=10")
    json_response = json.loads(response.text)
    assert len(json_response['data']) == size
    second_data = json_response['data'][1]
    print(second_data)
    assert jsonpath.jsonpath(second_data, '_id') == ['6465e4ccc3e393a28d798f35']
    assert jsonpath.jsonpath(second_data, 'name') == ['Anuj Kapadia']
    assert jsonpath.jsonpath(second_data, 'trips') == [450]
