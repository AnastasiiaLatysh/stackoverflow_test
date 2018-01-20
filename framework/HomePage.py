from selenium.webdriver.common.keys import Keys
from framework.BasePage import BasePage
from framework.Dictionary import DICTIONARY as test_data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from framework.LoginPage import LoginPage
from framework.ResultsPage import ResultsPage
from framework.Locators import CommonLocators
from selenium.common.exceptions import TimeoutException


class HomePage(BasePage):

    @property
    def is_home_page_opened(self):
        return WebDriverWait(self.driver, 5).until(EC.url_matches(test_data.get('site')))

    @property
    def is_user_logged_in(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(CommonLocators.LOGIN_BUTTON))
        except TimeoutException:
            return False

    @property
    def search_field(self):
        return self.driver.find_element(*CommonLocators.SEARCH_FIELD)

    def press_login_button(self):
        if not self.is_user_logged_in:
            self.click(*CommonLocators.LOGIN_BUTTON)
            return LoginPage(self.driver)

    def enter_word_in_search_filed(self, word_to_enter):
        self.search_field.send_keys(word_to_enter)
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element_value(
            CommonLocators.SEARCH_FIELD, word_to_enter))
        self.search_field.send_keys(Keys.ENTER)
        return ResultsPage(self.driver)
