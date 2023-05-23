import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def init__driver(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.close()
