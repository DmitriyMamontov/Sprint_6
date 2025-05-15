import allure

import curl
from pages.base_page import BasePage
from locators.order_locators import OrderLocators
from locators.landing_locators import LandingLocators
from data import *
from curl import *


class OrderPage(BasePage):
    @allure.step("Нажать на кнопку заказа в шапке")
    def click_order_header_button(self):
        self.click_on_element(LandingLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать на кнопку заказа в центре")
    def click_order_center_button(self):
        self.scroll_to_element(LandingLocators.ORDER_BUTTON_CENTER)
        self.wait_for_element_to_be_clickable(LandingLocators.ORDER_BUTTON_CENTER)
        self.click_on_element(LandingLocators.ORDER_BUTTON_CENTER)

    @allure.step("Заполнить первую страницу формы заказа")
    def fill_first_order_form(self, first_name, last_name, phone_number, city):
        self.send_keys_to_input(OrderLocators.FIRST_NAME, first_name)
        self.send_keys_to_input(OrderLocators.LAST_NAME, last_name)
        self.send_keys_to_input(OrderLocators.PHONE_NUMBER, phone_number)
        self.send_keys_to_input(OrderLocators.ADDRESS, city)
        self.click_on_element(OrderLocators.METRO_STATION)
        self.click_on_element(OrderLocators.FIRST_NAME_STATION)


    @allure.step("Нажать на кнопку далее")
    def click_button_next(self):
        self.click_on_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Заполнить обязательные поля на второй странице формы заказа")
    def fill_second_order_form(self, date):
        self.click_on_element(OrderLocators.ORDER_DATE)
        self.send_keys_to_input(OrderLocators.ORDER_DATE, date)
        self.click_on_element(OrderLocators.RENTAL_PERIOD)
        self.click_on_element(OrderLocators.TWO_DAYS_BUTTON_RENTAL_PERIOD)

    @allure.step("Нажать на кнопку заказать с заполненными полями")
    def click_confirm_order(self):
        self.click_on_element(OrderLocators.PLACE_AN_ORDER_BUTTON)

    @allure.step("Нажать на кнопку назад")
    def click_back_to_first_page_order(self):
        self.click_on_element(OrderLocators.BACK_BUTTON)

    @allure.step("Нажать на кнопку ДА, в окне подтверждения заказа")
    def click_submit_order(self):
        self.click_on_element(OrderLocators.BUTTON_YES)

    @allure.step("Нажать на кнопку НЕТ, в окне подтверждения заказа")
    def click_not_submit_order(self):
        self.click_on_element(OrderLocators.BUTTON_NO)

    @allure.step("Получить текст всплывающего сообщения об оформленном заказе")
    def get_order_popup_text(self):
        return self.get_text_on_element(OrderLocators.ORDER_POPUP)

    @allure.step("Нажать на лого самокат")
    def click_logo_scooter(self):
        self.click_on_element(OrderLocators.SCOOTER_LOGO)

    @allure.step("Подождать перехода на главную страницу")
    def go_to_main_page(self):
        self.wait_for_url(curl.main_site)

    @allure.step("Нажать на лого Яндекс")
    def click_logo_yandex(self):
        self.click_on_element(OrderLocators.YANDEX_LOGO)

    @allure.step("Подождать перехода на вкладку Дзена")
    def go_to_dzen_page(self):
        self.switch_to_new_tab()
        self.wait_for_url(curl.dzen_site)
