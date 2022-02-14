from selenium.webdriver.common.by import By
from Locators.Locators import Search_Locators
import time

class narrowSearchPage():
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_xpath= Search_Locators.search_textbox_xpath
        self.search_button_xpath = Search_Locators.search_button_xpath


    def featured_topic_search(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, Search_Locators.search_textbox_xpath).click()
        self.driver.find_element(By.XPATH, Search_Locators.search_textbox_xpath).send_keys("Narrow Search")

    def click_Search(self):
        self.driver.find_element(By.XPATH, Search_Locators.search_button_xpath).click()


