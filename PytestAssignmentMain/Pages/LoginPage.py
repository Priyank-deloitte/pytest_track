from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    SWITCH_LOGIN = (By.XPATH, "//a[text()='Login']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.do_click(self.SWITCH_LOGIN)

    def do_login(self, email, password):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)

    def get_current_url(self, current_url):
        return self.get_current_url(current_url)

