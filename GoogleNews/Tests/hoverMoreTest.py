import time
import unittest
from selenium import webdriver

from Pages.hoverMorePage import HoverMorePage
from Pages.saveForLaterPage import SaveForLaterPage
class CopyLinkText(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="F:/googlenews/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        print("Test Started......")

    def test_hover(self):
        driver = self.driver
        driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

        mouse = HoverMorePage(driver)
        mouse.hover_save_for_later()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
