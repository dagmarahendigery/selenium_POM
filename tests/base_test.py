import unittest
from selenium import webdriver
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base Page Object for each Test Case
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://16e.demofield.com/en/")
        self.home_page = HomePage(self.driver) #obiekt klasy homeepage

    def tearDown(self):
        self.driver.quit()

