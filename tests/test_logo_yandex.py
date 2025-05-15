import allure
from pages.order_page import OrderPage
from curl import *

class TestLogoYandexPress:
    @allure.title("Тест успешного перехода на вкладку Дзен")
    def test_press_logo_yandex(self, driver):
        order_page = OrderPage(driver)

        order_page.click_logo_yandex()
        order_page.go_to_dzen_page()

        assert dzen_site in order_page.get_current_url()