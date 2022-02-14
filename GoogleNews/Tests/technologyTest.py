import time

from Pages.basePage import BasePage
from Pages.technologyPage import TechnologyPage



class technologyTest(BasePage):

    def test_weather(self):
        driver = self.driver
        driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

        technology = TechnologyPage(driver)
        technology.clickTechnology()

        time.sleep(3)
        technology.clickLatest()

        time.sleep(3)
        technology.clickMobile()

        time.sleep(3)
        technology.clickGadgets()

        time.sleep(3)
        technology.clickInternet()

        time.sleep(3)
        technology.clickVirtualReality()

        time.sleep(3)
        technology.clickArtificialIntelligence()

        time.sleep(3)
        technology.clickComputing()
