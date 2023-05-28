from time import sleep

import pytest

from Pages.UserLandingPage import UserLandingPage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import Utils


class Test_AddNoteHome(BaseTest):
    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "AddNoteForHome"))
    def test_add_note_for_home(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_add_note_for_home(title, description)
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title


class Test_AddNoteWork(BaseTest):
    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "AddNoteForWork"))
    def test_add_note_for_work(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_add_note_for_work(title, description)
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title


class Test_AddNotePersonal(BaseTest):
    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "AddNoteForPersonal"))
    def test_add_note_for_personal(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_add_note_for_personal(title, description)
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title


class Test_EditNoteHome(BaseTest):
    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "EditNoteForHome"))
    def test_edit_note_for_home(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_edit_note_for_home(title, description)
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title


class Test_EditNoteWork(BaseTest):
    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "EditNoteForWork"))
    def test_edit_note_for_work(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_edit_note_for_work(title, description)
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title


class Test_EditNotePersonal(BaseTest):
    @pytest.mark.parametrize("title, description", Utils.read_data_from_excel(
        "C:\\Users\\priyankverma\\PycharmProjects\\PytestAssignmentMain\\TestData\\MyNotesAppData.xlsx",
        "EditNoteForPersonal"))
    def test_edit_note_for_personal(self, title, description):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_edit_note_for_personal(title, description)
        sleep(3)
        card_title = self.userLandingPage.get_created_note_card_title()
        assert card_title == title

    def test_mark_complete(self):
        self.userLandingPage = UserLandingPage(self.driver)
        self.userLandingPage.do_mark_complete()

