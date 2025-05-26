# import asyncio
#
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# @pytest.mark.one
# def un(web_driver):
#     driver = web_driver
#     driver.get('https://www.lgych.com/jinbi')
#     # cookies解析
#     cookies = "__51uvsct__K4Eg8SGElFhlWvHA=5; __51vcke__K4Eg8SGElFhlWvHA=6c2c6e53-cf2e-5a10-b816-aad5bd4c0775; __51vuft__K4Eg8SGElFhlWvHA=1747319822025; _ga_EYK4RPLNVD=GS2.1.s1747393092$o5$g1$t1747394689$j0$l0$h0; _ga=GA1.1.1277335637.1747319822; Hm_lvt_7233eaff4ea4aa81ba9933f3a0e42474=1747319825,1747325213,1747375074; wordpress_logged_in_c31b215c0db6cdb6478d719de4022ec2=loveone%7C1748534841%7C8ImoqsG79N6BCDPZestr4ph7b8hvd1tS4WtMBfRObZT%7Cd3d73975930cf5ea19d89da701000f1d763c8525b07788243ba01559fa323415; mycred_site_visit=1; __vtins__K4Eg8SGElFhlWvHA=%7B%22sid%22%3A%20%223d8c5161-5256-5cf2-b403-1eed05410711%22%2C%20%22vd%22%3A%202%2C%20%22stt%22%3A%201595598%2C%20%22dr%22%3A%201595598%2C%20%22expires%22%3A%201747396488909%2C%20%22ct%22%3A%201747394688909%7D; Hm_lpvt_7233eaff4ea4aa81ba9933f3a0e42474=1747394690; HMACCOUNT=680AC5ACEEDF92F1; PHPSESSID=8po021n8jnadkmkqf6ure6d9fb"
#     cookies_ls = []
#     for line in cookies.split(';'):
#         if line.strip():
#             parts = line.strip().split('=', 1)
#             if len(parts) == 2:
#                 name, value = parts
#                 cookies_ls.append({
#                     'name': name,
#                     'value': value,
#                     'domain': '.lgych.com'
#                 })
#     for i in cookies_ls:
#         driver.add_cookie(i)
#     # driver.get('https://www.lgych.com/user')
#     # driver.execute_script("window.open('https://www.lgych.com/jinbi', '_blank');")
#     # driver.switch_to.window(driver.window_handles[-1])
#     # wait = WebDriverWait(driver, 10)
#     # element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//textarea[@id=\"comment\"]")))
#     # element.send_keys('每日打卡')
#     input("阻塞：")
