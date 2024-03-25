from pages.main_page import MainPage
import datas
import pytest
import allure

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
    @allure.title('Тестируем вопросы о важном - проходят 8 проверок')
    def test_questions_and_answers(self, driver, num, result):
        general_page = MainPage(driver)
        general_page.accept_kooky()
        assert general_page.get_answer(num) == result

    @allure.title('Тестируем кнопку "Заказать" в верхнем углу основной страницы')
    def test_up_order_button(self, driver):
        general_page = MainPage(driver)
        assert general_page.up_order_button() == datas.order_for

    @allure.title('Тестируем кнопку "Заказать" в центре основной страницы')
    def test_main_order_button(self, driver):
        general_page = MainPage(driver)
        general_page.accept_kooky()
        assert general_page.main_order_button() == datas.order_for
