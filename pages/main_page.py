from .base_page import BasePage             # импорт базового класса BasePage
from .locators import MainPageLocators      # импорт класса с локаторами MainPageLocators
from .login_page import LoginPage           # импорт страницы с логином LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):                   # сделать наследником класса BasePage. Класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)    # создается новый объект - страница входа и регистрации


    def should_be_login_link(self):         # метод, который будет проверять наличие ссылки
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    
