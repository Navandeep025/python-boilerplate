#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=options)
driver.set_page_load_timeout(30)
driver.get("http://www.google.com")
driver.implicitly_wait(20)
driver.get_screenshot_as_file("screenshot.png")

driver.quit()

