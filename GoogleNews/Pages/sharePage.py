from prompt_toolkit.clipboard import pyperclip
from selenium.webdriver.common.by import By
from Locators.Locators import Headlines_Locators
import time


class SharePage():
    def __init__(self, driver):
        self.driver = driver

        self.click_headlines_xpath = Headlines_Locators.click_headlines_xpath
        self.click_share_xpath = Headlines_Locators.click_share_xpath
        self.click_copylink_xpath = Headlines_Locators.click_copylinkbutton_xpath
        self.share_button_facebook_xpath = Headlines_Locators.share_button_facebook_xpath
        self.share_button_twitter_xpath = Headlines_Locators.share_button_twitter_xpath

    def click_headlines(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Headlines_Locators.click_headlines_xpath).click()

    def click_share(self):
        self.driver.find_element(By.XPATH, Headlines_Locators.click_share_xpath).click()

    def click_copylink(self):
        self.driver.find_element(By.XPATH, Headlines_Locators.click_copylinkbutton_xpath).click()

    def create_new_tab(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        # link = pyperclip.paste()
        self.driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?ceid=US:en&oc=3")

    def share_with_facebook(self):
        self.driver.find_element(By.XPATH, Headlines_Locators.share_button_facebook_xpath).click()

    def share_with_twitter(self):
        self.driver.find_element(By.XPATH, Headlines_Locators.share_button_twitter_xpath).click()