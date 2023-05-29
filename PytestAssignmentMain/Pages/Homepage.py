from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Utilities.excelUtils import log_class


class HomePage(BasePage):
    SWITCH_LOGIN = (By.XPATH, "//a[text()='Login']")
    SWITCH_CREATE_ACCOUNT = (By.XPATH, "//a[text()='Create an account']")

    log = log_class.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.log.info("Browser Launched")

    def get_home_page_title(self, title):
        self.log.info("title= ", self.get_title(title))
        return self.get_title(title)

    def is_signup_link_exist(self):
        self.log.info("Check Signup Visibility")
        return self.is_visible(self.SWITCH_CREATE_ACCOUNT)

    def is_login_link_exist(self):
        self.log.info("Check Login Visibility")
        return self.is_visible(self.SWITCH_LOGIN)

    def switch_to_create_account(self):
        self.do_click(self.SWITCH_CREATE_ACCOUNT)
        self.log.info("On Signup Page")

    def switch_to_login_page(self):
        self.do_click(self.SWITCH_LOGIN)
        self.log.info("On Login Page")
