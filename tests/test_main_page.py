import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import datas
from conftest import *

class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, datas.answer_0),
            (1, datas.answer_1),
            (2, datas.answer_2),
            (3, datas.answer_3),
            (4, datas.answer_4),
            (5, datas.answer_5),
            (6, datas.answer_6),
            (7, datas.answer_7)
         ]
    )
    @allure.description('Тестируем вопросы о важном - проходят 8 проверок')
    def test_questions_and_answers(self, driver, num, result):
        general_page = MainPage(driver)
        general_page.click_element(MainPageLocators.COOKIES_BUTTON)
        assert general_page.get_answer(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,
            num
        ) == result

    @allure.description('Тестируем кнопку "Заказать" в верхнем углу основной страницы')
    def test_up_order_button(self, driver):
        general_page = MainPage(driver)
        general_page.click_element(MainPageLocators.ORDER_IN_THE_CORNER)
        assert general_page.get_value_from_element(MainPageLocators.ORDER_TEXT_RESULT) == 'Для кого самокат'

    @allure.description('Тестируем кнопку "Заказать" в центре основной страницы')
    def test_main_order_button(self, driver):
        general_page = MainPage(driver)
        general_page.click_element(MainPageLocators.COOKIES_BUTTON)
        general_page.click_element(MainPageLocators.ORDER_ON_PAGE)
        assert general_page.get_value_from_element(MainPageLocators.ORDER_TEXT_RESULT) == 'Для кого самокат'

    @allure.description('Переход на главную страницу')
    def test_scooter_logo(self, driver):
        general_page = MainPage(driver)
        # Перейти на страницу заказа
        general_page.click_element(MainPageLocators.ORDER_IN_THE_CORNER)
        # Нажать на логотип самоката
        general_page.click_element(MainPageLocators.SCOOTER_LOGO)
        assert "Привезём его прямо к вашей двери" in general_page.get_value_from_element(MainPageLocators.MAIN_PAGE_TEXT)

    @allure.description('Переход на страницу Яндекса по логотипу')
    def test_yandex_logo(self, driver):
        general_page = MainPage(driver)
        general_page.click_element(MainPageLocators.YANDEX_LOGO)
        assert general_page.transfer_to_window(MainPageLocators.DZEN, 1) == 'https://dzen.ru/?yredirect=true'
