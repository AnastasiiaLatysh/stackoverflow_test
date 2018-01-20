import unittest
from framework.DriverWrapper import Driver
from framework.HomePage import HomePage
from framework.Dictionary import DICTIONARY as test_data


class TestBase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        base_url = test_data.get('site')
        cls.driver = Driver.get_driver()

        cls.home_page = HomePage(cls.driver, base_url)
        cls.home_page.open_home_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
