import pytest
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        sleep(3)
        assert self.driver.title == "Google"

    def test_load_URL(self):
        self.driver.get('https://practice.expandtesting.com/webpark')
        sleep(3)
        assert self.driver.current_url == "https://practice.expandtesting.com/webpark"

    def test_enter_details(self):
        self.driver.find_element(By.XPATH, '//input[@name="entryDate"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="entryDate"]').send_keys("2023-06-06")
        sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="entryTime"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="entryTime"]').send_keys("12:00")
        sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="exitDate"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="exitDate"]').send_keys("2023-06-07")
        sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="exitTime"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="exitTime"]').send_keys("12:00")
        sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="calculateCost"]').click()
        sleep(5)
        assert self.driver.find_element(By.XPATH, "//b[@id='resultValue']").text == "18.00€"
        assert self.driver.find_element(By.XPATH, "//b[@id='resultMessage']").text == "1 Day(s), 0 Hour(s), 0 Minute(s)"
