import pytest
from curl import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--width=1800")
    options.add_argument("--height=1000")
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.get(main_site)
    yield driver
    driver.quit()
