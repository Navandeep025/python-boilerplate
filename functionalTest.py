#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options =Options() 
options = webdriver.ChromeOptions()
#chrome_options=chrome_options
#chrome_options.setBinary("/usr/bin/google-chrome-stable")
options.binary_location = "//usr//bin//google-chrome-stable"
options.add_argument("--headless")
#executable_path=r"chromedriver.exe"
driver = webdriver.Chrome("//usr//local//share//chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.python.org")
driver.implicitly_wait(20)
diver.get_screenshot_as_file("screenshot.png")


driver.quit()
