import json

import requests
import allure
from Config.config import Data
from Utilities.logger import log_class

log = log_class.custom_logger()


@allure.severity(allure.severity_level.NORMAL)
class Test_Health_API:
    @allure.feature("Health")
    def test_01_get_health_check(self):
        response = requests.get(f"{Data.BASE_URI}/health-check")
        log.info("getting checked API is running fine")
        response_json = json.loads(response.text)
        try:
            assert response.status_code == 200
            log.info(response.status_code)
            assert response.headers["Content-Type"] == "application/json; charset=utf-8"
            assert response_json["message"] == "Notes API is Running"
            log.info(response_json["message"])

        except AssertionError as e:
            assert response.status_code == 500
            assert response_json["message"] == "Internal Error Server"
            log.info(response_json["message"])
            log.info(e)
