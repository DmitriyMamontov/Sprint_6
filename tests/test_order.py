import allure
from pages.order_page import OrderPage
from data import *
from helper import *
from curl import *

class TestOrderWithNewCredentials:
    @allure.title("Тест успешного оформления заказа")
    def test_successful_registration(self, driver):
        order_page = OrderPage(driver)
        first_name, last_name, phone_number, city = generate_order_data()
        date = generate_date()

        order_page.click_order_header_button()
        order_page.fill_first_order_form(first_name, last_name, phone_number, city)
        order_page.click_button_next()
        order_page.fill_second_order_form(date)
        order_page.click_confirm_order()
        order_page.click_submit_order()
        popup_text = order_page.get_order_popup_text()

        assert 'Заказ оформлен' in popup_text
        assert order_page.get_current_url() == order_site
