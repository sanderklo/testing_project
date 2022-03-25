from selenium.webdriver.common.by import By

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