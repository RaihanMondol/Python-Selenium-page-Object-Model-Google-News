from prompt_toolkit.clipboard import pyperclip
from selenium.webdriver.common.by import By
from Locators.Locators import Save_for_later
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class SaveForLaterPage():
    def __init__(self, driver):

        self.driver = driver

        self.headlines_locator_xpath = Save_for_later.headlines_locator_xpath
        self.save_for_icon_xpath = Save_for_later.save_for_icon_xpath

    def hover_save_for_later(self):
        title = self.driver.find_element(By.XPATH, Save_for_later.headlines_locator_xpath)
        saveIcon = self.driver.find_element(By.XPATH, Save_for_later.save_for_icon_xpath)
        actions = webdriver.ActionChains(self.driver).move_to_element(title).move_to_element(saveIcon).perform()
        time.sleep(3)
        saveIcon.click()

