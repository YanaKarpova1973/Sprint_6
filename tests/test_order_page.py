from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
import pytest
import allure

class TestOrderPage:

    @pytest.mark.parametrize(
        'name, last_name, address, station, phone, comment',
                             [
                                 ('Яна', 'Карпова', 'Москва', 'Комсомольская', '+79161234567', 'Без комментариев'),
                                 ('Вася', 'Пупкин', 'Московская ', 'Комсомольская', '+79167654321', '')
                             ]
    )
    @allure.title('Заполнение заказа, проверка появления всплывающего окна "Заказ оформлен"')
    def test_set_order(self, driver, name, last_name, address, station, phone, comment):
        general_page = OrderPage(driver)
        general_page.click_element(OrderPageLocators.ORDER_BUTTON)
        general_page.click_order_button()
        general_page.input_name(name)
        general_page.input_last_name(last_name)
        general_page.input_adress(address)
        general_page.input_metro_station(station)
        general_page.input_telephone_number(phone)
        general_page.next_page()
        general_page.select_delivery_date()
        general_page.select_rent_period()
        general_page.select_color()
        general_page.input_comment(comment)
        general_page.create_order()
        assert general_page.check_order()
