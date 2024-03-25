from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:

    @allure.step('Конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_waiting (self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание наличия элемента с последующим кликом')
    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ввод значения в поле ввода')
    def add_value_to_element(self, locator, text):
        self.find_element_waiting(locator).send_keys(text)

    @allure.step('Получение значения элемента')
    def get_value_from_element(self, locator):
        return self.find_element_waiting(locator).text

    @allure.step('Форматирование локатора с окончанием-счетчиком')
    def format_locator(self, locator_full, num):
        method, locator = locator_full
        locator = locator.format(num)
        return method, locator

    @allure.step('Переход в другую вкладку браузера по заданному номеру')
    def transfer_to_window(self, locator, n):
        self.driver.switch_to.window(self.driver.window_handles[n])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.current_url
