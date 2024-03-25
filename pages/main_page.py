import allure
import datas
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step('Использование coockies')
    def accept_kooky(self):
        self.click_element(locator=MainPageLocators.COOKIES_BUTTON)

    @allure.step('Получение ответа на вопрос')
    def get_answer(self, num):
        locator_que_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        locator_ans_formatted = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_element(locator_que_formatted)
        return self.get_value_from_element(locator_ans_formatted)

    @allure.step('Клик по верхней кнопке Заказать')
    def up_order_button(self):
        self.click_element(locator=MainPageLocators.ORDER_IN_THE_CORNER)
        return self.get_value_from_element(MainPageLocators.ORDER_TEXT_RESULT)

    @allure.step('Тестируем кнопку "Заказать" в центре основной страницы')
    def main_order_button(self):
        self.click_element(locator=MainPageLocators.ORDER_ON_PAGE)
        return self.get_value_from_element(MainPageLocators.ORDER_TEXT_RESULT)

    @allure.step('Переход на главную страницу')
    def scooter_logo(self):
        # Перейти на страницу заказа
        self.click_element(locator=MainPageLocators.ORDER_IN_THE_CORNER)
        # Нажать на логотип самоката
        self.click_element(locator=MainPageLocators.SCOOTER_LOGO)
        return datas.scooter in self.get_value_from_element(MainPageLocators.MAIN_PAGE_TEXT)

    @allure.step('Переход на страницу Яндекса по логотипу')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Проверка перехода на страницу Яндекса')
    def check_dzen_window(self):
        return self.transfer_to_window(MainPageLocators.DZEN, 1)
