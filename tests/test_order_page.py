import allure
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from conftest import *

class TestOrderPage:

    @pytest.mark.parametrize(
        'name, last_name, address, station, phone, comment',
                             [
                                 ('Яна', 'Карпова', 'Москва', 'Комсомольская', '+79161234567', 'Без комментариев'),
                                 ('Вася', 'Пупкин', 'Московская ', 'Комсомольская', '+79167654321', '')
                             ]
    )
    @allure.description('Заполнение заказа, проверка появления всплывающего окна "Заказ оформлен"')
    def test_set_order(self, driver, name, last_name, address, station, phone, comment):
        general_page = OrderPage(driver)
        general_page.click_element(OrderPageLocators.ORDER_BUTTON)
        general_page.set_order(name, OrderPageLocators.FIRST_NAME, last_name,
                               OrderPageLocators.LAST_NAME, address, OrderPageLocators.ADDRESS,
                               OrderPageLocators.METRO, station, OrderPageLocators.CHOSEN_STATION,
                               phone, OrderPageLocators.PHONE, OrderPageLocators.DATE_CHOICE,
                               OrderPageLocators.DATE_CHOSEN, OrderPageLocators.RENT_PERIOD, OrderPageLocators.TWO_DAYS,
                               OrderPageLocators.BLACK_PERL, OrderPageLocators.COMMENT, comment,
                               OrderPageLocators.ORDER_NEXT)
        general_page.click_element(OrderPageLocators.MAKE_ORDER)
        general_page.click_element(OrderPageLocators.ORDER_YES)
        assert 'Заказ оформлен' in general_page.check_order(OrderPageLocators.ORDER_FORMED)
