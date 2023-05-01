from .base_page import BasePage
from .locators import BasketPageLocators
import time 

class BasketPage(BasePage):

    def should_be_empty_basket_message(self):
        # проверка, что есть текст о том что корзина пуста 
        expected_empty_basked_message = "Your basket is empty"
        empty_basked_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert expected_empty_basked_message in empty_basked_message.text, f"Wrong empty basket message. Expected message: '{expected_empty_basked_message}'. Actual message: '{empty_basked_message.text}'"
        # assert self.is_element_present(*ProductPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"

    def should_not_be_products_in_busket(self):
        # проверка, что товары НЕ появляются на странице корзины в течение заданного времени
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Products in busket, but should not be"



