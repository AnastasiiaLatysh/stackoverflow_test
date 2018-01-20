from framework.BasePage import BasePage
from framework.Locators import LoginLocators, CommonLocators


class LoginPage(BasePage):

    def enter_credentials(self, email, password):
        self.driver.find_element(*LoginLocators.EMAIL).send_keys(email)
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)

    def submit_login(self):
        self.click(*CommonLocators.SUBMIT_BUTTON)
