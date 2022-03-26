import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

BASE_LINK = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = BASE_LINK
        self.page = MainPage(browser, self.link)
        self.page.open() 

    def test_guest_can_go_to_login_page(self, browser): 
        self.page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self):
        self.page.should_be_login_link()

    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = BASE_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_busket_button()
    page.go_to_busket_page()
    busket_page = BasketPage(browser, browser.current_url)
    busket_page.should_be_empty_basket_text()
    busket_page.shoul_be_empty_busket()
