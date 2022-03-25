from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUSKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    SIGN_IN_MAIL = (By.NAME, "login-username")
    SIGN_IN_PASSWORD = (By.NAME, "login-password")
    SIGN_IN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_MAIL = (By.NAME, "registration-email")
    REGISTRARION_PASSWORD = (By.NAME, "registration-password1")
    REGISTRARION_CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGISTRARION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/p[@class = 'price_color']")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success")

class BasketPageLocators():
    ORDER_BUTTON = (By.CSS_SELECTOR, "div.col-sm-4.col-sm-offset-8")
    TEXT_BUSKET_EMPTY = (By.XPATH, "//p[contains(text(), 'empty')]")
    BUSKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")