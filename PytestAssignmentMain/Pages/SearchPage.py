from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.login = LoginPage(self.driver)
        self.login.do_login("priyankverma@deloitte.com", "Pass@123")

    SEARCH_INPUT = (By.XPATH, "//input[@id='search-note-input']")
    NOTE_CARD_TITLE = (By.XPATH, "//div[@data-testid='note-card-title']")
    NO_NOTE_EXIST = (By.XPATH, "//h4")

    def do_search_verify_note(self, title):
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT, Keys.CONTROL + 'a')
        self.do_send_keys(self.SEARCH_INPUT, title)

    def get_search_result_for_existing_note(self):
        return self.get_element_text(self.NOTE_CARD_TITLE)

    def get_search_result_for_non_existing_note(self):
        return self.get_element_text(self.NO_NOTE_EXIST)
