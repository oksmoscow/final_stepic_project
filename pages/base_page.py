from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)   # команда для неявного ожидания со значением по умолчанию в 10

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):    # метод, в котором перехватываем исключение. Передаются два аргумента: как искать (how - css, id, xpath и тд (By.CSS_SELECTOR)) и что искать (what - строку-селектор ("#login_link"))
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):          # метод для получения проверочного кода при добавлении товара в корзину
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

