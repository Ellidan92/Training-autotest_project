from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_register_email()
        self.should_be_login_register_password()
        self.should_be_login_register_password_repeat()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert LoginPageLocators.LOGIN_URL in self.current_url(), "Url is not login page"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login register form is not presented"

    def should_be_login_register_email(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_EMAIL), "Login register email element is not presented"

    def should_be_login_register_password(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_pass), "Login register password element is not presented"

    def should_be_login_register_password_repeat(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_PASS_REPEAT), "Login register password repeat element is not presented"


    def register_new_user(self, email, password):
        #регистрация нонового пользователя
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_PASS_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

