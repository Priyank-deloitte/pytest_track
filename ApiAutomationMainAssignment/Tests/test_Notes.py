import json
import requests
import allure
from Config.config import Data
from Utilities.logger import log_class

log = log_class.custom_logger()


@allure.severity(allure.severity_level.CRITICAL)
class Test_Notes_API:
    @allure.feature("Login")
    def test_01_login_user(self):
        global authToken
        login_data = {"email": "priyank1369@gmail.com", "password": "Pass@123"}
        response = requests.post(f"{Data.BASE_URI}/users/login", login_data)
        log.info(response.status_code)
        response_json = response.json()
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
        assert response_json["message"] == "Login successful"
        log.info(response_json["message"])
        authToken = response_json['data']['token']

    @allure.feature("Create Note")
    def test_02_post_create_note(self):
        global noteId
        file = open('..\\JsonFiles\\createNote.json', 'r')
        json_input = file.read()
        request_json = json.loads(json_input)
        response = requests.post(f"{Data.BASE_URI}/notes", request_json, headers={"x-auth-token": authToken})
        response_json = response.json()
        noteId = response_json["data"]["id"]
        print(noteId)
        try:
            assert response.status_code == 200
            log.info(response.status_code)
            assert response.headers['Content-Type'] == "application/json; charset=utf-8"
            assert response_json["message"] == "Note successfully created"
            log.info(response_json["message"])
        except AssertionError as e:
            assert response.status_code == 401
            assert response_json["message"] == "No authentication token specified in x-auth-token header"
            log.info(e)

    @allure.feature("Fetch all Notes")
    def test_03_get_all_notes(self):
        response = requests.get(f"{Data.BASE_URI}/notes", headers={"x-auth-token": authToken})
        log.info("getting all notes")
        response_json = response.json()
        print(response_json)
        try:
            assert response.status_code == 200
            log.info(response.status_code)
            assert response.headers['Content-Type'] == "application/json; charset=utf-8"
            assert response_json["message"] == "Notes successfully retrieved"
            log.info(response_json["message"])
        except AssertionError as e:
            assert response.status_code == 401
            log.info(response.status_code)
            assert response_json["message"] == "No authentication token specified in x-auth-token header"
            log.info(e)

    @allure.feature("Get Note by ID")
    def test_04_get_note_by_id(self):
        response = requests.get(f"{Data.BASE_URI}/notes/" + noteId, headers={"x-auth-token": authToken})
        log.info("getting note by id: " + noteId)
        response_json = response.json()
        print(response_json)
        try:
            assert response.status_code == 200
            log.info(response.status_code)
            assert response.headers['Content-Type'] == "application/json; charset=utf-8"
            assert response_json["message"] == "Note successfully retrieved"
            log.info(response_json["message"])
        except AssertionError as e:
            assert response.status_code == 401
            log.info(response.status_code)
            assert response_json["message"] == "No authentication token specified in x-auth-token header"
            log.info(e)

    @allure.feature("Update Note")
    def test_05_update_existing_note_by_id(self):
        file = open('..\\JsonFiles\\updateExistingNote.json', 'r')
        json_input = file.read()
        request_json = json.loads(json_input)
        response = requests.put(f"{Data.BASE_URI}/notes/" + noteId, request_json, headers={"x-auth-token": authToken})
        log.info("updating note by id: " + noteId)
        response_json = response.json()
        try:
            assert response.status_code == 200
            log.info(response.status_code)
            assert response.headers['Content-Type'] == "application/json; charset=utf-8"
            assert response_json["message"] == "Note successfully Updated"
            log.info(response_json["message"])
        except AssertionError as e:
            assert response.status_code == 401
            log.info(response.status_code)
            assert response_json["message"] == "No authentication token specified in x-auth-token header"
            log.info(e)

    @allure.feature("Update Complete Status")
    def test_06_update_note_completed_status(self):
        status = {"completed": 1}
        response = requests.patch(f"{Data.BASE_URI}/notes/" + noteId, status, headers={"x-auth-token": authToken})
        log.info("updating note by id: " + noteId)
        response_json = response.json()
        try:
            assert response.status_code == 200
            log.info(response.status_code)
            assert response.headers['Content-Type'] == "application/json; charset=utf-8"
            assert response_json["message"] == "Note successfully Updated"
            log.info(response_json["message"])
        except AssertionError as e:
            assert response.status_code == 401
            log.info(response.status_code)
            assert response_json["message"] == "No authentication token specified in x-auth-token header"
            log.info(e)

    @allure.feature("Delete Note")
    def test_07_delete_note(self):
        response = requests.delete(f"{Data.BASE_URI}/notes/" + noteId, headers={"x-auth-token": authToken})
        log.info("deleting note by id: " + noteId)
        response_json = response.json()
        try:
            assert response.status_code == 200
            log.info(response.status_code)
            assert response.headers['Content-Type'] == "application/json; charset=utf-8"
            assert response_json["message"] == "Note successfully deleted"
            log.info(response_json["message"])
        except AssertionError as e:
            assert response.status_code == 401
            log.info(response.status_code)
            assert response_json["message"] == "No authentication token specified in x-auth-token header"
            log.info(e)
