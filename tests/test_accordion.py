 #-*- coding: utf-8 -*-

import pytest
import data
import allure

from pages.main_page import MainPage

class TestMainPage:
    @allure.title("Тест соответствия текста вопросов-ответов выпадающего списка 'Вопросы о важном'")
    @pytest.mark.parametrize("question, answer", data.FaqData.faq_data, ids=[question for question, _ in data.FaqData.faq_data])
    def test_faq_accordion(self, driver, question, answer):
        page = MainPage(driver)
        page.close_cookie_window()
        page.click_question(question)
        assert page.is_answer_displayed(answer)


