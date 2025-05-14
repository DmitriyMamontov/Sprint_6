import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Подождать и проверить что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Подождать URL")
    def wait_for_url(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        new_tab = [tab for tab in self.driver.window_handles if tab != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_tab)
        return new_tab

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))