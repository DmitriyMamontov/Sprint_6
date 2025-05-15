import allure
from pages.base_page import BasePage
from locators.landing_locators import LandingLocators

class LandingPage(BasePage):

    @allure.step("Проскроллить до меню со вкладками")
    def scroll_to_tab_menu(self):
        self.scroll_to_element(LandingLocators.TABS_MENU)

    @allure.step("Кликнуть на вкладку #{question_number}")
    def click_on_faq_question(self, question_number):
        self.click_on_element(LandingLocators.faq_questions_items[question_number])

    @allure.step("Ожидание кликабельности вкладки")
    def wait_faq_question(self, question_number):
        self.wait_for_element_to_be_clickable(LandingLocators.faq_questions_items[question_number])

    @allure.step("Ожидание появления ответа #{question_number}")
    def wait_for_faq_answer(self, question_number):
        self.wait_for_element(LandingLocators.faq_answers_items[question_number])

    @allure.step("Получение текста ответа #{question_number}")
    def get_faq_answer_text(self, question_number):
        return self.get_text_on_element(LandingLocators.faq_answers_items[question_number])