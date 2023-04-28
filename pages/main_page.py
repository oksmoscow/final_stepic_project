from .base_page import BasePage             # импорт базового класса BasePage
from .locators import MainPageLocators      # импорт класса с локаторами MainPageLocators
from .login_page import LoginPage           # импорт страницы с логином LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):                   # сделать наследником класса BasePage. Класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
    # Так как методы из класса MainPage были перенесены в класс BasePage, то добавили заглушку: 
    def __init__(self, *args, **kwargs):                    # метод __init__ вызывается при создании объекта
        super(MainPage, self).__init__(*args, **kwargs)     # конструктор с ключевым словом super вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage


 


