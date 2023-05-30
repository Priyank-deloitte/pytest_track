import pytest
import requests
import json
import jsonpath


@pytest.fixture
def api_url():
    return "https://api.instantwebtools.net"


def test_post_data(api_url):
    global id
    # Create the data payload to be sent in the POST request
    file = open('postData.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    response = requests.post(f"{api_url}/v1/passenger", request_json)
    assert response.status_code == 200

    response_json = json.loads(response.text)

    id = jsonpath.jsonpath(response_json, '_id')

    assert jsonpath.jsonpath(response_json, 'name') == jsonpath.jsonpath(request_json, 'name')
    assert jsonpath.jsonpath(response_json, 'trips') == jsonpath.jsonpath(request_json, 'trips')


def test_put_data(api_url):
    file = open('putData.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    response = requests.put(f"{api_url}/v1/passenger/" + id[0], request_json)
    assert response.status_code == 200

    response_json = json.loads(response.text)

    successMessage = jsonpath.jsonpath(response_json, 'message')
    assert successMessage == ["Passenger data put successfully completed."]

    get_response = requests.get(f"{api_url}/v1/passenger/" + id[0])
    assert get_response.status_code == 200

    get_response_json = json.loads(get_response.text)

    updatedName = jsonpath.jsonpath(get_response_json, 'name')
    assert updatedName == jsonpath.jsonpath(request_json, 'name')


def test_delete_data(api_url):
    response = requests.delete(f"{api_url}/v1/passenger/" + id[0])
    assert response.status_code == 200

    response_json = json.loads(response.text)

    deleteMessage = jsonpath.jsonpath(response_json, 'message')
    assert deleteMessage == ["Passenger data deleted successfully."]

    get_response = requests.get(f"{api_url}/v1/passenger/" + id[0])
    assert get_response.status_code == 204
