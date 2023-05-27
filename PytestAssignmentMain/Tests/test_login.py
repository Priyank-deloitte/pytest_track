import pytest

from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils


class Test_LoginPage(BaseTest):
    @pytest.mark.parametrize("email, password, currentUrl", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx", "LoginData"))
    def test_signup(self, email, password, currentUrl):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(email, password)
        # CURRENT_URL = self.loginPage.get_current_url(currentUrl)
        # assert CURRENT_URL == currentUrl