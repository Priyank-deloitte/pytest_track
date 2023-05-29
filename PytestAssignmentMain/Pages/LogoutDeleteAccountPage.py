from time import sleep

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class LogoutDeleteAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.login = LoginPage(self.driver)
        self.login.do_login("arpitgupta26@deloitte.com", "Pass@123")

    LOGOUT_BTN = (By.XPATH, "//button[text()='Logout']")
    PROFILE_BTN = (By.XPATH, "//a[@data-testid='profile']")
    DELETE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Delete Account']")
    CONFIRM_DELETE = (By.XPATH, "//button[@data-testid='note-delete-confirm']")

    def do_Logout(self):
        self.do_click(self.LOGOUT_BTN)

    def do_Delete_Account(self):
        self.do_click(self.PROFILE_BTN)
        sleep(5)
        deleteButton = self.driver.find_element(By.XPATH, "//button[text()='Delete Account']")
        self.driver.execute_script("arguments[0].click()", deleteButton)
        sleep(2)
        self.do_click(self.CONFIRM_DELETE)
        # self.do_click(self.DELETE_ACCOUNT_BTN)
