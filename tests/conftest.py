import pytest
from selenium import webdriver


# 浏览器夹具
@pytest.fixture(scope='session')
def web_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()