from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = 'login'
    LOGIN_REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REGISTER_PASS_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name = registration_submit]')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ELEMENT_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
    ELEMENT_ADDED_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    ELEMENT_NAME = (By.CSS_SELECTOR,'.col-sm-6.product_main h1')
    ELEMENT_PRICE = (By.CSS_SELECTOR,'.col-sm-6.product_main .price_color')

class BasketPageLocators():
    ELEMENTS_ON_BASKET = (By.CSS_SELECTOR, '.ibasket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner')
    BASKET_URL = 'basket'