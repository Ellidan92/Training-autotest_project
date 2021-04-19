from .base_page import BasePage
from .locators import ProductPageLocators

class Product_page(BasePage):

    def should_be_product_page(self):
        self.should_be_basket_button()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "BasketButton is not present"

    def should_be_message_of_added(self):
        assert self.browser.find_element(*ProductPageLocators.ELEMENT_ADDED).text == "The shellcoder's handbook", "Wrong element name"

    def should_be_message_of_price(self):
        assert self.browser.find_element(*ProductPageLocators.ELEMENT_PRICE).text == "£9.99", "Wrong element price"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()
