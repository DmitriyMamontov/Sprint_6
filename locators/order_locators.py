from selenium.webdriver.common.by import By


class OrderLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    MENU_METRO_STATIONS = (By.XPATH, "//li[@class='select-search__row']/button[text()='Бульвар Рокоссовского']")
    FIRST_NAME_STATION = (By.XPATH, "//div[text()='Бульвар Рокоссовского']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    TWO_DAYS_BUTTON_RENTAL_PERIOD = (By.XPATH, "//div[text()='двое суток']")
    WINDOW_ORDER_CONFIRMATION = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ'][text()='Хотите оформить заказ?']")
    BACK_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Назад']")
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Да']")
    BUTTON_NO = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Нет']")
    ORDER_POPUP = (By.XPATH, "//div[text()='Заказ оформлен']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a.Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a.Header_LogoYandex__3TSOI')
