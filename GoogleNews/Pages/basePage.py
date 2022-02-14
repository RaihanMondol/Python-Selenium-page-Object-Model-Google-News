import time
import unittest
from selenium import webdriver


class BasePage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="F:/googlenews/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("Test Complete")


if __name__ == "__main__":
    unittest.main()
