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

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_IN_BASKET_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div strong')

    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)") 
    PRODUCT_IN_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner > p strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p") 
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    TOTAL_SUM = (By.CSS_SELECTOR, ".align-right > h3")
