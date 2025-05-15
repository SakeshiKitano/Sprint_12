import time

import allure


from curl import *
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestLogo:



    @allure.title("Тестирование клика по логотипу Самокат")
    def test_logo_samokat(self, driver):
        page = MainPage(driver)
        page.close_cookie_window()
        page.click_top_register_button()
        page.click_logo_samokat()
        assert driver.current_url == main_site

    @allure.title("Тестирование клика по логотипу Яндекс")
    def test_logo_yandex(self, driver):
        page = MainPage(driver)
        page.close_cookie_window()
        page.click_logo_yandex()
        driver.switch_to.window(driver.window_handles[-1])
        page.logo_dzen_is_displayed()
        assert driver.current_url == dzen_redirect

