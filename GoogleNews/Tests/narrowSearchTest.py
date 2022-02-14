import time
import unittest

from selenium import webdriver

from Pages.narrowSearchPage import narrowSearchPage


class SearchTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="F:/googlenews/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        print("Test Started......")

    def test_searchTest(self):
        driver = self.driver
        driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

        search = narrowSearchPage(driver)
        search.featured_topic_search()
        search.click_Search()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
