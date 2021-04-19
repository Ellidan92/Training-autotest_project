from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.should_be_login_link()

def test_elements_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()