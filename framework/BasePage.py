from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, base_url=''):
        self.driver = driver
        self.base_url = base_url

    def open_home_page(self):
        self.driver.get(self.base_url)

    def click(self, *locator):
        self.wait_until_element_to_be_clickable(locator)
        self.driver.find_element(*locator).click()

    def wait_until_element_to_be_clickable(self, *locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(*locator))
        except TimeoutException:
            raise AssertionError('It takes more than {} sec to load an element'.format(timeout))
