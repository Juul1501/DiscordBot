import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def get_result():
    browser = webdriver.Firefox()
    browser.get('http://www.google.com')

    search = browser.find_element_by_name('q')
    search.send_keys("google search through python")
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    browser.quit()

get_result()



