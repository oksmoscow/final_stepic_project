from .base_page import BasePage             # импорт базового класса BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):                   # сделать наследником класса BasePage. Класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):         # метод, который будет проверять наличие ссылки
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
    
