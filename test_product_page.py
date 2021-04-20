from pages.login_page import LoginPage
from pages.product_page import Product_page
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_be_element_name_is_right()
    page.should_be_element_price_is_right()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_success_message_disappered()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_page(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_page(browser, link)
    page.open()
    page.go_to_login_page()
    lpage = LoginPage(browser, browser.current_url)
    lpage.should_be_login_page()