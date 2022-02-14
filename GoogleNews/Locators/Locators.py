from selenium.webdriver.common.by import By


class Search_Locators():
    # Search page locators
    search_textbox_xpath = '//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]'
    search_button_xpath = '//*[@id="gb"]/div[2]/div[2]/div/form/button[4]'


class Headlines_Locators():
    click_headlines_xpath = '//*[@id="i45"]/div[2]/span/a'
    click_follow_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[1]/div'

    click_share_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[2]'
    click_copylinkbutton_xpath = '//*[@id="yDmH0d"]/div[12]/div[2]/div/div/div[3]/div[2]/div[1]'
    share_button_facebook_xpath = "//*[@id='yDmH0d']/div[12]/div[2]/div/div/div[3]/div[2]/div[2]"
    share_button_twitter_xpath = '//*[@id="yDmH0d"]/div[12]/div[2]/div/div/div[3]/div[2]/div[3]'


class Save_for_later():
    headlines_locator_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/h3/a'
    save_for_icon_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/div/menu/div/div'
    more_icon_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/div/menu/span[2]'
    view_full_coverage = 'View Full Coverage'


class Weather():
    celcius_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/div/div[1]/button'
    farenheight_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/div/div[2]'
    kelvin_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/div/div[3]'
    more_weather_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/small'


class Technology():
    technology_xpath = '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[8]/a/div[2]/span'
    latest_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[1]/span'
    mobile_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[2]/span'
    gadgets_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[3]/span'
    internet_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[4]/span'
    virtual_reality_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[5]/span'
    artificial_intelligence_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[6]/span/div'
    computing_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[7]/span/div'
