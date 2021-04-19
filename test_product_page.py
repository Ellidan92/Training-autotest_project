from pages.product_page import Product_page
import time
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_be_message_of_added()
    page.should_be_message_of_price()