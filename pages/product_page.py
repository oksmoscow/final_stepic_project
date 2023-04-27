from .base_page import BasePage
# from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import MainPageLocators
import time 

# ЗДЕСЬ проверки (Описать в нем метод для добавления в корзину)!
# Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
# Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_basket()
        self.should_be_same_product_name()
        self.should_be_same_product_price()
        
    def add_product_to_basket(self):
        # добавление товара в корзину (с методом решения задачи из BasePage)
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        #time.sleep(5)

    def should_be_same_product_name(self):
        # проверка, что название товара в сообщении совпадает с названием добавленного
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME)
        assert product_name.text == product_in_basket_name.text, f"Product name in basket is incorrect. Expected name: '{product_name.text}'. Actual name in message: '{product_in_basket_name.text}'"

    def should_be_same_product_price(self):
        # проверка, что название товара в сообщении совпадает с названием добавленного
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_in_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE)
        assert product_price.text == product_in_basket_price.text, f"Product price in basket is incorrect. Expected price: '{product_price.text}'. Actual price in message: '{product_in_basket_price.text}'"

