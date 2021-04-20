from pages.product_page import Product_page

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = Product_page(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_be_element_name_is_right()
    page.should_be_element_price_is_right()