from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = 'login'

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ELEMENT_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
    ELEMENT_ADDED_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    ELEMENT_NAME = (By.CSS_SELECTOR,'.col-sm-6.product_main h1')
    ELEMENT_PRICE = (By.CSS_SELECTOR,'.col-sm-6.product_main .price_color')