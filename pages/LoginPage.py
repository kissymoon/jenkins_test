from selenium.common import InvalidCookieDomainException, WebDriverException
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "/html/body/header/div/ul[2]/li[4]/a[1]/span")
    USERNAME_INPUT = (By.ID, "user_login")
    PASSWORD_INPUT = (By.ID, "user_pass")
    CAPTCHA = (By.XPATH, "/html/body/div[6]/div[2]/div/form[1]/div[4]/span")
    URL_FRONT = "https://www"
    URL_BACK = '.lgych.com'

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(self.URL_FRONT + self.URL_BACK + '/jinbi')

    def user(self, username, password):
        self.click(self.LOGIN_BUTTON)
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.CAPTCHA)
        return True

    def cookies(self, cookies):
        res = self.cookie_add(cookies, self.URL_BACK)
        return res
