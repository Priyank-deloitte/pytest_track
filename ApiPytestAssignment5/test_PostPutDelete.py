import pytest
import requests
import json
import jsonpath
import allure
from logger import log_class

log = log_class.custom_logger()


@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture
def api_url():
    return "https://api.instantwebtools.net"


@allure.feature("POST method")
def test_post_data(api_url):
    global id
    log.info("declared 'id' as global variable")
    # Create the data payload to be sent in the POST request
    file = open('postData.json', 'r')
    log.info("opening file - 'postData.json'")
    json_input = file.read()
    log.info("reading file - 'postData.json'")
    request_json = json.loads(json_input)
    log.info("parsing request data into json format")

    response = requests.post(f"{api_url}/v1/passenger", request_json)
    log.info("performing POST method and adding data from - 'postData.json'")
    assert response.status_code == 200
    log.info("status code : 200")

    response_json = json.loads(response.text)
    log.info("parsing response data into json format")

    id = jsonpath.jsonpath(response_json, '_id')
    log.info("fetching the value of 'id' of the newly created data")

    assert jsonpath.jsonpath(response_json, 'name') == jsonpath.jsonpath(request_json, 'name')
    log.info("asserting with 'name'")
    assert jsonpath.jsonpath(response_json, 'trips') == jsonpath.jsonpath(request_json, 'trips')
    log.info("asserting with 'trips'")


@allure.feature("PUT method")
def test_put_data(api_url):
    file = open('putData.json', 'r')
    log.info("opening file - 'putData.json'")
    json_input = file.read()
    log.info("reading file - 'putData.json'")

    request_json = json.loads(json_input)
    log.info("parsing request data into json format")

    response = requests.put(f"{api_url}/v1/passenger/" + id[0], request_json)
    log.info("performing PUT method and adding data from - 'putData.json'")
    assert response.status_code == 200
    log.info("status code : 200")

    response_json = json.loads(response.text)
    log.info("parsing response data into json format")

    successMessage = jsonpath.jsonpath(response_json, 'message')
    log.info("fetching the value of 'message' of the updated data")
    assert successMessage == ["Passenger data put successfully completed."]
    log.info("asserting the success message")

    get_response = requests.get(f"{api_url}/v1/passenger/" + id[0])
    log.info("getting the response to validate the updated message")
    assert get_response.status_code == 200
    log.info("status code : 200")

    get_response_json = json.loads(get_response.text)
    log.info("parsing response data into json format")

    updatedName = jsonpath.jsonpath(get_response_json, 'name')
    assert updatedName == jsonpath.jsonpath(request_json, 'name')
    log.info("asserting with the updated name")


@allure.feature("DELETE method")
def test_delete_data(api_url):
    response = requests.delete(f"{api_url}/v1/passenger/" + id[0])
    log.info("performing DELETE method to delete the details of the mentioned 'id'")
    assert response.status_code == 200
    log.info("status code : 200")

    response_json = json.loads(response.text)
    log.info("parsing response data into json format")

    deleteMessage = jsonpath.jsonpath(response_json, 'message')
    log.info("fetching the value of 'message' on performing DELETE method")
    assert deleteMessage == ["Passenger data deleted successfully."]
    log.info("asserting the success message")

    get_response = requests.get(f"{api_url}/v1/passenger/" + id[0])
    log.info("getting the response to validate the whether the user got deleted")
    assert get_response.status_code == 204
    log.info("status code : 204")
