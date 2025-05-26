import pytest
from pages.LoginPage import LoginPage

@pytest.mark.login_user
def test_user(web_driver):
    login = LoginPage(web_driver)
    username = 'loveone'
    password = '.q.MHF3HWXnk6At'
    assert login.user(username, password)


@pytest.mark.all
@pytest.mark.login_cookie
def test_cookie(web_driver):
    login = LoginPage(web_driver)
    cookies = "__51vcke__K4Eg8SGElFhlWvHA=22e92968-04ac-5b0f-826f-0457655ba299; __51vuft__K4Eg8SGElFhlWvHA=1747154325356; _ga=GA1.1.1231128337.1747154325; zh_choose=s; wordpress_logged_in_c31b215c0db6cdb6478d719de4022ec2=loveone%7C1748522199%7CJndrwneYIam6DNusQwuBjvs4zCgEpEHvAbrbplq3oZc%7C943cec75ce081d36ea0900b7a8bd3ca8da2a56f37acfeb0039c43b1c40d373d9; Hm_lvt_7233eaff4ea4aa81ba9933f3a0e42474=1747227705,1747247427,1747299099,1747395651; HMACCOUNT=D5CF44F1AC753B39; PHPSESSID=rgnjnr31ku86vk2316ncj0upgg; 0107bb65e17b1ed37f4d41ce8a35914e=c9f4a1edd4cb514720fda3c5dcc8b7a5; 186ff2f1b57f0818eb1663d7ee5bb8fe=03878dc2780d3239f0066de96fafe304; mycred_site_visit=1; Hm_lpvt_7233eaff4ea4aa81ba9933f3a0e42474=1747416788; __vtins__K4Eg8SGElFhlWvHA=%7B%22sid%22%3A%20%229e29a33d-9f66-56aa-8c74-e3be24c84421%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201747418588516%2C%20%22ct%22%3A%201747416788516%7D; __51uvsct__K4Eg8SGElFhlWvHA=12; _ga_EYK4RPLNVD=GS2.1.s1747416785$o14$g1$t1747416788$j0$l0$h0"
    assert login.cookies(cookies)