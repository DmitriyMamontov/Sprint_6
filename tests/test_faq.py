import allure
import pytest

import data
from pages.landing_page import LandingPage

class TestFaqSection:
    @allure.title("Проверка текста при раскрытии вопросов в FAQ")
    @pytest.mark.parametrize("question_number, expected_text", data.Data.accordion_answers)
    def test_faq_answers(self, driver, question_number, expected_text):
        landing_page = LandingPage(driver)
        landing_page.scroll_to_tab_menu()
        landing_page.wait_faq_question(question_number)
        landing_page.click_on_faq_question(question_number)
        landing_page.wait_for_faq_answer(question_number)
        actual_answer = landing_page.get_faq_answer_text(question_number)
        assert actual_answer == expected_text