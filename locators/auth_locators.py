class AuthLocators:
    def __init__(self, page):
        self.page = page

    @property
    def username(self):
        return (self.page.locator('div.remoteComponent').locator('label:text("Имя пользователя")').
                locator('xpath=following-sibling::input'))

    @property
    def email(self):
        return self.page.locator('div.remoteComponent').locator('input[id="username"]')

    @property
    def password(self):
        return self.page.locator('div.remoteComponent').locator('input[type="password"]')

    @property
    def referral_code(self):
        return (self.page.locator('div.remoteComponent').locator('label:text("Реферальный код")').
                locator('xpath=following-sibling::input'))

    @property
    def agreements(self):
        return self.page.locator('div.remoteComponent').locator('div.v-input__control').locator(
            'input[type="checkbox"]')

    @property
    def btn_further(self):
        return self.page.locator('div.remoteComponent').locator(
            'button[class="v-btn v-btn--block v-btn--has-bg v-btn--rounded v-btn--tile theme--light elevation-0 v-size--x-large"]')

    @property
    def blocked_btn_further(self):
        return self.page.locator('div.remoteComponent').locator(
            'button[class="v-btn v-btn--block v-btn--disabled v-btn--has-bg v-btn--rounded v-btn--tile theme--light v-size--x-large"]')

    @property
    def field_name_not_filled(self):
        return self.page.locator('div.remoteComponent').locator(
            'span:text(" Поле не заполнено ")').nth(0)

    @property
    def field_email_not_filled(self):
        return self.page.locator('div.remoteComponent').locator(
            'span:text(" Поле не заполнено ")').nth(1)

    @property
    def field_password_not_filled(self):
        return self.page.locator('div.remoteComponent').locator(
            'span:text(" Поле не заполнено ")').nth(2)

    @property
    def field_name_not_valid(self):
        return self.page.locator('div.remoteComponent').locator(
            'span:text(" Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы ")')

    @property
    def field_email_not_valid(self):
        return self.page.locator('div.remoteComponent').locator('span:text(" Формат e-mail: username@test.ru ")')

    @property
    def field_password_not_valid(self):
        return self.page.locator('div.remoteComponent').locator(
            'span:text(" Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры ")')

    @property
    def short_password(self):
        return (self.page.locator('div.remoteComponent').locator(
            'span:text(" Пароль должен содержать минимум 8 символов ")'))

    @property
    def invalid_link_format(self):
        return (self.page.locator('div.remoteComponent').locator(
            'span:text(" Неверный формат ссылки ")'))
