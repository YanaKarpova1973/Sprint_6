from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_waiting (self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_value_to_element(self, locator, text):
        self.find_element_waiting(locator).send_keys(text)

    def get_value_from_element(self, locator):
        return self.find_element_waiting(locator).text

    def format_locator(self, locator_full, num):
        method, locator = locator_full
        locator = locator.format(num)
        return method, locator
