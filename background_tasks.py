import asyncio
import os
import time


def delete_captcha(file_path: str, sleep_s: int = 15):
    time.sleep(sleep_s)
    try:
        # 检查文件是否存在
        if os.path.exists(file_path) and os.path.isfile(file_path):
            # 获取文件大小用于日志记录
            file_size = os.path.getsize(file_path)
            # 尝试删除文件
            os.remove(file_path)
            print(f"成功删除文件: {file_path} (大小: {file_size} 字节)")
        else:
            print(f"文件不存在，无需删除: {file_path}")

    except Exception as e:
        print(f"删除文件时出错: {file_path}, 错误: {str(e)}")

def parse_cookies(cookie_str, domain='.example.com'):
    """将Cookie字符串解析为Selenium可使用的字典格式"""
    cookies = []
    for line in cookie_str.split(';'):
        if line.strip():
            # 处理可能包含等号的复杂值（如JSON或JWT）
            parts = line.strip().split('=', 1)
            if len(parts) == 2:
                name, value = parts
                cookies.append({
                    'name': name,
                    'value': value,
                    'domain': domain
                })
    return cookies

# 使用示例
cookie_str = '__51uvsct__K4Eg8SGElFhlWvHA=2; __51vcke__K4Eg8SGElFhlWvHA=6c2c6e53-cf2e-5a10-b816-aad5bd4c0775; __51vuft__K4Eg8SGElFhlWvHA=1747319822025; _ga_EYK4RPLNVD=GS2.1.s1747325210$o2$g1$t1747325269$j0$l0$h0; _ga=GA1.1.1277335637.1747319822; Hm_lvt_7233eaff4ea4aa81ba9933f3a0e42474=1747319825,1747325213; c1b74ba4594ea9cbe653c15cb693bf25=2e9ea885ed5b4f6345635acb45318d8a; __vtins__K4Eg8SGElFhlWvHA=%7B%22sid%22%3A%20%2208700578-2240-5645-b5b8-2d354c354751%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%2059325%2C%20%22dr%22%3A%2020501%2C%20%22expires%22%3A%201747327069078%2C%20%22ct%22%3A%201747325269078%7D; Hm_lpvt_7233eaff4ea4aa81ba9933f3a0e42474=1747325255; HMACCOUNT=B6410012D4E17013; PHPSESSID=cdrs4m16r50c9l56eoq6ouump7; wordpress_logged_in_c31b215c0db6cdb6478d719de4022ec2=loveone%7C1748534841%7C8ImoqsG79N6BCDPZestr4ph7b8hvd1tS4WtMBfRObZT%7Cd3d73975930cf5ea19d89da701000f1d763c8525b07788243ba01559fa323415; erphp_login_tips=1; mycred_site_visit=1'
parsed_cookies = parse_cookies(cookie_str, domain='.lgych.com')