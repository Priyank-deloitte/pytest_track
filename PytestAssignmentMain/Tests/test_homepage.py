import allure
import pytest

from Config.config import TestData
from Pages.Homepage import HomePage
from Tests.test_Base import BaseTest


@allure.feature("HomePage")
@allure.severity(allure.severity_level.CRITICAL)
class Test_HomePage(BaseTest):

    def test_01_login_button(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_login_link_exist()
        assert flag

    def test_02_signup_button(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_signup_link_exist()
        assert flag

    def test_03_homepage_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_title(TestData.HomePageTitle)
        assert title == TestData.HomePageTitle
