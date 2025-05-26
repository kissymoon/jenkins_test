import pytest
from pages.GoPage import GoPage


@pytest.mark.all
@pytest.mark.func
def test_get(web_driver):
    login = GoPage(web_driver)
    login.all()
    input("阻塞：")