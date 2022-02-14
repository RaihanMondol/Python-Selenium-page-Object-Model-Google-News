from selenium.webdriver.common.by import By
from Locators.Locators import Headlines_Locators
import time

class followPage():
    def __init__(self, driver):
        self.driver = driver

        self.click_headlines_xpath = Headlines_Locators.click_headlines_xpath
        self.click_follow_xpath = Headlines_Locators.click_follow_xpath


    def test_click_headlines(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, Headlines_Locators.click_headlines_xpath).click()


    def click_follow(self):
        self.driver.find_element(By.XPATH, Headlines_Locators.click_follow_xpath).click()


