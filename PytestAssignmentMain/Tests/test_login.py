import allure
import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils, log_class


@allure.feature("Login")
@allure.severity(allure.severity_level.CRITICAL)
class Test_LoginPage(BaseTest):
    log = log_class.custom_logger()

    @pytest.mark.parametrize("email, password, currentUrl", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx", "LoginData"))
    def test_01_do_login(self, email, password, currentUrl):
        self.loginPage = LoginPage(self.driver)
        self.log.info("creating object for login")
        self.loginPage.do_login(email, password)
        self.log.info("login successfully")

    def test_02_login_success_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LoginSuccessPageTitle)
        assert title == TestData.LoginSuccessPageTitle
        self.log.info("user successfully enters the landing page")
