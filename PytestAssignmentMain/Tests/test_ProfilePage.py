import allure
import pytest

from Pages.ProfilePage import ProfilePage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils, log_class


@allure.severity(allure.severity_level.CRITICAL)
class Test_ProfilePage(BaseTest):
    log = log_class.custom_logger()

    @pytest.mark.parametrize("phoneNumber, companyName, fullName, alertMessage", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "UpdateProfileData"))
    def test_01_update_profile(self, phoneNumber, companyName, fullName, alertMessage):
        self.profilePage = ProfilePage(self.driver)
        self.profilePage.do_update_profile(phoneNumber, companyName, fullName)
        self.log.info("updating profile data")
        alert_message = self.profilePage.get_alert_message()
        assert alert_message == alertMessage
        self.log.info("profile data updated")

    @pytest.mark.parametrize("currentPassword, newPassword, alertMessage", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "ChangePasswordData"))
    def test_02_change_password(self, currentPassword, newPassword, alertMessage):
        self.profilePage = ProfilePage(self.driver)
        self.profilePage.do_change_password(currentPassword, newPassword)
        self.log.info("changing the password")
        alert_message = self.profilePage.get_password_change_alert_message()
        assert alert_message == alertMessage
        self.log.info("password changed successfully")
