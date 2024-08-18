from locators.auth_locators import AuthLocators
from page.base_page import BasePage


class InvalidNamePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = AuthLocators(self.page)

    # Заполняем данные
    def filling_data(self, auth):
        self.locators.username.fill(auth.name)
        self.locators.email.fill(auth.email)
        self.locators.password.fill(auth.password)

    # принимаем соглашение
    def accept_agreement(self):
        self.locators.agreements.click()

    # Нажимаем кнопку "Далее"
    def resume(self):
        self.locators.btn_further.click()

