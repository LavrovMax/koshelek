from locators.auth_locators import AuthLocators
from page.base_page import BasePage


class UnfilledPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = AuthLocators(page)

    def send_without_filling(self):
        self.locators.btn_further.click()


