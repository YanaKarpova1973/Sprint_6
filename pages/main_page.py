from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class MainPage(BasePage):

    def get_answer(self, locator_que, locator_ans, num):
        locator_que_formatted = self.format_locator(locator_que, num)
        locator_ans_formatted = self.format_locator(locator_ans, num)
        self.click_element(locator_que_formatted)
        return self.get_value_from_element(locator_ans_formatted)

    def transfer_to_window(self, locator, n):
        self.driver.switch_to.window(self.driver.window_handles[n])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.current_url
