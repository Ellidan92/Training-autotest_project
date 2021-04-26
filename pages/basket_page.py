from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert BasketPageLocators.BASKET_URL in self.current_url(), "Url is not basket page"

    def should_be_empty_basket(self):
        # реализуйте проверку, что в корзине нет элемента
        assert self.is_not_element_present(*BasketPageLocators.ELEMENTS_ON_BASKET), "Basket is not empty"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is missing"







