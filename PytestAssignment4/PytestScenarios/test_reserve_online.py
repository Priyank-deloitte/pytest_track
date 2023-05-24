import pytest
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_WebParkingReservation(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        sleep(3)
        assert self.driver.title == "Google"

    def test_load_URL(self):
        self.driver.get('https://practice.expandtesting.com/webpark')
        sleep(3)
        assert self.driver.current_url == "https://practice.expandtesting.com/webpark"

    @pytest.mark.parametrize(
                                "entryDate, entryTime, exitDate, exitTime, cost, totalTime , firstName, lastName, email, phone, licenseNumber",
                                [
                                    ("2023-06-06", "09:00", "2023-06-06", "11:00", "4.00€", "0 Day(s), 2 Hour(s), 0 Minute(s)", "Priyank", "Verma", "priyankverma@deloitte.com", "9625181982", "DL4C3432")
                                ]
                            )
    def test_cost_calculation(self, entryDate, entryTime, exitDate, exitTime, cost, totalTime, firstName, lastName, email, phone, licenseNumber):
        self.driver.find_element(By.XPATH, '//select[@id="parkingLot"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//option[@value="ShortTerm"]').click()
        sleep(1)
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
        sleep(2)
        assert self.driver.find_element(By.XPATH, "//b[@id='resultValue']").text == cost
        assert self.driver.find_element(By.XPATH, "//b[@id='resultMessage']").text == totalTime

    # def test_parking_reservation(self, entryDate, entryTime, exitDate, exitTime, cost, totalTime, firstName, lastName, email, phone, licenseNumber):

        self.driver.find_element(By.XPATH, '//button[@id="reserveOnline"]').click()
        sleep(1)
        assert self.driver.current_url == "https://practice.expandtesting.com/webpark/booking"
        self.driver.find_element(By.XPATH, '//input[@data-testid="first-name"]').send_keys(firstName)
        sleep(1)
        self.driver.find_element(By.XPATH, '//input[@data-testid="last-name"]').send_keys(lastName)
        sleep(1)
        self.driver.find_element(By.XPATH, '//input[@data-testid="email"]').send_keys(email)
        sleep(1)
        self.driver.find_element(By.XPATH, '//input[@data-testid="phone"]').send_keys(phone)
        sleep(1)
        self.driver.find_element(By.XPATH, '//select[@data-testid="vehicle-size"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//option[@value="medium"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//input[@data-testid="lpn"]').send_keys(licenseNumber)
        sleep(1)
        button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        self.driver.execute_script("arguments[0].click();", button)
        # self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        sleep(1)
        assert self.driver.current_url == "https://practice.expandtesting.com/webpark/confirmation"
        assert self.driver.find_element(By.XPATH, '//h1[text()="Reservation Confirmation"]').text == "Reservation Confirmation"
