import allure


from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage




class OrderPage(BasePage):


    @allure.step("Заполнить данные Для кого самокат")
    def input_credentials(self, first_name, last_name, address, metro_station, phone):
        self.click_on_element(OrderPageLocators.NAME_INPUT)
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, first_name)
        self.click_on_element(OrderPageLocators.LAST_NAME_INPUT)
        self.send_keys_to_input(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.click_on_element(OrderPageLocators.ADDRESS_INPUT)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, address)
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.send_keys_to_input(OrderPageLocators.METRO_STATION_INPUT, metro_station)
        self.click_on_element(OrderPageLocators.STATION_IN_DROPDOWN)
        self.click_on_element(OrderPageLocators.PHONE_INPUT)
        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные Про аренду ")
    def input_rent_data(self, date, comment):
        self.click_on_element(OrderPageLocators.DATE_INPUT)
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT,date)
        self.enter_after_text(OrderPageLocators.DATE_INPUT)
        self.click_on_element(OrderPageLocators.RENT_PERIOD)
        self.click_on_element(OrderPageLocators.PER_TWO_DAYS)
        self.click_on_element(OrderPageLocators.COLOR_BLACK)
        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Заполнить данные Про аренду без комментария и с другими данными")
    def input_rent_data2(self, date):
        self.click_on_element(OrderPageLocators.DATE_INPUT)
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT,date)
        self.enter_after_text(OrderPageLocators.DATE_INPUT)
        self.click_on_element(OrderPageLocators.RENT_PERIOD)
        self.click_on_element(OrderPageLocators.PER_ONE_DAY)
        self.click_on_element(OrderPageLocators.COLOR_GREY)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Нажать кнопку Да на форме уверенности")
    def accept_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получить текст  хедера формы Заказ оформлен")
    def get_text_ordered_header(self):
        self.wait_for_element(OrderPageLocators.ORDERED_FORM_HEADER)
        header = self.get_text_on_element(OrderPageLocators.ORDERED_FORM_HEADER)
        return header