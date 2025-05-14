import allure
from pages.order_page import OrderPage
from curl import *

class TestLogoScooterPress:
    @allure.title("Тест успешного перехода на главную страницу")
    def test_press_logo_scooter(self, driver):
        order_page = OrderPage(driver)

        order_page.click_order_header_button()
        order_page.click_logo_scooter()
        order_page.go_to_main_page()

        assert driver.current_url == main_site
