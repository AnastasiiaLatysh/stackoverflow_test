from selenium import webdriver

GECKO_DRIVER_PATH = 'PATH_TO_GECKO_DRIVER'


class Driver:

    @staticmethod
    def get_driver():
        driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
        return Driver.add_driver_settings(driver)

    @staticmethod
    def add_driver_settings(driver):
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(20)
        driver.set_window_size(1280, 1024)
        return driver
