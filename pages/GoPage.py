import time

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class GoPage(BasePage):
    SIGN = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/a')
    COMMENTS = (By.XPATH, "//textarea[@id=\"comment\"]")
    COMMENTS_BUTTON = (By.XPATH, '//*[@id="submit"]')
    FIND_BUTTON = (By.XPATH, "/html/body/header/div/ul[2]/li[4]/a/i")
    FIND_TEXT = (By.XPATH, "/html/body/div[1]/div/form/input[1]")
    URL_FRONT = 'https://www.lgych.com/'
    URL_USER = 'user'
    URL_JINBI = 'jinbi'

    def __init__(self, driver):
        super().__init__(driver)

    def sign(self):
        self.open(self.URL_FRONT + self.URL_USER)
        assert self.click(self.SIGN) == True
        return True

    def comments(self):
        self.send_keys(self.COMMENTS, '每日打卡', )
        # self.click(self.COMMENTS_BUTTON)
        return True

    def find(self):
        self.get_driver().switch_to.window(self.get_driver().window_handles[0])
        self.click(self.FIND_BUTTON)
        self.send_keys(self.FIND_TEXT, 'niziu', True)
        return True

    def all(self):
        self.comments()
        self.sign()
        self.find()
        return True