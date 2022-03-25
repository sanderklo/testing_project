from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.TEXT_BUSKET_EMPTY), "Basket not got text 'Your basket is empty'"

    def shoul_be_empty_busket(self):
        assert self.browser.find_element(*BasketPageLocators.BUSKET_EMPTY), "Basket got some product!"
