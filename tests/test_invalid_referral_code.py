import pytest
from page.invalid_referral_kode_page import InvalidReferralKodePage
from test_data.auth import InvalidReferralKode
from playwright.sync_api import expect


class TestInvalidReferralKodePage:
    @pytest.mark.parametrize("auth", [InvalidReferralKode()])
    def test_invalid_referral_kode(self, page, auth):
        auth_page = InvalidReferralKodePage(page)
        page.goto("https://koshelek.ru/authorization/signup")

        # Заполняем данные
        auth_page.filling_date(auth)

        # Принимаем соглашение и нажимаем кнопку "Далее"
        auth_page.accept_agreements()

        # Проверка
        expect(auth_page.locators.invalid_link_format).to_be_visible()
        expect(auth_page.locators.blocked_btn_further).to_be_visible()
