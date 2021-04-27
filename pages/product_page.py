from .base_page import BasePage
from .locators import ProductPageLocators

class Product_page(BasePage):

    def should_be_product_page(self):
        # функция проверяющая элементы страницы продукта
        self.should_be_basket_button()

    def should_be_basket_button(self):
        # функция проверяющая присутсвие кнопки корзины на странице продукта
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "BasketButton is not present"

    def get_element_name(self):
        # функция получения названия товара
        return self.browser.find_element(*ProductPageLocators.ELEMENT_NAME).text

    def get_element_price(self):
        # функция получения цены товара
        return self.browser.find_element(*ProductPageLocators.ELEMENT_PRICE).text

    def should_be_element_name_is_right(self):
        # функция проверяющая совпадение имени добавленного продукта с отображаемым
        assert self.browser.find_element(*ProductPageLocators.ELEMENT_ADDED).text == self.get_element_name(), "Wrong element name"

    def should_be_element_price_is_right(self):
        # функция проверяющая совпадение цены добавленного продукта с отображаемой
        assert self.browser.find_element(*ProductPageLocators.ELEMENT_ADDED_PRICE).text == self.get_element_price(), "Wrong element price"

    def add_to_basket(self):
        # функция добавления товара в корзину
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        # функция проверяющая, что нет сообщения о добавлении элемента
        assert self.is_not_element_present(*ProductPageLocators.ELEMENT_ADDED), \
            "Success message is presented, but should not be"

    def should_success_message_disappered(self):
        # функция проверяющая, что сообщение пропадает
        assert self.is_disappeared(*ProductPageLocators.ELEMENT_ADDED), \
            "Success message is presented, but should not be"
