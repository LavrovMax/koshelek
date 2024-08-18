from locators.auth_locators import AuthLocators
from page.base_page import BasePage


class InvalidReferralKodePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = AuthLocators(self.page)

    def filling_date(self, auth):
        self.locators.username.fill(auth.name)
        self.locators.email.fill(auth.email)
        self.locators.password.fill(auth.password)
        self.locators.referral_code.fill(auth.referral_code)

    def accept_agreements(self):
        self.locators.agreements.click()

    # def resume(self):
    #     self.locators.btn_further.click()
