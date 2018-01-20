import unittest
from tests.TestBase import TestBase
from framework.Dictionary import DICTIONARY as test_data


class TestPythonSearchStackOverflow(TestBase):

    def test_find_first_search_result(self):
        # check that home page is opened and open login page
        self.assertTrue(self.home_page.is_home_page_opened, 'Home page is opened')
        login_page = self.home_page.press_login_button()

        # login in site
        login_page.enter_credentials(test_data.get('email'), test_data.get('password'))
        login_page.submit_login()
        self.assertTrue(self.home_page.is_user_logged_in, 'User is logged in')

        # enter word in search field
        results_page = self.home_page.enter_word_in_search_filed(test_data.get('search_text'))

        # get name of first result
        first_result_text = results_page.get_result(result_number=0).text

        # open first result and check it's header
        results_page.open_result(result_number=0)
        self.assertEqual(first_result_text, results_page.result_header.text, 'First result is opened')


if __name__ == '__main__':
    unittest.main()
