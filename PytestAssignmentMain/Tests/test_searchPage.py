import allure
import pytest

from Pages.SearchPage import SearchPage
from Tests.test_Base import BaseTest
from Utilities.excelUtils import log_class


@allure.severity(allure.severity_level.CRITICAL)
class Test_SearchPage(BaseTest):
    log = log_class.custom_logger()

    def test_01_existing_note(self):
        self.search = SearchPage(self.driver)
        self.search.do_search_verify_note(title="Shopping")
        self.log.info("searching with the title")
        result = self.search.get_search_result_for_existing_note()
        assert result == "Shopping"
        self.log.info("result successfully fetched")

    def test_02_non_existing_note(self):
        self.search = SearchPage(self.driver)
        self.search.do_search_verify_note(title="xyz")
        self.log.info("searching with the title")
        result = self.search.get_search_result_for_non_existing_note()
        assert result == "Couldn't find any notes"
        self.log.info("result not available")
