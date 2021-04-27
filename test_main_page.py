from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # сьют для проверки страницы логина
    def test_guest_can_go_to_login_page(self, browser):
        # тест проверяющий переход на страницу авторизации
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # тест проверяющий присутствие кнопки перехода на страницу авторизации
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # тест проверяющий что при открытии с главной страницы, корзины, она пуста и есть сообщение, что она пуста.
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # тест проверяющий что при открытии со страницы продукта, корзины, она пуста и есть сообщение, что она пуста.
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()
