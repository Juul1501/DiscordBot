import selenium.webdriver as webdriver

def get_result(search_term):
    url = "https://images.google.com/"
    browser = webdriver.Firefox()
    browser.get(url)
    search_box = browser.find_element_by_id("lst-ib")
    search_box.send_keys(search_term)
    search_box.sumbit()
    links = browser.find_elements_by_xpath("//a")
    
    results = []

    for link in links:
        href = link.get_attribute("href")
        print(href)
        results.append(href)
    browser.close()
    return results

get_result("hond")



