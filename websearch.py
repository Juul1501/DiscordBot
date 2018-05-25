<<<<<<< HEAD
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
=======
import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
url = 'https://www.google.nl/search?hl=nl&authuser=0&tbm=isch&source=hp&biw=1920&bih=974&ei=Yf0HW-i1GcjNwALPtYrIAw&q=hihih&oq=hihih&gs_l=img.3..0l10.1067.1432.0.1633.7.6.0.0.0.0.158.305.0j2.2.0....0...1ac.1.64.img..5.2.304.0...0.nL0CRzqgKn4'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
>>>>>>> b06638ceeee2bad9f5356eda910af4187ed0551d



