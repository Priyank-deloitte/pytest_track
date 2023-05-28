import pytest

from Pages.ProfilePage import ProfilePage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils


class Test_UpdateProfilePage(BaseTest):
    @pytest.mark.parametrize("phoneNumber, companyName, fullName, alertMessage", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "UpdateProfileData"))
    def test_update_profile(self, phoneNumber, companyName, fullName, alertMessage):
        self.profilePage = ProfilePage(self.driver)
        self.profilePage.do_update_profile(phoneNumber, companyName, fullName)
        alert_message = self.profilePage.get_alert_message()
        assert alert_message == alertMessage


class Test_ChangePassword(BaseTest):
    @pytest.mark.parametrize("currentPassword, newPassword, alertMessage", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "ChangePasswordData"))
    def test_change_password(self, currentPassword, newPassword, alertMessage):
        self.profilePage = ProfilePage(self.driver)
        self.profilePage.do_change_password(currentPassword, newPassword)
        alert_message = self.profilePage.get_password_change_alert_message()
        assert alert_message == alertMessage
