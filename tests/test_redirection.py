from pages.main_page import MainPage
import allure
import datas

class TestRedirection:

    @allure.title('Переход на главную страницу')
    def test_scooter_logo(self, driver):
        general_page = MainPage(driver)
        assert general_page.scooter_logo()

    @allure.title('Переход на страницу Яндекса по логотипу')
    def test_yandex_logo(self, driver):
        general_page = MainPage(driver)
        general_page.click_yandex_logo()
        assert general_page.check_dzen_window() == datas.dzen_url
