import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.get_screenshot_as_file("screenshot1.png")

        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.get_screenshot_as_file("screenshot2.png")


    def test_navigation(self):
        driver = self.driver

        driver.get("http://www.google.com")
        driver.forward()
        driver.get_screenshot_as_file("screenshot3.png")
        driver.back()
        driver.get_screenshot_as_file("screenshot4.png")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
