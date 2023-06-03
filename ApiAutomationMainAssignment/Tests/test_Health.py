import json

import requests
from Config.config import Data
from Utilities.logger import log_class

log = log_class.custom_logger()


def test_01_get_health_check():
    response = requests.get(f"{Data.BASE_URI}/health-check")
    log.info("GET health-check")
    response_json = json.loads(response.text)
    try:
        assert response.status_code == 200
        log.info("status code = 200")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        assert response_json["message"] == "Notes API is Running"
        log.info("notes api is running")

    except InternalErrorServerException:
        assert response.status_code == 500
        assert response_json["message"] == "Internal Error Server"
        log.info("internal server error")


class InternalErrorServerException:
    pass
