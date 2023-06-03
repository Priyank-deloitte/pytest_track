import json
import requests
from Config.config import Data
from Utilities.logger import log_class

log = log_class.custom_logger()


def test_01_post_register_new_user():
    file = open('..\\JsonFiles\\registerNewUser.json', 'r')
    log.info("opening file - 'registerNewUser.json'")
    json_input = file.read()
    log.info("reading file - 'registerNewUser.json'")
    request_json = json.loads(json_input)
    log.info("parsing request data into json format")
    response = requests.post(f"{Data.BASE_URI}/users/register", request_json)
    response_json = response.json()
    log.info("performing POST method and adding data from - 'registerNewUser.json'")
    try:
        assert response.status_code == 201
        log.info("status code : 201")
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
        assert response_json["message"] == "User account created successfully"
        log.info("user account created successfully")
    except AssertionError as e:
        assert response.status_code == 409
        log.info("status code : 409")
        assert response_json["message"] == "An account already exists with the same email address"
        log.info(e)


def test_02_post_login_user():
    global authToken
    file = open('..\\JsonFiles\\loginUser.json', 'r')
    log.info("opening file - 'loginUser.json'")
    json_input = file.read()
    log.info("reading file - 'loginUser.json'")
    request_json = json.loads(json_input)
    log.info("parsing request data into json format")
    response = requests.post(f"{Data.BASE_URI}/users/login", request_json)

    response_json = response.json()
    print(response_json)

    authToken = response_json['data']['token']
    print(authToken)

    log.info("performing POST method and adding data from - 'loginUser.json'")
    log.info(response_json)
    try:
        assert response.status_code == 200
        log.info("status code : 200")
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
        assert response_json["message"] == "Login successful"
        log.info("user logged in successfully")
    except AssertionError as e:
        assert response.status_code == 401
        log.info("status code : 401")
        assert response_json["message"] == "Incorrect email address or password"
        log.info(e)


def test_03_get_user_profile():
    response = requests.get(f"{Data.BASE_URI}/users/profile", headers={"x-auth-token": authToken})
    log.info("GET user profile")
    response_json = response.json()
    try:
        assert response.status_code == 200
        log.info("status code : 200")
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
        assert response_json["message"] == "Profile successful"
        log.info("user profile fetched successfully")
    except AssertionError as e:
        assert response.status_code == 401
        log.info("status code : 401")
        assert response_json["message"] == "No authentication token specified in x-auth-token header"
        log.info(e)


def test_04_patch_user_profile():
    file = open('..\\JsonFiles\\updateUserProfile.json', 'r')
    log.info("opening file - 'updateUserProfile.json'")
    json_input = file.read()
    log.info("reading file - 'updateUserProfile.json'")
    request_json = json.loads(json_input)
    log.info("parsing request data into json format")
    response = requests.patch(f"{Data.BASE_URI}/users/profile", request_json, headers={"x-auth-token": authToken})
    response_json = response.json()
    log.info("performing PATCH method and updating data from - 'updateUserProfile.json'")
    try:
        assert response.status_code == 200
        log.info("status code : 200")
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
        assert response_json["message"] == "Profile updated successful"
        log.info("user profile updated successfully")
    except AssertionError as e:
        assert response.status_code == 401
        log.info("status code : 401")
        assert response_json["message"] == "No authentication token specified in x-auth-token header"
        log.info(e)


def test_05_user_forgot_password():
    email = {"email": "anderson03789@gmail.com"}
    log.info(email)
    response = requests.post(f"{Data.BASE_URI}/users/forgot-password", email)
    response_json = response.json()
    try:
        assert response.status_code == 200
        log.info(response.status_code)
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
        assert response_json[
                   "message"] == "Password reset link successfully sent to " + email[
                   "email"] + ". Please verify by clicking on the given link"
        log.info(response_json["message"])
    except AssertionError as e:
        assert response.status_code == 401
        log.info(response.status_code)
        assert response_json["message"] == "No account found with the given email address"
        log.info(response_json["message"])
        log.info(e)
