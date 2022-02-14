from prompt_toolkit.clipboard import pyperclip
from selenium.webdriver.common.by import By
from Locators.Locators import Save_for_later
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class HoverMorePage():
    def __init__(self, driver):

        self.driver = driver

        self.headlines_locator_xpath = Save_for_later.headlines_locator_xpath
        self.more_icon_xpath = Save_for_later.more_icon_xpath
        self.view_full_coverage_linkText = Save_for_later.view_full_coverage

    def hover_save_for_later(self):
        title = self.driver.find_element(By.XPATH, Save_for_later.headlines_locator_xpath)
        moreIcon = self.driver.find_element(By.XPATH, Save_for_later.more_icon_xpath)
        actions = webdriver.ActionChains(self.driver).move_to_element(title).move_to_element(moreIcon).perform()
        time.sleep(3)
        moreIcon.click()
        self.driver.find_element(By.LINK_TEXT, Save_for_later.view_full_coverage).click()

