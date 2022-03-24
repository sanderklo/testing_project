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