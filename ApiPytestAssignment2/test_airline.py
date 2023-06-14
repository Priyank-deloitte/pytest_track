import pytest
import requests
import jsonpath
import json


@pytest.fixture
def api_url():
    return "https://api.instantwebtools.net/v1"


# Test case for API endpoint 1
def test_api_status_code(api_url):
    response = requests.get(f"{api_url}/airlines/1")
    print(response)
    assert response.status_code == 200


# Verifying using json path
def test_content(api_url):
    response = requests.get(f"{api_url}/airlines/1")
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'id')
    name = jsonpath.jsonpath(json_response, 'name')
    country = jsonpath.jsonpath(json_response, 'country')
    logo = jsonpath.jsonpath(json_response, 'logo')
    slogan = jsonpath.jsonpath(json_response, 'slogan')
    head_quaters = jsonpath.jsonpath(json_response, 'head_quaters')
    website = jsonpath.jsonpath(json_response, 'website')
    established = jsonpath.jsonpath(json_response, 'established')
    assert id == [1]
    assert name == ["Sri Lankan Airways"]
    assert country == ["Sri Lanka"]
    assert logo == ["https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Qatar_Airways_Logo.svg/sri_lanka.png"]
    assert slogan == ["From Sri Lanka"]
    assert head_quaters == ["Katunayake, Sri Lanka"]
    assert website == ["www.srilankaairways.com"]
    assert established == ["1990"]
