from pages.base_page import BasePage

class OrderPage(BasePage):

    def set_order(self, first_name, first_name_locator, last_name, last_name_locator, address,
                               address_locator, station_locator, station, chosen_station, phone, phone_locator,
                               date_of_order_locator, date_of_order, rent_period_locator, rent_period, colour_locator,
                               comment_locator, comment_text, next_button):
        self.add_value_to_element(first_name_locator, first_name)
        self.add_value_to_element(last_name_locator, last_name)
        self.add_value_to_element(address_locator, address)
        self.click_element(station_locator)
        self.add_value_to_element(station_locator, station)
        self.click_element(chosen_station)
        self.add_value_to_element(phone_locator, phone)
        self.click_element(next_button)
        self.click_element(date_of_order_locator)
        self.click_element(date_of_order)
        self.click_element(rent_period_locator)
        self.click_element(rent_period)
        self.click_element(colour_locator)
        self.click_element(comment_locator)
        self.add_value_to_element(comment_locator, comment_text)


    def check_order(self, locator):
        return self.get_value_from_element(locator)
