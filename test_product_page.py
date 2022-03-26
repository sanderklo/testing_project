import pytest, time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_compare_product_in_basket()

@pytest.mark.guest_adding_product
class TestGuestAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, self.link)
        self.page.open()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.page.click_to_button_add_to_basket()
        self.page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.page.click_to_button_add_to_basket()
        self.page.should_disapiered_success_message()

@pytest.mark.login_from_product_page
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, self.link)
        self.page.open()

    def test_guest_should_see_login_link_on_product_page(self):
        self.page.should_be_login_link()
    
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.page.should_be_login_link()
        self.page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_busket_button()
        page.go_to_busket_page()
        busket_page = BasketPage(browser, browser.current_url)
        busket_page.should_be_empty_basket_text()
        busket_page.shoul_be_empty_busket()

@pytest.mark.user_adding_product
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.registration_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, self.registration_link)
        self.login_page.open()
        self.login_page.should_be_register_form()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "test"
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

        self.product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.product_page = ProductPage(browser, self.product_link)
        self.product_page.open() 

    def test_user_cant_see_success_message(self):
        self.product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.product_page.should_be_button_add_to_basket()
        self.product_page.click_to_button_add_to_basket()
        self.product_page.should_compare_product_in_basket()