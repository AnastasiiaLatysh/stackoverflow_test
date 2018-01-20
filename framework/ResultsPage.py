from framework.BasePage import BasePage
from framework.Locators import ResultsLocators
import logging


class ResultsPage(BasePage):

    @property
    def results(self):
        return self.driver.find_elements(*ResultsLocators.RESULTS)

    def get_result(self, result_number):
        if self.results:
            try:
                return self.results[result_number].find_element_by_tag_name('a')
            except IndexError:
                logging.warning(msg="There are only %d found results when you are trying to get % d result" %
                                    (len(self.results), result_number))
        else:
            return None

    def open_result(self, result_number):
        if self.results:
            self.results[result_number].find_element_by_tag_name('a').click()

    @property
    def result_header(self):
        return self.driver.find_element(*ResultsLocators.RESULT_HEADER)
