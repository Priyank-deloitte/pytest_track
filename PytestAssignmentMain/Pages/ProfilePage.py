from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class ProfilePage(BasePage):
    SWITCH_LOGIN = (By.XPATH, "//a[text()='Login']")
    PROFILE_BTN = (By.XPATH, "//a[@data-testid='profile']")
    PHONE_NUMBER = (By.XPATH, "//input[@name='phone']")
    COMPANY_NAME = (By.XPATH, "//input[@name='company']")
    FULL_NAME = (By.XPATH, "//input[@name='name']")
    UPDATE_PROFILE_BTN = (By.XPATH, "//button[text()='Update profile']")
    ALERT_MESSAGE = (By.XPATH, "//div[@data-testid='alert-message']")
    CHANGE_PASSWORD_BTN =(By.XPATH, "//button[text()='Change password']")
    CURRENT_PASSWORD = (By.XPATH, "//input[@name='currentPassword']")
    NEW_PASSWORD = (By.XPATH, "//input[@name='newPassword']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@name='confirmPassword']")
    UPDATE_PASSWORD_BTN = (By.XPATH, "//button[@data-testid='update-password']")
    PASSWORD_CHANGE_ALERT_MESSAGE = (By.XPATH, "//div[@data-testid='alert-message']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.login = LoginPage(self.driver)
        self.login.do_login("priyankverma@deloitte.com", "Pass@123")
        # self.do_click(self.PROFILE_BTN)

    def do_update_profile(self, phoneNumber, companyName, fullName):
        self.do_click(self.PROFILE_BTN)
        self.do_send_keys(self.PHONE_NUMBER, Keys.CONTROL + 'a')
        self.do_send_keys(self.PHONE_NUMBER, phoneNumber)
        self.do_send_keys(self.COMPANY_NAME, Keys.CONTROL + 'a')
        self.do_send_keys(self.COMPANY_NAME, companyName)
        self.do_send_keys(self.FULL_NAME, Keys.CONTROL + 'a')
        self.do_send_keys(self.FULL_NAME, fullName)
        self.do_click(self.UPDATE_PROFILE_BTN)


    def get_alert_message(self):
        return self.get_element_text(self.ALERT_MESSAGE)

    def do_change_password(self, currentPassword, newPassword):
        self.do_click(self.PROFILE_BTN)
        self.do_click(self.CHANGE_PASSWORD_BTN)
        self.do_send_keys(self.CURRENT_PASSWORD, currentPassword)
        self.do_send_keys(self.NEW_PASSWORD, newPassword)
        self.do_send_keys(self.CONFIRM_PASSWORD, newPassword)
        self.do_click(self.UPDATE_PASSWORD_BTN)

    def get_password_change_alert_message(self):
        return self.get_element_text(self.PASSWORD_CHANGE_ALERT_MESSAGE)