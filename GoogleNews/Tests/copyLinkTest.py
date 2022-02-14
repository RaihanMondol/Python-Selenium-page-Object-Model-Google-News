import time
import unittest

from selenium import webdriver

from Pages.sharePage import SharePage


class CopyLinkText(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="F:/googlenews/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        print("Test Started......")

    def test_copy_link(self):
        driver = self.driver
        driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

        copy = SharePage(driver)
        copy.click_headlines()
        copy.click_share()
        copy.click_copylink()
        copy.create_new_tab()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
