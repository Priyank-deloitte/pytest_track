import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture(scope="class")
def chrome_driver(request):
    print("Launch Browser")
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    print("Close Browser")
    chrome_driver.close()


@pytest.mark.usefixtures(chrome_driver)
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):

    def test_google_url(self):
        self.driver.get("https://www.google.com/ncr")
        assert "Google" == self.driver.title
        sleep(5)
