from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import time 


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_basket()
        self.should_be_same_product_name()
        self.should_be_same_product_price()
        
    def add_product_to_basket_with_promo(self):
        # добавление товара в корзину (с методом решения задачи из BasePage)
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def add_product_to_basket(self):
        # добавление товара в корзину
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        add_to_basket_button.click()   

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

    def should_be_success_message(self):
        # проверка, что элемент появляется на странице в течение заданного времени
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_not_be_success_message(self):
        # проверка, что элемент НЕ появляется на странице в течение заданного времени
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        # проверка, что элемент исчезает на странице в течение заданного времени
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

