import allure

from Tests.test_Base import BaseTest
from Pages.LogoutDeleteAccountPage import LogoutDeleteAccountPage
from Utilities.excelUtils import log_class


@allure.severity(allure.severity_level.CRITICAL)
class Test_Logout(BaseTest):
    log = log_class.custom_logger()

    @allure.feature("Logout")
    def test_logout_user(self):
        self.log.info("logging out")
        self.logout = LogoutDeleteAccountPage(self.driver)
        self.logout.do_Logout()
        self.log.info("user logged out")

    @allure.feature("Account Deletion")
    def test_user_account_deletion(self):
        self.log.info("deleting account")
        self.logout = LogoutDeleteAccountPage(self.driver)
        self.logout.do_Delete_Account()
        self.log.info("user account deleted permanently")

