from .base_page import BasePage
from .locators import ProductPageLocators

class Product_page(BasePage):

    def should_be_product_page(self):
        self.should_be_basket_button()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "BasketButton is not present"

    def get_element_name(self):
        return self.browser.find_element(*ProductPageLocators.ELEMENT_NAME).text

    def get_element_price(self):
        return self.browser.find_element(*ProductPageLocators.ELEMENT_PRICE).text

    def should_be_element_name_is_right(self):
        assert self.browser.find_element(*ProductPageLocators.ELEMENT_ADDED).text == self.get_element_name(), "Wrong element name"

    def should_be_element_price_is_right(self):
        assert self.browser.find_element(*ProductPageLocators.ELEMENT_ADDED_PRICE).text == self.get_element_price(), "Wrong element price"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()
