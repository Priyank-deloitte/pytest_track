import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope='class', autouse=True)
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.close()
