from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class SignupPage(BasePage):
    SWITCH_CREATE_ACCOUNT = (By.XPATH, "//a[text()='Create an account']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    NAME = (By.XPATH, "//input[@id='name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='confirmPassword']")
    REGISTER_BTN = (By.XPATH, "//button[@type='submit']")
    SUCCESS_ALERT_MESSAGE = (By.XPATH, "//b[1]")
    FAILED_ALERT_MESSAGE = (By.XPATH, "//div[@data-testid='alert-message']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.do_click(self.SWITCH_CREATE_ACCOUNT)

    def do_signup(self, email, name, password):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONFIRM_PASSWORD, password)
        self.do_click(self.REGISTER_BTN)

    def get_success_alert_message(self):
        return self.get_element_text(self.SUCCESS_ALERT_MESSAGE)

    def get_failed_alert_message(self):
        return self.get_element_text(self.FAILED_ALERT_MESSAGE)
