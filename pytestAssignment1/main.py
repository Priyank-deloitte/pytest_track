import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/ncr')
    assert "Google" == driver.title
    sleep(5)
    driver.get('https://practice.expandtesting.com/webpark')
    sleep(3)
    driver.find_element(By.XPATH, '//input[@name="entryTime"]').click()
    driver.find_element(By.XPATH, '//input[@name="entryTime"]').send_keys(Keys.CONTROL + "a")
    driver.find_element(By.XPATH, '//input[@name="entryTime"]').send_keys("18:00")
    driver.find_element(By.XPATH, '//input[@name="exitTime"]').send_keys(Keys.CONTROL + "a")
    driver.find_element(By.XPATH, '//input[@name="exitTime"]').send_keys("18:00")
    sleep(3)
    driver.find_element(By.XPATH, '//button[@id="calculateCost"]').click()
    sleep(5)
    assert "18.00€" == driver.find_element(By.XPATH, "//b[@id='resultValue']").text
    assert "1 Day(s), 0 Hour(s), 0 Minute(s)" == driver.find_element(By.XPATH, "//b[@id='resultMessage']").text
