from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button is not presented!"

    def click_to_button_add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_compare_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented!"
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented!"
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), "Product in basket name is not presented!"
        name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text

        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET), "Product in basket price is not presented!"
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text

        assert name == name_in_basket, "Product name in basket wrong!"
        assert price == price_in_basket, "Product price in basket wrong!"