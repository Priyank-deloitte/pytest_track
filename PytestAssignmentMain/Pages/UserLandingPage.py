from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class UserLandingPage(BasePage):
    LOGOUT_BTN = (By.XPATH, "//button[text()='Logout']")
    ADD_NOTE_BTN = (By.XPATH, "//button[text()='Add Note']")
    SELECT_CATEGORY = (By.XPATH, "//select[@id='category']")
    CHOOSE_HOME = (By.XPATH, "//option[@value='Home']")
    CHOOSE_WORK = (By.XPATH, "//option[@value='Work']")
    CHOOSE_PERSONAL = (By.XPATH, "//option[@value='Personal']")
    TITLE = (By.XPATH, "//input[@id='title']")
    DESCRIPTION = (By.XPATH, "//textarea[@id='description']")
    CREATE_BUTTON = (By.XPATH, "//button[text()='Create']")
    NOTE_CARD_TITLE = (By.XPATH, "//div[@data-testid='note-card-title'][1]")
    HOME_BTN = (By.XPATH, "//span[text()='Home']")
    WORK_BTN = (By.XPATH, "//span[text()='Work']")
    PERSONAL_BTN = (By.XPATH, "//span[text()='Personal']")
    EDIT_NOTE_BTN = (By.XPATH, "//button[text()='Edit']")
    VIEW_NOTE_BTN = (By.XPATH, "//a[@data-testid='note-view']")
    SAVE_BTN = (By.XPATH, "//button[text()='Save']")
    HOMEPAGE_MYNOTES = (By.XPATH, "//a[text()='Home - My Notes ']")
    MARK_COMPLETE_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.login = LoginPage(self.driver)
        self.login.do_login("priyankverma@deloitte.com", "Pass@123")

    def do_add_note_for_home(self, title, description):
        self.do_click(self.ADD_NOTE_BTN)
        self.do_click(self.SELECT_CATEGORY)
        self.do_click(self.CHOOSE_HOME)
        self.do_send_keys(self.TITLE, title)
        self.do_send_keys(self.DESCRIPTION, description)
        self.do_click(self.CREATE_BUTTON)

    def do_add_note_for_work(self, title, description):
        self.do_click(self.ADD_NOTE_BTN)
        self.do_click(self.SELECT_CATEGORY)
        self.do_click(self.CHOOSE_WORK)
        self.do_send_keys(self.TITLE, title)
        self.do_send_keys(self.DESCRIPTION, description)
        self.do_click(self.CREATE_BUTTON)

    def do_add_note_for_personal(self, title, description):
        self.do_click(self.ADD_NOTE_BTN)
        self.do_click(self.SELECT_CATEGORY)
        self.do_click(self.CHOOSE_PERSONAL)
        self.do_send_keys(self.TITLE, title)
        self.do_send_keys(self.DESCRIPTION, description)
        self.do_click(self.CREATE_BUTTON)

    def get_created_note_card_title(self):
        return self.get_element_text(self.NOTE_CARD_TITLE)

    def do_edit_note_for_home(self, title, description):
        self.do_click(self.HOME_BTN)
        # element = driver.find_element_by_id("element_id")
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()
        self.do_click(self.VIEW_NOTE_BTN)
        self.do_click(self.EDIT_NOTE_BTN)
        self.do_send_keys(self.TITLE, Keys.CONTROL + 'a')
        self.do_send_keys(self.TITLE, title)
        self.do_send_keys(self.DESCRIPTION, Keys.CONTROL + 'a')
        self.do_send_keys(self.DESCRIPTION, description)
        self.do_click(self.SAVE_BTN)
        self.do_click(self.HOMEPAGE_MYNOTES)

    def do_edit_note_for_work(self, title, description):
        self.do_click(self.WORK_BTN)
        self.do_click(self.VIEW_NOTE_BTN)
        self.do_click(self.EDIT_NOTE_BTN)
        self.do_send_keys(self.TITLE, Keys.CONTROL + 'a')
        self.do_send_keys(self.TITLE, title)
        self.do_send_keys(self.DESCRIPTION, Keys.CONTROL + 'a')
        self.do_send_keys(self.DESCRIPTION, description)
        self.do_click(self.SAVE_BTN)
        self.do_click(self.HOMEPAGE_MYNOTES)

    def do_edit_note_for_personal(self, title, description):
        self.do_click(self.PERSONAL_BTN)
        self.do_click(self.VIEW_NOTE_BTN)
        self.do_click(self.EDIT_NOTE_BTN)
        self.do_send_keys(self.TITLE, Keys.CONTROL + 'a')
        self.do_send_keys(self.TITLE, title)
        self.do_send_keys(self.DESCRIPTION, Keys.CONTROL + 'a')
        self.do_send_keys(self.DESCRIPTION, description)
        self.do_click(self.SAVE_BTN)
        self.do_click(self.HOMEPAGE_MYNOTES)

    def do_mark_complete(self):
        self.do_click(self.HOME_BTN)
        self.do_click(self.MARK_COMPLETE_CHECKBOX)


