
from selenium.webdriver.common.by import By
from Locators.Locators import Weather



class WeatherPage():
    def __init__(self, driver):

        self.driver = driver

        self.celcius_xpath = Weather.celcius_xpath
        self.farenheight_xpath = Weather.farenheight_xpath
        self.kelvin_xpath = Weather.kelvin_xpath
        self.more_weather_xpath = Weather.more_weather_xpath

    def  clickCelcius(self):
        self.driver.find_element(By.XPATH, Weather.celcius_xpath).click()

    def  clickKelvin(self):
        self.driver.find_element(By.XPATH, Weather.kelvin_xpath).click()

    def clickMoreWeather(self):
        self.driver.find_element(By.XPATH, Weather.more_weather_xpath).click()




