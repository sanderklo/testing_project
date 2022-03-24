from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Url is not going to login-form!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_MAIL), "Input email is not presented!"
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_PASSWORD), "Input password is not presented!"
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_BUTTON), "Button 'sign in' is not presented!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_MAIL), "Input email is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTRARION_PASSWORD), "Input password is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTRARION_CONFIRM_PASSWORD), "Input confirm password is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTRARION_BUTTON), "Button 'registration' is not presented!"