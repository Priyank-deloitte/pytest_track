import pytest

from Pages.SignupPage import SignupPage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils


class Test_SignupPage(BaseTest):

    @pytest.mark.parametrize("email, name, password, successAlert, failedAlert", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx", "SignupData"))
    def test_signup(self, email, name, password, successAlert, failedAlert):
        self.signupPage = SignupPage(self.driver)
        self.signupPage.do_signup(email, name, password)
        alert_message = self.signupPage.get_success_alert_message()
        try:
            assert alert_message == successAlert
        except:
            assert alert_message == failedAlert
