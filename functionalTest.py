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
driver = webdriver.Chrome()
driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()

# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
