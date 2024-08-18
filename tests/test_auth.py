from playwright.sync_api import expect
from page.unfilled_page import UnfilledPage


class TestZeroAuth:
    def test_zero_auth_page(self, page):
        auth_page = UnfilledPage(page)
        page.goto('https://koshelek.ru/authorization/signup')

        # попытаемся отправить данные без заполнения полей
        auth_page.send_without_filling()

        # Проверки
        expect(auth_page.locators.field_name_not_filled).to_be_visible()
        expect(auth_page.locators.field_email_not_filled).to_be_visible()
        expect(auth_page.locators.field_email_not_filled).to_be_visible()
        expect(auth_page.locators.agreements).not_to_be_checked()
        pass




