from selenium.webdriver.common.by import By
from Locators.Locators import Technology



class TechnologyPage():
    def __init__(self, driver):

        self.driver = driver

        self.technology_xpath = Technology.technology_xpath
        self.latest_xpath = Technology.latest_xpath
        self.mobile_xpath = Technology.mobile_xpath
        self.gadgets_xpath = Technology.gadgets_xpath
        self.internet_xpath = Technology.internet_xpath
        self.virtual_reality_xpath = Technology.virtual_reality_xpath
        self.artificial_intelligence_xpath = Technology.artificial_intelligence_xpath
        self.computing_xpath = Technology.computing_xpath


    def clickTechnology(self):
        self.driver.find_element(By.XPATH, Technology.technology_xpath).click()

    def clickLatest(self):
        self.driver.find_element(By.XPATH, Technology.latest_xpath).click()

    def clickMobile(self):
        self.driver.find_element(By.XPATH, Technology.mobile_xpath).click()

    def clickGadgets(self):
        self.driver.find_element(By.XPATH, Technology.gadgets_xpath).click()

    def clickInternet(self):
        self.driver.find_element(By.XPATH, Technology.internet_xpath).click()

    def clickVirtualReality(self):
        self.driver.find_element(By.XPATH, Technology.virtual_reality_xpath).click()

    def clickArtificialIntelligence(self):
        self.driver.find_element(By.XPATH, Technology.artificial_intelligence_xpath).click()

    def clickComputing(self):
        self.driver.find_element(By.XPATH, Technology.computing_xpath).click()