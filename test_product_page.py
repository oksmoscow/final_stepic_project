from .pages.main_page import MainPage
from .pages.product_page import ProductPage

# ЗДЕСЬ Тесты (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear).
# Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
# Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.add_product_to_basket()
    page.should_be_same_product_name()
    page.should_be_same_product_price()  


