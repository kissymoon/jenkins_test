import logging

from selenium.common import InvalidCookieDomainException, WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_driver(self):
        return self.driver

    def find_element(self, locator):
        try:
            element = self.wait.until(
            expected_conditions.presence_of_element_located(locator)
        )
        except Exception as e:
            print("找不到元素")
            return e
        else:
            return element

    def click(self, locator):
        try:
            element = self.wait.until(
                expected_conditions.element_to_be_clickable(locator)
            )
        except Exception as e:
            logging.info('点击元素不存在' + str(e))
            return e
        else:
            element.click()
            return True
        finally:
            try:
                self.wait.until(
                    expected_conditions.presence_of_element_located(locator)
                )
            except Exception as e:
                logging.error('重试依旧不存在'+ str(e))


    def send_keys(self, locator, text, enter_bool=False):
        try:
            element = self.wait.until(
                expected_conditions.presence_of_element_located(locator)
            )
        except Exception as e:
            print("输入框不存在", e)
            return e
        else:
            element.send_keys(text)
            if enter_bool:
                self.send_enter(element)
            return True

    def send_enter(self, element1):
        element1.send_keys(Keys.ENTER)
        return

    def open(self, url:str):
        self.driver.execute_script(f"window.open('{url}', '_blank');")
        self.driver.switch_to.window(self.get_driver().window_handles[-1])
        return True

    def cookie_add(self, cookies, url_back, new_url=None):
        cookies_ls = []
        for line in cookies.split(';'):
            if line.strip():
                parts = line.strip().split('=', 1)
                if len(parts) == 2:
                    name, value = parts
                    cookies_ls.append({
                        'name': name,
                        'value': value,
                        'domain': url_back
                    })
        # 添加cookies
        try:
            for i in cookies_ls:
                self.driver.add_cookie(i)
        except InvalidCookieDomainException as e:
            print('非本域名，登陆失败')
            return e
        except WebDriverException as e:
            print('格式有误，登陆失败')
            return e
        except Exception as e:
            print('场外异常', e)
            return e
        else:
            if new_url:
                self.driver.get(new_url)
            else:
                self.driver.refresh()
            return True