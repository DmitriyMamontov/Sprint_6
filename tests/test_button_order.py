import allure
from pages.order_page import OrderPage
from curl import order_site

class TestButtonOrder:
    @allure.title("Тест успешного нажатия кнопки Заказать в шапке")
    def test_press_button_order_header(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_header_button()

        assert order_page.get_current_url() == order_site


    @allure.title("Тест успешного нажатия кнопки Заказать в центре")
    def test_press_button_order_centre(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_center_button()

        assert order_page.get_current_url() == order_site
