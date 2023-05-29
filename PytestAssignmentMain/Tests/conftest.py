import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=["chrome"], scope='function', autouse=True)
def init__driver(request):
    if request.param == "chrome":
        # c = Options()
        # c.add_argument("--headless")
        # web_driver = webdriver.Chrome(options=c)
        web_driver = webdriver.Chrome()
    if request.param == "edge":
        web_driver = webdriver.Edge()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.close()

