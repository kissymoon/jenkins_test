# import asyncio
# import threading
# import uuid
#
# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# from background_tasks import delete_captcha, parse_cookies
#
# firefox_options = Options()
# firefox_options.add_argument("--headless")
# firefox_options = None
# driver = webdriver.Firefox(options=firefox_options)
# driver.implicitly_wait(5)
# # driver.maximize_window()
# driver.get('https://www.lgych.com/')
# # cookie登陆
# cookie_str = \
#     '__51uvsct__K4Eg8SGElFhlWvHA=2; __51vcke__K4Eg8SGElFhlWvHA=6c2c6e53-cf2e-5a10-b816-aad5bd4c0775; __51vuft__K4Eg8SGElFhlWvHA=1747319822025; _ga_EYK4RPLNVD=GS2.1.s1747325210$o2$g1$t1747325269$j0$l0$h0; _ga=GA1.1.1277335637.1747319822; Hm_lvt_7233eaff4ea4aa81ba9933f3a0e42474=1747319825,1747325213; c1b74ba4594ea9cbe653c15cb693bf25=2e9ea885ed5b4f6345635acb45318d8a; __vtins__K4Eg8SGElFhlWvHA=%7B%22sid%22%3A%20%2208700578-2240-5645-b5b8-2d354c354751%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%2059325%2C%20%22dr%22%3A%2020501%2C%20%22expires%22%3A%201747327069078%2C%20%22ct%22%3A%201747325269078%7D; Hm_lpvt_7233eaff4ea4aa81ba9933f3a0e42474=1747325255; HMACCOUNT=B6410012D4E17013; PHPSESSID=cdrs4m16r50c9l56eoq6ouump7; wordpress_logged_in_c31b215c0db6cdb6478d719de4022ec2=loveone%7C1748534841%7C8ImoqsG79N6BCDPZestr4ph7b8hvd1tS4WtMBfRObZT%7Cd3d73975930cf5ea19d89da701000f1d763c8525b07788243ba01559fa323415; erphp_login_tips=1; mycred_site_visit=1'
# parsed_cookies = parse_cookies(cookie_str, domain='.lgych.com')
# for i in parsed_cookies:
#     driver.add_cookie(i)
# driver.refresh()
# print('加载完成')
# # 点击登陆按钮
# try:
#     wait = WebDriverWait(driver, timeout=3)
#     element = wait.until(
#         expected_conditions.presence_of_element_located((By.XPATH, "/html/body/header/div/ul[2]/li[4]/a[1]/span"))
#     )
# except TimeoutException:
#     element = False
#     print("无需登陆")
# if element:
#     element.click()
#     # 用户名输入
#     username = driver.find_element(By.XPATH, "//*[@id=\"user_login\"]")
#     username.send_keys("loveone")
#     # 密码输入
#     password = driver.find_element(By.XPATH, "//*[@id=\"user_pass\"]")
#     password.send_keys(".q.MHF3HWXnk6At")
#     # 验证码点击
#     captcha = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/form[1]/div[4]/span")
#     captcha.click()
#     # 验证码截图
#     captcha_img = captcha.find_element(By.XPATH, "./img")
#     captcha_path = "./img/" + str(uuid.uuid4()) + ".png"
#     captcha_img.screenshot(captcha_path)
#     # 识别验证码
#     # image = Image.open(captcha_path)
#     # text = pytesseract.image_to_string(image)
#     # print("识别结果:", text.strip())
#     # 多线程删除截图
#     thread = threading.Thread(target=delete_captcha, args=(captcha_path,))
#     thread.start()
# # # 签到
# # element = driver.find_element(By.XPATH, "/html/body/header/div/ul[2]/li[5]/a/img")
# # element.click()
# # element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/a")
# # element.click()
# # # 评论
# # driver.get("https://www.lgych.com/jinbi")
# # element = driver.find_element(By.XPATH, "//*[@id=\"comment\"]")
# # element.send_keys("每日签到")
# # element.send_keys(Keys.RETURN)
# # 搜索
# driver.find_element(By.XPATH, "/html/body/header/div/ul[2]/li[4]/a/i").click()
# element = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/input[1]")
# element.send_keys("niziu")
# element.send_keys(Keys.ENTER)
#
# print("完成")
# input('阻塞：')
# driver.quit()
