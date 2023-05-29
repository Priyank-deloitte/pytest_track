from time import sleep

import allure
import pytest

from Pages.UserLandingPage import UserLandingPage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils, log_class


@allure.severity(allure.severity_level.CRITICAL)
class Test_UserLandingPage(BaseTest):
    log = log_class.custom_logger()

    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "AddNoteForHome"))
    def test_01_add_note_for_home(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_add_note_for_home(title, description)
        self.log.info("adding note for home")
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title
        self.log.info("note added for home successfully")

    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "AddNoteForWork"))
    def test_02_add_note_for_work(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_add_note_for_work(title, description)
        self.log.info("adding note for work")
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title
        self.log.info("note added for work successfully")

    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "AddNoteForPersonal"))
    def test_03_add_note_for_personal(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_add_note_for_personal(title, description)
        self.log.info("adding note for personal")
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title
        self.log.info("note added for personal successfully")

    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "EditNoteForHome"))
    def test_04_edit_note_for_home(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_edit_note_for_home(title, description)
        self.log.info("editing note for home")
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title
        self.log.info("note edited for home successfully")

    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "EditNoteForWork"))
    def test_05_edit_note_for_work(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_edit_note_for_work(title, description)
        self.log.info("editing note for work")
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title
        self.log.info("note edited for work successfully")

    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "EditNoteForPersonal"))
    def test_06_edit_note_for_personal(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_edit_note_for_personal(title, description)
        self.log.info("editing note for personal")
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title
        self.log.info("note edited for personal successfully")

    def test_07_mark_complete(self):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_mark_complete()
        self.log.info("note marked completed")
