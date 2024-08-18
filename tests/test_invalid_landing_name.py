import pytest
from playwright.sync_api import sync_playwright
from page.invalid_date_page import InvalidNamePage
from test_data.auth import (InvalidLendingName, InvalidLendingNameTwo, InvalidSymbolsName, InvalidSymbolsNameTwo,
                            InvalidEmailOne, InvalidEmailTwo, InvalidEmailThree,
                            InvalidPasswordOne, InvalidPasswordTwo, InvalidPasswordThree, InvalidPasswordAgain)

from playwright.sync_api import expect


class TestWithoutAgreement:
    @pytest.mark.parametrize("auth", [InvalidLendingName(), InvalidLendingNameTwo(), InvalidSymbolsName(),
                                      InvalidSymbolsNameTwo(), InvalidEmailOne(), InvalidEmailTwo(), InvalidEmailThree(),
                                      InvalidPasswordOne(), InvalidPasswordTwo(), InvalidPasswordThree(),
                                      InvalidPasswordAgain()])
    def test_invalid_date(self, page, auth):
        auth_page = InvalidNamePage(page)
        page.goto("https://koshelek.ru/authorization/signup")

        # Заполняем поля
        auth_page.filling_data(auth)

        # Принимаем соглашение и нажимаем кнопку далее
        auth_page.accept_agreement()
        auth_page.resume()

        # Проверки в зависимости от передаваемого набора входных данных
        if isinstance(auth, (InvalidLendingName, InvalidLendingNameTwo, InvalidSymbolsName, InvalidSymbolsNameTwo)):
            expect(auth_page.locators.field_name_not_valid).to_be_visible()

        if isinstance(auth, (InvalidEmailOne, InvalidEmailTwo, InvalidEmailThree)):
            expect(auth_page.locators.field_email_not_valid).to_be_visible()

        if isinstance(auth, InvalidPasswordOne):
            expect(auth_page.locators.short_password).to_be_visible()

        if isinstance(auth, (InvalidPasswordTwo, InvalidPasswordThree, InvalidPasswordAgain)):
            expect(auth_page.locators.field_password_not_valid).to_be_visible()
        expect(auth_page.locators.agreements).not_to_be_checked()
