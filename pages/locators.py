from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    INPUT_LOGIN_ENTRANCE = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_PASSWORD_ENTRANCE = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_ENTRANCE = (By.NAME, "login_submit")

    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    INPUT_LOGIN_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_CONFIRM_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")

