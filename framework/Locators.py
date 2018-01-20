from selenium.webdriver.common.by import By


class CommonLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.login-link.btn-clear')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.f-input.js-search-field')
    SUBMIT_BUTTON = (By.ID, 'submit-button')


class LoginLocators:
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')


class ResultsLocators:
    FIRST_RESULT = (By.CSS_SELECTOR, '#questions div.summary a')
    RESULT_HEADER = (By.XPATH, '//div[@id="question-header"]/*/a')

    RESULTS = (By.CSS_SELECTOR, '.question-summary')
