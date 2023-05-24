import pytest
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_WebParkingCost(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        sleep(3)
        assert self.driver.title == "Google"

    def test_load_URL(self):
        self.driver.get('https://practice.expandtesting.com/webpark')
        sleep(3)
        assert self.driver.current_url == "https://practice.expandtesting.com/webpark"
    @pytest.mark.parametrize(
                                "entryDate, entryTime, exitDate, exitTime, cost, totalTime",
                                [
                                    ("2023-06-06", "12:00", "2023-06-07", "12:00", "18.00€", "1 Day(s), 0 Hour(s), 0 Minute(s)"),
                                    ("2023-06-14", "09:00", "2023-06-14", "11:00", "12.00€", "0 Day(s), 2 Hour(s), 0 Minute(s)")
                                ]
                            )
    def test_enter_details(self, entryDate, entryTime, exitDate, exitTime, cost, totalTime):
        self.driver.find_element(By.XPATH, '//input[@name="entryDate"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="entryDate"]').send_keys(entryDate)
        sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="entryTime"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="entryTime"]').send_keys(entryTime)
        sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="exitDate"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="exitDate"]').send_keys(exitDate)
        sleep(2)
        self.driver.find_element(By.XPATH, '//input[@name="exitTime"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, '//input[@name="exitTime"]').send_keys(exitTime)
        sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="calculateCost"]').click()
        sleep(5)
        assert self.driver.find_element(By.XPATH, "//b[@id='resultValue']").text == cost
        assert self.driver.find_element(By.XPATH, "//b[@id='resultMessage']").text == totalTime
