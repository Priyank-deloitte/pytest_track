import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.SignupPage import SignupPage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils, log_class


@allure.feature("Signup")
@allure.severity(allure.severity_level.CRITICAL)
class Test_SignupPage(BaseTest):
    log = log_class.custom_logger()

    @pytest.mark.parametrize("email, name, password, successAlert, failedAlert", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx", "SignupData"))
    def test_01_signup(self, email, name, password, successAlert, failedAlert):
        self.signupPage = SignupPage(self.driver)
        self.signupPage.do_signup(email, name, password)
        self.log.info("signing up new user")
        alert_message = self.signupPage.get_success_alert_message()
        if alert_message == successAlert:
            assert True
            self.log.info("new user created successfully")
        else:
            allure.attach(self.get_screenshot_as_png(), name="testSignupScreen",
                          attachment_type=AttachmentType.PNG)
            assert alert_message == failedAlert
            self.log.info("user already exists")
