from selenium.common.exceptions import NoSuchElementException

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

