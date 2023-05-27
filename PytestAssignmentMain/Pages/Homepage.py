from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    SWITCH_LOGIN = (By.XPATH, "//a[text()='Login']")
    SWITCH_CREATE_ACCOUNT = (By.XPATH, "//a[text()='Create an account']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SWITCH_CREATE_ACCOUNT)

    def is_login_link_exist(self):
        return self.is_visible(self.SWITCH_LOGIN)

    def switch_to_create_account(self):
        self.do_click(self.SWITCH_CREATE_ACCOUNT)

    def switch_to_login_page(self):
        self.do_click(self.SWITCH_LOGIN)



