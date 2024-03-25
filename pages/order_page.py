from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import datas
import allure

class OrderPage(BasePage):

    @allure.step('кнопка "Заказать"')
    def click_order_button(self):
        self.click_element(locator=OrderPageLocators.ORDER_BUTTON)

    @allure.step('Ввести имя')
    def input_name(self, name):
        self.add_value_to_element(locator=OrderPageLocators.FIRST_NAME, text=name)

    @allure.step('Ввести фамилию')
    def input_last_name(self, last_name):
        self.add_value_to_element(locator=OrderPageLocators.LAST_NAME, text=last_name)

    @allure.step('Ввести адрес')
    def input_adress(self,address):
        self.add_value_to_element(locator=OrderPageLocators.ADDRESS, text=address)

    @allure.step('Выбрать метро из выпадающего списка')
    def input_metro_station(self, station):
        self.click_element(locator=OrderPageLocators.METRO)
        self.add_value_to_element(locator=OrderPageLocators.METRO, text=station)
        self.click_element(locator=OrderPageLocators.CHOSEN_STATION)

    @allure.step('Ввести телефонный номер')
    def input_telephone_number(self, phone):
        self.add_value_to_element(locator=OrderPageLocators.PHONE, text=phone)

    @allure.step('Переход на вторую страницу')
    def next_page(self):
        self.click_element(locator=OrderPageLocators.ORDER_NEXT)

    @allure.step('Выбрать дату доставки')
    def select_delivery_date(self):
        self.click_element(locator=OrderPageLocators.DATE_CHOICE)
        self.click_element(locator=OrderPageLocators.DATE_CHOSEN)

    @allure.step('Выбрать срок аренды - 2 дня')
    def select_rent_period(self):
        self.click_element(locator=OrderPageLocators.RENT_PERIOD)
        self.click_element(locator=OrderPageLocators.TWO_DAYS)

    @allure.step('Выбирать черный цвет самоката')
    def select_color(self):
        self.click_element(locator=OrderPageLocators.BLACK_PERL)

    @allure.step('Комментарий курьеру')
    def input_comment(self, comment):
        self.add_value_to_element(locator=OrderPageLocators.COMMENT, text=comment)

    @allure.step('Создать заказ')
    def create_order(self):
        self.click_element(locator=OrderPageLocators.MAKE_ORDER)
        self.click_element(locator=OrderPageLocators.ORDER_YES)

    @allure.step('Проверка текста в окне заказа')
    def check_order(self):
        return datas.order_status in self.get_value_from_element(locator=OrderPageLocators.ORDER_FORMED)
