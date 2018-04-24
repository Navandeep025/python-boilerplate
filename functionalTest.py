#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options =Options()       
#chrome_options=chrome_options
#chrome_options.setBinary("/usr/bin/google-chrome-stable")
#chrome_options.binary_location = "/usr/bin/google-chrome-stable"
chrome_options.add_argument("--headless")
#executable_path=r"chromedriver.exe"
driver = webdriver.Chrome("//usr//local//share//chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.python.org")
driver.implicitly_wait(20)
diver.get_screenshot_as_file("screenshot.png")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()

# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.quit()
