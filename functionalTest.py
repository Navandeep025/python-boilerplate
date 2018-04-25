# #!/usr/bin/env python

# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

# chrome_options =Options() 
# options = webdriver.ChromeOptions()
# #chrome_options=chrome_options
# #chrome_options.setBinary("/usr/bin/google-chrome-stable")
# options.binary_location = "/usr/bin/google-chrome-stable"
# #options.add_argument("--headless")
# #executable_path=r"chromedriver.exe"
# driver = webdriver.Chrome(executable_path="/usr/local/share/chromedriver.exe")
# driver.set_page_load_timeout(30)
# driver.get("http://www.python.org")
# driver.implicitly_wait(20)
# diver.get_screenshot_as_file("screenshot.png")

# driver.quit()



#!/usr/bin/env python

import os
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.set_page_load_timeout(30)
driver.get("http://www.google.com")
driver.implicitly_wait(20)
driver.get_screenshot_as_file("screenshot.png")


driver.quit()

