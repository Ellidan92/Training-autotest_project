from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = 'login'

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ELEMENT_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
    ELEMENT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")