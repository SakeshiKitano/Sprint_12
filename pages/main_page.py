import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликнуть на вопрос FAQ и получить его текст")
    def click_question(self, text):
        self.scroll_to_element(MainPageLocators.ACCORDION_BUTTON)
        locator = MainPageLocators.QUESTION_LOCATOR(text)
        self.click_on_element(locator)

    @allure.step("Дождаться ответа FAQ")
    def is_answer_displayed(self, text):
        locator = MainPageLocators.ANSWER_LOCATOR(text)
        return self.wait_for_element(locator).is_displayed()

    @allure.step("Закрыть куки")
    def close_cookie_window(self):
        self.click_on_element(MainPageLocators.APPLY_COOKIE_BUTTON)

    @allure.step("Нажать на верхнюю кнопку Заказать")
    def click_top_register_button(self):
        self.click_on_element(MainPageLocators.TOP_BUTTON_ORDER)

    @allure.step("Нажать на кнопку Заказать в середине страницы")
    def click_mid_register_button(self):
        self.click_on_element(MainPageLocators.MIDDLE_BUTTON_ORDER)

    @allure.step("Нажать на лого Самокат")
    def click_logo_samokat(self):
        self.click_on_element(MainPageLocators.LOGO_SAMOKAT)

    @allure.step("Нажать на лого Yandex")
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Дождаться прогрузки лого Дзен")
    def logo_dzen_is_displayed(self):
        self.wait_for_element(MainPageLocators.LOGO_DZEN).is_displayed()




