import time

from Pages.basePage import BasePage
from Pages.weatherPage import WeatherPage


class weatherTest(BasePage):
    def test_weather(self):
        driver = self.driver
        driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

        celcius = WeatherPage(driver)
        celcius.clickCelcius()
        time.sleep(5)
        kelvin = WeatherPage(driver)
        kelvin.clickKelvin()

        time.sleep(5)
        more = WeatherPage(driver)
        more.clickMoreWeather()