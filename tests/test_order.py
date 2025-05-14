import allure

from helper import generate_order_data, generate_order_credentials, generate_date
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestMainPage:
    @allure.title("Заказ самоката с помощью верхней кнопки Заказать")
    def test_order(self, driver):
        page = MainPage(driver)
        page.close_cookie_window()
        first_name, last_name, address, metro_station, phone = generate_order_credentials()
        page.click_top_register_button()
        page = OrderPage(driver)
        page.input_credentials(first_name, last_name, address, metro_station, phone)
        date, comment = generate_order_data()
        page.input_rent_data(date, comment)
        page.accept_order()
        text = 'Заказ оформлен'
        header = page.get_text_ordered_header()
        assert text in header, f"Ожидали текст '{text}', но получили: '{header}'"

    @allure.title("Заказ самоката с помощью средней кнопки Заказать")
    def test_order_mid(self, driver):
        page = MainPage(driver)
        page.close_cookie_window()
        first_name, last_name, address, metro_station, phone = generate_order_credentials()
        page.click_top_register_button()
        page = OrderPage(driver)
        page.input_credentials(first_name, last_name, address, metro_station, phone)
        date = generate_date()
        page.input_rent_data2(date)
        page.accept_order()
        text = 'Заказ оформлен'
        header = page.get_text_ordered_header()
        assert text in header, f"Ожидали текст '{text}', но получили: '{header}'"




