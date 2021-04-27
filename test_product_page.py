from pages.login_page import LoginPage
from pages.product_page import Product_page
from pages.basket_page import BasketPage
import pytest
import time

@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage():
    # сьют для тестов с авторизованым пользователем
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #фикстура создающая пользователя при помощи страницы авторизации для каждого теста
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        page.open()
        page.register_new_user(email,'Ellidan1992')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # тест для проверки того, что при открытии страницы продукта необходимые элементы присутсвуют и нет сообщения о добавлении
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = Product_page(browser, link)
        page.open()
        page.should_be_product_page()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # тест для проверки добавления продукта в корзину и верного отображения цены и названия
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = Product_page(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_to_basket()
        page.should_be_element_name_is_right()
        page.should_be_element_price_is_right()

def test_guest_cant_see_success_message(browser):
    # тест для проверки того, что при открытии страницы продукта необходимые элементы присутсвуют и нет сообщения о добавлении
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    # тест для проверки того, что при открытии страницы продукта необходимые элементы присутсвуют
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_be_element_name_is_right()
    page.should_be_element_price_is_right()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # учебный тест для тренировки работы с xfail
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # учебный тест для тренировки работы с xfail
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_success_message_disappered()

def test_guest_should_see_login_link_on_product_page(browser):
    # тест для проверки присутсвия кнопки перехода на страницу авторизации со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_page(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # тест для проверки перехода на страницу авторизации со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_page(browser, link)
    page.open()
    page.go_to_login_page()
    lpage = LoginPage(browser, browser.current_url)
    lpage.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # тест для проверки того, что при открытии корзины нет сообщений о добавлении товара и корзина пуста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_page(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()